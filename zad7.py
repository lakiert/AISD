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
            result += f'- {key.data}: v{key.data} ----> [{value}] \n'
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

    # def show(self):
    #
    #     values = self.adjacencies.values()
    #     values_list = list(values)
    #
    #     g = nx.Graph()
    #     nx.draw(g, with_labels=True)
    #     plt.savefig("filename.png")


graf1 = Graph()

graf1.create_vertex(0)
graf1.create_vertex(1)
graf1.create_vertex(2)
graf1.create_vertex(3)
graf1.create_vertex(4)
graf1.create_vertex(5)

klucze = graf1.adjacencies.keys()
klucze_x = [x for x in klucze]

graf1.add(EdgeType(1), klucze_x[0], klucze_x[1])
graf1.add(EdgeType(1), klucze_x[0], klucze_x[5])
graf1.add(EdgeType(1), klucze_x[2], klucze_x[1])
graf1.add(EdgeType(1), klucze_x[4], klucze_x[1])
graf1.add(EdgeType(1), klucze_x[5], klucze_x[1])
graf1.add(EdgeType(1), klucze_x[5], klucze_x[2])
graf1.add(EdgeType(1), klucze_x[2], klucze_x[3])
graf1.add(EdgeType(1), klucze_x[3], klucze_x[4])
graf1.add(EdgeType(1), klucze_x[4], klucze_x[5])
