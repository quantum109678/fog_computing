
FROM alpine:3.7
RUN apk add --no-cache python3-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
COPY api_example /api_example
COPY iotdevices /iotdevices
COPY api_example /api_example
COPY manage.py /manage.py
RUN pip3 install django
RUN pip3 install djangorestframework
RUN python3 manage.py migrate
RUN pip3 install pysqlite3
