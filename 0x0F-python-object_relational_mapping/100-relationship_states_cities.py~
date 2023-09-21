#!/usr/bin/python3
"""
script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name))

    session = Session(engine)
    new_state = State(name="California")
    session.add(new_state)
    session.commit()
    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()
    session.close()
