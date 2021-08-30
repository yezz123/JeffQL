![JeffQL](.github/header.svg)

# JeffQL

A Simple FastAPI authentication & Login API using GraphQL and JWT.

## Getting Started

### Prerequisites

- Python 3.8.6 or higher
- FastAPI
- Docker

### Project setup

```sh
# clone the repo
$ git clone https://github.com/yezz123/JeffQL

# move to the project folder
$ cd JeffQL
```

### Creating virtual environment

- Install `pipenv` a global python project `pip install pipenv`
- Create a `virtual environment` for this project

```shell
# creating pipenv environment for python 3
$ pipenv --three

# activating the pipenv environment
$ pipenv shell

# if you have multiple python 3 versions installed then
$ pipenv install -d --python 3.8

# install all dependencies (include -d for installing dev dependencies)
$ pipenv install -d
```

### Running the Application

- To run the [Main](main.py) we need to use [uvicorn](https://www.uvicorn.org/) a lightning-fast ASGI server implementation, using uvloop and httptools.

```sh
# Running the application using uvicorn
$ uvicorn main:app

## To run the Application under a reload enviromment use -- reload
$ uvicorn main:app --reload
```

## Running the Docker Container

- We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the FastAPI app and then start the FastAPI app container.

```sh
$ docker build
```

- list all the docker images and you can also see the image `jeffql:latest` in the list.

```sh
$ docker images
```

- run the application at port 5000. The various options used are:

> - `-p`: publish the container's port to the host port.
> - `-d`: run the container in the background.
> - `-i`: run the container in interactive mode.
> - `-t`: to allocate pseudo-TTY.
> - `--name`: name of the container

```sh
$ docker container run -p 5000:5000 -dit --name JeffQL jeffql:latest
```

- Check the status of the docker container

```sh
$ docker container ps
```

## Preconfigured Packages

Includes preconfigured packages to kick start JeffQL by just setting appropriate configuration.

| Package                                                      | Usage                                                                        |
| ------------------------------------------------------------ | -----------------------------------------------------------------------------|
| [uvicorn](https://www.uvicorn.org/)                          | a lightning-fast ASGI server implementation, using uvloop and httptools.     |
| [graphene-python](https://graphene-python.org/)              | a library for building GraphQL APIs in Python easily.                        |
| [PyJWT](https://pyjwt.readthedocs.io/en/stable/)             | a Python library which allows you to encode and decode JSON Web Tokens (JWT).|
| [starlette](https://www.starlette.io/)                       | a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services. |

## Contributing

- Join the JeffQL Creator and Contribute to the Project if you have any enhancement or add-ons to create a good and Secure Project, Help any User to Use it in a good and simple way.

## License

This project is licensed under the terms of the MIT license.
