import argparse
import boto3
import difflib
import json

parser = argparse.ArgumentParser()
parser.add_argument('--task-definition', required=True)
parser.add_argument('--region', default='us-east-1')
parser.add_argument('--versions', required=True,
                    help="Provide versions in <num>:<num> format. e.g. 28:29")
args = parser.parse_args()

ecs_client = boto3.client('ecs', region_name=args.region)
version_a, version_b = args.versions.split(":")

a_results = ecs_client.describe_task_definition(
    taskDefinition="%s:%s" % (args.task_definition, version_a)
)

b_results = ecs_client.describe_task_definition(
    taskDefinition="%s:%s" % (args.task_definition, version_b)
)

aa = json.dumps(
    a_results['taskDefinition'], sort_keys=True,
    indent=4, separators=(',', ': ')).splitlines()
bb = json.dumps(
    b_results['taskDefinition'], sort_keys=True,
    indent=4, separators=(',', ': ')).splitlines()

d = difflib.Differ()
diff = d.compare(aa, bb)
print '\n'.join(diff)
