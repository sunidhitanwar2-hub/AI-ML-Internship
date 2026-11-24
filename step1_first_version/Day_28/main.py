from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn = sqlite3.connect("students.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, age INTEGER, course TEXT)")
conn.commit()


@app.post("/add")
def add(d: dict):
    c.execute(f"INSERT INTO students (name, email, age, course) VALUES ('{d['name']}', '{d['email']}', {d['age']}, '{d['course']}')")
    conn.commit()
    return {"msg": "added"}


@app.get("/all")
def all():
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    res = []
    for r in rows:
        res.append({"id": r[0], "name": r[1], "email": r[2], "age": r[3], "course": r[4]})
    return res


@app.get("/get/{id}")
def get(id):
    c.execute(f"SELECT * FROM students WHERE id = {id}")
    r = c.fetchone()
    if r:
        return {"id": r[0], "name": r[1], "email": r[2], "age": r[3], "course": r[4]}
    return None


@app.put("/update/{id}")
def update(id, d: dict):
    c.execute(f"UPDATE students SET name = '{d['name']}', email = '{d['email']}', age = {d['age']}, course = '{d['course']}' WHERE id = {id}")
    conn.commit()
    return {"msg": "updated"}


@app.delete("/delete/{id}")
def delete(id):
    c.execute(f"DELETE FROM students WHERE id = {id}")
    conn.commit()
    return {"msg": "deleted"}
