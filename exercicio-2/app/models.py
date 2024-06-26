from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Todo {self.task}>'
    