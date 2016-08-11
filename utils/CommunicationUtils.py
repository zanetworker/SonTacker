
__author__ = 'zanetworker'

import ConfigurationUtils
import requests
import os
import json


from SonatackerExceptions import SonatackerException
from CommonUtils import log_this
from Constants import *

URI = {'auth': AUTH_URI, 'version': VERSION_URI}
TACKER_CRED = ConfigurationUtils.load_tacker_credentials()
TACKER_CONN = ConfigurationUtils.load_tacker_connection_data()


def _construct_root_uri():
    return
    {
        'auth_uri':  "http://{}:{}{}".format(TACKER_CONN['endpoint'], TACKER_CONN['auth_port'], URI['auth']),
        'service_uri':"http://{}:{}{}".format(TACKER_CONN['endpoint'], TACKER_CONN['service_port'], URI['version'])
    }



def _request(uri_type='service_uri', json_payload='{}', http_verb='GET', params=None, headers=None):


    try:
        if http_verb == "PUT":
            req = requests.put(_construct_root_uri()[uri_type], json=json_payload, headers = headers)

        elif http_verb == 'POST':
            req = requests.post(_construct_root_uri()[uri_type], json=json_payload, headers=headers)

        else:  # Default to GET
            req = requests.get(_construct_root_uri()[uri_type], headers=headers)

        if req.status_code not in [STATUS_OK, STATUS_PENDING]:

            raise SonatackerException(
                http_status_code=req.status_code,
                message=req.text)

        return req.json(), req.status_code

    except requests.ConnectionError as conn_err:
        raise SonatackerException(message=conn_err.message)

    except requests.HTTPError as http_err:
        raise SonatackerException(message=http_err.message)

    except requests.RequestException as req_err:
        raise SonatackerException(message=req_err.message)

    except ValueError:
        return

def authenticate(username=TACKER_CRED['username'],
                 password=TACKER_CRED['password'],
                 tenantName=TACKER_CRED['tenant-id']):

    auth_data = {'auth':
        {
            'passwordCredentials':
                {
                    'username': username,
                    'password': password
                },
            'tenantName': tenantName
        }
    }

    headers = {'Content-Type': 'application/json'}

    return _request(uri_type='auth-uri', json_payload=auth_data, headers=headers, http_verb='POST')[0]


def get_version():
    return _request()