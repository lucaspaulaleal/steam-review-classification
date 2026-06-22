# Implementar Busca Binária para Resgate de Nós (Correção Crítica)

## Descrição do Problema
De acordo com o edital do projeto, a solução deve conter obrigatoriamente o uso de **Grafos** e **pelo menos uma outra estrutura de dados**. 
No arquivo `README.md`, foi documentado que a segunda estrutura de dados adotada são "listas ordenadas com Busca Binária $O(\log N)$" em substituição às tabelas hash (`dict`/`set`) que são proibidas pelas regras.

No entanto, ao analisar a implementação atual nos arquivos:
- `backend/graph/graph.py` (método `_find_node_idx`)
- `backend/graph/builder.py` (método `_find_index`)

Constatou-se que a busca pelo índice de um nó a partir de seu rótulo (`label`) está sendo feita com uma varredura linear simples ($O(N)$) usando um laço `for`.

## Impacto
Se a implementação for entregue dessa forma, o grupo sofrerá a penalização de **-5,0 pontos** (rubrica: "Trabalho sem outra estrutura de dados além do grafo").

## Solução Proposta (Tarefas)
- [ ] Refatorar a lista `self.labels` (e listas associadas, se necessário) para garantir que elas sempre se mantenham ordenadas após as inserções.
- [ ] Substituir o laço `for` nas funções de busca (`_find_node_idx` e `_find_index`) por um algoritmo clássico de **Busca Binária** que opere em $O(\log N)$.
- [ ] Rodar os testes no backend para assegurar que a mudança estrutural não quebrou a construção do Grafo Tripartido.
