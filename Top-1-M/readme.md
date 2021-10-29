Purpose:
To satisfy the requirement to identify traffic to sites not listed in the top 1 million sites visited

Script purposes
1. LogAnalysis.py  - Analyze the previous day logs and generate a report
2. LogAnalysisManual.py - Analyze specific day logs and generate a reports
3. log-grab-daily.py - Grab logs from Umbrella and the latest top 1 million sites file and process the previous days logs for analysis
4. log-grab.py - Grab logs from Umbrella, the latest top 1 million file and process all captured logs for analysis 

Prerequisites:
1. Enable logging of your Umbrella DNS Data
2. Install and configure the AWS CLI
3. Modify parameters.json with your specific aws and program progpath
4. Schedule the scripts to download and process logs

Enable logging of your Umbrella DNS Data:
1. From Admin --> Log Management Select either your Cisco managed or company S3 Bucket
2. Select your Data Center and Retention Duration
3. Save your selections and continue
4. VERY IMPORTANT - Save your Data Path, Access Key and Secret Key from the activation complete screen

Install and configure AWS CLI:
Scripts were tested with AWS CLI V1 and V2.  Instructions from Amazon can be found
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
Your Access Key and Secret Key will be used here to authenticate your requests

Modify parameters.json:
There are 2 settings in parameters.json.  awspath and progpath
1. awspath is the Data Path information you SAVED when you enabled logging in Umbrella
2. progpath is simply the path to this programs directory.
  a. without it your logs will not be in the right location

Schedule the scripts to download and process logs
1. Schedule log-grab-daily.py to run.  Linux users would most likely use crontab to accomplish this
  a. I suggest you run it in the early morning to get all the previous days logs.
2. Schedule LogAnalysis.py to run sometime after.  Depending on the amount of logs gathered, speed of Your
Internet connection.... etc. will determine how long after.

final reports will be found in {progpath}/final
