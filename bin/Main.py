import os, sys, argparse, getpass
import json

parent_dir = "/home/zanetworker/PycharmProjects/Sonatacker/utils"
sys.path.append(parent_dir)

from CommunicationUtils import *


class PasswordPromptAction(argparse.Action):

    def __init__(self,
             option_strings,
             dest=None,
             nargs=0,
             default=None,
             required=False,
             type=None,
             metavar=None,
             help=None):

        super(PasswordPromptAction, self).__init__(
             option_strings=option_strings,
             dest=dest,
             nargs=nargs,
             default=default,
             required=required,
             metavar=metavar,
             type=type,
             help=help)

    def __call__(self, parser, args, values, option_string=None):
        password = getpass.getpass()
        setattr(args, self.dest, password)



def get_token_id(auth_resposne):
         return auth_response['access']['token']['id'] if auth_response else None

if __name__ == "__main__":
    text = "Welcome to Sonatacker, a lightweight Tacker client"
    parser = argparse.ArgumentParser(description=text)

    parser.add_argument('-u', '--user',
                        help= 'the username to authenticate with',
                        dest= 'user',
                        type= str,
                        required= False)

    parser.add_argument('-p', '--password',
                        help= 'the password to authenticate with',
                        dest= 'password',
                        action= PasswordPromptAction,
                        type= str,
                        required=False)

    parser.add_argument('-c', '--create-vnf',
                        help='this will create a vnf from the specified vnfd',
                        dest='user',
                        type=str,
                        required=False)

    parser.add_argument('-d', '--create-vnfd',
                        help='this will create a custom vnfd',
                        dest='password',
                        type=str,
                        required=False)
    try:

        args = parser.parse_args()
        auth_response = authenticate()
        token = get_token_id(auth_response)
        print token
    except Exception as e:
        print e.message