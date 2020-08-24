"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create the new key with the vertex ID, and set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id] 

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        queue = Queue()
        # enqueue our starting node
        queue.enqueue(starting_vertex)
        # make a set to track if we have been here before
        visited = set()
        # while our queue is not empty
        while queue.size() > 0:
            # dequeue whatever is in the front of our line, this is our current node
            current = queue.dequeue()
            # if we have not visited this node yet,
            if current not in visited:
                # mark as visited
                print(current)
                visited.add(current)
                 # for each of its neighbors
                for i in self.get_neighbors(current):
                    # add to queue
                    queue.enqueue(i)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create the stack
        stack = Stack()
        # push the starting node
        stack.push(starting_vertex)
        # create set to track
        visited = set()
        # while the stack is not empty
        while stack.size() > 0:
            current = stack.pop()

            if current not in visited:
                print(current)
                visited.add(current)
                # get the neighbors involved
                for i in self.get_neighbors(current):
                    stack.push(i)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        queue = Queue()
        # Create a set to store visited vertices
        visited = set()
        # enqueue a PATH to the starting vertex
        queue.enqueue({
            'current_vert': starting_vertex,
            'path': [starting_vertex]
        })
        # While the queue is not empty:
        while queue.size() > 0:
            # Dequeue the first PATH and set it to current
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vert = current_obj['current_vert']
            # If that vertex has not been visited:
            if current_vert not in visited:
                 # Check if it's the target
                if current_vert == destination_vertex:
                    # Return PATH
                    print(current_path)
                    return current_path
                # Mark as visited
                visited.add(current_vert)
                # Add a PATH to its neighbors to the back of the queue
                for neighbor_vert in self.get_neighbors(current_vert):
                    new_path = list(current_path)
                    # Append neighbor - append returns None
                    new_path.append(neighbor_vert)

                    queue.enqueue({
                        'current_vert': neighbor_vert,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a stack
        stack = []
        # create a set to store visited vertices
        visited = set()
        # push a PATH to the starting vertex
        stack.append([starting_vertex])
        # while the stack is not empty
        while len(stack) > 0:
            # pop and set it to current
            current_path = stack.pop()
            # Grab last vertex from the PATH
            current = current_path[-1]
            # Check if it is the target
            if current == destination_vertex:
                # Return PATH
                return current_path
            # Mark as visited and add to stack
            visited.add(current)

            for vert in self.get_neighbors(current):
                new_stack = list(current_path)
                new_stack.append(vert)

                stack.append(new_stack)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
