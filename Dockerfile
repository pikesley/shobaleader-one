FROM python:3.7

ENV PROJECT shobaleader-one

RUN apt-get update && apt-get install -y make rsync

COPY docker-config/bashrc /root/.bashrc

WORKDIR /opt/${PROJECT}
COPY ${PROJECT}/requirements.txt /opt/${PROJECT}/requirements.txt
COPY ${PROJECT}/Makefile /opt/${PROJECT}/Makefile
RUN pip install --upgrade pip
RUN make install

COPY ${PROJECT} /opt/${PROJECT}

