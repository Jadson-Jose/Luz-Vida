from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app import models, schemas
from app.auth import require_admin
from app.database import SessionLocal
from app.utils.pagination import apply_pagination

router = APIRouter(prefix="/api", tags=["bible"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- LIVROS ----------
@router.get("/books", response_model=list[schemas.BookOut])
def list_books(
    response: Response,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    total = db.query(models.Book).count()
    books = (
        db.query(models.Book).order_by(models.Book.id).offset(skip).limit(limit).all()
    )
    apply_pagination(response, skip, limit, total)
    return books


@router.get("/books/{book_id}", response_model=schemas.BookWithChapters)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return book


@router.post(
    "/books",
    response_model=schemas.BookOut,
    dependencies=[Depends(require_admin)],
)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.put(
    "/books/{book_id}",
    response_model=schemas.BookOut,
    dependencies=[Depends(require_admin)],
)
def update_book(
    book_id: int, updated: schemas.BookCreate, db: Session = Depends(get_db)
):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    for key, value in updated.dict().items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book


@router.delete(
    "/books/{book_id}", status_code=204, dependencies=[Depends(require_admin)]
)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    db.delete(book)
    db.commit()


# ---------- CAPÍTULOS ----------
@router.get("/chapters/{chapter_id}", response_model=schemas.ChapterWithVerses)
def get_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Capítulo não encontrado")
    return chapter


@router.get("/books/{book_id}/chapters", response_model=list[schemas.ChapterOut])
def list_chapters_by_book(
    book_id: int,
    response: Response,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    total = db.query(models.Chapter).filter(models.Chapter.book_id == book_id).count()
    chapters = (
        db.query(models.Chapter)
        .filter(models.Chapter.book_id == book_id)
        .order_by(models.Chapter.number)
        .offset(skip)
        .limit(limit)
        .all()
    )
    apply_pagination(response, skip, limit, total)
    return chapters


@router.post(
    "/chapters",
    response_model=schemas.ChapterOut,
    dependencies=[Depends(require_admin)],
)
def create_chapter(chapter: schemas.ChapterCreate, db: Session = Depends(get_db)):
    db_chapter = models.Chapter(**chapter.dict())
    db.add(db_chapter)
    db.commit()
    db.refresh(db_chapter)
    return db_chapter


@router.put(
    "/chapters/{chapter_id}",
    response_model=schemas.ChapterOut,
    dependencies=[Depends(require_admin)],
)
def update_chapter(
    chapter_id: int, updated: schemas.ChapterCreate, db: Session = Depends(get_db)
):
    chapter = db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Capítulo não encontrado")
    for key, value in updated.dict().items():
        setattr(chapter, key, value)
    db.commit()
    db.refresh(chapter)
    return chapter


@router.delete(
    "/chapters/{chapter_id}", status_code=204, dependencies=[Depends(require_admin)]
)
def delete_chapter(chapter_id: int, db: Session = Depends(get_db)):
    chapter = db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()
    if not chapter:
        raise HTTPException(status_code=404, detail="Capítulo não encontrado")
    db.delete(chapter)
    db.commit()


# ---------- VERSÍCULOS ----------
@router.get("/verses/{verse_id}", response_model=schemas.VerseOut)
def get_verse(verse_id: int, db: Session = Depends(get_db)):
    verse = db.query(models.Verse).filter(models.Verse.id == verse_id).first()
    if not verse:
        raise HTTPException(status_code=404, detail="Versículo não encontrado")
    return verse


@router.get("/chapters/{chapter_id}/verses", response_model=list[schemas.VerseOut])
def list_verses_by_chapter(
    chapter_id: int,
    response: Response,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    total = db.query(models.Verse).filter(models.Verse.chapter_id == chapter_id).count()
    verses = (
        db.query(models.Verse)
        .filter(models.Verse.chapter_id == chapter_id)
        .order_by(models.Verse.number)
        .offset(skip)
        .limit(limit)
        .all()
    )
    apply_pagination(response, skip, limit, total)
    return verses


@router.post(
    "/verses",
    response_model=schemas.VerseOut,
    dependencies=[Depends(require_admin)],
)
def create_verse(verse: schemas.VerseCreate, db: Session = Depends(get_db)):
    db_verse = models.Verse(**verse.dict())
    db.add(db_verse)
    db.commit()
    db.refresh(db_verse)
    return db_verse


@router.put(
    "/verses/{verse_id}",
    response_model=schemas.VerseOut,
    dependencies=[Depends(require_admin)],
)
def update_verse(
    verse_id: int, updated: schemas.VerseCreate, db: Session = Depends(get_db)
):
    verse = db.query(models.Verse).filter(models.Verse.id == verse_id).first()
    if not verse:
        raise HTTPException(status_code=404, detail="Versículo não encontrado")
    for key, value in updated.dict().items():
        setattr(verse, key, value)
    db.commit()
    db.refresh(verse)
    return verse


@router.delete(
    "/verses/{verse_id}", status_code=204, dependencies=[Depends(require_admin)]
)
def delete_verse(verse_id: int, db: Session = Depends(get_db)):
    verse = db.query(models.Verse).filter(models.Verse.id == verse_id).first()
    if not verse:
        raise HTTPException(status_code=404, detail="Versículo não encontrado")
    db.delete(verse)
    db.commit()


# ---------- BUSCA ----------
@router.get("/search", response_model=list[schemas.SearchResult])
def search_verses(q: str, db: Session = Depends(get_db)):
    pattern = f"%{q}%"
    results = (
        db.query(
            models.Verse,
            models.Book.name.label("book_name"),
            models.Chapter.number.label("chapter_number"),
        )
        .join(models.Chapter, models.Verse.chapter_id == models.Chapter.id)
        .join(models.Book, models.Chapter.book_id == models.Book.id)
        .filter(models.Verse.text.ilike(pattern))
        .limit(50)
        .all()
    )

    return [
        schemas.SearchResult(
            verse=schemas.VerseOut.model_validate(verse),
            book_name=book_name,
            chapter_number=chapter_number,
        )
        for verse, book_name, chapter_number in results
    ]

@router.get("/chapters/{chapter_id}/navigation")
def get_chapter_navigation(chapter_id: int, db: Session = Depends(get_db)):
    # 1. Encontra o capítulo atual
    current_chapter = db.query(models.Chapter).filter(models.Chapter.id == chapter_id).first()
    if not current_chapter:
        raise HTTPException(status_code=404, detail="Capítulo não encontrado")

    # 2. Encontra o livro atual
    current_book = db.query(models.Book).filter(models.Book.id == current_chapter.book_id).first()

    # 3. Encontra o capítulo anterior (mesmo livro)
    prev_chapter = db.query(models.Chapter).filter(
        models.Chapter.book_id == current_book.id,
        models.Chapter.number < current_chapter.number
    ).order_by(models.Chapter.number.desc()).first()

    # 4. Encontra o capítulo seguinte (mesmo livro)
    next_chapter = db.query(models.Chapter).filter(
        models.Chapter.book_id == current_book.id,
        models.Chapter.number > current_chapter.number
    ).order_by(models.Chapter.number.asc()).first()

    # 5. Se não houver próximo no mesmo livro, tenta o primeiro capítulo do próximo livro
    if not next_chapter:
        next_book = db.query(models.Book).filter(models.Book.id > current_book.id).order_by(models.Book.id).first()
        if next_book:
            next_chapter = db.query(models.Chapter).filter(
                models.Chapter.book_id == next_book.id,
                models.Chapter.number == 1
            ).first()

    # 6. Se não houver anterior no mesmo livro, tenta o último capítulo do livro anterior
    if not prev_chapter:
        prev_book = db.query(models.Book).filter(models.Book.id < current_book.id).order_by(models.Book.id.desc()).first()
        if prev_book:
            prev_chapter = db.query(models.Chapter).filter(
                models.Chapter.book_id == prev_book.id
            ).order_by(models.Chapter.number.desc()).first()

    return {
        "prev_id": prev_chapter.id if prev_chapter else None,
        "next_id": next_chapter.id if next_chapter else None,
        "book_name": current_book.name,
        "chapter_number": current_chapter.number
    }