import graphene
from graphene import ObjectType, InputObjectType


class CustomerType(ObjectType): 
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()
    address = graphene.String()

    def resolve_id(parent, info):
        return parent.get('id')
    
    def resolve_name(parent, info):
        return parent.get('name')

    def resolve_email(parent, info):
        return parent.get('email')

    def resolve_address(parent, info):
        return parent.get('address')
