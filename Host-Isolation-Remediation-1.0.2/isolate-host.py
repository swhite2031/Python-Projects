#!/usr/bin/env python
import sys
import json
import urllib2
import socket
import xml.etree.ElementTree as ET
import requests

'''
@Author Steven White stewhit2@cisco.com
Isolate Host Remediation
'''

dic = {}
tree = ET.parse('instance.conf')
root = tree.getroot()
for child in root[0]:
    dic[child.get('name')] = child.text

client_id = dic['client_id']
api_key = dic['api_key']
ip = sys.argv[2]
url1 = ("https://api.amp.cisco.com/v1/computers?internal_ip={}".format(ip))

response = requests.get(url1, auth=(client_id, api_key))

response_json = response.json()
#print(response_json)

for computer in response_json['data']:
    connector_guid = computer['connector_guid']
#    print(connector_guid)

# Used to isolate the specified host
url2 = ("https://api.amp.cisco.com/v1/computers/{}".format(connector_guid) + "/isolation")
action = requests.put(url2, auth=(client_id,api_key))
