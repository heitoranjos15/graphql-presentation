import graphene
from bson.objectid import ObjectId
from graphene import ObjectType, InputObjectType

from schemas.customer.types import CustomerType
from schemas.comments.types import CommentType

from src.core.customer import CustomerCore
from src.core.comments import CommentsCore


class VideoType(ObjectType):
    id = graphene.Int()
    name = graphene.String()
    author = graphene.Field(CustomerType)
    url = graphene.String()
    created_at = graphene.Date()
    duration_minutes = graphene.Int()
    comments = graphene.List(CommentType, last= graphene.Int(), top= graphene.Int())
    category = graphene.String()
    likes = graphene.Int()
    description = graphene.String()

    def resolve_id(parent, info):
        return parent.get('id')

    def resolve_name(parent, info):
        return parent.get('name')

    def resolve_author(parent, info):
        return CustomerCore.get_customer('id', parent.get('author_id'))[0]
    
    def resolve_url(parent, info):
        id = parent.get('id')
        return f'video/${id}'

    def resolve_created_at(parent, info):
        return parent.get('created_at')

    def resolve_duration_minutes(parent, info):
        return parent.get('duration')

    def resolve_category(parent, info):
        return parent.get('category')

    def resolve_comments(parent, info, last=None, top= None):
        video_id = parent.get('id')
        comment =  CommentsCore.get_comment('video_id', video_id)
        if top:
            return comment[:top]
        return comment

    def resolve_likes(parent, info):
        return parent.get('likes')

    def resolve_description(parent, info):
        return parent.get('description')


