from queue import PriorityQueue
from vertice import *
class Grafo:
  def __init__(self):
    self.listaVertices = []

  def pegar_vertice(self, estado):
    for vertice in self.listaVertices:
      if vertice.estado == estado:
        return vertice 

  def adicionar_vertice(self, estado, heuristica=0):
    vertice = Vertice(estado, heuristica)
    self.listaVertices.append(vertice)

  def adicionar_aresta(self, primeiro_estado, segundo_estado, peso):
    primeiro_vertice = None
    segundo_vertice = None
    
    primeiro_vertice = self.pegar_vertice(primeiro_estado)
    segundo_vertice = self.pegar_vertice(segundo_estado)

    # cria uma aresta para cada vertice (uma implementacao de grafo)
    primeiro_vertice.adicionar_aresta(segundo_vertice, peso)
    segundo_vertice.adicionar_aresta(primeiro_vertice, peso)

  def __str__(self):
    str_retorno = ""
    tamanhoListaVertice = len(self.listaVertices)
    
    divisao = "-"
    for i in range(0, tamanhoListaVertice):
      divisao += "-|--"
    divisao += "-"
    linha_matriz = "  "
    
    # cabecalho
    for vertice in self.listaVertices:
      linha_matriz += "| " + vertice.estado + " "
    str_retorno += linha_matriz + "\n"
    str_retorno += divisao + "\n"
  
    # linhas com os dados
    linha_matriz = ""
    for i in range(0, (tamanhoListaVertice)):
      for j in range(0, (tamanhoListaVertice)):
        if j == 0:
            linha_matriz += self.listaVertices[i].estado + " | "
        peso = self.listaVertices[i].achar_peso(self.listaVertices[j])
        linha_matriz += str(peso)
        if j != (tamanhoListaVertice - 1):
            linha_matriz += " | "
        else:
          str_retorno += linha_matriz + "\n"
          str_retorno += divisao + "\n"
          linha_matriz = ""

    return str_retorno

  def criar_exemplo(self):
    # criando os vertices
    self.adicionar_vertice('S', 0)
    self.adicionar_vertice('A', 0)
    self.adicionar_vertice('B', 0)
    self.adicionar_vertice('C', 0)
    self.adicionar_vertice('D', 0)
    self.adicionar_vertice('E', 0)
    self.adicionar_vertice('F', 0)
    self.adicionar_vertice('G', 0)

    # criando as arestas
    # S
    self.adicionar_aresta('S','A', 2)
    self.adicionar_aresta('S','B', 1)
    self.adicionar_aresta('S','F', 3)

    # A
    self.adicionar_aresta('A','C', 2)
    self.adicionar_aresta('A','D', 3)

    # B
    self.adicionar_aresta('B','D', 2)
    self.adicionar_aresta('B','E', 4)

    # C
    self.adicionar_aresta('C','G', 4)

    # D
    self.adicionar_aresta('D','G', 4)

    # F
    self.adicionar_aresta('F','G', 6)

  def criar_exemploHeuristicas(self):
    self.adicionar_heuristica('S', 6)
    self.adicionar_heuristica('A', 4)
    self.adicionar_heuristica('B', 5)
    self.adicionar_heuristica('C', 2)
    self.adicionar_heuristica('D', 2)
    self.adicionar_heuristica('E', 8)
    self.adicionar_heuristica('F', 4)
    self.adicionar_heuristica('G', 0)

  def adicionar_heuristica(self, estado, heuristica):
    vertice = self.pegar_vertice(estado)
    vertice.heuristica = heuristica

  def encontrar_caminho(self, estadoInicio, estadoDestino):
    fila = PriorityQueue()
    vertice_inicial = self.pegar_vertice(estadoInicio)
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
            aresta_descoberta = aresta.verticeLigado.arestas[0]
            aresta_descoberta.peso_acumulado = novo_custo + aresta.verticeLigado.heuristica
            fila.put(aresta_descoberta)
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
