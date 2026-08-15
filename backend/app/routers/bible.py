from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/api", tags=["bible"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/books", response_model=list[schemas.BookOut])
def list_books(db: Session = Depends(get_db)):
    return db.query(models.Book).order_by(models.Book.id).all()


@router.get("/books/{book_id}", response_model=schemas.BookWithChapters)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return book


@router.get("/chapters/{chapter_id}", response_model=schemas.ChapterWithVerses)
def get_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Capítulo não encontrado")
    return chapter


@router.get("/verses/{verse_id}", response_model=schemas.VerseOut)
def get_verse(verse_id: int, db: Session = Depends(get_db)):
    verse = db.query(models.Verse).filter(models.Verse.id == verse_id).first()
    if not verse:
        raise HTTPException(status_code=404, detail="Versículo não encontrado")
    return verse
