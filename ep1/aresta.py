class Aresta:
  def __init__(self, proprioVertice, verticeLigado, peso):
    self.proprioVertice = proprioVertice
    self.verticeLigado = verticeLigado
    self.peso = peso
    self.peso_acumulado = 0

  def __lt__(self, outro):
    return self.peso_acumulado <= outro.peso_acumulado
    # return (self.peso + self.proprioVertice.heuristica) < (outro.peso + outro.proprioVertice.heuristica)