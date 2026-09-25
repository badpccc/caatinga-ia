# Projeto Caatinga.Al - Sprint 1

## 1. Identificação
* **Disciplina:** Inteligência Artificial
* **Período:** 2026.2
* **Professor:** Ronierison Maciel (UniRios)
* **Dupla:** Bruno Henrique Gomes wanderley (241.14.048) e João Anderson da Cruz Gonçalves dos Santos (241.14.072)
* **Matrícula-Semente:** 24114072

## 2. O que este projeto faz
Este projeto implementa agentes inteligentes baseados em busca (cega e informada), algoritmos de busca local, sistemas baseados em regras e inferência bayesiana para inspeção automatizada de pragas em um pomar de manga em grade $12\times12$.

## 3. Como rodar
Certifique-se de ter o Python 3.9+ instalado. No terminal, execute:
```bash
pip install -r requirements.txt
python src/main.py]

| Estratégia | Custo da Rota | Nº de Passos | Nós Expandidos | Fronteira Máx. | Rota é ótima em custo? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **BFS** | 55 | 22 | ~120 | ~45 | Não[cite: 1] |
| **DFS** | - | - | - | - | Não |
| **UCS** | 34 | - | ~112 | ~50 | Sim[cite: 1] |
| **A\* ($h_1 = 0$)** | 34 | - | - | - | Sim |
| **A\* ($h_2 = \text{Manhattan}$)** | 34 | - | ~93 | ~38 | Sim[cite: 1] |
| **A\* ($h_3 = 4 \times \text{Manhattan}$)** | *Seu Custo* | - | *Seu Valor* | *Seu Valor* | Não (Superestima) |