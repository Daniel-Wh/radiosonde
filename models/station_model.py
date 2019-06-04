from db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


# class that models the individual stations
class StationModel(db.Model):

    __tablename__ = "stations"  # table name is stations

    id = db.Column(db.INTEGER, primary_key=True)  # column in table for id that will be represented in both tables
    name = db.Column(db.String(10))  # column in table for the name of the station(max length of 10)
    station_number = db.Column(db.INTEGER)  # column in table for identifying number for each station
    station_lat = db.Column(db.REAL)  # column in table for latitude location for station
    station_lon = db.Column(db.REAL)  # column in table for longitude location for station
    children = relationship("StationData", backref='stations')  # links the stations table with the station_data table

    # initializes an instance of StationModel with the data for all columns given as parameters
    def __init__(self, name, number, lat, lon):
        self.name = name
        self.station_number = number
        self.station_lat = lat
        self.station_lon = lon

    # saves the StationModel(self) to the database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # method that finds the right row by the name given
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    # method that finds the right row by the id given
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    # method that finds the right row by the staition number
    @classmethod
    def find_by_station_num(cls, station_number):
        return cls.query.filter_by(station_number=station_number).first()


# class that models the data taken at each station
class StationData(db.Model):

    __tablename__ = "station_data"  # name of the table is station_data

    id = db.Column(db.INTEGER, primary_key=True)  # column in table for id for each individual set of data
    pressure = db.Column(db.REAL)  # column in table for the pressure at that station
    height = db.Column(db.INTEGER)  # column in table for height where the temp is a minimum
    temp = db.Column(db.REAL)  # column in table for the minimum temp
    station_id = db.Column(db.INTEGER, ForeignKey('stations.id'))  # StationModel id
    # station_name = db.Column(db.String(10))
    date = db.Column(db.Integer)  # column in table for date the data was taken( may break into year/month and day)

    # initializes the StationData model to have the data specified for all columns given as parameters
    def __init__(self, pressure, height, temp, date):
        self.pressure = pressure
        self.height = height
        self.temp = temp
        # self.station_name = station_name
        self.date = date

    # saves the station data to the database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
