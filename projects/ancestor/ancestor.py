class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph():
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex_id):
    if vertex_id not in self.vertices:
      self.vertices[vertex_id] = set()
    else:
      pass

  def add_edge(self, v_from, v_to):
    if v_from in self.vertices and v_to in self.vertices:
      self.vertices[v_from].add(v_to)
    else:
      pass

def earliest_ancestor(ancestors, starting_node):
  graph = Graph()

  for pair in ancestors:
    graph.add_vertex(pair[0])
    graph.add_vertex(pair[1])
    graph.add_edge(pair[1]. pair[0])

  q = Queue()
  q.enqueue(starting_node)

  max_path_size: 1
  earliest_ancestor = -1

  while q.size() > 0
    path = q.dequeue()
    node = path[-1]

    if len(path) > max_path_size or (len(path) == max_path_size and node < earliest_ancestor):
      earliest_ancestor = node
      