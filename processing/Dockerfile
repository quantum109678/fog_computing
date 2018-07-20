
FROM alpine:3.7
RUN apk add --no-cache python3-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools


COPY p1.py /p1.py


RUN pip3 install requests

RUN pip3 install python-firebase
