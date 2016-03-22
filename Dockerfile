FROM python:2.7.11
MAINTAINER "Brian Nuszkowski <nuszkowski@protonmail.com>"

ADD requirements.txt /tmp/requirements.txt

RUN apt-get update -y && \
    apt-get install vim -y && \
    pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    groupadd -g 666 worker && \
    useradd -m -g 666 -s /bin/bash -g worker worker

ADD utils /home/worker/utils

USER worker
WORKDIR /home/worker
CMD ["/bin/bash"]
