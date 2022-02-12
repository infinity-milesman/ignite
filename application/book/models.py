from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, SmallInteger, String, UniqueConstraint, text
from sqlalchemy.orm import relationship

from application import db


class BooksAuthor(db.Model):
    __tablename__ = 'books_author'

    id = Column(Integer, primary_key=True)
    birth_year = Column(SmallInteger)
    death_year = Column(SmallInteger)
    name = Column(String(128), nullable=False)


class BooksBook(db.Model):
    __tablename__ = 'books_book'
    __table_args__ = (
        CheckConstraint('download_count >= 0'),
        CheckConstraint('gutenberg_id >= 0')
    )

    id = Column(Integer, primary_key=True)
    download_count = Column(Integer)
    gutenberg_id = Column(Integer, nullable=False, unique=True)
    media_type = Column(String(16), nullable=False)
    title = Column(String(1024))
    books_format = relationship('BooksFormat', backref='books_book')


class BooksBookshelf(db.Model):
    __tablename__ = 'books_bookshelf'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)


class BooksLanguage(db.Model):
    __tablename__ = 'books_language'

    id = Column(Integer, primary_key=True)
    code = Column(String(4), nullable=False, unique=True)


class BooksSubject(db.Model):
    __tablename__ = 'books_subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)


class BooksBookAuthor(db.Model):
    __tablename__ = 'books_book_authors'
    __table_args__ = (
        UniqueConstraint('book_id', 'author_id'),
    )

    id = Column(Integer, primary_key=True)
    book_id = Column(ForeignKey('books_book.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    author_id = Column(ForeignKey('books_author.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    author = relationship('BooksAuthor')
    book = relationship('BooksBook')


class BooksBookBookshelf(db.Model):
    __tablename__ = 'books_book_bookshelves'
    __table_args__ = (
        UniqueConstraint('book_id', 'bookshelf_id'),
    )

    id = Column(Integer, primary_key=True)
    book_id = Column(ForeignKey('books_book.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    bookshelf_id = Column(ForeignKey('books_bookshelf.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    book = relationship('BooksBook')
    bookshelf = relationship('BooksBookshelf')


class BooksBookLanguage(db.Model):
    __tablename__ = 'books_book_languages'
    __table_args__ = (
        UniqueConstraint('book_id', 'language_id'),
    )

    id = Column(Integer, primary_key=True)
    book_id = Column(ForeignKey('books_book.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    language_id = Column(ForeignKey('books_language.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    book = relationship('BooksBook')
    language = relationship('BooksLanguage')


class BooksBookSubject(db.Model):
    __tablename__ = 'books_book_subjects'
    __table_args__ = (
        UniqueConstraint('book_id', 'subject_id'),
    )

    id = Column(Integer, primary_key=True)
    book_id = Column(ForeignKey('books_book.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    subject_id = Column(ForeignKey('books_subject.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)

    book = relationship('BooksBook')
    subject = relationship('BooksSubject')


class BooksFormat(db.Model):
    __tablename__ = 'books_format'

    id = Column(Integer, primary_key=True)
    mime_type = Column(String(32), nullable=False)
    url = Column(String(256), nullable=False)
    book_id = Column(ForeignKey('books_book.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)


