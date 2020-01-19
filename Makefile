PROJECT = shobaleader-one
ID = pikesley/${PROJECT}

all: build

build:
	docker build --tag ${ID} .

run:
	docker run \
		--volume $(shell pwd)/${PROJECT}:/opt/${PROJECT} \
		--volume $(shell echo ${HOME})/.ssh:/root/.ssh \
		--env PIHOST=shobaleader.local \
		--interactive \
		--tty \
		${ID} \
		bash
