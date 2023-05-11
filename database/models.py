from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Boolean, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import ENUM

Base = declarative_base()


class Airport(Base):
    __tablename__ = "airports"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    code = Column(String(3), nullable=False)
    altitude = Column(Float, nullable=False)


class Flight(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    airport = Column(Integer, ForeignKey("airports.id"), nullable=False)
    flight_no = Column(String(10), nullable=False)
    bound = Column(String(1), ENUM("a", "d", name="operation_type", create_type=False), nullable=False)
    aircraft_type = Column(String(10), nullable=False)
    UniqueConstraint('airport_id', 'flight_no', name='unique_flight')


class Waypoint(Base):
    __tablename__ = 'waypoints'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    airport = Column(Integer, ForeignKey("airports.id"), nullable=False)
    name = Column(String(15), nullable=False)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    type = Column(String(15), nullable=False)
    exit_waypoint = Column(Boolean, nullable=False)


class Parameter(Base):
    __tablename__ = 'parameters'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    type = Column(String(20), nullable=False)
    name = Column(String(20), nullable=False, unique=True)
    value = Column(String(20), nullable=False)


class Runway(Base):
    __tablename__ = 'runways'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    airport = Column(Integer, ForeignKey("airports.id"), nullable=False)
    name = Column(String(3), nullable=False)
    name_other_end = Column(String(3), nullable=False)
    length = Column(Float, nullable=False)
    heading = Column(Float, nullable=False)
    x_init = Column(Float, nullable=False)
    y_init = Column(Float, nullable=False)
    active = Column(Integer, nullable=False)
    main_side = Column(Boolean, nullable=False)
