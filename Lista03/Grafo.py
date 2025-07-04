

class Grafo:
    
    def __init__(self,tamanho, matriz):

        #iniciar os vértices com a mesma cor
        vertices = {}
        for i in range(tamanho):
            vertices[i] = 0
        self.vertices = vertices
        self.matriz = matriz
