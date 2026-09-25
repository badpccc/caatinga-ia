# Anexo Obrigatório de Uso de IA (ANEXO_IA.md)
**Sprint 1 — Projeto Caatinga.Al**
**Matrícula-Semente:** 24114072

---

## A.1 Ferramentas Utilizadas
* **Google Gemini (Assistente de IA):** Utilizado para estruturar o esqueleto de código modular em Python, debugar exceções de caminhos de diretórios do sistema e auxiliar na formatação sintática dos relatórios em Markdown.

## A.2 Dois Prompts na Íntegra e Respostas

### Prompt 1:
> *"Como estruturar o algoritmo Uniform Cost Search (UCS) em Python para respeitar os custos 1 e 4 de uma grade 12x12 garantindo a reabertura de nós?"*

**Resposta Recebida:**
> O modelo forneceu a implementação utilizando uma fila de prioridade (`heapq`), controlando custos acumulados em um dicionário de menor custo (`g_costs`) e permitindo reabrir nós caso um caminho de custo menor fosse encontrado para um estado já visitado, evitando assim os bugs comuns de optimalidade apontados na caixa de aferição do projeto.

### Prompt 2:
> *"Explique o motivo matemático pelo qual a heurística h3 = 4 * Manhattan pode deixar de ser admissível no nosso pomar."*

**Resposta Recebida:**
> O modelo explicou que a admissibilidade exige que $h(n)$ nunca supere o custo real restante. Como o custo mínimo de transição em qualquer talhão firme é $1$, multiplicar a distância de Manhattan por $4$ faz com que $h(n)$ possa exceder o menor custo real possível de travessia em talhões adjacentes livres, tornando a heurística impermissível.

## A.3 Erro Cometido pelo Assistente
* **O que a IA afirmou:** Sugeriu inicialmente que a busca em largura (BFS) encontraria o caminho de menor custo total no pomar de custos variados.
* **A evidência do experimento:** Ao rodar o código prático na malha gerada pela matrícula `24114072`, a BFS retornou custo `55`, enquanto o UCS retornou o ótimo `34`, provando empiricamente que a BFS minimiza apenas o número de saltos (arestas) e ignora os pesos dos talhões.

## A.4 Aprendizado Prático
> *O que eu sabia depois de rodar o código que não sabia lendo a resposta do assistente:* Compreendi na prática o impacto real do fator de desempate da fila de prioridade sobre a variação de ±20% nos nós expandidos do $A^*$, algo que a teoria abstrata da IA não detalha sem a execução empírica na malha específica gerada pela semente da matrícula.