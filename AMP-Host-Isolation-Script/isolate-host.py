#!/usr/bin/env python
import sys
import json
import urllib2
import requests
import socket
'''
@Author Steven White stewhit2@cisco.com
Populate the client_id and api_key variables
Usage "python isolate-host.py {ip address}"
un-remark the action lines to isolate host or un-isolate host
You will need read/write access on the amp_client_id and amp_client_password
'''

amp_client_id = " "
amp_client_password = " "

ip = sys.argv[1]
url1 = ("https://api.amp.cisco.com/v1/computers?internal_ip={}".format(ip))

response = requests.get(url1, auth=(amp_client_id, amp_client_password))

response_json = response.json()
#print(response_json)

for computer in response_json['data']:
    connector_guid = computer['connector_guid']
    print(connector_guid)

# Used to isolate the specified host
url2 = ("https://api.amp.cisco.com/v1/computers/{}".format(connector_guid) + "/isolation")
#un-remark to isolate host
action = requests.put(url2, auth=(amp_client_id,amp_client_password))
#un-remark to stop isolation
#action = requests.delete(url2, auth=(amp_client_id,amp_client_password))
