from ariadne import QueryType, ObjectType, gql, make_executable_schema
from hotel_resolver import HotelResolver

with open('type_definitions/type_defs.graphql', 'r') as file:
    type_defs = gql(file.read())

schema = make_executable_schema(type_defs, HotelResolver.query)
