# GraphQL - Presentation
This repo uses graphql to solve a simple case of video platform

## Summary
- [installation](#installation)
- [running](#running-app)
- [testing](#testing)
- [slides](./docs/slides.md)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements. Linux enviroments just follow the commands bellow:

```bash
$ git clone https://github.com/heitoranjos15/graphql-presentation
$ cd graphql-presentation
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

## Running App
This app uses [fast-api](https://fastapi.tiangolo.com/) framework to build the server

```bash
$ uvicorn main:app --reload
```

## Testing
You can test the application locally in your browser using [GraphIQL](https://github.com/graphql/graphiql).
<br>
Address: http://localhost:8000/

Using curl
```bash
  curl --location --request POST 'http://localhost:8000' \
    --header 'Content-Type: application/json' \
    --data-raw '{"query":"  {\n    customer(id: 1){\n        name\n    }\n  }","variables":{}}'
```
