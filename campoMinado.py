from random import *
def criar_campo(dimensao1):
    global matriz
    for i in range(dimensao1):
        linha = []
        for j in range(dimensao1):
            linha.append(0)
        matriz.append(linha)
    return matriz

def criar_mapa(dimensao1):
    global matriz1
    for i in range(dimensao1):
        linha = []
        for j in range(dimensao1):
            linha.append("x")
        matriz1.append(linha)
    return matriz1


def exibir_matriz(matriz):
    global dimensao
    print(" "*4, end="")
    for i in range(dimensao):
        print(f"{i} ", end="")
    print()
    for i in range(dimensao):
        print(f"{i} [ ", end="")
        for j in range(dimensao):
            print(f"{matriz[i][j]} ", end="")
        print("]")
    print()

def sorteio():

    for i in range(10):
        linha= randint(1, 7)
        coluna = randint(1,7)

        if matriz[linha][coluna]==0:
            matriz[linha][coluna]= "B"
            matriz[linha-1][coluna-1]=1
            matriz[linha-1][coluna]=1
            matriz[linha-1][coluna+1]=1
            matriz[linha+1][coluna]=1
            matriz[linha+1][coluna-1]=1
            matriz[linha+1][coluna+1]=1
            matriz[linha][coluna-1]=1
            matriz[linha][coluna+1]=1

        else:
            if matriz[linha][coluna]==1:
                matriz[linha][coluna] = "B"
                matriz[linha - 1][coluna - 1] = 2
                matriz[linha - 1][coluna] = 2
                matriz[linha - 1][coluna + 1] = 2
                matriz[linha + 1][coluna] = 2
                matriz[linha + 1][coluna - 1] = 2
                matriz[linha + 1][coluna + 1] = 1
                matriz[linha][coluna - 1] = 2
                matriz[linha][coluna + 1] = 2
            else:
                if matriz[linha][coluna] == 2:
                    matriz[linha][coluna] = "B"
                    matriz[linha - 1][coluna - 1] = 3
                    matriz[linha - 1][coluna] = 3
                    matriz[linha - 1][coluna + 1] = 3
                    matriz[linha + 1][coluna] = 2
                    matriz[linha + 1][coluna - 1] = 3
                    matriz[linha + 1][coluna + 1] = 3
                    matriz[linha][coluna - 1] = 3
                    matriz[linha][coluna + 1] = 3
                else:
                    if matriz[linha][coluna] == "B":
                        sorteio()



def abrir_matriz(matriz, i, j,matriz1 ):

    dimensao = len(matriz)

    if matriz[i][j] == 0:
        matriz[i][j] = " "
        matriz1[i][j] = " "

        linha_inicial = i - 1
        if linha_inicial < 0:
            linha_inicial = 0
        linha_final = i + 1
        if linha_final > dimensao - 1:
            linha_final = dimensao - 1
        coluna_inicial = j - 1
        if coluna_inicial < 0:
            coluna_inicial = 0
        coluna_final = j + 1
        if coluna_final > dimensao - 1:
            coluna_final = dimensao - 1

        for l in range(linha_inicial, linha_final + 1):
            for c in range(coluna_inicial, coluna_final + 1):
                abrir_matriz(matriz, l, c,matriz1)

#variaveis

matriz=[]
matriz1=[]
dimensao= 9
dimensao1= 9
mapa= criar_mapa(dimensao1)
campo= criar_campo(dimensao)

sorteio()

while True:
    bomba = 0
    contador = -1
    ganhador = 0
    for i in range(12):
        contador=contador+1

        marcar_bandeira= int (input("DIGITE 1 PRA MARACAR BANDEIRA OU 2 PARA ABRIR CAMPO"))
        if contador== 10:
            print("fim de jogo ")
            if bomba >= 1:
                print("VOCÊ PERDEU")
                exit()
            if ganhador== 10:
                print("Você Ganhou")
                exit()

        if marcar_bandeira==1:
            print(f"VOCÊ PODE MARCAR  10 CASAS, ATÉ AGORA VC JA MARCOU {contador} BANDEIRAS")
            linha1= int(input("Digite linha de 0 a 8:"))
            coluna1 = int(input("Digite coluna de 0 a 8:"))
            if matriz1[linha1][coluna1]=="P":
                print("VOCÊ JÁ MARCOU ESSE LOCAL")
                contador = contador - 1
            else:
                if matriz1[linha1][coluna1]== "x":
                    matriz1[linha1][coluna1]="P"
                    exibir_matriz(mapa)

                    if matriz[linha1][coluna1]=="B":
                        matriz1[linha1][coluna1]= "P"
                        ganhador = ganhador+1

                        if matriz[linha1][coluna1]!= "B":
                            matriz1[linha1][coluna1]= "E"
                            bomba= bomba + 1

        if marcar_bandeira==2:
            print(f"QUAL CASA VOCÊ QUER ABRIR")
            linha1 = int(input("Digite linha de 0 a 8:"))
            coluna1 = int(input("Digite coluna de 0 a 8:"))

            if matriz1[linha1][coluna1]=="P":
                print("VOCÊ JÁ MARCOU ESSE LOCAL")
                contador = contador- 1
            else:
                if matriz1[linha1][coluna1]==1 or matriz1[linha1][coluna1]==2 or matriz1[linha1][coluna1]==3:
                    print(f"LINHA{linha1} E COLUNA {coluna1} ESTÃO OCUPADOS")
                else:
                    if matriz1[linha1][coluna1]=="x":
                        if matriz[linha1][coluna1]==0:
                            abrir_matriz(matriz,linha1,coluna1,matriz1)
                            exibir_matriz(mapa)
                            exibir_matriz(campo)
                        if matriz[linha1][coluna1]==1:
                            matriz1[linha1][coluna1]=1
                            exibir_matriz(mapa)

                        else:
                            if matriz[linha1][coluna1] == 2:
                                matriz1[linha1][coluna1] = 2
                                exibir_matriz(mapa)

                            else:
                                if matriz[linha1][coluna1] == 3:
                                    matriz1[linha1][coluna1] = 3
                                    exibir_matriz(mapa)

                                else:
                                    if matriz[linha1][coluna1] == "B":
                                        matriz1[linha1][coluna1]="E"
                                        exibir_matriz(mapa)
                                        exibir_matriz(campo)
                                        print("Você perdeu")
                                        exit()














