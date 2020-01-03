from ariadne import QueryType, ObjectType, gql, make_executable_schema
from hotel_repository import HotelRepository

class HotelResolver:
    
    def __init__(self, id):
        self.id = id
        
    query = QueryType()

    @query.field('hotel')
    def resolve_hotel(self, info, id):
        return next((item for item in HotelRepository().hotels 
            if item['id'] == id), 
            None)

    @query.field('hotels')
    def resolve_hotels(self, info):
        return HotelRepository().hotels
