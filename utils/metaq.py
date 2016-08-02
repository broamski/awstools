import argparse
import boto3
import sys

"""
Query for instances based upon tag data"
"""

parser = argparse.ArgumentParser()
parser.add_argument('-q', '--query-type', required=True,
                    choices=["key", "value", "both"])
parser.add_argument('-k', '--key')
parser.add_argument('-v', '--value')
parser.add_argument('--region', default='us-east-1')
args = parser.parse_args()


if args.query_type == "key":
    if args.key is None:
        sys.exit("Must provide --key when query type is 'key'")
    filter = {
        'Name': "tag-key",
        'Values': [
            args.key
        ]
    }

if args.query_type == "value":
    if args.value is None:
        sys.exit("Must provide --value when query type is 'value'")
    filter = {
        'Name': "tag-value",
        'Values': [
            args.value
        ]
    }

if args.query_type == "both":
    if args.key is None:
        sys.exit("Must provide --key")

    if args.value is None:
        sys.exit("Must provide --value")

    filter = {
        'Name': "tag:%s" % (args.key,),
        'Values': [
            args.value
        ]
    }


client = boto3.client('ec2', region_name=args.region)

instances = client.describe_instances(
    Filters=[
        filter
    ]
)

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print "InstanceId: %s" % (instance['InstanceId'],)
        public_ip = instance.get('PublicIpAddress')
        if public_ip is not None:
            print "Public IP: %s" % (public_ip,)
        private_ip = instance.get('PrivateIpAddress')
        if private_ip is not None:
            print "Private IP: %s" % (private_ip,)
        tags = [tag for tag in instance['Tags'] if tag["Key"] == "Name"]
        if len(tags) > 0:
            print "Name Tag: %s" % (tags[0]['Value'],)
        print "--------------------------"
