from Grafo import Grafo

class Lista03:
    def contaCoresVizinhos(vertices,vizinhanca):
        cores = {}
        for i in range(len(vizinhanca)):
            if vizinhanca[i]:
                if vertices[i] not in cores:
                    cores[vertices[i]] = 1
                else:
                    cores[vertices[i]] += 1
        return cores
    
    def contaCores(vertices):          
        cores = {}
        for vertice in vertices:
            if vertices[vertice] not in cores:
                cores[vertices[vertice]] = 1
            else:
                cores[vertices[vertice]] += 1
        return cores

    def coloreGrafo(grafo: Grafo):
        estavel = False
        while not estavel:

            cores = list(set(grafo.vertices.values()))
            novo_vertices = grafo.vertices.copy()

            for cor in cores:
                for v1 in grafo.vertices:
                    cor_v1 = novo_vertices[v1]
                    if cor_v1 == cor:
                        for v2 in range(v1+1,max(grafo.vertices)+1):
                            
                            cor_v2 = novo_vertices[v2]

                            if cor_v1 == cor_v2:
                                v1_vizinhos = grafo.matriz[v1]
                                cores_v1_vizinhos = Lista03.contaCoresVizinhos(grafo.vertices,v1_vizinhos)

                                v2_vizinhos = grafo.matriz[v2]
                                cores_v2_vizinhos = Lista03.contaCoresVizinhos(grafo.vertices,v2_vizinhos)

                                if cores_v1_vizinhos != cores_v2_vizinhos:
                                    novo_vertices[v2] += 1

            if novo_vertices == grafo.vertices:
                estavel = True
            else:
                grafo.vertices = novo_vertices

    def analisaLista():
        with open('Lista03/Instâncias_isomorfismo.txt') as string_instancias:
            sequencias = string_instancias.read().split(sep='\n')
            i = 0
            contador = 0
            n_iso = []
            while i < len(sequencias):

                tamanho_par = int(sequencias[i])
                contador+=1
                i+=1
                par = ([],[])
                for j in range (0,tamanho_par):
                    linha_par_0 = [int(x) for x in list(sequencias[i+j])]
                    par[0].append(linha_par_0)

                    linha_par_1 = [int(x) for x in list(sequencias[i+j+tamanho_par+1])]
                    par[1].append(linha_par_1)

                G1 = Grafo(tamanho_par,par[0])
                Lista03.coloreGrafo(G1)
                cores_g1 = Lista03.contaCores(G1.vertices)

                G2 = Grafo(tamanho_par,par[1])
                Lista03.coloreGrafo(G2)
                cores_g2 = Lista03.contaCores(G2.vertices)
                
                if cores_g1 != cores_g2:
                    n_iso.append(contador)
                i+=2*(tamanho_par+1)
            return n_iso 

if __name__ == '__main__':
    print(Lista03.analisaLista())