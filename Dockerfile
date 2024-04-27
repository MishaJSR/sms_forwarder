FROM python:3.10-alpine
WORKDIR /usr/src/app/bot_forwarder_my
COPY requirements.txt /usr/src/app/bot_forwarder_my
RUN pip install -r /usr/src/app/bot_forwarder_my/requirements.txt
COPY . /usr/src/app/bot_forwarder_my
