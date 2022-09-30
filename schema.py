from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter
from db_function import (create_usuarios, get_post, get_usuarios, create_posts,get_post)

@strawberry.type
class Usuario:
    id: int
    nome: str
    idade: int

@strawberry.type
class Post:
    id: int
    texto: str
    usuario_id: int
    
@strawberry.type
class Comentarios:
    id: int
    texto: str
    
@strawberry.type
class Reacoes:
    id: int
    tipo: bool
    
@strawberry.type
class Query:
    all_usuarios: List[Usuario] = strawberry.field(resolver=get_usuarios)
    all_posts: List[Post] = strawberry.field(resolver=get_post)

@strawberry.type
class Mutation:
    create_usuario: Usuario = strawberry.field(resolver=create_usuarios)
    create_post: Post = strawberry.field(resolver=create_posts)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)

graphql_app = GraphQLRouter(schema)