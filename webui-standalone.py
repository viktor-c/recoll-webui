#!/usr/bin/env python
import os
import argparse
import webui

# handle command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', default='127.0.0.1',help='address to bind to [127.0.0.1]')
parser.add_argument('-p', '--port', default='8080', type=int, help='port to listen on [8080]')
#give the user the chance to use custom recoll config files when invoking this script. 
#When initialised without a parameter rclConfig will try to find a recoll.conf file in the home directory of the user.
#when using custom recoll.conf files give the possibility to the user to specify the base directory where the conf file resides
#this argument will be set in webui.py and given to rclconfig.py
parser.add_argument('-c', '--config', default=None, help='location of the recoll.conf file')
args = parser.parse_args()

# change to webui's directory and import
if os.path.dirname(__file__) != "":
    os.chdir(os.path.dirname(__file__))

webui.recoll_config_path = args.config
# set up webui and run in own http server
webui.bottle.debug(True)
webui.bottle.run(host=args.addr, port=args.port, reloader=False)

# vim: foldmethod=marker:filetype=python:textwidth=80:ts=4:et
