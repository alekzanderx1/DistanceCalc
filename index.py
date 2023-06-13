from flask import Flask, render_template, request, jsonify, Response
from math import radians, cos, sin, asin, sqrt


# We need to initialise the Flask object to run the flask app 
# By assigning parameters as static folder name,templates folder name
app = Flask(__name__, static_folder='static', template_folder='templates')


# Homepage endpoint
@app.route('/',methods=['GET'])
def main():
  # on GET we display the homepage  
  if request.method=='GET':
    return render_template('index.html')
  else:
    return Response(
        "Only GET Method allowed",
        status=400,
    )
  
# Calculation endpoint
@app.route('/calculateDistance',methods=['POST'])
def calculateDistance():
    if request.method=='POST':
        # Read request parameter
        request_data = request.get_json()
        print(f"Request_data: {request_data}")
        lon1, lat1 = request_data['pointA'].split(',')
        lon2, lat2 = request_data['pointB'].split(',')
        distance = haversine(float(lon1), float(lat1), float(lon2), float(lat2))
        result = dict()
        result['distance'] = distance
        return jsonify(result)
    else:
        return Response(
            "Only POST Method allowed",
            status=400,
        )
    
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return round(c * r,2)