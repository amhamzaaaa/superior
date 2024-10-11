graph = {
    'A': ['B', 'C'],  
    'B': ['D', 'E'], 
    'C': ['F'],      
    'D': [],         
    'E': ['F'],      
    'F': []           
}


def in_DFS(graph, node, visited=None):
    if visited is None:
        visited = [] 

    if graph[node]:
        left_child = graph[node][0]
        if left_child not in visited:
            in_DFS(graph, left_child, visited) 

    if node not in visited:
        visited.append(node)

    for neighbour in graph[node][1:]:
        if neighbour not in visited:
            in_DFS(graph, neighbour, visited)

    print(visited)


def pre_DFS( graph, node, goal=None):
    stack = [node]
    visited = [node]
    while stack:
        flag = 0
        for neighbour in graph[stack[-1]]:
            if neighbour not in visited:
                stack += [neighbour]
                visited += [neighbour]
                if neighbour == goal:
                    return visited
                flag += 1
                break
        if flag == 0:        
            stack.pop()
    print(visited)


def postorder_dfs(graph, node, visited=None):
    if visited is None:
        visited = []

    for neighbor in graph[node]:
        if neighbor not in visited:
            postorder_dfs(graph, neighbor, visited)

    if node not in visited:
        visited.append(node)

    print(visited)