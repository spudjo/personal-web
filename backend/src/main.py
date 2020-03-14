# coding=utf-8

from flask import Flask, jsonify, request
from flask_cors import CORS
from .database.database import Session, engine, Base
from .database.guestbook import Guestbook, GuestbookSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)
# generate database schema
Base.metadata.create_all(engine)


@app.route('/guestbook')
def get_guestbook():
    # fetching from the database
    session = Session()
    guestbook_objects = session.query(Guestbook).all()

    # transforming into JSON-serializable objects
    schema = GuestbookSchema(many=True)
    guestbook = schema.dump(guestbook_objects)

    # serializing as JSON
    session.close()
    return jsonify(guestbook)


@app.route('/guestbook', methods=['POST'])
def add_exam():
    # mount exam object
    new_post = GuestbookSchema(only=('name', 'message')).load(request.get_json())
    guestbook = Guestbook(**new_post, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(guestbook)
    session.commit()

    # return created exam
    new_post = GuestbookSchema().dump(guestbook)
    session.close()
    return jsonify(new_post), 201
