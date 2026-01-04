from flask import Flask
from app.config import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models

    from .routes.tasks import task_bp
    app.register_blueprint(task_bp, url_prefix="/api/tasks")

    return app
