# Projeto ECM967 – Tópicos Avançados em Back End

# Integrantes do grupo

- Bruna Galastri Guedes Ra: 18.00189-0

- Daniel Ughini Xavier Ra: 18.00022-3

- Rodolfo Cochi Bezerra Ra: 18.00202-0

- Vitor Martin Simoni Ra: 18.00050-9

# Para rodar o projeto
`uvicorn app:app --reload`

# Operacoes 
## Lista completa de usuários, incluindo seus posts, comentários e reações.
```
query{
  allPosts{
    texto
    comentarios{
      texto
    }
    reacoes{
      tipo
    }
  }
  }
  ```
## Lista completa de posts, incluindo seus comentários e reações
```
query{
  allUsuarios{
    nome
    posts{
      texto
    }
    comentarios{
      texto
    }
    reacoes{
      id
      tipo

    }
  }
```
## Lista completa de comentários, incluindo seus autores.
```
query{
  allComentarios{
    id
    texto
      usuario{
      nome
    }
    }
```

## Uma consulta que mostra, dentro da lista completa de reações, o percentual de reações positivas e negativas.
```
{
  porcentagemReacaoes {
    porcentagemLike
    porcentagemDislike
  }
}
```