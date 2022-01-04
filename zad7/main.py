from Queue1 import Queue
from enum import *
from typing import *
import networkx as nx
import matplotlib.pyplot as plt


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data, index):
        self.data = data
        self.index = index


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def __str__(self):
        result = ""
        list1 = self.adjacencies.items()
        for key, value in list1:
            result += f'- {key.data}: {key.data} ----> [] \n'
        return result

    def create_vertex(self, value):
        vertex = Vertex(value, len(self.adjacencies))
        self.adjacencies[vertex] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float]):
        edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float]):
        edge = Edge(source, destination, weight)
        edge2 = Edge(destination, source, weight)
        self.adjacencies[source].append(edge)
        self.adjacencies[destination].append(edge2)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]):
        queue = Queue()
        vertices = list(graf1.adjacencies.keys())
        visited = [vertices[0]]
        queue.enqueue(vertices[0])
        while len(queue):
            v = queue.dequeue()
            visit(v)
            visited.append(v)
            for neighbour in self.adjacencies[v]:
                if neighbour.destination not in visited:
                    visited.append(neighbour.destination)
                    queue.enqueue(neighbour.destination)

    def dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
        visit(v)
        visited.append(v)
        for neighbour in self.adjacencies[v]:
            if neighbour.destination not in visited:
                self.dfs(neighbour.destination, visited, visit)

    def traverse_depth_first(self, visit: Callable[[Any], None]):
        vertices = list(graf1.adjacencies.keys())
        visited = []
        self.dfs(vertices[0], visited, visit)


def visit(vertex: Any) -> None:
    print(vertex.data)


graf1 = Graph()

graf1.create_vertex("v0")
graf1.create_vertex("v1")
graf1.create_vertex("v2")
graf1.create_vertex("v3")
graf1.create_vertex("v4")
graf1.create_vertex("v5")

vertex = list(graf1.adjacencies.keys())

graf1.add_directed_edge(vertex[0], vertex[1], None)
graf1.add_directed_edge(vertex[0], vertex[5], None)
graf1.add_directed_edge(vertex[2], vertex[1], None)
graf1.add_directed_edge(vertex[4], vertex[1], None)
graf1.add_directed_edge(vertex[5], vertex[1], None)
graf1.add_directed_edge(vertex[5], vertex[2], None)
graf1.add_directed_edge(vertex[2], vertex[3], None)
graf1.add_directed_edge(vertex[3], vertex[4], None)
graf1.add_directed_edge(vertex[4], vertex[5], None)


# graf1.traverse_breadth_first(visit)
# print(" ")
# graf1.traverse_depth_first(visit)
print(" ")
print(graf1)
