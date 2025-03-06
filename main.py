from problem import initial_state, goal_state
from search_algorithms import greedy_search, dijkstra_search, astar_search

def main():
    print("Estado inicial:")
    for i, pile in enumerate(initial_state):
        print(f"Posição {i}: {pile}")
    print("\nEstado objetivo:")
    for i, pile in enumerate(goal_state):
        print(f"Posição {i}: {pile}")

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


if __name__ == '__main__':
    main()
