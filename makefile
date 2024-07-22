# Variables
APP_NAME = googley-image-transformer
DOCKER_IMAGE = $(APP_NAME):latest

# Default target
.PHONY: help
help:  ## Display this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Poetry commands
.PHONY: install
install:  ## Install dependencies using Poetry
	poetry install

# Docker commands
.PHONY: docker-build
docker-build:  ## Build the Docker image
	sudo docker build -t $(DOCKER_IMAGE) .

.PHONY: run
run: docker-build  ## Run app using Docker
	sudo docker run --network host  $(DOCKER_IMAGE)

.PHONY: test
test:  ## Run tests using pytest inside docker container
	sudo docker run $(DOCKER_IMAGE) poetry run pytest

.PHONY: api-docs
api-docs:  ## starts swagger ui in a docker container
	sudo docker run -p 80:8080 -e SWAGGER_JSON=/swagger.yaml -v "$(PWD)/api/swagger.yaml":/swagger.yaml swaggerapi/swagger-ui
	echo docs are available using http://localhost
