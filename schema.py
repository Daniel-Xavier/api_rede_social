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
    posts: List['Post']
    reacoes: List['Reacoes']
    comentarios: List['Comentarios']

@strawberry.type
class Post:
    id: int
    texto: str
    usuario: List[Usuario]
    reacoes: List['Reacoes']
    comentarios: List['Comentarios']

@strawberry.type
class Reacoes:
    id: int
    tipo: bool
    usuario: List[Usuario]
    posts: List[Post]

@strawberry.type
class Comentarios:
    id: int
    texto: str
    usuario: List[Usuario]
    posts: List[Post]

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