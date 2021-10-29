import csv
import os
import subprocess
import sys
import json
import datetime

#Load Variables
today = datetime.date.today()
yesterday = sys.argv[1]
config = json.loads(open("parameters.json").read())
awspath = config["awspath"]
progpath = config["progpath"]

#Begin File Processing
topopen = open("{}".format(progpath) + "/top/top-1m-final.csv", "r")
toppath = ("{}".format(progpath) + "/top/top-1m-final.csv")
top = topopen.readline()
for line in top:
    line.strip("\n")
actionitems = open("{}".format(progpath) + "/final/" + "{}".format(yesterday) + ".csv" , "w")
actionpath = ("{}".format(progpath) + "/final/" + "{}".format(yesterday) + ".csv")


cmd1 = ("echo Datetime, Hostname, InternalIP, Destination, >> {}".format(actionpath))
logpath = ("{}".format(progpath) + "/logs/" + "{}".format(yesterday) + ".csv")

with open('{}'.format(logpath)) as csv_file:
    columnlist = ['Datetime' , 'Hostname' , 'Policies' , 'InternalIP' , 'ExternalIP' , 'Action' , 'DnsType' , 'Type' , 'Destination' , 'Classification' , 'ID1' , 'ID2' , 'ID3']
    csv_reader = csv.DictReader(csv_file, fieldnames=columnlist)

    for row in csv_reader:
        dest = (row['Destination'] )
        dest= dest.rstrip(dest[-1])
        cmd = ("cat {}".format(toppath) + " | " + " grep -c {}".format(dest))

        iit = subprocess.call("{}".format(cmd), shell=True)
        if iit != 0:
            print(iit)
            cmd2 = ("echo {}".format(row['Datetime']) + " , " + "{}".format(row['Hostname']) + " , " + "{}".format(row['InternalIP']) + " , " + "{}".format(dest) + " >> {}".format(actionpath))
            subprocess.call("{}".format(cmd2), shell=True)



        else:
            pass
