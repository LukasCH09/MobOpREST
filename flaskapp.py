from stations import StationItem, stationList
from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/stations/v1')
def stationsv1():
    return stationList[0].toJson()

@app.route('/stations/v2')
def stationsv2():
    toReturn = {}
    #toReturn = [x.toJson() for x in stationList] 
    toReturn = stationList[0].toJson()

    return make_response(toReturn)

if __name__ == '__main__':
    app.run()
