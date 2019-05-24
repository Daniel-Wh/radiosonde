from db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class StationModel(db.Model):

    __tablename__ = "stations"

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(10))
    station_number = db.Column(db.INTEGER)
    station_lat = db.Column(db.REAL)
    station_lon = db.Column(db.REAL)
    children = relationship("StationData", backref='station')

    def __init__(self, name, number, lat, lon):
        self.name = name
        self.station_number = number
        self.station_lat = lat
        self.station_lon = lon

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_station_num(cls, station_number):
        return cls.query.filter_by(station_number=station_number).first()


class StationData(db.Model):

    __tablename__ = "station_data"

    id = db.Column(db.INTEGER, primary_key=True)
    pressure = db.Column(db.REAL)
    height = db.Column(db.INTEGER)
    temp = db.Column(db.REAL)
    station_id = db.Column(db.INTEGER, ForeignKey('stations.id'))
    station_name = db.Column(db.String(10))
    date = db.Column(db.Integer)

    def __init__(self, pressure, height, temp, station_name, date):
        self.pressure = pressure
        self.height = height
        self.temp = temp
        self.station_name = station_name
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
