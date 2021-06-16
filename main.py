from fastapi import FastAPI, Depends, Request
from starlette.graphql import GraphQLApp
from starlette.datastructures import URL
from graphene import ObjectType, Field, Schema, Mutation, String

# locale imports:
from resolvers import user, login
from auth import auth_bearer



class Query(ObjectType):
    me = Field(user.UserProfileQuery, lan=String(default_value="en"))

    def resolve_me(self, info, lan):

        return user.UserProfileQuery(language=lan)


class Mutation(ObjectType):
    login = login.UserLogin.Field()


app = FastAPI()

app.add_route('/', GraphQLApp(schema=Schema(query=Query, mutation=Mutation)))

graphql_app = GraphQLApp(schema=Schema(query=Query))


@app.get('/')
async def graphiql(request: Request):
    request._url = URL('/data')
    return await graphql_app.handle_graphiql(request=request)

@app.post('/data')
async def graphql(request: Request, authorize: str = Depends(auth_bearer.JWTBearer())):
    request.state.authorize = authorize
    return await graphql_app.handle_graphql(request=request)


@app.post('/user', dependencies=[Depends(auth_bearer.JWTBearer())])
async def graphql(request: Request):
    return await graphql_app.handle_graphql(request=request)