from flask import Flask, jsonify

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# creating engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()

# reflecting an existing database into a new model
Base=automap_base()
# reflecting the tables
Base.prepare(engine, reflect=True)

# Saving references to each table
Measurement=Base.classes.measurement
Station=Base.classes.station

# Creating our session (link) from Python to the DB
session=Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start></br>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation(): 
    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date <= '2017-08-23').\
    filter(Measurement.date >= '2016-08-24').\
    order_by(Measurement.date).all()

    precipitation = []
    for item in results:
        prcp_dict = {}
        prcp_dict["date"] = item.date
        prcp_dict["precipitation"] = item.prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    query = session.query(Station.station, Station.name).all()
    station=[]
    for element in query:
        station_dict={}
        station_dict["ID"] = element.station
        station_dict["Name"] = element.name
        station.append(station_dict)

    return jsonify(station)

@app.route("/api/v1.0/tobs")
def tobs():
    most_active = engine.execute("SELECT DISTINCT station, COUNT(prcp) AS prcp_count FROM measurement GROUP BY station ORDER BY prcp_count DESC").first()
    temp = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date > '2016-08-23').\
    filter(Measurement.station== most_active[0]).\
    order_by(Measurement.tobs).all()
    
    annual_temp=[]
    for item in temp:
        temp_dict={}
        temp_dict["Date"]=item.date
        temp_dict["TOBS"] = item.tobs
        annual_temp.append(temp_dict)

    return jsonify(annual_temp)

@app.route("/api/v1.0/<start>")
def start(start):
    try:
        start = dt.strptime(str(start), '%Y-%m-%d').strftime('%Y-%m-%d')
        
        min_temp = session.query(func.min(Measurement.tobs).label('Min_temp')).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <'2017-08-23')

        max_temp = session.query(func.max(Measurement.tobs).label('Max_temp')).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <'2017-08-23')

        avg_temp = session.query(func.avg(Measurement.tobs).label('Avg_temp')).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <'2017-08-23')

        start_range={}
        start_range["Min_temp"] = min_temp
        start_range["Max_temp"] = max_temp
        start_range["Avg_temp"] = avg_temp

        return jsonify(start_range)

    except:
        ValueError
        print("Please enter date in format: YYYY-MM-DD")


@app.route("/api/v1.0/<start>/<end>")
def end(start, end):
    try:
        start = dt.strptime(str(start), '%Y-%m-%d').strftime('%Y-%m-%d')
        end = dt.strptime(str(end), '%Y-%m-%d').strftime('%Y-%m-%d')
        
        min_temp2 = session.query(func.min(Measurement.tobs).label('Min_temp')).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end)

        max_temp2 = session.query(func.max(Measurement.tobs).label('Max_temp')).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end)

        avg_temp2 = session.query(func.avg(Measurement.tobs).label('Avg_temp')).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end)

        end_range={}
        end_range["Min_temp"] = min_temp2
        end_range["Max_temp"] = max_temp2
        end_range["Avg_temp"] = avg_temp2

        return jsonify({f"The minimum temprature for selected date range is {end_range[0]}, the maximum temperature is {end_range[1]} and average {end_range[2]} "})

    except:
        ValueError
        print("Please enter date in format: YYYY-MM-DD")

if __name__ == "__main__":
    app.run(debug=True)