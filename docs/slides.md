---
author: Heitor
date: January 2, 2006
paging: Slide %d / %d
---

# GraphQL
## Heitor Anjos @ queimadiaria

---

# Oque e GraphQL?

## GraphQL é uma linguagem de busca para APIs e um motor para executar as queries com os seus dados existentes. GraphQL te traz uma descrição completa dos dados em sua API, dá aos clientes (front) o poder de pedir exatamente o que ele precisa e nada mais, facilita a evolução das API com o passar do tempo, e permite ferramentas de desenvolvimento poderosas
  GraphQL Website: https://graphql.org/

## GraphQL retorna todos os dados que o seu app precisa em uma requisição.
  Adhithi Ravichandran: [GraphQL: The Big Picture](https://app.pluralsight.com/courses/c903e73b-cf1c-4c30-8548-279088986422/table-of-contents)

## GraphQL é uma linguagem de busca para API, que possibilita ao cliente um retorno de todos os dados que precisa e somente o que precisa usando uma requisição.
---

# Como funciona no rest?
  ~~~graph-easy --as=boxart
  [ App ] - endpoint -> [ RestApi ] -> [ Database ]
  ~~~
---

# Como funciona o GraphQL?
  ~~~graph-easy --as=boxart
  [ App ] - query -> [ GraphQLServer ] -> [ Database ]
  ~~~
---

---
# Query, Argument e Fields

```graphql
{
  person(id: 1) {
    name
  }
```
- Query = person
- Arguments = id
- Fields = name

---
# Problema

## Plataforma de video

## Home
- Mostrar nome do usuario 
- Mostrar videos recomendados pelo usuario logado
- Mostrar ultimos 5 videos assistidos
- Mostrar os 5 videos mais relevantes

![home](./docs/images/home.png)

## Video
- Exibir o video
- Exibir recomendacoes de acordo com o cliente e o video visualizado

![video](./docs/images/video.png)
---

# Rest

## Rotas:
- /user/<id>
- /user/<id>/recommendations
- /user/<id>/views
- /video/relevants

- /video/<id>
- /video/<id>/details
- /video/<id>/comments
- /user/<id>/video/<id>/recomendations

--- 
# GraphQL

## Queries
```graphql
{
  customer(id: 1) {
    name,
    recommendations(qtd: 5) {
      url,
      name,
      duration,
    },
    views(last: 5) {
      url,
      name,
      duration,
    },
  }
  video(relevant: 5) {
    url,
    name,
    duration,
  }
}
```

```graphql
{
  video(id: 1) {
    videoContentUrl,
    details {
      likes
    },
    comments {
      user {
        id,
        name
      },
      text,
    },
    recommendation(videoId: 1, userId: 1) {
      url,
      name,
      duration,
    }
  }
}
```
---
# Agradecimentos

- Pedro 
- Lucas Amorim
- Gabriel Mundim
---
# Referencias
- GraphQL Doc: https://graphql.org/learn/
- Adhithi Ravichandran
  - http://adhithiravichandran.com/
  - GraphQL: The Big Picture
---
# Mais conhecimento

[How airbnb is moving 10x faster at scale with graphql and apollo](https://medium.com/novvum/how-companies-are-using-graphql-and-what-they-migrated-from-844b1d8a164b)
<br><br>
[GraphQL Federation - Netflix](https://www.youtube.com/watch?v=QrEOvHdH2Cg)
---
