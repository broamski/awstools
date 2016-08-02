import argparse
import boto3

"""
Query instances based upon tag data"
"""

parser = argparse.ArgumentParser()
parser.add_argument('-tn', '--tag-name', required=True)
parser.add_argument('-tv', '--tag-value', required=True)
parser.add_argument('--region', default='us-east-1')
args = parser.parse_args()

client = boto3.client('ec2', region_name=args.region)

instances = client.describe_instances(
    Filters=[
        {
            'Name': "tag:%s" % args.tag_name,
            'Values': [
                args.tag_value
            ]
        }]
)

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print "InstanceId: %s" % (instance['InstanceId'],)
        print "Private IP: %s" % (instance['PrivateIpAddress'],)
        tags = [tag for tag in instance['Tags'] if tag["Key"] == "Name"]
        print "Name Tag: %s" % (tags[0]['Value'],)
        print "--------------------------"
