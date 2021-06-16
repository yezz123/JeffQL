import graphene
import pydantic
from graphene_pydantic import PydanticObjectType


class ProfileModel(pydantic.BaseModel):
    name: str
    gender: str


def GetUser(lan):
    if lan == 'eng':
        user = ProfileModel(name='Yasser', gender='Men')

    else:
        user = ProfileModel(name='Yasser', gender='Men')

    return user


class UserProfile(PydanticObjectType):
    class Meta:
        model = ProfileModel


class UserProfileQuery(graphene.ObjectType):

    people = graphene.List(UserProfile)
    language = graphene.String()

    def resolve_people(self, info):
        # fetch actual PersonModels here
        user_data = GetUser(self.language)
        return [user_data]
