import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #username and password necessary for login account
    id = Column(Integer, primary_key=True)
    user_name = Column(String(120), nullable=False)
    password_hash = Column(String(80), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(120), nullable=False)
    user_favorites = Column(Integer, ForeignKey("favorites.id"))#stakes relationship between user and it's favorites


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #ForeignKey is used to establish a relationship, the table "name".id is the link
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("user.id")) #ForeignKey is used to establish a relationship, the table name.id is the link
    title = Column(String(32))
    content = Column(String(250))
    create_time = Column(DateTime)

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    favorite_char_id = Column(Integer, ForeignKey("characters.id"))#stakes relationship between favorites and character tables
    favorite_planet_id = Column(Integer, ForeignKey("planets.id"))#stakes relationship between favorites and planets table
    favorite_vehicle_id = Column(Integer, ForeignKey("vehicles.id"))#you know the drill by now

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    gender = Column(String(6))
    eye_color = Column(String(32))
    birth_year = Column(String(20))#string to accomodate all characters

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    population = Column(Integer)
    terrain = Column(String(250))


class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    max_atmosphering_speed = Column(Integer)
    passengers = Column(Integer)
    crew = Column(Integer)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
