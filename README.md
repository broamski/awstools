# awstools [![Docker Repository on Quay](https://quay.io/repository/broamski/awstools/status "Docker Repository on Quay")](https://quay.io/repository/broamski/awstools)

## Usage
    docker pull quay.io/broamski/awstools
    docker run --rm -it -v ~/.aws:/home/worker/.aws quay.io/broamski/awstools

## Included Tools
```
ecs\
    task_def_diff.py - Perform a visual diff of Elastic Container Service Task Definitions
cloudwatch\
    cw_logs_tail.py - Tail a CloudWatch Logs log group, similar to your favorite command: tail -f <file>
```
