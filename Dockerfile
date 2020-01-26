FROM python:3.7

ENV PROJECT shobaleader-one

RUN apt-get update && apt-get install -y curl make rsync

COPY docker-config/bashrc /root/.bashrc

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN ln -s /root/.poetry/bin/poetry /usr/local/bin/

WORKDIR /opt/${PROJECT}
COPY ${PROJECT}/poetry.lock /opt/${PROJECT}/poetry.lock
COPY ${PROJECT}/pyproject.toml /opt/${PROJECT}/pyproject.toml
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ${PROJECT} /opt/${PROJECT}

