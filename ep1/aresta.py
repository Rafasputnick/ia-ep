class Aresta:
  def __init__(self, proprioVertice, verticeLigado, peso):
    self.proprioVertice = proprioVertice
    self.verticeLigado = verticeLigado
    self.peso = peso

  def __lt__(self, outro):
    return (self.peso + self.proprioVertice.heuristica) < (outro.peso + outro.proprioVertice.heuristica)
#   def __lt__(self, outro):
#     return (self.peso + self.heuristica) < (outro.peso + outro.heuristica)