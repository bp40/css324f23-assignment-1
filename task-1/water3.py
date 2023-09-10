def initial_state():
    return (8, 0, 0)

def is_goal(state):
    return state[0] == 4 and state[1] == 4

def successors(state):
    capacities = [8,5,3]
    # 8L=0, 5L=1, 3L=2
    movePairs = [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)] 

    for pair in movePairs:
        source, destination = pair
        # min(water in source , empty space in destination)
        amount = min(state[source], capacities[destination] - state[destination])

        if amount > 0:
            updatedState = list(state)
            updatedState[source] -= amount
            updatedState[destination] += amount
            yield (tuple(updatedState), amount)
