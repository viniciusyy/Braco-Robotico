import heapq
from problem import heuristic, get_successors, goal_state

# ----------------------------------------------------------------
# Implementações usando a representação de estados (tuplas)
# ----------------------------------------------------------------

def greedy_search(initial):
    """
    Busca gananciosa (greedy) onde a prioridade é dada somente à heurística.
    """
    frontier = []
    heapq.heappush(frontier, (heuristic(initial), initial, [], 0))
    explored = set()

    while frontier:
        h_val, state, path, cost_so_far = heapq.heappop(frontier)
        if state in explored:
            continue
        explored.add(state)
        if state == goal_state:
            return path, cost_so_far
        for succ, move_descr, move_cost in get_successors(state):
            if succ in explored:
                continue
            new_path = path + [move_descr]
            heapq.heappush(frontier, (heuristic(succ), succ, new_path, cost_so_far + move_cost))
    return None, float('inf')

def dijkstra_search(initial):
    """
    Busca de custo uniforme (Dijkstra) usando a representação de estados.
    """
    frontier = []
    heapq.heappush(frontier, (0, initial, []))
    explored = {}

    while frontier:
        cost_so_far, state, path = heapq.heappop(frontier)
        if state in explored and explored[state] <= cost_so_far:
            continue
        explored[state] = cost_so_far
        if state == goal_state:
            return path, cost_so_far
        for succ, move_descr, move_cost in get_successors(state):
            new_cost = cost_so_far + move_cost
            new_path = path + [move_descr]
            heapq.heappush(frontier, (new_cost, succ, new_path))
    return None, float('inf')

def astar_search(initial):
    """
    Busca A* (A-estrela) usando a representação de estados.
    """
    frontier = []
    heapq.heappush(frontier, (heuristic(initial), 0, initial, []))
    explored = {}

    while frontier:
        f_val, cost_so_far, state, path = heapq.heappop(frontier)
        if state in explored and explored[state] <= cost_so_far:
            continue
        explored[state] = cost_so_far
        if state == goal_state:
            return path, cost_so_far
        for succ, move_descr, move_cost in get_successors(state):
            new_cost = cost_so_far + move_cost
            new_path = path + [move_descr]
            heapq.heappush(frontier, (new_cost + heuristic(succ), new_cost, succ, new_path))
    return None, float('inf')

