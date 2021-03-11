class Vertex:
    def __init__(self,name,obj_distance):
        self.name = name
        self.obj_distance = obj_distance
        self.visited = False
        self.adjacents = []

    def add_adjacent(self,adj):
        self.adjacents.append(adj)

class Adjacent:
    def __init__(self,vertex,cost):
        self.vertex = vertex
        self.cost = cost
        self.astar_distance = vertex.obj_distance + cost

class Grafo:

    porto_uniao = Vertex('Porto União',208)
    paulo_frontin = Vertex('Paulo Frontin',172)
    canoinhas = Vertex('Canoinhas',141)
    tres_barras = Vertex('Três Barras',131)
    sao_mateus_do_sul = Vertex('São Mateus do Sul',123)
    irati = Vertex('Irati',139)
    curitiba = Vertex('Curitiba',0)
    palmeira = Vertex('Palmeira',59)
    mafra = Vertex('Mafra',94)
    campo_largo = Vertex('Campo Largo', 27)
    balsa_nova = Vertex('Balsa Nova',41)
    lapa = Vertex('Lapa',74)
    tijucas_do_sul = Vertex('Tijucas do Sul',56)
    araucaria = Vertex('Araucária',23)
    sao_jose_dos_pinhais = Vertex('São José dos Pinhais',13)
    contenda = Vertex('Contenda',39)

    porto_uniao.add_adjacent(Adjacent(paulo_frontin,46))
    porto_uniao.add_adjacent(Adjacent(sao_mateus_do_sul,87))
    porto_uniao.add_adjacent(Adjacent(canoinhas,78))

    paulo_frontin.add_adjacent(Adjacent(porto_uniao,46))
    paulo_frontin.add_adjacent(Adjacent(irati,75))

    canoinhas.add_adjacent(Adjacent(porto_uniao,78))
    canoinhas.add_adjacent(Adjacent(tres_barras,12))
    canoinhas.add_adjacent(Adjacent(mafra,66))

    tres_barras.add_adjacent(Adjacent(sao_mateus_do_sul,43))
    tres_barras.add_adjacent(Adjacent(canoinhas,12))

    sao_mateus_do_sul.add_adjacent(Adjacent(porto_uniao,87))
    sao_mateus_do_sul.add_adjacent(Adjacent(irati,57))
    sao_mateus_do_sul.add_adjacent(Adjacent(palmeira,77))
    sao_mateus_do_sul.add_adjacent(Adjacent(lapa,60))
    sao_mateus_do_sul.add_adjacent(Adjacent(tres_barras,43))

    irati.add_adjacent(Adjacent(palmeira,75))
    irati.add_adjacent(Adjacent(sao_mateus_do_sul,57))
    irati.add_adjacent(Adjacent(paulo_frontin,75))

    curitiba.add_adjacent(Adjacent(sao_jose_dos_pinhais,15))
    curitiba.add_adjacent(Adjacent(araucaria,37))
    curitiba.add_adjacent(Adjacent(balsa_nova,51))
    curitiba.add_adjacent(Adjacent(campo_largo,29))

    palmeira.add_adjacent(Adjacent(irati,75))
    palmeira.add_adjacent(Adjacent(campo_largo,55))
    palmeira.add_adjacent(Adjacent(sao_mateus_do_sul,77))

    mafra.add_adjacent(Adjacent(canoinhas,66))
    mafra.add_adjacent(Adjacent(lapa,57))
    mafra.add_adjacent(Adjacent(tijucas_do_sul,99))

    campo_largo.add_adjacent(Adjacent(palmeira,55))
    campo_largo.add_adjacent(Adjacent(curitiba,29))
    campo_largo.add_adjacent(Adjacent(balsa_nova,22))

    balsa_nova.add_adjacent(Adjacent(contenda,19))
    balsa_nova.add_adjacent(Adjacent(campo_largo,22))
    balsa_nova.add_adjacent(Adjacent(curitiba,51))

    lapa.add_adjacent(Adjacent(sao_mateus_do_sul,60))
    lapa.add_adjacent(Adjacent(contenda,26))
    lapa.add_adjacent(Adjacent(mafra,57))

    tijucas_do_sul.add_adjacent(Adjacent(mafra,99))
    tijucas_do_sul.add_adjacent(Adjacent(sao_jose_dos_pinhais,49))

    araucaria.add_adjacent(Adjacent(contenda,18))
    araucaria.add_adjacent(Adjacent(curitiba,37))
    
    sao_jose_dos_pinhais.add_adjacent(Adjacent(tijucas_do_sul,49))
    sao_jose_dos_pinhais.add_adjacent(Adjacent(curitiba,15))

    contenda.add_adjacent(Adjacent(lapa,26))
    contenda.add_adjacent(Adjacent(balsa_nova,22))
    contenda.add_adjacent(Adjacent(araucaria,18))