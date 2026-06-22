# Refinar e Evidenciar Análise e Interpretação dos Resultados

## Descrição do Problema
O **Critério 5** de avaliação do edital destina **2,0 pontos (20% da nota final)** à *"Capacidade de interpretar e justificar os resultados obtidos. Discussão sobre padrões, relações, agrupamentos, similaridades, métricas ou conclusões extraídas."*

Atualmente, o projeto classifica as reviews e monta o grafo perfeitamente de forma algorítmica. Contudo, precisamos garantir que o sistema (seja via Frontend ou através da própria API) retorne algum tipo de sumário analítico mostrando as palavras que mais pesaram para definir a categoria (justificativa).

## Solução Proposta (Tarefas)
- [ ] No Backend (FastAPI), após rodar o Label Propagation em uma Review não-categorizada, retornar as top N palavras (`word_labels`) que mais influenciaram o resultado da propagação, junto com a categoria vencedora.
- [ ] No Frontend, criar um painel ou aba exibindo os grupos semânticos de palavras e categorias geradas após o grafo convergir, para enriquecer a discussão.
- [ ] Adicionar na apresentação slides discutindo esses padrões observados nos testes com as base real (Kaggle), extraindo conclusões sobre as dificuldades do NLP no contexto das reviews.
