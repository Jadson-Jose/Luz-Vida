from datetime import datetime

from pydantic import BaseModel, ConfigDict


# ========== Bíblia ==========
class VerseOut(BaseModel):
    id: int
    number: int
    text: str
    chapter_id: int

    model_config = ConfigDict(from_attributes=True)


class VerseCreate(BaseModel):
    number: int
    text: str
    chapter_id: int


class ChapterOut(BaseModel):
    id: int
    number: int
    book_id: int

    model_config = ConfigDict(from_attributes=True)


class ChapterCreate(BaseModel):
    number: int
    book_id: int


class ChapterWithVerses(ChapterOut):
    verses: list[VerseOut] = []


class BookOut(BaseModel):
    id: int
    name: str
    abbreviation: str

    model_config = ConfigDict(from_attributes=True)


class BookCreate(BaseModel):
    name: str
    abbreviation: str


class BookWithChapters(BookOut):
    chapters: list[ChapterOut] = []


# ========== Anjos ==========
class AngelBase(BaseModel):
    name: str
    title: str
    icon: str
    short_text: str
    full_text: str


class AngelCreate(AngelBase):
    pass


class AngelOut(AngelBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


# ========== Santos ==========
class SaintBase(BaseModel):
    name: str
    title: str | None = None
    image_url: str | None = None
    short_text: str
    full_text: str
    feast_day: str | None = None


class SaintCreate(SaintBase):
    pass


class SaintOut(SaintBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class SearchResult(BaseModel):
    verse: VerseOut
    book_name: str
    chapter_number: int
