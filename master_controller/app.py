# -*- coding: utf-8 -*-
"""Example Master Controller with a REST API."""
import random

from flask import Flask, jsonify, request


# Create Flask application
APP = Flask(__name__)


STATES = ['OFF', 'INIT', 'STANDBY', 'ON', 'DISABLE', 'FAULT', 'ALARM',
          'UNKNOWN']


@APP.route('/state', methods=['GET'])
def get_state():
    """Return the SDP State."""
    return jsonify(state=random.choice(STATES))

@APP.route('/state', methods=['POST'])
def trigger_state():
    """Trigger state change"""
    request_data = request.get_json(silent=False)
    state = request_data['state']
    return jsonify(message='Triggered state: ' + state)

@APP.errorhandler(404)
def not_found(error=None):
    """Example custom error handler"""
    response = jsonify(error='Invalid URL: ' + request.url)
    response.status_code = 404
    return response

if __name__ == '__main__':
    APP.run(debug=True)
