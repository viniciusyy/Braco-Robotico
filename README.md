# Braço Robotico - Busca com Estados

Este repositório contém a implementação do problema dos boxes utilizando algoritmos de busca (Dijkstra, Busca Gananciosa e A*) com modelagem de estados representados por tuplas.

## Descrição do Problema


                             | ------
                             |      |
                             | 
_10_  _30_  ____  _10_  ____ | _40_  ____  _20_  ____  _30_ 


Assim, uma possível configuração final seria:

                             | ------
 10    10                    |      |
 30    20                    | 
_40_  _30_  ____  ____  ____ | ____  ____  ____  ____  ____ 

Cada estado é representado por uma tupla de 10 tuplas, onde cada tupla corresponde a uma pilha de caixas.  
- **Estado Inicial:**  
  - Posição 0: `(10,)`  
  - Posição 1: `(30,)`  
  - Posição 2: `()`  
  - Posição 3: `(10,)`  
  - Posição 4: `()`  
  - Posição 5: `(40,)`  
  - Posição 6: `()`  
  - Posição 7: `(20,)`  
  - Posição 8: `()`  
  - Posição 9: `(30,)`

- **Estado Objetivo:**  
  - Posição 0: `(40, 30, 10)`  
  - Posição 1: `(30, 20, 10)`  
  - Posições 2 a 9: `()`

As ações consistem em mover a caixa do topo de uma pilha para o topo de outra, obedecendo às seguintes restrições:
- A pilha destino deve ter menos de 3 caixas.
- Se a pilha destino não estiver vazia, o peso da caixa no topo deve ser maior ou igual ao da caixa a ser movida.
- Ao mover uma casa, há o custo de 1 de energia. Porém, mover mais de 2 casas, custa 75% do movimento. Por exemplo: 4 casas, custa 3 de energia. A cada 10kg, o custo aumenta em 1 energia, assim uma caixa de 20 kg, custa 2.
Exemplo: Mover 2 casas uma caixa de 40kg: 2*0,75 + 40/10 = 5,5 de energia

## Funcionalidades

- **Modelagem de Estados e Ações:**  
  Os estados são modelados como tuplas imutáveis, permitindo comparações diretas para a verificação do estado objetivo.

- **Função Sucessora:**  
  Gera todos os estados alcançáveis a partir de um estado atual, retornando:
  - Um novo estado (após a movimentação)
  - Uma descrição textual da ação realizada
  - O custo do movimento, calculado a partir da distância entre as pilhas e do peso da caixa

- **Checagem do Estado Objetivo:**  
  A verificação é feita comparando o estado atual com o estado objetivo definido.

- **Função Heurística:**  
  Estima o custo mínimo para levar o estado atual ao objetivo.  
  **Cálculo:**  
  \[
  h(s) = \sum_{\substack{i \geq 2 \\ \text{para cada caixa na pilha } i}} \left( d(i,0) + \frac{w}{10} \right)
  \]
  onde:
  - \(d(i,0)\) é definido por:
    \[
    d(i,0)= 
    \begin{cases}
    1, & \text{se } |i-0| = 1 \\
    |i-0| \times 0.75, & \text{se } |i-0| \geq 2
    \end{cases}
    \]
  - \(w\) é o peso da caixa.

- **Função Custo:**  
  Calcula o custo de cada movimento:  
  \[
  \text{custo} = d(i,j) + \frac{w}{10}
  \]
  onde:
  - \(d(i,j)= 
    \begin{cases}
    1, & \text{se } |i-j| = 1 \\
    |i-j| \times 0.75, & \text{se } |i-j| \geq 2
    \end{cases}\)
  - \(w\) é o peso da caixa movida.

- **Algoritmo A\*:**  
  Combina o custo acumulado \(g(s)\) e a heurística \(h(s)\) na função:
  \[
  f(s) = g(s) + h(s)
  \]
  onde:
  - \(g(s)\) é o custo acumulado desde o estado inicial até \(s\).
  - \(h(s)\) é a estimativa heurística para alcançar o objetivo.

## Algoritmos Implementados

### Dijkstra (Custo Uniforme)
- **Teoria:** Explora os estados priorizando o menor custo acumulado \(g(s)\).  
- **Observação:** Por não usar heurística, pode expandir muitos estados, o que pode aumentar o tempo de execução em problemas com grande espaço de estados.

### Busca Gananciosa (Greedy)
- **Teoria:** Seleciona, a cada passo, o estado com menor valor heurístico \(h(s)\).  
- **Observação:** Pode ser rápida, mas não garante encontrar a solução de menor custo, pois ignora o custo acumulado.

### A\* (A-Estrela)
- **Teoria:** Equilibra o custo acumulado \(g(s)\) e a estimativa heurística \(h(s)\), guiando a busca para estados que minimizam \(f(s) = g(s) + h(s)\).  
- **Observação:** Geralmente encontra a solução ótima expandindo menos estados do que o algoritmo de Dijkstra, desde que a heurística seja bem formulada.


