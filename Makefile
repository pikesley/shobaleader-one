PROJECT = shobaleader-one
ID = pikesley/${PROJECT}

all: build

build:
	docker build --tag ${ID} .

run:
	docker run \
		--volume $(shell pwd)/${PROJECT}:/opt/${PROJECT} \
		--volume $(shell echo ${HOME})/.ssh:/root/.ssh \
		--publish 5000:5000 \
		--env PIHOST=shoba.local \
		--interactive \
		--tty \
		${ID} \
		bash
