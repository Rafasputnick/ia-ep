from grafo import Grafo

if __name__ == "__main__":
  grafo = Grafo()
  grafo.criar_exemplo()
  print(grafo)
  print("\nDijkstra’s (heuristica sempre zero)")
  grafo.encontrar_caminho('S','G')
  
  print("\nA* (heuristica valida)")
  grafo.criar_exemploHeuristicas()
  grafo.encontrar_caminho('S','G')