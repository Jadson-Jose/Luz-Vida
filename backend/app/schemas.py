from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict


class VerseOut(BaseModel):
    id: int
    number: int
    text: str
    chapter_id: int

    class Config:
        from_attributes = True


class ChapterOut(BaseModel):
    id: int
    number: int
    book_id: int

    class Config:
        from_attributes = True


class ChapterWithVerses(ChapterOut):
    verses: list[VerseOut] = []


class BookOut(BaseModel):
    id: int
    name: str
    abbreviation: str

    class Config:
        from_attributes = True


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
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


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
    create_at: datetime
    update_at: datetime | None = None

    class Config:
        from_attributes = True


class BookWithChapters(BookOut):
    chapters: list[ChapterOut] = []
