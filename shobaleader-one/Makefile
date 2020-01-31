PROJECT = $(shell basename $$(pwd))
PIHOST = shobaleader.local

all: isort black lint test clean

black:
	poetry run black .

isort:
	poetry run isort --recursive --atomic

lint:
	poetry run pylint \
		--disable C0103 \
		--disable C0114 \
		--disable C0330 \
		--disable R0201 \
		--disable R0801 \
		--disable R0903 \
		lib/ tests/

test:
	poetry run pytest \
		--random-order \
		--cov \
		-vv \
		-s \
		--exitfirst

install:
	poetry install

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;
	@find . -depth -name ".coverage.*" -exec rm {} \;

push-code: clean
	rsync -av /opt/${PROJECT} pi@${PIHOST}:
	scp /opt/${PROJECT}/Makefile.pi pi@${PIHOST}:${PROJECT}/Makefile

run-api:
	poetry run python shobaserver.py
