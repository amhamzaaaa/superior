graph = {
    'A': ['B', 'C'],  
    'B': ['D', 'E'], 
    'C': ['F'],      
    'D': [],         
    'E': ['F'],      
    'F': []           
}

def BFS(graph, start):
    
    visited = set()
    lis = [start] 
    result = []           

    while lis:

        node = lis.pop(0)
        
        if node not in visited:
            visited.add(node)       
            result.append(node)     
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    lis.append(neighbor)
    
    return result


start_node = 'A'
BFS(graph, start_node)
