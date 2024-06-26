#!/usr/bin/python3
"""Module that adds a city and its associated state\
        to a MySQL database using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create the database tables based on the defined models
    Base.metadata.create_all(engine)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Create a new city and its associated state
    state = State(name="California")
    city = City(name="San Francisco", state=state)

    # Add the new city and associated state to the session
    session.add(state)
    session.add(city)

    # Commit the session to persist the changes in the database
    session.commit()

0x0F-python-object_relational_mapping/100-relationship_states_cities.sql

-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

SELECT * FROM states;
SELECT * FROM cities;

0x0F-python-object_relational_mapping/101-relationship_states_cities_list.py

#!/usr/bin/python3
"""Module that lists all State objects, and corresponding City objects,\
        contained in the mySQL database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create a database engine using the provided arguments
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Retrieve all states from the database and order them by ID
    for state in session.query(State).order_by(State.id):
        # Print state ID and name
        print("{}: {}".format(state.id, state.name))

        # Iterate over the cities associated with the current state
        for city in state.cities:
            # Print city ID and name
            print("    {}: {}".format(city.id, city.name))
