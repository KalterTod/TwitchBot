from app import db
import datetime
from sqlalchemy.sql import func

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime(), index=True, server_default=func.now())
    channel_name = db.Column(db.String(64), index=True)