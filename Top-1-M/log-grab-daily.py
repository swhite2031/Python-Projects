import sys
import subprocess
import json
import os
import csv
import datetime



# Variable Load
config = json.loads(open("parameters.json").read())
awspath = config["awspath"]
progpath = config["progpath"]
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

#Begin Log pull
cmd1 = ("aws" + " s3" + " sync" + " {}".format(awspath) + " {}".format(progpath) + "/logs-raw")
subprocess.call("{}".format(cmd1), shell=True)

#Begin Log Processing
listdir =("ls" + " {}".format(progpath) + "/logs-raw/dnslogs > dir.txt")
subprocess.call("{}".format(listdir),shell=True)


subprocess.call("gunzip -c" + " {}".format(progpath) + "/logs-raw/dnslogs/{}".format(yesterday) + "/*.gz " + "> " + "{}".format(progpath) + "/logs/{}".format(yesterday) + ".csv", shell=True)

#pull top 1 Million DNS Domains
cmd2 = ("curl http://s3-us-west-1.amazonaws.com/umbrella-static/top-1m.csv.zip --output top-1m.csv.zip")
cmd3 = ("unzip -o top-1m.csv.zip -d ./top")

subprocess.call("{}".format(cmd2), shell=True)
subprocess.call("{}".format(cmd3), shell=True)

with open("./top/top-1m.csv", "rt") as source:
    rdr = csv.reader( source )
    with open("./top/top-1m-final.csv", "wt") as result:
        wtr = csv.writer(result)
        for r in rdr:
            del r[0]
            wtr.writerow(r)

filed = open("{}".format(progpath) + "/logs/{}".format(yesterday) + ".csv", "r")
linelist = filed.readlines()
filed.close

filef = open("{}".format(progpath) + "/logs/{}".format(yesterday) + ".csv", "w")

for line in linelist:
    line = line.replace("(", "")
    line = line.replace(")", "")
    filef.write(line)

filef.close
