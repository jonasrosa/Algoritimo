#2.	Implemente uma função que retorne o maior elemento de um vetor de inteiros

def achar_valor(valor):

    maior_valor = valor[0]
    for i in range(1,len(valor)):
        if valor[i]> maior_valor:
            maior_valor = valor [i]

    return maior_valor


vetor = [100, 20,288,3]
print(f"{achar_valor(vetor)}")


