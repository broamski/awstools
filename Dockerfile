FROM python:2.7.11
MAINTAINER "Brian Nuszkowski <nuszkowski@protonmail.com>"

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

CMD ["/bin/bash"]
