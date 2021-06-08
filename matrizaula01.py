
def somar_matrizes(matriz):
    for i in range(5):
        print(matriz[i])
        valor = []
        soma = 0

        for j in range(5):
            soma = soma + matriz[i][j]
            valor.append(soma)



    for i in range(5):
        somatotal = 0
        for j in range(5):
            somatotal= somatotal+ valor[i]
    return somatotal



vetor=[[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10],[10,10,10,10,10]]
print(somar_matrizes(vetor))
