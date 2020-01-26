import strawberry
from songs.schema import SongQuery, SongMutation


@strawberry.type
class Query(
    SongQuery
):
    pass


class Mutation(
    SongMutation
):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
