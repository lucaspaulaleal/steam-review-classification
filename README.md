<div align="center">
  <h1>🎮 Classificação Semissupervisionada de Reviews da Steam</h1>
  <p><i>Projeto Acadêmico - Disciplina de Estruturas de Dados e Algoritmos (UnB)</i></p>
  
  [![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://python.org)
  [![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
  [![Next.js](https://img.shields.io/badge/Next.js-Frontend-black?logo=next.js&logoColor=white)](https://nextjs.org/)
  [![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker&logoColor=white)](https://docker.com/)
</div>

<br/>

## 📖 Resumo (Abstract)

Este projeto tem como objetivo realizar a classificação automática de reviews textuais da plataforma **Steam**, identificando o aspecto técnico principal abordado pelos jogadores. Como as avaliações oficiais contêm apenas um rótulo de polaridade binária (*Recomendado / Não Recomendado*), utilizamos uma abordagem de **Machine Learning Semissupervisionado** através da modelagem de um **Grafo Tripartido** e da aplicação do algoritmo de **Label Propagation**.

As categorias de classificação inferidas são:
- ⚡ **Performance**
- 🎨 **Gráficos**
- 🕹️ **Gameplay**
- 📖 **Narrativa**

---

## 🔬 Metodologia e Modelagem

O texto das avaliações é estruturado matematicamente em uma rede complexa formada por três subconjuntos de nós disjuntos (Grafo Tripartido):

1. **Camada de Reviews ($R$)**: Representa o texto original escrito pelo usuário.
2. **Camada de Palavras ($P$)**: Tokens extraídos após pré-processamento (NLP).
3. **Camada de Categorias ($C$)**: Classes alvo da nossa inferência.

### Pesos e Arestas do Grafo

A propagação da informação flui com base em pesos matematicamente definidos:

- **Arestas $R \leftrightarrow P$ (Review-Palavra)**: Ponderadas utilizando **TF-IDF** (Term Frequency - Inverse Document Frequency), indicando a relevância estatística da palavra para o documento específico.
- **Arestas $P \leftrightarrow P$ (Palavra-Palavra)**: Ponderadas pelo índice **NPMI** (Normalized Pointwise Mutual Information), capturando as probabilidades conjuntas de coocorrência de termos em toda a base de dados.
- **Arestas $P \leftrightarrow C$ (Palavra-Categoria)**: Sementes (seeds) inicialmente polarizadas com peso máximo conectando palavras-chave óbvias (ex: "fps" $\rightarrow$ "Performance").

### 🔮 Inferência em Tempo Real
A API possui um módulo de classificação em *Real-Time* (`/backend/classification`) que injeta dinamicamente textos não vistos previamente pelo modelo no Grafo, extrai seus radicais via RSLPStemmer, cálcula similaridade contra as `seeds` estendidas e retorna a propagação probabilística instantaneamente.

---

## ⚠️ Restrições de Implementação Estrutural

De acordo com as exigências da disciplina, o núcleo estrutural e algorítmico do projeto segue restrições rígidas para provar o domínio sobre Estruturas de Dados Básicas:

> **O uso de tabelas de dispersão (*Hash Tables*, `dict` e `set` no Python) é estritamente proibido.** Todas as buscas de índices devem ser feitas via *Busca Binária* $O(\log N)$ em listas ordenadas.
> **Bibliotecas prontas de Grafos (ex: `networkx`) são proibidas.** O grafo foi implementado "do zero" utilizando estritamente **Listas de Adjacência**. 

---

## 🛠️ Arquitetura e Tecnologias

A aplicação é dividida em três frentes e totalmente conteinerizada para garantir fácil reprodutibilidade.

* **Backend / Algoritmos (`/backend`)**: Python (FastAPI, NumPy, Pandas, NLTK).
* **Frontend (`/frontend`)**: Interface gráfica Rica desenvolvida em Next.js (React) + TailwindCSS para exploração visual do grafo.
* **Infraestrutura e Dados (`/infra` & `/scripts`)**: Scripts autônomos para conexão com a API do Kaggle e ingestão dos dados, orquestrados via `docker-compose`.

### Estrutura de Diretórios
```text
/
├── backend/                   # Lógica de ML e API
│   ├── api/                   # Controladores REST FastAPI (main.py)
│   ├── classification/        # Inferência de NLP em Tempo Real
│   ├── graph/                 # Estrutura do Grafo em Listas e Builder
│   ├── preprocessing/         # NLP, Sublinear TF-IDF manual
│   ├── propagation/           # Label Propagation e NPMI manual
│   └── tests/                 # Testes unitários (PyTest)
├── frontend/                  # Interface Visual (Next.js)
├── infra/                     # Configurações de Deploy (Vercel/Render)
├── scripts/                   # Automação de extração do Kaggle
└── datasets/                  # Diretório para montagem do dataset do GTA V
```

---

## 🚀 Como Executar Localmente

### Pré-requisitos
* Git instalado.
* Docker instalado e em execução.
* Docker Compose disponível pelo comando `docker compose`.
* Node.js instalado para executar o frontend localmente.
* Opcionalmente, arquivo `kaggle.json` posicionado na sua pasta *home* (`~/.kaggle/`) ou variáveis `KAGGLE_USERNAME` e `KAGGLE_KEY` para autenticar o download da base.

### Passo 1: Clonar o repositório
```bash
git clone https://github.com/lucaspaulaleal/steam-review-classification.git
cd steam-review-classification
```

### Passo 2: Construir e inicializar o backend
Suba o ambiente utilizando o Docker Compose na raiz do projeto:
```bash
docker compose up --build
```

Esse comando constrói a imagem do backend, instala as dependências Python e inicia a API FastAPI em `http://localhost:8000`.

### Passo 3: Validar a API
Com o container em execução, acesse:

* **Health check:** `http://localhost:8000/health`
* **Swagger Docs:** `http://localhost:8000/docs`
* **Classificações mockadas:** `http://localhost:8000/reviews/mock-classifications`

### Passo 4: Extrair a base de dados
Em outro terminal, execute a pipeline de extração para o jogo "Grand Theft Auto V":
```bash
docker exec -it steam_reviews_backend python scripts/download_dataset.py
```

Caso prefira usar variáveis de ambiente para o Kaggle, crie um arquivo `.env` na raiz do projeto ou exporte `KAGGLE_USERNAME` e `KAGGLE_KEY` antes de subir o Docker Compose.

### Passo 5: Executar o frontend
O `docker-compose.yml` atual sobe apenas o backend. Para iniciar o frontend localmente, use outro terminal:
```bash
cd frontend
npm install
npm run dev
```

Depois acesse:

* **Frontend Visualizador:** `http://localhost:3000`

### Documentação de reprodutibilidade
As instruções detalhadas para avaliação do projeto do zero estão em [`docs/reprodutibilidade.md`](docs/reprodutibilidade.md).

---

## 👥 Equipe do Projeto

Desenvolvido por estudantes de Engenharia de Software para a disciplina de **Estruturas de Dados 2**.

- **João Marcelo Guimarães Costa Naves** ([@JoaoMarceloGCN](https://github.com/JoaoMarceloGCN))
- **Lucas de Paula Leal** ([@lucaspaulaleal](https://github.com/lucaspaulaleal))
- **Pedro Henrique Pereira Santos** ([@pedrohpsantos](https://github.com/pedrohpsantos))
- **Raissa Silva de Oliveira** ([@daisha19](https://github.com/daisha19))
- **Yasmin Dayrell Albuquerque** ([@YasminDayrell](https://github.com/YasminDayrell))

---
*Universidade de Brasília (UnB)*
