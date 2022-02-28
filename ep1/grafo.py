from ast import List
# from asyncio import PriorityQueue
from multiprocessing.dummy import Array
from queue import PriorityQueue
import random
from vertice import *
# from a_estrela import a_estrela
# from aux_ import vertice_caminho, no_caminho 
# from vertice import No

class Grafo:
  def __init__(self):
    self.listaVertices = []

  def pegarVertice(self, estado):
    for vertice in self.listaVertices:
      if vertice.estado == estado:
        return vertice 

  def adicionarVertice(self, estado, heuristica=0):
    vertice = Vertice(estado, heuristica)
    self.listaVertices.append(vertice)

  def adicionarAresta(self, primeiro_estado, segundo_estado, peso):
    primeiro_vertice = None
    segundo_vertice = None
    
    primeiro_vertice = self.pegarVertice(primeiro_estado)
    segundo_vertice = self.pegarVertice(segundo_estado)

    # cria uma aresta para cada vertice (uma implementacao de grafo)
    primeiro_vertice.adicionarAresta(segundo_vertice, peso)
    segundo_vertice.adicionarAresta(primeiro_vertice, peso)

  def imprimir(self):
    tamanhoListaVertice = len(self.listaVertices)
    
    divisao = "-"
    for i in range(0, tamanhoListaVertice):
      divisao += "-|--"
    divisao += "-"
    linha_matriz = "  "
    
    # cabecalho
    for vertice in self.listaVertices:
      linha_matriz += "| " + vertice.estado + " "
    print(linha_matriz)
    print(divisao)
  
    # linhas com os dados
    linha_matriz = ""
    for i in range(0, (tamanhoListaVertice)):
      for j in range(0, (tamanhoListaVertice)):
        if j == 0:
            linha_matriz += self.listaVertices[i].estado + " | "
        peso = self.listaVertices[i].acharPeso(self.listaVertices[j])
        linha_matriz += str(peso)
        if j != (tamanhoListaVertice - 1):
            linha_matriz += " | "
        else:
          print(linha_matriz)
          print(divisao)
          linha_matriz = ""
  
  def criarExemplo(self):
    # criando os vertices
    self.adicionarVertice('S')
    self.adicionarVertice('A')
    self.adicionarVertice('B')
    self.adicionarVertice('C')
    self.adicionarVertice('D')
    self.adicionarVertice('E')
    self.adicionarVertice('F')
    self.adicionarVertice('G')

    # criando as arestas
    # S
    self.adicionarAresta('S','A', 2)
    self.adicionarAresta('S','B', 1)
    self.adicionarAresta('S','F', 3)

    # A
    self.adicionarAresta('A','C', 2)
    self.adicionarAresta('A','D', 3)

    # B
    self.adicionarAresta('B','D', 2)
    self.adicionarAresta('B','E', 4)

    # C
    self.adicionarAresta('C','G', 4)

    # D
    self.adicionarAresta('D','G', 4)

    # F
    self.adicionarAresta('F','G', 6)

  def criarExemploHeuristicas(self):
    self.adicionarHeuristica('S', 6)
    self.adicionarHeuristica('A', 4)
    self.adicionarHeuristica('B', 5)
    self.adicionarHeuristica('C', 2)
    self.adicionarHeuristica('D', 2)
    self.adicionarHeuristica('E', 8)
    self.adicionarHeuristica('F', 4)
    self.adicionarHeuristica('G', 0)

  def adicionarHeuristica(self, estado, heuristica):
    vertice = self.pegarVertice(estado)
    vertice.heuristica = heuristica

  def encontrarCaminho(self, estadoInicio, estadoDestino):
    fila = PriorityQueue()
    vertice_inicial = self.pegarVertice(estadoInicio)
    fila.put(vertice_inicial.arestas[0], 0)
    veio_de = dict()
    custo_ate = dict()
    veio_de[vertice_inicial.estado] = None
    custo_ate[vertice_inicial.estado] = vertice_inicial.heuristica

    estados_visitados = ""

    while not fila.empty():
      arestaAtual = fila.get()

      estados_visitados += arestaAtual.proprioVertice.estado

      if self.testar_objetivo(arestaAtual.proprioVertice.estado, estadoDestino):
          break

      estados_visitados += " -> "

      for aresta in arestaAtual.proprioVertice.arestas:
          novo_custo = custo_ate[arestaAtual.proprioVertice.estado] + aresta.peso
          if aresta.verticeLigado.estado not in custo_ate or novo_custo < custo_ate[aresta.verticeLigado.estado]:
            custo_ate[aresta.verticeLigado.estado] = novo_custo
            prioridade = novo_custo + aresta.verticeLigado.heuristica
            fila.put(aresta.verticeLigado.arestas[0], prioridade)
            veio_de[aresta.verticeLigado.estado] = arestaAtual.proprioVertice.estado
    print("Ordem de estados visitados: " + estados_visitados)
    array_menor_custo = []
    estado_atual = estadoDestino
    while estado_atual != None:
      array_menor_custo.append(estado_atual)
      array_menor_custo.append(" -> ")
      estado_atual = veio_de[estado_atual]
    array_menor_custo.reverse()
    str_menor_caminho = ""
    for i in range(1, len(array_menor_custo)):
      str_menor_caminho += array_menor_custo[i]
    print("Caminho encontrado: " + str_menor_caminho)
    

  # Função booleana que verifica se o estado atual
  # é o estado objetivo do problema
  def testar_objetivo(self, estado_atual, estado_destino):
    return estado_atual == estado_destino
