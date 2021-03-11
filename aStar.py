from grafo import Grafo,Vertex,Adjacent
from orderedVector import OrderedVector

class AStar:
    def __init__(self,objective):
        self.objective = objective
        self.found = False

    def seach(self,actual):
        print(actual.name, actual.obj_distance)
        actual.visited = True

        if actual == self.objective:
            self.found = True
        else:
            adj_cities = OrderedVector(len(actual.adjacents))
            
            for adj in actual.adjacents:
                if adj.vertex.visited == False:
                    adj.vertex.visited = True
                    adj_cities.insert(adj)

            #if adj_cities.valors[1] != None:
            self.seach(adj_cities.valors[0].vertex)

grafo = Grafo()
astar = AStar(grafo.curitiba)
astar.seach(grafo.porto_uniao)
