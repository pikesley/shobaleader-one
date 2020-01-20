PROJECT = $(shell basename $$(pwd))
all: black lint test clean

black:
	@poetry run black .

lint:
	@poetry run pylint \
		--disable all \
		--enable C0115 \
		--enable C0116 \
		--enable E0602 \
		--enable W0611 \
		--enable W0612 \
		lib/ tests/

test:
	@poetry run pytest \
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

push-code: clean
	rsync -av /opt/${PROJECT} pi@${PIHOST}:
	scp /opt/${PROJECT}/Makefile.pi pi@${PIHOST}:${PROJECT}/Makefile

