from sayhello import db
from datetime import datetime


class Message(db.Model):
    __tablename__='messages'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)  #插入记录时才执行datetime.now()
