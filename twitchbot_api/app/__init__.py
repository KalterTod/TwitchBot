from flask import Flask, request, jsonify
from config import Config
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_migrate import Migrate
from flask_graphql import GraphQLView

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.schemas import schema
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.route('/channel_rate', methods=['POST'])
def message_rate():
    params = {
        "channelName": request.get_json()['channelName']
    }

    result = db.session.execute(text("""
        SELECT *
        FROM 'messages'
        WHERE channel_name = :channelName"""), params=params).fetchall()

    format = "%Y-%m-%d %H:%M:%S"
    
    total_time = datetime.strptime(result[len(result) - 1].timestamp, format) - datetime.strptime(result[0].timestamp, format)
    total_time_seconds = total_time.total_seconds()
 
    return jsonify({
        "total_messages": len(result),
        "message_rate_seconds": len(result) / total_time_seconds,
        "message_rate_minutes": len(result) * 60 / total_time_seconds,
    })

@app.route('/channel_mood', methods=['POST'])
def channel_mood():

    ## Check messages only from the last hour
    time = datetime.now() - timedelta(hours=1)
    format = "%Y-%m-%d %H:%M:%S"
    
    params = {
        "channelName": request.get_json()['channelName'],
        "ts_hour_ago": datetime.strftime(time, format)
    }

    result = db.session.execute(text("""
        SELECT *
        FROM 'messages'
        WHERE channel_name = :channelName AND timestamp > :ts_hour_ago AND message LIKE "PogChamp" """), params=params).fetchall()
    
     ## channel mood is the number messages containing PogChamps in the last hour 
    return jsonify({
        "recent_pogchamps": len(result)
    })
        