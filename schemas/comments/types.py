import graphene
from graphene import ObjectType, InputObjectType

from schemas.customer.types import CustomerType

from src.core.customer import CustomerCore

class CommentType(ObjectType):
    id = graphene.Int()
    text = graphene.String()
    author = graphene.Field(CustomerType)
    video_id = graphene.Int()
    likes = graphene.Int()
    
    def resolve_author(parent, info):
        return CustomerCore.get_customer('id', parent.get('author_id'))[0]

    def resolve_text(parent, info):
        return parent.get('text')

    def resolve_likes(parent, info):
        return parent.get('likes')
