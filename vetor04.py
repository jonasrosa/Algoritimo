

def achar_valor(valor):

    menor_valor = valor[0]
    for i in range(1,len(valor)):
        if valor[i] < menor_valor:
            menor_valor = valor[i]

    return menor_valor


vetor = [100, -20, 288,3]
print(type(vetor))


