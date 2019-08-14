"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        if not vertex in self.vertices:
          self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
          if not v2 in self.vertices[v1]:
            self.vertices[v1].add(v2)
        else:
          print("Need both vertices to exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        q = Queue()
        visited = [False] * len(self.vertices)
        q.enqueue(starting_vertex)
        # print(f"enqueue: {starting_vertex}")
        visited[starting_vertex-1] = True
        
        while q.size() > 0:
          current = q.dequeue()
          print(f"dequeue: {current}")
          for v in self.vertices[current]:
            if visited[v-1] == False:
              # print(f"visited: {v}")
              visited[v-1] = True
              q.enqueue(v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        s = Stack()
        visited = [False] * len(self.vertices)
        s.push(starting_vertex)
        # print(f"enqueue: {starting_vertex}")
        visited[starting_vertex-1] = True
        
        while s.size() > 0:
          current = s.pop()
          print(f"pop: {current}")
          for v in self.vertices[current]:
            if visited[v-1] == False:
              # print(f"visited: {v}")
              visited[v-1] = True
              s.push(v)

    def dft_actually_recursive(self, starting_vertex, visited):
        visited[starting_vertex-1] = True
        print(starting_vertex)

        for v in self.vertices[starting_vertex]:
          if visited[v-1] == False:
            self.dft_actually_recursive(v, visited)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        
        visited = [False] * len(self.vertices)
        self.dft_actually_recursive(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        queue = Queue()
        visited = [False] * len(self.vertices)
        queue.enqueue([starting_vertex])
        visited[starting_vertex-1] = True
        
        while queue.size() > 0:
          current_path = queue.dequeue()
          last_vertex = current_path[-1]
          if last_vertex == destination_vertex:
            return current_path
          for vertex in self.vertices[last_vertex]:
            if visited[vertex-1] == False:
              visited[vertex-1] = True
              new_path = current_path + [vertex]
              queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        stack = Stack()
        visited = [False] * len(self.vertices)
        stack.push([starting_vertex])
        visited[starting_vertex-1] = True
        
        while stack.size() > 0:
          current_path = stack.pop()
          last_vertex = current_path[-1]
          if last_vertex == destination_vertex:
            return current_path
          for vertex in self.vertices[last_vertex]:
            if visited[vertex-1] == False:
              visited[vertex-1] = True
              new_path = current_path + [vertex]
              stack.push(new_path)


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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
