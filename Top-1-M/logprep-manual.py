import sys
import subprocess
import json
import os
import datetime


# Variable Load
config = json.loads(open("parameters.json").read())
awspath = config["awspath"]
progpath = config["progpath"]
day = sys.argv[1]

filed = open("{}".format(progpath) + "/logs/{}".format(day) + ".csv", "r")
linelist = filed.readlines()
filed.close

filef = open("{}".format(progpath) + "/logs/{}".format(day) + ".csv", "w")

for line in linelist:
    line = line.replace("(", "")
    line = line.replace(")", "")
    filef.write(line)

filef.close
