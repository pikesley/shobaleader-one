PROJECT = $(shell basename $$(pwd))
all: fix-imports style test clean

travis: style test-no-cov

style:
	python -m pylama

test:
	python -m pytest \
		--random-order \
		--cov \
		-vv \
		-s \
		--exitfirst

install:
	python -m pip install -r requirements.txt

clean:
	@find . -depth -name __pycache__ -exec rm -fr {} \;
	@find . -depth -name .pytest_cache -exec rm -fr {} \;

fix-imports:
	isort -rc --atomic

push-code: clean
	rsync -av /opt/${PROJECT} pi@${PIHOST}:
	scp /opt/${PROJECT}/Makefile.pi pi@${PIHOST}:${PROJECT}/Makefile

