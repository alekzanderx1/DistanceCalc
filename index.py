from flask import Flask, render_template, request, jsonify, Response

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
        
        result = dict()
        result['distance'] = 12.0
        return jsonify(result)
    else:
        return Response(
            "Only POST Method allowed",
            status=400,
        )