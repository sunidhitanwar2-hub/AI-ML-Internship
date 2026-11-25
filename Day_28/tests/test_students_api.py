"""API tests for the student profiles feature.

Each test uses its own temporary database, so real data is never touched.
Run with:  python -m pytest tests -v   (or: python -m unittest discover -s tests -v)
"""

import os
import tempfile
import unittest

from fastapi.testclient import TestClient

from main import app

RIYA = {"name": "Riya Sharma", "email": "Riya@Example.com", "age": 20, "course": "BCA"}
AMAN = {"name": "Aman Verma", "email": "aman@example.com", "age": 21, "course": "BTech"}


class StudentApiTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_path = os.environ.get("DATABASE_PATH")
        os.environ["DATABASE_PATH"] = os.path.join(self.temp_dir.name, "test.db")
        self.client = TestClient(app)
        self.client.__enter__()  # runs startup, which creates the table

    def tearDown(self):
        self.client.__exit__(None, None, None)
        if self.old_path is None:
            os.environ.pop("DATABASE_PATH", None)
        else:
            os.environ["DATABASE_PATH"] = self.old_path
        self.temp_dir.cleanup()

    def register(self, student):
        return self.client.post("/students", json=student)

    def test_register_returns_201_and_normalised_email(self):
        response = self.register(RIYA)
        self.assertEqual(response.status_code, 201)
        body = response.json()
        self.assertEqual(body["email"], "riya@example.com")
        self.assertIsInstance(body["id"], int)

    def test_duplicate_email_returns_409(self):
        self.register(RIYA)
        response = self.register({**AMAN, "email": "riya@example.com"})
        self.assertEqual(response.status_code, 409)

    def test_invalid_input_returns_422(self):
        for bad in ({**RIYA, "age": 3}, {**RIYA, "email": "not-an-email"},
                    {**RIYA, "name": " "}, {"name": "Riya"}):
            with self.subTest(bad=bad):
                self.assertEqual(self.register(bad).status_code, 422)

    def test_sql_injection_text_is_stored_as_plain_text(self):
        name = "Bob'); DROP TABLE students; --"
        self.assertEqual(self.register({**RIYA, "name": name}).status_code, 201)
        students = self.client.get("/students").json()
        self.assertEqual(students[0]["name"], name)

    def test_list_and_pagination(self):
        self.register(RIYA)
        self.register(AMAN)
        self.assertEqual(len(self.client.get("/students").json()), 2)
        page = self.client.get("/students", params={"skip": 1, "limit": 1}).json()
        self.assertEqual([s["name"] for s in page], ["Aman Verma"])

    def test_get_missing_student_returns_404(self):
        self.assertEqual(self.client.get("/students/999").status_code, 404)

    def test_partial_update(self):
        student_id = self.register(RIYA).json()["id"]
        response = self.client.patch(f"/students/{student_id}", json={"course": "MCA"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["course"], "MCA")
        self.assertEqual(response.json()["name"], "Riya Sharma")

    def test_update_missing_or_to_duplicate_email(self):
        self.assertEqual(self.client.patch("/students/999", json={"age": 22}).status_code, 404)
        self.register(RIYA)
        aman_id = self.register(AMAN).json()["id"]
        response = self.client.patch(f"/students/{aman_id}", json={"email": "riya@example.com"})
        self.assertEqual(response.status_code, 409)

    def test_delete(self):
        student_id = self.register(RIYA).json()["id"]
        self.assertEqual(self.client.delete(f"/students/{student_id}").status_code, 204)
        self.assertEqual(self.client.get(f"/students/{student_id}").status_code, 404)
        self.assertEqual(self.client.delete(f"/students/{student_id}").status_code, 404)

    def test_non_numeric_id_returns_422(self):
        self.assertEqual(self.client.get("/students/abc").status_code, 422)


if __name__ == "__main__":
    unittest.main()
