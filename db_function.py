from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from models import PctReacoes, Usuario, Reacoes, Post, Comentarios, engine


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


def create_react(id: int, tipo: str, usuario_id: int, post_id: int):
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


def get_usuarios(id: int = None, nome: str = None):

    query = select(Usuario).options(joinedload('*'))
    
    if id:
        query = query.where(Usuario.id == id)
    if nome:
        query = query.where(Usuario.nome == nome)

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result


def get_posts(id: int = None, usuario_id: int = None):

    query = select(Post).options(joinedload('*'))
    if id:
        query = query.where(Post.id == id)
    if usuario_id:
        query = query.where(Post.usuario_id == usuario_id)
        

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result


def get_comentarios(id: int = None, usuario_id: int = None):

    query = select(Comentarios).options(joinedload('*'))

    if id:
        query = query.where(Comentarios.id == id)
    if usuario_id:
        query = query.where(Comentarios.usuario_id == usuario_id)

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result    

def get_reacoes(id: int = None, usuario_id: int = None):

    query = select(Reacoes).options(joinedload('*'))

    if id:
        query = query.where(Comentarios.id == id)
    if usuario_id:
        query = query.where(Comentarios.usuario_id == usuario_id)

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()

    return result    


def porcentagem_reacao():

    query = select(Reacoes).options(joinedload('*'))

    with Session(engine) as session:
        result = session.execute(query).scalars().unique().all()
        
    lista = result
    gostei = 0
    nao_gostei =0
    for i in lista:
        for j in i:
            for k in j:
                if k == 'Gostei':
                    gostei += 1
                if k == 'Nao Gostei':
                    nao_gostei += 1

    total = gostei + nao_gostei
    gosteipct = (gostei/total) * 100
    nao_gosteipct = nao_gostei/total * 100
    
    resultpct = [
        PctReacoes(
            porcentagem_like = gosteipct,
            porcentagem_dislike = nao_gosteipct),
            ]
    
    
    return resultpct 
