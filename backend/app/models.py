from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
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


class Angel(Base):
    __tablename__ = "angels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    icon = Column(String, nullable=False)
    short_text = Column(Text, nullable=False)
    full_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Saint(Base):
    __tablename__ = "saints"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    short_text = Column(Text, nullable=False)
    full_text = Column(Text, nullable=False)
    feast_day = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
