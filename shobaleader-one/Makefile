PROJECT = $(shell basename $$(pwd))
all: black test clean

black:
	poetry run black .

test:
	poetry run pytest \
		--random-order \
		--cov \
		-vv \
		-s \
		--exitfirst \
		tests/**test_*.py

install:
	poetry install

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;

push-code: clean
	rsync -av /opt/${PROJECT} pi@${PIHOST}:
	scp /opt/${PROJECT}/Makefile.pi pi@${PIHOST}:${PROJECT}/Makefile

