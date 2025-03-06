from problem import initial_state, goal_state, get_successors, heuristic
from node import No

class MyProblem:
    def iniciar(self):
        # Retorna o nó inicial com o estado inicial
        return No(initial_state)
    
    def testar_objetivo(self, no):
        # Testa se o estado do nó é o estado objetivo
        return no.estado == goal_state
    
    def gerar_sucessores(self, no):
        """
        Para cada sucessor a partir do estado atual, cria um novo nó.
        Armazena o custo do movimento na propriedade 'custo_increment'.
        """
        successors = []
        for novo_estado, move_descr, move_cost in get_successors(no.estado):
            novo_no = No(novo_estado, no_pai=no, aresta=move_descr)
            # Armazena o custo incremental para a transição
            novo_no.custo_increment = move_cost
            successors.append(novo_no)
        return successors
    
    def custo(self, no, no_sucessor):
        # Retorna o custo do movimento que gerou o no_sucessor
        return getattr(no_sucessor, 'custo_increment', 0)
    
    def heuristica(self, no):
        # Calcula a heurística para o estado do nó
        return heuristic(no.estado)
