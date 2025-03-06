# main.py

from problem import initial_state, goal_state
from search_algorithms import greedy_search, dijkstra_search, astar_search, dijkstra, a_estrela
from my_problem import MyProblem
from node import no_caminho

def main():
    # Exibição do estado inicial e do estado objetivo
    print("Estado inicial:")
    for i, pile in enumerate(initial_state):
        print(f"Posição {i}: {pile}")
    print("\nEstado objetivo:")
    for i, pile in enumerate(goal_state):
        print(f"Posição {i}: {pile}")
    
    # Busca usando a representação de estados (tuplas)
    print("\nExecutando busca Greedy (estados)...")
    path, cost = greedy_search(initial_state)
    if path is not None:
        print(f"Encontrada solução (custo total = {cost:.2f}) com {len(path)} movimentos:")
        for step in path:
            print("  ", step)
    else:
        print("Nenhuma solução encontrada com Greedy.")
    
    print("\nExecutando busca Dijkstra (estados)...")
    path, cost = dijkstra_search(initial_state)
    if path is not None:
        print(f"Encontrada solução (custo total = {cost:.2f}) com {len(path)} movimentos:")
        for step in path:
            print("  ", step)
    else:
        print("Nenhuma solução encontrada com Dijkstra (estados).")
    
    print("\nExecutando busca A* (estados)...")
    path, cost = astar_search(initial_state)
    if path is not None:
        print(f"Encontrada solução (custo total = {cost:.2f}) com {len(path)} movimentos:")
        for step in path:
            print("  ", step)
    else:
        print("Nenhuma solução encontrada com A* (estados).")
    
    # --- Agora, utilizando a abordagem baseada em nós ---
    problema = MyProblem()
    
    print("\nExecutando busca Dijkstra (com No)...")
    visitados_tamanho, no_solucao = dijkstra(problema)
    if no_solucao is not None:
        print(f"Encontrada solução com {visitados_tamanho} nós visitados.")
        print("Caminho dos estados:")
        for estado in no_caminho(no_solucao):
            print(estado)
    else:
        print("Nenhuma solução encontrada com Dijkstra (com No).")
    
    print("\nExecutando busca A* (com No)...")
    visitados_tamanho, no_solucao = a_estrela(problema)
    if no_solucao is not None:
        print(f"Encontrada solução com {visitados_tamanho} nós visitados.")
        print("Caminho dos estados:")
        for estado in no_caminho(no_solucao):
            print(estado)
    else:
        print("Nenhuma solução encontrada com A* (com No).")

if __name__ == '__main__':
    main()
