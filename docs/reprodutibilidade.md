# Reprodutibilidade do Ambiente

Este documento descreve os passos para executar o projeto do zero usando Docker, de forma que a avaliacao possa ser reproduzida em outra maquina.

## Pre-requisitos

- Git instalado.
- Docker instalado e em execucao.
- Docker Compose disponivel pelo comando `docker compose`.
- Opcionalmente, credenciais do Kaggle para baixar a base real.

## Execucao do backend com Docker

Na raiz do repositorio, execute:

```bash
docker compose up --build
```

Esse comando constroi a imagem Python do backend, instala as dependencias listadas em `infra/requirements.txt` e inicia a API FastAPI na porta `8000`.

Quando o container estiver em execucao, acesse:

- Swagger da API: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`
- Classificacoes mockadas: `http://localhost:8000/reviews/mock-classifications`

## Download da base de dados

Para baixar a base real pelo Kaggle, configure as credenciais antes de executar o script. Existem duas opções:

1. Criar o arquivo `~/.kaggle/kaggle.json` na maquina host.
2. Definir as variaveis de ambiente `KAGGLE_USERNAME` e `KAGGLE_KEY`.

Com o backend em execucao, rode:

```bash
docker exec -it steam_reviews_backend python scripts/download_dataset.py
```

Os arquivos baixados devem ficar em `datasets/`.

## Execucao do frontend

O `docker-compose.yml` atual sobe apenas o backend. Para executar o frontend em desenvolvimento, use outro terminal:

```bash
cd frontend
npm install
npm run dev
```

Depois acesse:

```text
http://localhost:3000
```

## Passos recomendados para avaliação

1. Clonar o repositorio.
2. Entrar na pasta do projeto.
3. Rodar `docker compose up --build`.
4. Validar `http://localhost:8000/health`.
5. Abrir `http://localhost:8000/docs`.
6. Opcionalmente, executar o download da base com as credenciais do Kaggle.
7. Opcionalmente, iniciar o frontend com `npm run dev` dentro de `frontend/`.

## Observacoes

- O backend usa dados mockados no endpoint `/reviews/mock-classifications`, permitindo validar a API mesmo sem baixar a base do Kaggle.
- A porta `8000` precisa estar livre para o backend.
- A porta `3000` precisa estar livre para o frontend, caso ele seja executado localmente.
