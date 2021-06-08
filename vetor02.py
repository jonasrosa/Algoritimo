# Escrever uma função que receba um vetor com 10 valores e retorne quantos destes valores são negativos.

def contar_negativos(vetor_valores):
    qtde_negativos = 0
    for i in range(len(vetor_valores)):
        if valores[i] < 0:
            qtde_negativos = qtde_negativos + 1
    return qtde_negativos


valores = []
for i in range(4):
    valor = int(input("Digite um valor: "))
    valores.append(valor)

print(f"O número de valores negativos é {contar_negativos(valores)}")

