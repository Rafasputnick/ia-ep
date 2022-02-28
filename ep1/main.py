from grafo import *

if __name__ == "__main__":
  grafo = Grafo()
  grafo.criarExemplo()
  grafo.imprimir()
  print("\nDijkstra’s (heuristica sempre zero)")
  grafo.encontrarCaminho('S','G')
  
  print("\nA* (heuristica valida)")
  grafo.criarExemploHeuristicas()
  grafo.encontrarCaminho('S','G')
