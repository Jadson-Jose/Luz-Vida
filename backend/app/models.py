from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    abbreviation = Column(String, nullable=False)

    chapters = relationship("Chapter", back_populates="book")


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    book = relationship("Book", back_populates="chapters")
    verses = relationship("Verse", back_populates="chapter")


class Verse(Base):
    __tablename__ = "verses"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)

    chapter = relationship("Chapter", back_populates="verses")
