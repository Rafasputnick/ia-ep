class Aresta:
  def __init__(self, proprio_vertice, vertice_ligado, peso):
    self.proprio_vertice = proprio_vertice
    self.vertice_ligado = vertice_ligado
    self.peso = peso
    self.prioridade = 0

  def __lt__(self, outro):
    return self.prioridade <= outro.prioridade