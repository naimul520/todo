from app import app,db
from datetime import datetime

class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250),nullable = False)
    desc = db.Column(db.Text,nullable = False)
    # create_at = db.column(db.DateTime, default = datetime.utcnow)




