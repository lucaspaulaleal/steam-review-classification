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
- **Arestas $P \leftrightarrow P$ (Palavra-Palavra)**: Ponderadas pelo índice **PMI** (Pointwise Mutual Information), capturando as probabilidades conjuntas de coocorrência de termos em toda a base de dados.
- **Arestas $P \leftrightarrow C$ (Palavra-Categoria)**: Sementes (seeds) inicialmente polarizadas com peso máximo conectando palavras-chave óbvias (ex: "fps" $\rightarrow$ "Performance").

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
│   ├── api/                   # Controladores REST FastAPI
│   ├── graph/                 # Estrutura do Grafo em Listas e Builder
│   ├── preprocessing/         # NLP e TF-IDF manual
│   ├── propagation/           # Label Propagation e PMI manual
│   ├── tests/                 # Testes unitários (PyTest)
│   └── main.py                # Ponto de inicialização
├── frontend/                  # Interface Visual (Next.js)
├── infra/                     # Configurações de Deploy (Vercel/Render)
├── scripts/                   # Automação de extração do Kaggle
└── datasets/                  # Diretório para montagem do dataset do GTA V
```

---

## 🚀 Como Executar Localmente

### Pré-requisitos
* Docker e Docker Compose instalados na máquina.
* Arquivo `kaggle.json` posicionado na sua pasta *home* (`~/.kaggle/`) para autenticar o download da base.

### Passo 1: Construir e Inicializar os Serviços
Suba o ambiente utilizando o Docker Compose na raiz do projeto:
```bash
docker-compose up --build
```

### Passo 2: Extrair a Base de Dados
Em outro terminal (ou pelo container do Backend), execute a pipeline de extração para o jogo "Grand Theft Auto V":
```bash
docker exec -it steam_reviews_backend python scripts/download_dataset.py
```

### Passo 3: Acessar a Aplicação
* **Backend API (Swagger Docs):** `http://localhost:8000/docs`
* **Frontend Visualizador:** `http://localhost:3000`

---

## 👥 Equipe do Projeto

Desenvolvido por estudantes do curso de Engenharia de Software para a disciplina de **Estruturas de Dados e Algoritmos**.

---
*Universidade de Brasília (UnB)*
