from models import Dog
from sqlalchemy import create_engine

def create_table(base, engine):
    base.metadata.create_all(engine)
    pass

def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    dogs = session.query(Dog)
    return ([dog for dog in dogs])
    pass

def find_by_name(session, name):
    firstname = session.query(Dog).filter_by(name=name).first()
    return firstname
    pass

def find_by_id(session, id):
    firstid = session.query(Dog).filter_by(id=id).first()
    return firstid
    pass

def find_by_name_and_breed(session, name, breed):
    first = session.query(Dog).filter_by(name=name , breed=breed).first()
    return first
    pass

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()
    session.refresh(dog)
    pass