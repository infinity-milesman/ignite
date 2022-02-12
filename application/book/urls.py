from . import book_bp
from .views import BookApi

book_bp.add_url_rule('/book_api', view_func=BookApi.as_view("get_book_api"), methods=['GET'])