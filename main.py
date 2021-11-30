"""
LAVINA KATHAMBI 
Advanced Algorithm_Assignment2
Handling Minimum Spanning Trees with Prim's Algorithm
"""

# Assign no. vertices in the graph (Image in google docs)
no_vertices = 7

#Adjacency Matrix from the graph
graph_matrix = [[0, 28, 0, 0, 0, 10, 0],
    [28, 0, 16, 0, 0, 0, 14],
    [0, 16, 0, 12, 0, 0, 0 ],
    [0, 0, 12, 0, 22, 0, 18],
    [0, 0, 0, 22, 0, 25, 24],
    [10, 0, 0, 0, 25, 0, 0],
    [0, 14, 0, 18, 34, 0, 0]]


# Defining the starting point, where i'll keep adding edges as I iterate
source_node = [0, 0, 0, 0, 0, 0, 0]

# Set the Source Node to be True initially as the lowest weight vertex
source_node[0] = True

# Defining the starting edge, will be updated with the edge with lowest weight
current_edge = 0

# Creating an infinity variable to compare with weight of edges
infinity_var = 9999999 

# Loop through to iterate over edges and vertices to return MST
while (current_edge < no_vertices - 1):
    min_Val = infinity_var
    i = 0
    j = 0
    for p in range(no_vertices):
        if source_node[p]:
            for q in range(no_vertices):
                if ((not source_node[q]) and graph_matrix[p][q]):  
                    # Check to ensure no repeated vertices are already existing
                    if min_Val > graph_matrix[p][q]:
                        min_Val = graph_matrix[p][q]
                        i = p
                        j = q
    print("Vertex 1:" + str(i+1) + " " + "Vertex 2:" + str(j+1) + ":" +  " " + "Weight = " + str(graph_matrix[i][j]))
    source_node[j] = True
    current_edge += 1