import graphene
from graphene import ObjectType, InputObjectType


from schemas.video.types import VideoType

from src.core.video import VideoCore


class Query(ObjectType):
    video = graphene.Field(VideoType, id= graphene.Int())

    top_rated_videos = graphene.List(VideoType, qtd= graphene.Int())
    
    def resolve_video(parent, info, id):
        return VideoCore.get_video('id', id)[0]

    def resolve_top_rated_videos(parent, info, qtd):
        return VideoCore.get_tops_videos()[:qtd]


