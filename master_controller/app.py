# -*- coding: utf-8 -*-
"""Example Master Controller with a REST API."""
import random
import json

from flask_api import FlaskAPI, status, exceptions
from flask import request


APP = FlaskAPI(__name__)


@APP.route('/state', methods=['GET', 'PUT'])
def state():
    """SDP State"""
    states = ['OFF', 'INIT', 'STANDBY', 'ON', 'DISABLE', 'FAULT', 'ALARM',
              'UNKNOWN']

    if request.method == 'PUT':
        requested_state = request.data.get('state', '').upper()
        if requested_state not in states:
            return ({'error': 'Invalid state: {}'.format(requested_state),
                     "allowed_states": states},
                    status.HTTP_400_BAD_REQUEST)
        return ({'message': 'Triggered state: {}'.format(requested_state)},
                status.HTTP_202_ACCEPTED)

    return {'state': random.choice(states)}
