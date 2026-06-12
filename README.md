# Classificação de Reviews da Steam por Aspecto Técnico via Grafo Tripartido

## Visão Geral do Projeto
Este projeto tem como objetivo classificar automaticamente reviews de jogos da plataforma Steam, identificando qual aspecto técnico cada review discute: **Performance**, **Gráficos**, **Gameplay** ou **Narrativa**. Como as reviews na Steam possuem apenas um rótulo binário (positivo/negativo), este trabalho utiliza um **grafo tripartido** e o algoritmo de **Label Propagation** para inferir a categoria de cada review sem a necessidade de anotação manual em massa.

## Modelagem do Grafo Tripartido
O corpus de texto é representado como um grafo contendo três camadas distintas de nós:
1. **Review (R)**: Textos dos usuários.
2. **Palavra (P)**: Tokens extraídos após o pré-processamento.
3. **Categoria (C)**: Aspectos técnicos (Performance, Gráficos, Gameplay, Narrativa) definidos por palavras-semente (seeds).

### Arestas
- **R → P**: Peso baseado em **TF-IDF**, indicando a importância da palavra na review.
- **P ↔ P**: Peso baseado em **PMI** (Pointwise Mutual Information), indicando a coocorrência estatística entre palavras.
- **P → C**: Arestas fixas ligando as palavras-semente às suas respectivas categorias.

## Restrições e Estruturas de Dados
Atendendo às ressalvas e exigências de implementação customizada:
- **SEM BIBLIOTECAS PRONTAS**: O grafo e as estruturas de dados não utilizarão bibliotecas como `networkx`. Tudo será implementado nativamente do zero.
- **SEM TABELAS HASH**: Não utilizaremos dicionários em Python (`dict`), `set`, ou outras formas de tabelas hash.
- **PREFERÊNCIA POR LISTAS**: A estrutura principal do grafo será implementada utilizando **listas de adjacência** puramente baseadas em arrays (listas no Python).
  - Para evitar matrizes de adjacência (que ficariam muito esparsas e ocupariam memória excessiva), representaremos o grafo como uma lista de listas: `adj = [ [(vizinho1_idx, peso), ...], ... ]`.
  - Como não podemos usar dicionários para mapear strings (nomes de palavras/reviews) para índices, utilizaremos **listas ordenadas e busca binária** $O(\log N)$ para garantir uma performance aceitável nas buscas.

## Algoritmos Implementados Manualmente
1. **Grafo por Listas de Adjacência**: Estrutura eficiente em memória utilizando apenas arrays.
2. **TF-IDF**: Cálculo da frequência de termos e inverso da frequência nos documentos iterando sobre listas.
3. **PMI**: Cálculo das coocorrências utilizando matrizes esparsas via listas de listas.
4. **Label Propagation**: Propagação iterativa dos scores das categorias para o restante do grafo, convergindo até um limiar definido.

## Stack Tecnológica Inicial
- **Backend**: Python (sem uso de libs estruturais prontas para os grafos/dicionários).
- **Frontend**: Next.js (já inicializado na pasta `/src`).

## Estrutura de Diretórios

```text
/
├── backend/
│   ├── graph.py               # Estrutura do Grafo customizada usando listas (sem dicionários)
│   ├── utils.py               # Funções auxiliares (como busca binária em listas)
│   ├── tf_idf.py              # Cálculo de TF-IDF manual
│   ├── pmi.py                 # Cálculo de PMI manual
│   ├── label_propagation.py   # Algoritmo de Label Propagation
│   ├── main.py                # Ponto de entrada
│   └── tests/                 # Testes unitários (pytest)
│       ├── __init__.py
│       └── test_graph.py      # Testes da estrutura de listas
├── frontend/                  # Aplicação Web (Next.js/React)
│   ├── src/
│   ├── package.json
│   └── ...
├── infra/                     # Infraestrutura e Setup
│   ├── requirements.txt       # Dependências do backend
│   └── Makefile               # Scripts para setup, instalação e execução
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline de Integração Contínua (GitHub Actions)
└── README.md                  # Este arquivo
```
