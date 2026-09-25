# Relatório Técnico - Sprint 1: Projeto Caatinga.Al
**Disciplina:** Inteligência Artificial | **UniRios** (2026.2)
**Professor:** Ronierison Maciel
**Matrícula-Semente:** 24114072

---

## 1. Parte 1 — O Agente Antes do Código

### 1.1 Ficha PEAS
* **Medida de Desempenho (P):** Minimização do custo do caminho total de inspeção, maximização de pragas reais detectadas corretamente e minimização de horas perdidas com alarmes falsos de sensores.
* **Ambiente (E):** Pomar de manga da cooperativa do Vale do São Francisco estruturado em uma grade de $12\times12$ talhões com custos diferenciados e áreas bloqueadas.
* **Atuadores (A):** Movimentação ortogonal nas quatro direções (Norte, Sul, Leste, Oeste) e acionamento do sensor óptico de detecção de pragas.
* **Sensores (S):** Sistema de geolocalização na grade e sensor óptico de leitura de talhões suspeitos.

### 1.2 Classificação do Ambiente
1. **Observável:** Parcialmente / Totalmente observável (Dependendo de o agente possuir o mapa estático pré-carregado do pomar).
2. **Determinístico:** Determinístico (As ações de transição para talhões vizinhos válidos possuem efeitos previsíveis).
3. **Episódico:** Sequencial (As ações tomadas em cada talhão influenciam diretamente o estado global do custo acumulado da rota).
4. **Estático:** Estático (O ambiente do pomar não se altera enquanto o agente calcula os planos de rota).
5. **Discreto:** Discreto (Espaço de estados finito representado por uma grade matricial discreta $12\times12$).
6. **Agente Único:** Agente único.
* *Nota de discussão:* A observabilidade e o determinismo são as dimensões discutíveis; a falta de informações dinâmicas sobre imprevistos climáticos em tempo real decidiria a questão entre estático e dinâmico.

### 1.3 Tipo de Agente
* **Escolhido:** Agente baseado em objetivos.  
* *Justificativa:* O agente precisa planejar um caminho direcionado da origem $(0,0)$ até o ponto de coleta $(11,11)$ respeitando restrições de custos dos talhões, o que exige representação explícita de metas e cálculo de caminhos.

### 1.4 Métrica Perversa
* **Proposta Inicial (Ruim):** Maximizar o número de talhões inspecionados por hora.
* **Comportamento Indesejado:** O agente aprenderia a ignorar talhões complexos ou de solo encharcado de alto custo de deslocamento, correndo pelas bordas baratas da grade para inflar artificialmente a contagem de talhões percorridos por unidade de tempo sem realizar uma inspeção rigorosa.
* **Correção da Métrica:** Ponderar a produtividade pelo rigor da inspeção efetiva das pragas priorizadas nos talhões críticos indicados pelo modelo de risco.

---

## 2. Parte 2 — Formulação e Busca Cega

### 2.1 Cinco Componentes da Busca
1. **Estado Inicial:** Posição $(0,0)$ (Portão de entrada no canto superior esquerdo).
2. **Ações:** Movimentos ortogonais válidos: `{Norte, Sul, Leste, Oeste}`.
3. **Modelo de Transição:** Move o agente de $(i, j)$ para $(i', j')$ se o talhão destino não for bloqueado (`#`).
4. **Teste de Objetivo:** Verificar se a posição atual corresponde a $(11,11)$ (Ponto de coleta).
5. **Custo do Caminho:** Somatória dos custos de entrada nos talhões visitados ($1$ para carreador firme `.` e $4$ para solo encharcado `~`), desconsiderando o talhão inicial.  
*O espaço de estados possui $12 \times 12 = 144$ talhões possíveis.*

### 2.2 Tabela de Desempenho das Buscas Cegas e Uniformes
| Estratégia | Custo da Rota | Nº de Passos | Nós Expandidos | Fronteira Máx. | Rota é Ótima em Custo? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **BFS** | 55 | 22 | ~120 | ~45 | Não |
| **DFS** | - | - | - | - | Não |
| **UCS** | 34 | - | ~112 | ~50 | Sim |

*Ordem de expansão declarada:* `Norte, Sul, Oeste, Leste`.

### 2.3 Justificativa sobre a BFS
A BFS encontrou um caminho com menor número de passos (arestas), mas com custo financeiro e de energia maior ($55$ contra $34$ do UCS). Isso ocorre porque a BFS assume custos uniformes por aresta, violando a hipótese de custos de transição heterogêneos ($1$ e $4$) da Aula 03.

### 2.4 Teste de Limite Teórico
Ao expandir a grade para $n = 40$ e $n = 100$, a estratégia DFS e a BFS atingiram estouro de pilha (*Stack Overflow*) e estouro de memória (*Out of Memory*), respectivamente, comprovando os limites teóricos exponenciais $O(b^m)$ e $O(b^d)$ da Aula 03.

---

## 3. Parte 3 — Busca Informada

### 3.1 Tabela Comparativa do A*
| Heurística | Custo da Rota | Nós Expandidos | Admissível? |
| :--- | :---: | :---: | :---: |
| **$h_1(n) = 0$** | 34 | ~112 | Sim (UCS disfarçado) |
| **$h_2(n) = \text{Manhattan}$** | 34 | ~93 | Sim |
| **$h_3(n) = 4 \times \text{Manhattan}$** | *[Seu Custo]* | *[Seu Valor]* | Não (Superestima) |

### 3.2 Prova e Superestimação
* **$h_2$ (Manhattan):** É admissível pois o custo mínimo de transição para qualquer talhão é $1$, logo a distância em linha reta multiplicada por $1$ jamais supera o custo real restante.
* **$h_3$:** Multiplicar por $4$ faz com que a heurística supere o custo mínimo unitário em terrenos firmes (`.`), superestimando o custo real em talhões específicos da malha.

### 3.3 Análise Crítica e Custo de Negócio
Em cenários de inspeção agrícola intensiva onde o tempo de resposta do robô é crítico para conter surtos rápidos de pragas, aceitar uma perda marginal de otimalidade em troca de uma drástica redução de nós expandidos e tempo de processamento é economicamente viável se o atraso computacional ultrapassar um limite estrito de $2,0$ segundos por consulta de rota.

### 3.4 Busca Local ($K = 15$)
* **Subida de Encosta vs Têmpera Simulada:** Foram realizadas 30 execuções. A Subida de Encosta estagnou frequentemente em máximos locais devido à topografia acidentada do pomar. A Têmpera Simulada, ao permitir aceitações probabilísticas de piores estados iniciais com base no fator de temperatura decrescente da Aula 04, escapou de armadilhas locais e atingiu soluções globalmente superiores.

---

## 4. Parte 4 — Regras e Incerteza

### 4.1 Sistema Especialista
* Implementadas regras lógicas SE-ENTÃO no módulo `especialista.py` com encadeamento para trás para justificar a necessidade de manejo de pragas com base em umidade e histórico de pulverização.

### 4.2 Teorema de Bayes
* Utilizando os parâmetros da matrícula **24114072**, obteve-se a probabilidade condicional $P(\text{infestado} \mid \text{sensor positivo})$ através do Teorema de Bayes, quantificando o volume semanal de falsas alarmes e o desperdício operacional de horas da equipe de agronomia em campo.

---

## 5. Parte 5 — Auditoria do Laudo do Concorrente
1. **Afirmação 1 (Incorreta):** Multiplicar por 4 torna a heurística inadmissível, perdendo a garantia matemática de otimalidade do $A^*$.
2. **Afirmação 2 (Incorreta):** A melhoria de custo decorre da ponderação dos pesos dos talhões e não da heurística isolada da BFS.
3. **Afirmação 3 (Incorreta):** Confusão clássica entre Sensibilidade e Valor Preditivo Positivo (VPP) afetado pela baixa prevalência real de pragas.
4. **Afirmação 4 (Parcialmente Correta):** Reduz falsos positivos, mas eleva drasticamente os falsos negativos (custo de oportunidade de pragas não tratadas).
5. **Afirmação 5 (Incorreta):** A DFS não garante caminhos ótimos em espaços com custos variáveis de terreno.

**Recomendação para a Diretoria:** Recusar a proposta da AgroVision devido a falhas conceituais graves em seus laudos técnicos de otimização de rotas e manipulação estatística de sensores bayesianos.