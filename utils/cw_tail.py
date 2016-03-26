import argparse
import boto3
import time

parser = argparse.ArgumentParser()
parser.add_argument('--log-group-name', required=True,
                    help="Name of the CloudWatch Logs Log Group")
parser.add_argument('--region', required=True, default='us-east-1',
                    help="Name of the AWS Region which to connect")
args = parser.parse_args()

client = boto3.client('logs', region_name=args.region)

log_group_name = args.log_group_name

t = client.describe_log_streams(
    logGroupName=log_group_name,
    orderBy='LastEventTime',
    descending=True
)

events = client.get_log_events(
    logGroupName=log_group_name,
    logStreamName=t['logStreams'][0]['logStreamName']
)
newlist = sorted(events['events'], key=lambda k: k['timestamp'], reverse=True)
start_time = newlist[0]['timestamp']

while True:
    t = client.describe_log_streams(
        logGroupName=log_group_name,
        orderBy='LastEventTime',
        descending=True
    )

    events = client.get_log_events(
        logGroupName=log_group_name,
        logStreamName=t['logStreams'][0]['logStreamName'],
        startTime=start_time
    )

    for event in events['events']:
        print event['message'].strip()
    if len(events['events']) > 0:
        newlist = sorted(
            events['events'], key=lambda k: k['timestamp'], reverse=True)
        start_time = newlist[0]['timestamp'] + 1
    time.sleep(5)
