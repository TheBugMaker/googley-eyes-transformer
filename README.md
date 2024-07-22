Web application that adds googley eyes to pictures

**Original Image:**
![before](assets/faces.png?raw=true "Original Image")

**After:**
![after](assets/faces_after.jpeg?raw=true "After")


# Requirements 

- Docker

# How to run

`make run`

and then navigate to localhost:5000

# Available commands
```
help                           Display this help
install                        Install dependencies using Poetry
docker-build                   Build the Docker image
run                            Run app using Docker
test                           Run tests using pytest inside docker container
api-docs                       starts swagger ui in a docker container
```

# Project structure

```
api/
  └── swagger.yaml
src/
  └── app/
      ├── templates/
      ├── containers.py
      ├── routes.py
      ├── services.py
  └── transformer/
      ├── assets/
      ...
      ├── utils.py
tests/
  └── app/
      ├── __init__.py
      ├── test_transform_image_route.py
  └── transformer/
      ├── __init__.py
      ├── test_image_transformer.py
Dockerfile
poetry.lock
pyproject.toml
```

## api
swagger.yaml: This file contains the OpenAPI (Swagger) specification for the API. It documents the available endpoints, request parameters, and responses.

##src
This is the main source directory containing the application and its components.

### app
This directory contains the main Flask application code.

templates: This directory contains HTML templates for rendering web pages.
containers.py: Defines the dependency injection container for managing services and their dependencies.
routes.py: Contains route definitions and view functions for the application.
services.py: Contains business logic and service layer code.

### transformer
This directory contains image processing and transformation logic.

assets/: This directory contains additional assets, such as needed images.
eye_detector.py: Contains logic for detecting eyes in an image.
eye_drawer.py: Contains logic for drawing on detected eyes.
image_transformer.py: Contains the ImageTransformer class that applies transformations to images.
utils.py: Contains utility functions for image processing.

##tests
This directory contains tests for the application components.
