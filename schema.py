from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter
from db_function import (create_usuarios, create_posts, create_comentarios, create_react,
                         get_posts, get_usuarios,get_comentarios, porcentagem_reacao,get_reacoes)

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
    tipo: str
    usuario: Usuario
    posts: Post
    
@strawberry.type
class PctReacoes:
    porcentagem_like: float
    porcentagem_dislike: float
    reacoes: Reacoes

@strawberry.type
class Comentarios:
    id: int
    texto: str
    usuario: Usuario
    posts: Post

@strawberry.type
class Query:
    all_usuarios: List[Usuario] = strawberry.field(resolver=get_usuarios)
    all_posts: List[Post] = strawberry.field(resolver=get_posts)
    all_comentarios: List[Comentarios] = strawberry.field(resolver=get_comentarios)
    all_reacoes: List[Reacoes] = strawberry.field(resolver=get_reacoes)
    porcentagem_reacaoes: List[PctReacoes] = strawberry.field(resolver=porcentagem_reacao)

@strawberry.type
class Mutation:
    create_usuario: Usuario = strawberry.field(resolver=create_usuarios)
    create_post: Post = strawberry.field(resolver=create_posts)
    create_comentario: Comentarios = strawberry.field(resolver=create_comentarios)
    create_reacao: Reacoes = strawberry.field(resolver=create_react)
    

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)

graphql_app = GraphQLRouter(schema)