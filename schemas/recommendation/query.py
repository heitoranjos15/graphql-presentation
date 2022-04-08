import graphene
from bson.objectid import ObjectId
from graphene import ObjectType, InputObjectType

from schemas.recommendation.types import RecommendationType

from schemas.recommendation.input import RecommendationInput, VideoRecommendationInput

from src.core.video import VideoCore
from src.core.customer import CustomerCore
from src.core.comments import CommentsCore


class Query(ObjectType):
    customer_recommendation = graphene.List(
            RecommendationType,
            filter_options = graphene.Argument(RecommendationInput)
            )

    customer_latest_views = graphene.List(RecommendationType, filter_options = graphene.Argument(RecommendationInput))

    video_recomendation = graphene.List(RecommendationType, filter_options = graphene.Argument(VideoRecommendationInput))

    def resolve_customer_latest_views(parent, info, filter_options):
        customer_id = filter_options.get('customer_id')
        last = filter_options.get('last')
        category = filter_options.get('category')

        return CustomerCore.get_views(customer_id, last, category)

    def resolve_customer_recommendation(parent, info, filter_options):
        customer_id = filter_options.get('customer_id')
        top = filter_options.get('top')
        category = filter_options.get('category')

        return VideoCore.get_recommendations('customer_id', customer_id, category, top)

    def resolve_video_recomendation(parent, info, filter_options):
        video_id = filter_options.get('video_id')
        top = filter_options.get('top')
        category = filter_options.get('category')

        return VideoCore.get_recommendations('video_id', video_id, category, top)
