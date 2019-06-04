from datetime import datetime
from flask import Flask
from models.station_model import StationData, StationModel
from db import db
# import pandas as pd
import numpy as np


from siphon.simplewebservice.wyoming import WyomingUpperAir

date = datetime(2019, 1, 20)
station = 'BRO'

df = WyomingUpperAir.request_data(date, station)


x = 0
new_station = None
while x < len(df['pressure']):
    if x == 0:
        new_station = StationModel(df['station'][x],
                                   df['station_number'][x],
                                   df['latitude'][x],
                                   df['longitude'][x])
        new_station.save_to_db()
    else:
        date = int(df['date'][x].replace('-', ''))
        data = StationData(df['pressure'][x],
                           df['height'][x],
                           df['temperature'][x],
                           df['station'][x],
                           date, station=new_station)
        data.save_to_db()
    x += 1
