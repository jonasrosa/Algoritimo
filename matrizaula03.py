# 3.	Faça uma função que recebe, por parâmetro,
# uma matriz 7x6 e retorna a soma dos elementos da linha 5
# e da coluna 3.


def somar_matriz(matriz):
    solucao = []

    for i in range(1):
        soma = 0
        for j in range(6):
            resultado = matriz[i][2]
            resultado1 = matriz[4][j]
            soma = soma +( resultado + resultado1)
            solucao.append(soma)

    return (f"O resultado sa soma é{soma} = {solucao}  {resultado} {resultado1}")

matriz = [
    [1, 2, 3, 4, 5, 6],
    [6, 7, 8, 9, 0, 1],
    [2, 3, 4, 5, 6, 7],
    [7, 8, 9, 0, 1, 2],
    [2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8],
    [4, 5, 6, 7, 8, 9]
]


print(somar_matriz(matriz))