import graphene
from bson.objectid import ObjectId
from graphene import ObjectType, InputObjectType

from schemas.customer.types import CustomerType
from schemas.video.types import VideoType

from src.core.customer import CustomerCore


class RecommendationType(ObjectType):
    customer = graphene.Field(CustomerType, required=False)
    video = graphene.Field(VideoType)

    def resolve_customer(parent, info):
        customer_id = parent.get('customer_id')

        if not customer_id:
            return

        return CustomerCore.get_customer('id', customer_id)[0]

    def resolve_video(parent, info):
        return parent.get('video')
