<p align="center"> 
    <img src="https://github.com/yezz123/yezz123/blob/master/img/school-of-athens.jpg" alt="School of Athena">
</p>

## JeffQL :rocket:

> Note : Note : This is one of my learning path projects about how coding GraphQL in different environments ex. Django | Flask | FastAPI :heart:

> I chose the name JeffQL as I have a low level friend goes by the nickname Jeff and  I wish would understand that Python and JavaScript are the future :rocket:

- A Simple fastAPI authentication & Login API using GraphQL and JWT.

- Using `Graphene-Python` a library for building GraphQL APIs in Python easily, its main goal is to provide a simple but extendable API for making developers’ lives easier.

- Using `fastapi-jwt-auth` a FastAPI extension that provides JWT Auth support.

## Get Started :rocket:

- Clone the Repository into your local Machine :

```sh
git clone https://github.com/yezz123/JeffQL
```

- I prefer creating a virtual env to facilitate my workflow :

```sh
sudo pip3 install virtualenv

virtualenv venv

source venv/bin/activate
```

- Then Try to install the requirements :

```sh
pip install -r requirements.txt
```

- Now you can run the `main.py` using `uvicorn`, or use the file pre-created `start.py` :

```py
import uvicorn
import main

uvicorn.run(main.app, host="0.0.0.0", port=8080)
```

- After running the `start.py`, you can start now trying some Queries and mutations :rocket:.

## Resources :rocket:

- [GraphQL](https://fastapi.tiangolo.com/advanced/graphql/)

- [Getting started with GraphQL in Python with FastAPI and Graphene](https://itnext.io/getting-started-with-graphql-in-python-with-fastapi-and-graphene-abb4f3eb04f4)

- [Developing an API with FastAPI and GraphQL](https://testdriven.io/blog/fastapi-graphql/)

- [OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

- [FastAPI JWT Auth](https://indominusbyte.github.io/fastapi-jwt-auth/)