#!/usr/bin/python3
"""Script that lists all States and their Cities via relationship."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
import relationship_city  # noqa

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        cities = sorted(state.cities, key=lambda c: c.id)
        for city in cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
