from flask import Blueprint

book_bp = Blueprint('book_bp', __name__)

# from . import views
from . import models
from . import urls