from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from models import Usuario, Reacoes, Post, Comentarios, engine




def create_usuarios(id: int, idade: int, nome: str):
    user = Usuario(id=id, nome=nome, idade=idade)

    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)

    return user


def create_posts(id: int, texto: str, usuario_id: int):
    post = Post(id=id, texto=texto, usuario_id=usuario_id)

    with Session(engine) as session:
        session.add(post)
        session.commit()
        session.refresh(post)

    return post

def create_reacao(id: int, tipo: bool, usuario_id: int, post_id: int):
    react = Reacoes(id=id, tipo=tipo, usuario_id=usuario_id, post_id=post_id)

    with Session(engine) as session:
        session.add(react)
        session.commit()
        session.refresh(react)

    return react


def create_comentarios(id: int, texto: str, usuario_id: int, post_id: int):
    comment = Comentarios(id=id, texto=texto, usuario_id=usuario_id, post_id=post_id)

    with Session(engine) as session:
        session.add(comment)
        session.commit()
        session.refresh(comment)

    return comment



def get_usuarios(id: int = None, idade: int = None):

    query = select(Usuario)
    if id:
        query = query.where(Usuario.id == id)
    if idade:
        query = query.where(Usuario.idade == idade)

    with Session(engine) as session:
        result = session.execute(query).scalars().all()

    return result

def get_posts(id: int = None, usuario_id: int = None):

    query = select(Post)
    if id:
        query = query.where(Post.id == id)
    if usuario_id:
        query = query.where(Usuario.id == usuario_id)
        # query = select(Usuario.nome)

    with Session(engine) as session:
        result = session.execute(query).scalars().all()

    return result

def get_comentarios(id: int = None, usuario_id: int = None):

    query = select(Comentarios)

    with Session(engine) as session:
        result = session.execute(query).scalars().all()

    return result    