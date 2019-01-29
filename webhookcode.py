import json
import os
import requests

from flask import Flask

from flask import request

from flask import make_response

##Flask app should start in global layout

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True,force=True)
    print(json.dumps(req, indent=4))
    r= make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeResponse(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    date = parameters.get("date")
    r = requests.get('https://michelin-digital-prod.apigee.net/search/v2'+city+'&appid=731814cd02f9d71cfb5ed382c4342c88')
    json_object = r.json()
    
    
    
    speech = "The forecast for" +city+ "for "+date+ " is " + condition
    return {
        "speech":speech,
        "displayText":speech,
        "source":"apiai-weather-webhook"
    }
    
    
    if __name__ == '__main__':
        port = int(os.getenv('PORT',5000))
        print("Starting app on port %d" % port)
        app.run(debug=False, port=port, host='0.0.0.0')

