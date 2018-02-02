# -*- coding: utf-8 -*-
"""Example Master Controller with a REST API."""
import random
from flask_api import FlaskAPI
from flask import request


APP = FlaskAPI(__name__)


@APP.route('/state', methods=['GET', 'PUT'])
def sdp_state():
    """SDP State"""
    states = ['OFF', 'INIT', 'STANDBY', 'ON', 'DISABLE', 'FAULT', 'ALARM',
              'UNKNOWN']

    if request.method == 'PUT':
        request_data = request.get_json(silent=False)
        state = request_data['state'].upper()
        if state.upper() not in states:
            return {'error': 'Invalid state: {}'.format(state)}, 400
        return {'message': 'Triggered state: {}'.format(state)}, 202

    return {'state': random.choice(states)}
