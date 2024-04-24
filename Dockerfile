FROM python:3.10-alpine
WORKDIR /usr/src/app/bot_forwarder
COPY requirements.txt /usr/src/app/bot_forwarder
RUN pip install -r /usr/src/app/bot_forwarder/requirements.txt
COPY . /usr/src/app/bot_forwarder
