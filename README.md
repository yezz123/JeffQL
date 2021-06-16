<p align="center"> 
    <img src="https://github.com/yezz123/yezz123/blob/master/img/school-of-athens.jpg" alt="School of Athena">
</p>

## JeffQL :rocket:

> Note : This is one of my learning path project on how i can code GraphQL in different environments ex. Django | Flask | FastAPI :love:

> I choose this Name JeffQL cause i have a Low level Friend with a Nickname Jeff i wish he understand that Python and JavaScript is the future :rocket:

- A Simple fastAPI authentication & Login API using GraphQL and JWT.

- Using `Graphene-Python` a library for building GraphQL APIs in Python easily, its main goal is to provide a simple but extendable API for making developers’ lives easier.

- Using `fastapi-jwt-auth` a FastAPI extension that provides JWT Auth support.

## Get Started :rocket:

- Clone the Repository into your local Machine :

```sh
git clone https://github.com/yezz123/JeffQL
```

- I prefer to create a virtual env to work in a good way :

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

- After running the file you can start now trying some Queries and mutations :rocket:.

## Resources :rocket:

- [GraphQL](https://fastapi.tiangolo.com/advanced/graphql/)

- [Getting started with GraphQL in Python with FastAPI and Graphene](https://itnext.io/getting-started-with-graphql-in-python-with-fastapi-and-graphene-abb4f3eb04f4)

- [Developing an API with FastAPI and GraphQL](https://testdriven.io/blog/fastapi-graphql/)

- [OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

- [FastAPI JWT Auth](https://indominusbyte.github.io/fastapi-jwt-auth/)