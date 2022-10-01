from typing import Optional, List
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    Relationship
)

# Criar engine do banco
engine = create_engine('sqlite:///database.db')

class Usuario(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nome: str
    idade: int
    
class Reacoes(SQLModel, table=True):
    id: int = Field(primary_key=True)
    tipo: bool
    usuario_id: int = Field(default=None, foreign_key='usuario.id')
    post_id: int = Field(default=None, foreign_key='post.id')

class Comentarios(SQLModel, table=True):
    id: int = Field(primary_key=True)
    texto: str
    usuario_id: int = Field(default=None, foreign_key='usuario.id')
    post_id: int = Field(default=None, foreign_key='post.id')


class Post(SQLModel, table=True):
    id: int = Field(primary_key=True)
    texto: str
#  Usuario.id = Relationship(back_populates='posts')
    usuario_id: int = Field(default=None, foreign_key='usuario.id')
    reaoces_id: Optional[int] = Field(default=None, foreign_key='reacoes.id')
    # comentarios_id: Comentarios = Relationship(back_populates='comentario.id')




SQLModel.metadata.create_all(engine)