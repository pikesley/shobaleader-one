FROM python:3.7

ENV PROJECT shobaleader-one

RUN apt-get update && apt-get install -y make rsync

COPY docker-config/bashrc /root/.bashrc

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /opt/${PROJECT}
COPY ${PROJECT}/poetry.lock /opt/${PROJECT}/poetry.lock
COPY ${PROJECT}/pyproject.toml /opt/${PROJECT}/pyproject.toml
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ${PROJECT} /opt/${PROJECT}

