class Aresta:
  def __init__(self, proprio_vertice, vertice_ligado, peso):
    self.proprio_vertice = proprio_vertice
    self.vertice_ligado = vertice_ligado
    self.peso = peso
    self.peso_acumulado = 0

  def __lt__(self, outro):
    return self.peso_acumulado <= outro.peso_acumulado