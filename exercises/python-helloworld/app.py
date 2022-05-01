import json
import logging
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    # Logging a CUSTOM message
    app.logger.info('Main Request Successful')
    return "Hello World!"


@app.route('/status')
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('/status Request Successful')
    return response


@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('/metrics Request Successful')
    return response


if __name__ == "__main__":
    # Stream logs to a file, and set the default log level to DEBUG
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
