import graphene
from graphene import ObjectType, InputObjectType

from schemas.customer.types import CustomerType
from src.core.customer import CustomerCore


class Query(ObjectType): 
    customer = graphene.Field(CustomerType, id=graphene.Int(required=True))
    customers = graphene.List(CustomerType, last=graphene.Int())

    def resolve_customer(parent, info, id):
        return CustomerCore.get_customer('id', id)[0]

    def resolve_customers(parent, info, last=None):
        return CustomerCore.get_customers(last)
