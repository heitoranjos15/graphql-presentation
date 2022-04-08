import graphene

import schemas.customer.query
import schemas.video.query
import schemas.recommendation.query


class Query(
    schemas.customer.query.Query,
    schemas.video.query.Query,
    schemas.recommendation.query.Query,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query)
