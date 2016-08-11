__author__  = 'zanetworker'

from ConfigParser import SafeConfigParser
import CommonUtils as CommonUtil


parser = SafeConfigParser()

try:
    config_file = CommonUtil.get_file_location('config', 'tacker.ini')
    parser.read(config_file)

except Exception as e:
    print e.message



def load_tacker_credentials():

    results = {
        'username': parser.get('credentials', 'USERNAME'),
        'password': parser.get('credentials', 'PASSWORD'),
        'tenant-id': parser.get('credentials', 'TENANT-ID')
    }

    return results

def load_tacker_connection_data():

    results = {
        'endpoint': parser.get('connection', 'ENDPOINT'),
        'auth_port': parser.get('connection', 'AUTH_PORT'),
        'service_port': parser.get('connection', 'SERVICE_PORT')
    }

    return results


