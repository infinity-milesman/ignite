from flask import make_response, jsonify, request

from flask.views import MethodView
from sqlalchemy import or_


from .models import *
from .. import db
from sqlalchemy import func



class BookApi(MethodView):
    def get(self):
        my_dict = {}
        request_data = request.get_json()
        per_page = request_data.get('per_page', 25)
        page = request_data.get('page', 1)

        q = db.session.query(BooksBook.title,BooksAuthor.name.label('Author'),BooksLanguage.code,BooksSubject.name.label('Subject'),BooksBookshelf.name.label('Bookshelf'),BooksFormat.url)
        q = q.join(BooksBookAuthor, BooksBook.id == BooksBookAuthor.book_id).join(BooksAuthor, BooksBookAuthor.author_id == BooksAuthor.id).join(BooksBookLanguage, BooksBook.id == BooksBookLanguage.book_id).join(BooksLanguage, BooksBookLanguage.language_id == BooksLanguage.id).join(BooksBookSubject, BooksBook.id == BooksBookSubject.book_id)
        q = q.join(BooksSubject, BooksBookSubject.subject_id == BooksSubject.id).join(BooksBookBookshelf, BooksBook.id == BooksBookBookshelf.book_id).join(BooksBookshelf, BooksBookBookshelf.bookshelf_id == BooksBookshelf.id).join(BooksFormat, BooksBook.id == BooksFormat.book_id)

        if 'author_name' in request_data:
            q = q.filter(BooksAuthor.name.ilike('%'+request_data['author_name'] + '%'))
        if 'title' in request_data:
            q = q.filter(BooksBook.title.ilike('%'+request_data['title']+'%'))
        if 'book_id_number' in request_data:
            q = q.filter(BooksBook.gutenberg_id.in_(request_data['book_id_number'].split(',')))
        if 'mime_type' in request_data:
            q = q.filter(BooksFormat.mime_type.in_([x.lower() for x in request_data['mime_type'].split(',')]))
        if 'language_code' in request_data:
            q = q.filter(func.lower(BooksLanguage.code).in_([x.lower() for x in request_data['language_code'].split(',')]))
        if 'topic' in request_data:
            q = q.filter(or_(BooksBookshelf.name.in_([x.lower() for x in request_data['topic'].split(',')]), BooksSubject.name.in_([x.lower() for x in request_data['topic'].split(',')])))

        data = q.limit(per_page).offset(page).all()
        count = q.count()

        my_dict['data'] = [u._asdict() for u in data]

        my_dict.update({"total_records": count})
        my_dict.update({'per_page':per_page,'page':page, 'next_page':int(page) + 1,'prev_page': (int(page) - 1) if int(page)> 1 else 1, 'total_pages': (count // per_page) + 1})

        return make_response(jsonify(my_dict), 200)
