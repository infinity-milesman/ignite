from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from config import app_config


db = SQLAlchemy()
migrate = Migrate(compare_type=True)

def init_app(config):
    app = Flask(__name__)
    app.config.from_object(app_config[config])
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def health_check():
        return "Server is running...."

    with app.app_context():

        from .book import book_bp
        app.register_blueprint(book_bp, url_prefix='/book')

        return app



