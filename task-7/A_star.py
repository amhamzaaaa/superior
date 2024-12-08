import heapq

class Node:
    def __init__(self, position, g=0, h=0):
        self.position = position
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def a_star(start, end, grid):
    open_list = []
    closed_list = set()
    
    start_node = Node(start, 0, manhattan_distance(start, end))
    end_node = Node(end)
    
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)
        
        if current_node.position == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        for neighbor in get_neighbors(current_node.position, grid):
            if neighbor in closed_list:
                continue

            g = current_node.g + 1
            h = manhattan_distance(neighbor, end)
            neighbor_node = Node(neighbor, g, h)
            neighbor_node.parent = current_node

            if add_to_open(open_list, neighbor_node):
                heapq.heappush(open_list, neighbor_node)
    
    return None

def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def get_neighbors(position, grid):
    neighbors =
