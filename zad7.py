from enum import *
from typing import *

class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]
