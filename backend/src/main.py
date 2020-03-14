# coding=utf-8

from .database.database import Session, engine, Base
from .database.guestbook import Guestbook

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
exams = session.query(Guestbook).all()

if len(exams) == 0:
    # create and persist dummy exam
    post = Guestbook("Shawn", "First guestbook post!.", "script")
    session.add(post)
    session.commit()
    session.close()

    # reload exams
    guestbook = session.query(Guestbook).all()

# show existing exams
print('### Guestbook:')
for post in guestbook:
    print(f'({post.id}) {post.name} - {post.message}')