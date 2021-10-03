import graphene
import pydantic
from graphene_pydantic import PydanticInputObjectType, PydanticObjectType

from services import user_service


class UserModel(pydantic.BaseModel):
    id: int
    name: str
    token: str


class UserInput(PydanticInputObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ("id", "token")


class User(PydanticObjectType):
    class Meta:
        model = UserModel


class UserLogin(graphene.Mutation):
    class Arguments:
        user = UserInput()

    Output = User

    def mutate(self, info, user):
        data = user_service.user_login(user.name)
        return User(id=data["id"], name=user.name, token=data["token"])
