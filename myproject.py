
#import sys
#sys.stdout = open('output_file', 'w')
import json
import requests
from flask import Flask,request,jsonify
from main import fact_check

app = Flask(__name__)


# if the button "showResults" is clicked , redirect the user to the results page carrying the textfield value in the request object


# direct the user to the main page when the app starts
@app.route("/", methods=['GET', 'POST'])
def checkClaim():
    print("recieved a request with the claim:")
    #return "Hi"
    #claim = request.form['claim']
    json = request.get_json()
    claim = json['claim']
    print(claim)
    report = fact_check(claim)
    return jsonify(report=report)

if __name__=="__main__" :
    app.run(host='0.0.0.0')
