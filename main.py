from fastapi import Depends, FastAPI, Request
from graphene import Field, Mutation, ObjectType, Schema, String
from starlette.datastructures import URL
from starlette.graphql import GraphQLApp

from auth import auth_bearer

# locale imports:
from resolvers import login, user


class Query(ObjectType):
    me = Field(user.UserProfileQuery, lan=String(default_value="en"))

    def resolve_me(self, info, lan):

        return user.UserProfileQuery(language=lan)


class Mutation(ObjectType):
    login = login.UserLogin.Field()


app = FastAPI(
    title="JeffQL",
    description="FastAPI authentication & Login API using GraphQL and JWT.",
    version="1.0.0",
)

app.add_route("/", GraphQLApp(schema=Schema(query=Query, mutation=Mutation)))

graphql_app = GraphQLApp(schema=Schema(query=Query))


@app.get("/")
async def graphiql(request: Request):
    request._url = URL("/data")
    return await graphql_app.handle_graphiql(request=request)


@app.post("/data")
async def graphql(request: Request, authorize: str = Depends(auth_bearer.JWTBearer())):
    request.state.authorize = authorize
    return await graphql_app.handle_graphql(request=request)


@app.post("/user", dependencies=[Depends(auth_bearer.JWTBearer())])
async def graphql(request: Request):
    return await graphql_app.handle_graphql(request=request)
