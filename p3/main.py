from Queue1 import Queue
from enum import *
from typing import *
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


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
    list_from = []
    list_to = []

    def __init__(self):
        self.adjacencies = {}
        self.list_from = []
        self.list_to = []

    def __str__(self):
        result = ""
        list1 = self.adjacencies.keys()
        for key in list1:
            temp = []
            for i in range(len(self.list_from)):
                if self.list_from[i] == key.data:
                    temp.append(self.list_to[i])
                if self.list_to[i] == key.data:
                    temp.append(self.list_from[i])
            result += f'- {key.data}: {key.data} ----> [{temp}] \n'
        return result

    def create_vertex(self, value):
        vertex = Vertex(value, len(self.adjacencies))
        self.adjacencies[vertex] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float]):
        edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)
        self.list_from.append(source.data)
        self.list_to.append(destination.data)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float]):
        edge = Edge(source, destination, weight)
        edge2 = Edge(destination, source, weight)
        self.adjacencies[source].append(edge)
        self.adjacencies[destination].append(edge2)
        self.list_from.append(source.data)
        self.list_to.append(destination.data)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge.name == "directed":
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]):
        queue = Queue()
        vertices = list(self.adjacencies.keys())
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
        vertices = list(self.adjacencies.keys())
        visited = []
        self.dfs(vertices[0], visited, visit)

    def show(self):
        relationships = pd.DataFrame({'from': [x for x in self.list_from],
                                      'to': [y for y in self.list_to]})
        g = nx.from_pandas_edgelist(relationships, 'from', 'to', create_using=nx.Graph())
        nx.draw(g, with_labels=True)
        # plt.savefig("graf0.png")
        plt.show()


def mutual_friends(g: Graph, f0: Any, f1: Any) -> List[Any]:
    f0_friends = []
    f1_friends = []
    for i in range(len(g.list_from)):
        if g.list_from[i] == f0:
            f0_friends.append(g.list_to[i])
        if g.list_from[i] == f1:
            f1_friends.append(g.list_to[i])
    for i in range(len(g.list_to)):
        if g.list_to[i] == f0:
            f0_friends.append(g.list_from[i])
        if g.list_to[i] == f1:
            f1_friends.append(g.list_from[i])
    mut = set(f0_friends) & set(f1_friends)
    mut_friends = list(mut)
    return mut_friends


def visit(vertex: Any) -> None:
    print(vertex.data)


# g = Graph()
#
# g.create_vertex('VI')  # 0
# g.create_vertex('CH')  # 1
# g.create_vertex('RU')  # 2
# g.create_vertex('PA')  # 3
# g.create_vertex('RA')  # 4
# g.create_vertex('SU')  # 5
# g.create_vertex('CO')  # 6
# g.create_vertex('KE')  # 7
#
# vertex = list(g.adjacencies.keys())
#
# g.add_undirected_edge(vertex[0], vertex[1], None)
# g.add_undirected_edge(vertex[0], vertex[2], None)
# g.add_undirected_edge(vertex[0], vertex[3], None)
# g.add_undirected_edge(vertex[2], vertex[4], None)
# g.add_undirected_edge(vertex[2], vertex[5], None)
# g.add_undirected_edge(vertex[3], vertex[6], None)
# g.add_undirected_edge(vertex[3], vertex[7], None)
# g.add_undirected_edge(vertex[6], vertex[2], None)
# g.add_undirected_edge(vertex[6], vertex[0], None)
#
# print(mutual_friends(g, 'SU', 'RA'))
# print(mutual_friends(g, 'VI', 'CO'))
# print(mutual_friends(g, 'PA', 'RU'))


# graf testowy nr 1
# g1 = Graph()
# g1.create_vertex('AB')  # 0
# g1.create_vertex('CD')  # 1
# g1.create_vertex('EF')  # 2
# g1.create_vertex('GH')  # 3
# vertex1 = list(g1.adjacencies.keys())
# g1.add_undirected_edge(vertex1[0], vertex1[1], None)
# g1.add_undirected_edge(vertex1[0], vertex1[3], None)
# g1.add_undirected_edge(vertex1[2], vertex1[1], None)
# g1.add_undirected_edge(vertex1[2], vertex1[3], None)
# print(mutual_friends(g1, 'AB', 'EF'))
# print(mutual_friends(g1, 'CD', 'GH'))


# graf testowy nr 2
# g2 = Graph()
# g2.create_vertex('A')  # 0
# g2.create_vertex('B')  # 1
# g2.create_vertex('C')  # 2
# g2.create_vertex('D')  # 3
# g2.create_vertex('E')  # 4
# g2.create_vertex('F')  # 5
# g2.create_vertex('G')  # 6
# vertex2 = list(g2.adjacencies.keys())
# g2.add_undirected_edge(vertex2[0], vertex2[1], None)
# g2.add_undirected_edge(vertex2[0], vertex2[6], None)
# g2.add_undirected_edge(vertex2[6], vertex2[1], None)
# g2.add_undirected_edge(vertex2[0], vertex2[2], None)
# g2.add_undirected_edge(vertex2[0], vertex2[3], None)
# g2.add_undirected_edge(vertex2[2], vertex2[3], None)
# g2.add_undirected_edge(vertex2[0], vertex2[4], None)
# g2.add_undirected_edge(vertex2[0], vertex2[5], None)
# g2.add_undirected_edge(vertex2[5], vertex2[4], None)
# print(mutual_friends(g2, 'G', 'B'))
# print(mutual_friends(g2, 'A', 'D'))
# print(mutual_friends(g2, 'E', 'G'))


# graf testowy nr 3
# g3 = Graph()
# g3.create_vertex('A')  # 0
# g3.create_vertex('B')  # 1
# g3.create_vertex('C')  # 2
# g3.create_vertex('D')  # 3
# g3.create_vertex('E')  # 4
# g3.create_vertex('F')  # 5
# g3.create_vertex('G')  # 6
# vertex3 = list(g3.adjacencies.keys())
# g3.add_undirected_edge(vertex3[0], vertex3[1], None)
# g3.add_undirected_edge(vertex3[0], vertex3[2], None)
# g3.add_undirected_edge(vertex3[0], vertex3[3], None)
# g3.add_undirected_edge(vertex3[2], vertex3[1], None)
# g3.add_undirected_edge(vertex3[2], vertex3[3], None)
# g3.add_undirected_edge(vertex3[1], vertex3[3], None)
# g3.add_undirected_edge(vertex3[3], vertex3[4], None)
# g3.add_undirected_edge(vertex3[3], vertex3[5], None)
# g3.add_undirected_edge(vertex3[4], vertex3[6], None)
# g3.add_undirected_edge(vertex3[5], vertex3[6], None)
# print(mutual_friends(g3, 'C', 'D'))
# print(mutual_friends(g3, 'D', 'G'))
# print(mutual_friends(g3, 'A', 'E'))
