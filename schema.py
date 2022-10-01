from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter
from db_function import (create_usuarios, create_posts, create_comentarios, 
                         get_posts, get_usuarios,get_comentarios)

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
    comentario_id: int
    reacao_id: int
@strawberry.type
class Comentarios:
    id: int
    texto: str
    usuario_id: int
    post_id: int
@strawberry.type
class Reacoes:
    id: int
    tipo: bool
    usuario_id: int
    post_id: int
@strawberry.type
class Query:
    all_usuarios: List[Usuario] = strawberry.field(resolver=get_usuarios)
    all_posts: List[Post] = strawberry.field(resolver=get_posts)
    all_comentarios: List[Comentarios] = strawberry.field(resolver=get_comentarios)
@strawberry.type
class Mutation:
    create_usuario: Usuario = strawberry.field(resolver=create_usuarios)
    create_post: Post = strawberry.field(resolver=create_posts)
    create_comentario: Comentarios = strawberry.field(resolver=create_comentarios)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)

graphql_app = GraphQLRouter(schema)