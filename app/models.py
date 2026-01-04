from datetime import datetime
from .extensions import db

class Task(db.Model):
    """
    Task model represents a todo task in the system.
    """
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(120),nullable=False)
    description =db.Column(db.Text)
    is_completed =db.Column(db.Boolean,default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Task {self.title}>"

