from ariadne.asgi import GraphQL
import ariadne_gql

app = GraphQL(ariadne_gql.schema, debug=True)
