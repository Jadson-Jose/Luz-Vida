from typing import List

from pydantic import BaseModel


class VerseOut(BaseModel):
    id: int
    number: int
    text: str
    chapter_id: int

    class Config:
        orm_mode = True


class ChapterOut(BaseModel):
    id: int
    number: int
    book_id: int

    class Config:
        orm_mode = True


class ChapterWithVerses(ChapterOut):
    verses: List[VerseOut] = []


class BookOut(BaseModel):
    id: int
    name: str
    abbreviation: str

    class Config:
        orm_mode = True


class BookWithChapters(BookOut):
    chapters: List[ChapterOut] = []
