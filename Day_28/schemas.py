"""Request and response models for the student API (validated by Pydantic)."""

from pydantic import BaseModel, ConfigDict, Field, field_validator

MIN_AGE, MAX_AGE = 5, 100
EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"


class StudentBase(BaseModel):
    """Fields shared by create requests and responses."""

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=2, max_length=100, examples=["Riya Sharma"])
    email: str = Field(max_length=254, pattern=EMAIL_PATTERN, examples=["riya@example.com"])
    age: int = Field(ge=MIN_AGE, le=MAX_AGE, examples=[20])
    course: str = Field(min_length=2, max_length=100, examples=["BCA"])

    @field_validator("email")
    @classmethod
    def normalise_email(cls, value: str) -> str:
        return value.lower()


class StudentCreate(StudentBase):
    """Body of POST /students."""


class StudentUpdate(BaseModel):
    """Body of PATCH /students/{id}: send only the fields to change."""

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str | None = Field(default=None, min_length=2, max_length=100)
    email: str | None = Field(default=None, max_length=254, pattern=EMAIL_PATTERN)
    age: int | None = Field(default=None, ge=MIN_AGE, le=MAX_AGE)
    course: str | None = Field(default=None, min_length=2, max_length=100)

    @field_validator("email")
    @classmethod
    def normalise_email(cls, value: str | None) -> str | None:
        return value.lower() if value is not None else None


class Student(StudentBase):
    """A stored student, as returned by the API."""

    id: int
