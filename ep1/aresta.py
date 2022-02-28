class Aresta:
  def __init__(self, proprio_vertice, vertice_ligado, peso):
    self.proprio_vertice = proprio_vertice
    self.vertice_ligado = vertice_ligado
    self.peso = peso
    self.peso_acumulado = 0

  def __lt__(self, outro):
    return ((self.peso_acumulado <= outro.peso_acumulado) if self.proprio_vertice.heuristica != 0 else (self.peso + self.proprio_vertice.heuristica < outro.peso + outro.proprio_vertice.heuristica))