from ast import List
from multiprocessing.dummy import Array
import random
from vertice import *
# from a_estrela import a_estrela
# from aux_ import vertice_caminho, no_caminho 
# from vertice import No

class Grafo:
  def __init__(self):
    self.listaVertices = []

  def adicionarVertice(self, estado, heuristica=0):
    vertice = Vertice(estado, heuristica)
    self.listaVertices.append(vertice)

  def adicionarAresta(self, primeiro_estado, segundo_estado, peso):
    primeiro_vertice = None
    segundo_vertice = None
    
    for vertice in self.listaVertices:
      # pega o primeiro vertice
      if vertice.estado == primeiro_estado:
        primeiro_vertice = vertice
      # pega o segundo vertice
      if vertice.estado == segundo_estado:
        segundo_vertice = vertice

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
    grafo.adicionarVertice('S')
    grafo.adicionarVertice('A')
    grafo.adicionarVertice('B')
    grafo.adicionarVertice('C')
    grafo.adicionarVertice('D')
    grafo.adicionarVertice('E')
    grafo.adicionarVertice('F')
    grafo.adicionarVertice('G')

    # criando as arestas
    # S
    grafo.adicionarAresta('S','A', 2)
    grafo.adicionarAresta('S','B', 1)
    grafo.adicionarAresta('S','F', 3)

    # A
    grafo.adicionarAresta('A','C', 2)
    grafo.adicionarAresta('A','D', 3)

    # B
    grafo.adicionarAresta('B','D', 2)
    grafo.adicionarAresta('B','E', 4)

    # C
    grafo.adicionarAresta('C','G', 4)

    # D
    grafo.adicionarAresta('D','G', 4)

    # F
    grafo.adicionarAresta('F','G', 6)

  # Função booleana que verifica se o estado atual
  # é o estado objetivo do problema
  def testar_objetivo(self, estado_atual, estado_destino):
    return estado_atual == estado_destino

  # Função que gera os sucessores válidos 
  # a partir de um estado válido
  def gerar_sucessores(self, estado):
    sucessores = []

    # encontra a posição do _
    posicao = estado.index("_")

    expansoes = [self._direita, self._esquerda, self._cima, self._baixo]
    random.shuffle(expansoes)
    for expansao in expansoes:
      sucessor = expansao(posicao, estado)
      if sucessor is not None: sucessores.append(sucessor)

    return sucessores

  def _esquerda(self, posicao, estado_atual):
    # movimento para esquerda
    if posicao not in [0, 3, 6]:
      # peça de baixo desce
      sucessor = list(estado_atual)
      sucessor[posicao] = sucessor[posicao - 1]
      sucessor[posicao - 1] = "_"
      return (tuple(sucessor), "⬅️")
    
  def _cima(self, posicao, estado_atual):
    # movimento para cima
    ## Não gera se estiver no topo
    if posicao not in [0, 1, 2]:
      # peça de baixo sobe
      sucesso = list(estado_atual)
      sucesso[posicao] = sucesso[posicao - 3]
      sucesso[posicao - 3] = "_"
      return (tuple(sucesso), "⬆️")

  def _baixo(self, posicao, estado_atual):
    # movimento para baixo
    ## Não gera se estiver no fundo
    if posicao not in [6, 7, 8]:
      # peça de baixo desce
      sucessor = list(estado_atual)
      sucessor[posicao] = sucessor[posicao + 3]
      sucessor[posicao + 3] = "_"
      return (tuple(sucessor), "⬇️")

  def _direita(self, posicao, estado_atual):
    # movimento para direita
    ## Não gera se estiver na direita
    if posicao not in [2, 5, 8]:
      # peça de baixo desce
      sucessor = list(estado_atual)
      sucessor[posicao] = sucessor[posicao + 1]
      sucessor[posicao + 1] = "_"
      return (tuple(sucessor), "➡️")
  
  # Heurística 1: Checar se os valores 
  # esta heurística não é admissível, pois, pode dificultar 
  # a chegada de um resultado final
  def heuristica(self, estado):
    resultado = ["1", "2", "3", "4", "5", "6", "7", "8", "_"]
    return sum(1 for i in range(len(resultado)) if resultado[i] == estado[i])

  # Heurística 2: Distância para o resultado espero
  # Heurística adminissível, pois, sempre o resultado chega mais perto
  # Transformei o array em matriz para fazer cálculo de distância
  def heuristica2(self, estado):
    resultado = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "_"]]
    estado_matriz = [estado[0:3], estado[3:6], estado[6:9]]

    soma = 0

    for i in range(len(resultado)):
      for j in range(len(resultado[i])):
        valor = resultado[i][j]
        soma = soma + self.distancia_manhattan(valor, estado_matriz, i, j)

    return soma

  # Distância de Manhattan: d = |xi-xj| + |yi-yj|
  def distancia_manhattan(self, valor, estado, i, j):
    for k in range(len(estado)):
      for h in range(len(estado[k])):
        if valor == estado[k][h]: return abs(i-k)+abs(j-h)
    
  # Função de peso: Quando custa mover de um 
  # estado_origem para estado_destino. No Quebra Cabeça 
  # de 8, este peso é fixo e arbitrariamente será 1.
  def peso(self, estado_origem, estado_destino):
    return 1

if __name__ == "__main__":
  grafo = Grafo()
  grafo.criarExemplo()
  grafo.imprimir()


  # grafo.imprimir()

  # no_solucao = a_estrela(estado_inicial, 
  #                       q.testar_objetivo, 
  #                       q.gerar_sucessores, 
  #                       q.heuristica2,
  #                       q.peso,
  #                       q.imprimir)

  # print("Estado Inicial:")
  # print(q.imprimir(estado_inicial))

  # if(no_solucao is None):
  #   print("Não houve solução ao problema...")
  # else:
  #   print("Solução:")
  #   #caminho = no_caminho(no_solucao)
  #   caminho = vertice_caminho(no_solucao)
    # print(caminho)