import heapq

# Configuração inicial (conforme o desenho sugerido):
#  - posição 0: pilha com caixa 10
#  - posição 1: pilha com caixa 30
#  - posição 2: vazia
#  - posição 3: pilha com caixa 10
#  - posição 4: vazia
#  - posição 5: pilha com caixa 40
#  - posição 6: vazia
#  - posição 7: pilha com caixa 20
#  - posição 8: vazia
#  - posição 9: pilha com caixa 30
initial_state = (
    (10,), 
    (30,), 
    (), 
    (10,), 
    (), 
    (40,), 
    (), 
    (20,), 
    (), 
    (30,)
)

# Configuração objetivo: as pilhas válidas ficam nas posições iniciais (0 e 1)
goal_state = (
    (40, 30, 10),   # pilha 0: de baixo para cima
    (30, 20, 10),   # pilha 1
    (), (), (), (), (), (), (), ()
)

def get_successors(state):
    """
    Para um estado dado, gera todos os estados alcançáveis com um movimento legal.
    Cada movimento consiste em retirar a caixa do topo de uma pilha (fonte)
    e colocá-la no topo de outra pilha (destino), obedecendo:
      - A pilha destino deve ter menos de 3 caixas.
      - Se a pilha destino não for vazia, o peso da caixa no topo deve ser
        maior ou igual ao da caixa que se deseja mover.
    O custo do movimento é calculado de acordo com a distância (número de casas)
    entre a pilha fonte (i) e a pilha destino (j) e o peso da caixa movida.
      - Se a distância == 1: custo_deslocamento = 1.
      - Se a distância >= 2: custo_deslocamento = distância * 0.75.
      - Custo total = custo_deslocamento + (peso / 10).
    """
    num_positions = len(state)
    for i in range(num_positions):
        if not state[i]:
            continue  # não há caixa para mover nesta pilha
        # a caixa a mover é a do topo da pilha i
        moving_box = state[i][-1]
        for j in range(num_positions):
            if i == j:
                continue
            # Verifica se a pilha destino tem espaço (< 3 caixas)
            if len(state[j]) >= 3:
                continue
            # Se a pilha destino não estiver vazia, respeita a regra de empilhamento
            if state[j] and state[j][-1] < moving_box:
                continue

            # Calcula a distância (número de casas entre i e j)
            distance = abs(i - j)
            if distance == 0:
                continue  # não deve ocorrer, mas por segurança
            # Define o custo de deslocamento conforme a regra:
            if distance == 1:
                cost_distance = 1
            else:
                cost_distance = distance * 0.75
            # Custo adicional relativo ao peso
            cost_weight = moving_box / 10.0
            move_cost = cost_distance + cost_weight

            # Cria o novo estado:
            new_state = list(list(pile) for pile in state)
            # Remove a caixa do topo da pilha i
            new_state[i].pop()
            # Adiciona a caixa na pilha j (no topo)
            new_state[j].append(moving_box)
            # Converte de volta para tupla de tuplas (para ser hasheável)
            new_state = tuple(tuple(pile) for pile in new_state)

            move_descr = f"Mover caixa {moving_box} de posição {i} para {j} (distância {distance})"
            yield new_state, move_descr, move_cost

def heuristic(state):
    """
    Uma heurística admissível simples: soma, para cada caixa que não está
    nas duas primeiras posições (que são as únicas que devem ter caixas no final),
    o custo mínimo para movê-la para a posição 0.
    
    (Para as caixas que já estão em 0 ou 1, a heurística é zero.)
    
    """
    h = 0
    for i, pile in enumerate(state):
        if i < 2:
            continue  # assume que, se já está em uma das duas primeiras casas, está "próximo do objetivo"
        for box in pile:
            # Custo mínimo de mover uma caixa de 'i' para a posição 0
            distance = abs(i - 0)
            if distance == 1:
                cost_distance = 1
            else:
                cost_distance = distance * 0.75
            h += cost_distance + (box / 10.0)
    return h
