class Visitados:
    def __init__(self):
        # Como o estado precisa ser um objeto imutável, convertemos para tupla.
        self.visitados = set({})

    def adicionar(self, no):
        self.visitados.add(tuple(no.estado))

    def foi_visitado(self, no):
        return tuple(no.estado) in self.visitados

    def tamanho(self):
        return len(self.visitados)
