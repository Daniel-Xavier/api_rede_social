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

    posts: List['Post'] = Relationship(back_populates='usuario')
    reacoes: List['Reacoes'] = Relationship(back_populates='usuario')
    comentarios: List['Comentarios'] = Relationship(back_populates='usuario')

class Post(SQLModel, table=True):
    id: int = Field(primary_key=True)
    texto: str

    usuario_id: int = Field(default=None, foreign_key='usuario.id')

    usuario: List[Usuario] = Relationship(back_populates='posts')
    reacoes: List['Reacoes'] = Relationship(back_populates='posts')
    comentarios: List['Comentarios'] = Relationship(back_populates='posts')

class Reacoes(SQLModel, table=True):
    id: int = Field(primary_key=True)
    tipo: str

    usuario_id: int = Field(default=None, foreign_key='usuario.id')
    post_id:  int = Field(default=None, foreign_key='post.id')

    usuario: List[Usuario] = Relationship(back_populates='reacoes')
    posts: List['Post'] = Relationship(back_populates='reacoes')

    pct_reacoes: List['PctReacoes'] = Relationship(back_populates='reacoes')

class Comentarios(SQLModel, table=True):
    id: int = Field(primary_key=True)
    texto: str

    usuario_id: int = Field(default=None, foreign_key='usuario.id')
    post_id:  int = Field(default=None, foreign_key='post.id')

    usuario: List[Usuario] = Relationship(back_populates='comentarios')
    posts: List['Post'] = Relationship(back_populates='comentarios')

class PctReacoes(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)

    porcentagem_like: Optional[float]
    porcentagem_dislike: Optional[float]

    reacoes_id: Optional[int] = Field(default=None, foreign_key='reacoes.id')
    reacoes: List[Reacoes] = Relationship(back_populates='pct_reacoes')
 


SQLModel.metadata.create_all(engine)