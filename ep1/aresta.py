class Aresta:
  def __init__(self, verticeLigado, peso):
    self.verticeLigado = verticeLigado
    self.peso = peso

#   def __lt__(self, outro):
#     return (self.peso + self.heuristica) < (outro.peso + outro.heuristica)