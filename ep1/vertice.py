from aresta import *
class Vertice:
  def __init__(self, estado, heuristica):
    self.estado = estado
    self.heuristica = heuristica
    self.arestas = []

  def adicionarAresta(self, verticeRelacionado, peso):
    aresta = Aresta(self, verticeRelacionado, peso)
    self.arestas.append(aresta)

  def acharPeso(self, vertice):
    for aresta in self.arestas:
      if aresta.verticeLigado == vertice:
        return aresta.peso
    return 0 # se nao achar peso ele retorna 0