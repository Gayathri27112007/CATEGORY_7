# Map Coloring using Constraint Satisfaction Problem (CSP)

# Map of states and their neighboring states
map_graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Available colors
colors = ["Red", "Green", "Blue"]

# Store the color assigned to each state
assignment = {}


def is_valid(state, color):
    # Check all neighboring states
    for neighbor in map_graph[state]:

        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False

    return True


def map_coloring(state_list, index):

    # If all states are colored
    if index == len(state_list):
        return True

    state = state_list[index]

    # Try each color
    for color in colors:

        if is_valid(state, color):

            assignment[state] = color

            # Move to the next state
            if map_coloring(state_list, index + 1):
                return True

            # Backtracking
            del assignment[state]

    return False


states = list(map_graph.keys())

print("Map Coloring using CSP")
print("----------------------")

if map_coloring(states, 0):

    for state in states:
        print(state, "->", assignment[state])

else:
    print("No solution exists.")