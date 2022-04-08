import graphene
from graphene import Interface, InputObjectType

class RecommendationInput(InputObjectType):
    top = graphene.Int()
    category = graphene.String()
    customer_id = graphene.Int(required=True)

class VideoRecommendationInput(InputObjectType):
    top = graphene.Int()
    category = graphene.String()
    video_id = graphene.Int(required=True)
