#!/usr/bin/env python3
# imports
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Define the base class
Base = declarative_base()

# Define the Student class representing the "users" table
class Student(Base):
    pass
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    
if __name__ == '__main__':
# Create an SQLite database in memory for this example
    engine = create_engine('sqlite:///students.db')

# Create the "users" table in the database
    Base.metadata.create_all(engine)