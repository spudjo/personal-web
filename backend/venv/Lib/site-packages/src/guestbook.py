from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, Flask
)

from .database.database import Session, engine, Base
from .database.guestbook import Guestbook, GuestbookSchema

bp = Blueprint('guestbook', __name__)


@bp.route('/guestbook')
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


@bp.route('/guestbook', methods=['POST'])
def add_guestbook():
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