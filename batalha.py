# equipe MARCIANA COSTA PEREIRA E JONAS DAVID ROSA

from random import *
# mapas
def criar_tabuleiro(dimensao):
    global matriz
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append(0)
        matriz.append(linha)
    return matriz

def criar_mapa(dimensao1):
    matriz1=[]
    for i in range(dimensao1):
        linha = []
        for j in range(dimensao1):
            linha.append(0)
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

def posicionar(mapa,jogador):
    global frota
    numero_frota= 4
    contador_frota =-1
    contador=0

    for i in range(numero_frota):

        contador_frota += 1
        contador += 1
        print(f"JOGADOR{jogador}E SUA VEZ DE: POSICIONAR O {frota[contador_frota]} DE TAMANHO NA {frota_posicao[contador_frota]}")
        linha = int(input(f"LINHA: DIGITE DE O {dimensao - 1} : "))
        coluna = int(input(f"COLUNA: DIGITE DE O {dimensao - 1} : "))

        if linha < 0 or linha > dimensao or coluna < 0 or coluna > dimensao:
            numero_frota = numero_frota + 1
            contador = contador - 1
            contador_frota = contador_frota - 1
            print("LUGAR OCUPADO OU JOGADA INVALIDA")

        else:
            if mapa[linha][coluna] == 0 and contador == 1:
                mapa[linha][coluna] = contador
                mapa[linha][coluna + 1] = contador
                print(exibir_matriz(mapa))

            else:
                if mapa[linha][coluna] == 0 and contador == 2:
                    mapa[linha][coluna] = contador
                    mapa[linha + 1][coluna] = contador
                    mapa[linha + 2][coluna] = contador
                    print(exibir_matriz(mapa))

                else:
                    if mapa[linha][coluna] == 0 and contador == 3:
                        mapa[linha][coluna] = contador
                        mapa[linha][coluna + 1] = contador
                        mapa[linha][coluna + 2] = contador
                        print(exibir_matriz(mapa))

                    else:
                        if mapa[linha][coluna] == 0 and contador == 4:
                            mapa[linha][coluna] = contador
                            mapa[linha][coluna + 1] = contador
                            mapa[linha][coluna + 2] = contador
                            print(exibir_matriz(mapa))

def jogar_maquina():
     contador= 0

     for i in range(4):
        contador= contador+ 1
        linha = randint(0,8)
        coluna= randint(0,8)

        if linha < 0 or linha > dimensao or coluna < 0 or coluna > dimensao:
            contador = contador - 1
            print("LUGAR OCUPADO")

        else:
            if mapa_jogador2[linha][coluna] == 0 and contador == 1:
                mapa_jogador2[linha][coluna] = contador
                mapa_jogador2[linha][coluna + 1] = contador
                #print(exibir_matriz(mapa_jogador2))

            else:
                if mapa_jogador2[linha][coluna] == 0 and contador == 2:
                    mapa_jogador2[linha][coluna] = contador
                    mapa_jogador2[linha + 1][coluna] = contador
                    mapa_jogador2[linha + 2][coluna] = contador
                    #print(exibir_matriz(mapa_jogador2))

                else:
                    if mapa_jogador2[linha][coluna] == 0 and contador == 3:
                        mapa_jogador2[linha][coluna] = contador
                        mapa_jogador2[linha][coluna + 1] = contador
                        mapa_jogador2[linha][coluna + 2] = contador
                        #print(exibir_matriz(mapa_jogador2))

                    else:
                        if mapa_jogador2[linha][coluna] == 0 and contador == 4:
                            mapa_jogador2[linha][coluna] = contador
                            mapa_jogador2[linha][coluna + 1] = contador
                            mapa_jogador2[linha][coluna + 2] = contador
                            #print(exibir_matriz(mapa_jogador2))

def iniciar_jogo():
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    while True :
        jogando = int(input("Digite (1) 1 JOGADOR ou (2) PARA 2 JOGADORES:"))
        if jogando < 1 or jogando > 2:
            print("jogada invalida")
            break
        else:
            if jogando == 1:
                print(posicionar(mapa_jogador1, jogador1))
                print(jogar_maquina())
                while True:

                    if pontos_jogador1 == 4 and pontos_jogador2 == 4:
                        print("jogo empatado")
                        break
                    else:
                        if pontos_jogador1 == 4 and pontos_jogador2 < 4:
                            print("jogador 1 Ganhou")
                        else:
                            if pontos_jogador2 == 4 and pontos_jogador1 < 4:
                                print("jogador 2 Ganhou")
                            else:
                                for i in range(1):
                                    print(f"jogador 1 e sua vez: de atirar ")
                                    linha = int(input(f"Digite o numero 0 a {dimensao - 1} na linha: "))
                                    coluna = int(input(f"Digite o numero 0 a {dimensao - 1} na coluna: "))
                                    if mapa_jogador2[linha][coluna] == 0:
                                        mapa_jogador1[linha][coluna] = "/"
                                        exibir_matriz(mapa_jogador1)
                                        print("Tiro na água")
                                        pontos_jogador1 = pontos_jogador1+1
                                        sortear()
                                    else:
                                        if mapa_jogador2[linha][coluna] == 1:
                                            pontos_jogador1 = pontos_jogador1 + 1
                                            mapa_jogador2[linha][coluna] = "x"
                                            print(f"vc acertou {frota[0]} ")
                                            print(exibir_matriz(mapa_jogador1))
                                            pontos_jogador1 = pontos_jogador1 + 1
                                            sortear()
                                        else:
                                            if mapa_jogador2[linha][coluna] == 2:
                                                pontos_jogador1 = pontos_jogador1 + 1
                                                mapa_jogador2[linha][coluna] = "x"
                                                print(f"vc acertou {frota[1]} ")
                                                print(exibir_matriz(mapa_jogador1))
                                                pontos_jogador1 = pontos_jogador1 + 1
                                                sortear()
                                            else:
                                                if mapa_jogador2[linha][coluna] == 3:
                                                    pontos_jogador1 = pontos_jogador1 + 1
                                                    mapa_jogador2[linha][coluna] = "x"
                                                    print(f"vc acertou {frota[2]}")
                                                    print(exibir_matriz(mapa_jogador1))
                                                    pontos_jogador1 = pontos_jogador1 + 1
                                                    sortear()
                                                else:
                                                    if mapa_jogador2[linha][coluna] == 4:
                                                        pontos_jogador1 = pontos_jogador1 + 1
                                                        mapa_jogador2[linha][coluna] = "x"
                                                        print(f"vc acertou {frota[3]}")
                                                        print(exibir_matriz(mapa_jogador1))
                                                        pontos_jogador1 = pontos_jogador1 + 1
                                                        sortear()

            if jogando == 2:
                print(posicionar(mapa_jogador1,jogador1))
                print(posicionar(mapa_jogador2,jogador2))
                while True:

                    if pontos_jogador1 ==4 and pontos_jogador2 ==4:
                        print("jogo empatado")
                        break
                    else:
                        if pontos_jogador1 == 4 and pontos_jogador2 < 4:
                            print("jogador 1 Ganhou")
                        else:
                            if pontos_jogador2 == 4 and pontos_jogador1 < 4 :
                                print("jogador 2 Ganhou")
                            else:
                                for i in range(1):
                                    print(f"jogador 1 e sua vez: de atirar ")
                                    linha = int(input(f"Digite o numero 0 a {dimensao - 1} na linha: "))
                                    coluna = int(input(f"Digite o numero 0 a {dimensao - 1} na coluna: "))
                                    if mapa_jogador2[linha][coluna] ==0:
                                        mapa_jogador1[linha][coluna] = "/"
                                        print(exibir_matriz(mapa_jogador1))
                                        print("Tiro na água")


                                        pontos_jogador1 = pontos_jogador1 + 1

                                    else:
                                        if mapa_jogador2[linha][coluna] == 1:
                                            pontos_jogador1 = pontos_jogador1 + 1
                                            mapa_jogador2[linha][coluna] = "x"
                                            print(f"VOCÊ ACERTOU {frota[0]} ")
                                            print(exibir_matriz(mapa_jogador1))
                                            pontos_jogador1 = pontos_jogador1 + 1

                                        else:
                                            if mapa_jogador2[linha][coluna] == 2:
                                                pontos_jogador1 = pontos_jogador1 + 1
                                                mapa_jogador2[linha][coluna] = "x"
                                                print(f"VOCÊ ACERTOU {frota[1]} ")
                                                print(exibir_matriz(mapa_jogador1))
                                                pontos_jogador1 = pontos_jogador1 + 1


                                            else:
                                                if mapa_jogador2[linha][coluna] == 3:
                                                    pontos_jogador1 = pontos_jogador1 + 1
                                                    mapa_jogador2[linha][coluna] = "x"
                                                    print(f"VOCÊ ACERTOU  {frota[2]}")
                                                    print(exibir_matriz(mapa_jogador1))
                                                    pontos_jogador1 = pontos_jogador1 + 1

                                                else:
                                                    if mapa_jogador2[linha][coluna] == 4:
                                                        pontos_jogador1 = pontos_jogador1 + 1
                                                        mapa_jogador2[linha][coluna] = "x"
                                                        print(f"VOCÊ ACERTOU  {frota[3]}")
                                                        print(exibir_matriz(mapa_jogador1))
                                                        pontos_jogador1 = pontos_jogador1 + 1

                                for j in range(1):
                                    print(f"jogador 2 e sua vez: de atirar ")
                                    linha1 = int(input(f"Digite o numero 0 a {dimensao - 1} na linha: "))
                                    coluna1 = int(input(f"Digite o numero 0 a {dimensao - 1} na coluna: "))
                                    if mapa_jogador1[linha1][coluna1] == 0:
                                        mapa_jogador2[linha1][coluna1] = "/"
                                        print(mapa_jogador2)
                                        print("Tiro na água")
                                        print(exibir_matriz(mapa_jogador2))
                                        pontos_jogador2 = pontos_jogador2 + 1
                                    else:
                                        if mapa_jogador1[linha1][coluna1] == 1:
                                            pontos_jogador2 = pontos_jogador2+1
                                            mapa_jogador2[linha1][coluna1]="x"
                                            print(mapa_jogador2)
                                            print(f"vc acertou {frota[0]} ")
                                            print(exibir_matriz(mapa_jogador2))
                                            pontos_jogador2 = pontos_jogador2 + 1
                                        else:
                                            if mapa_jogador1[linha1][coluna1] == 2:
                                                pontos_jogador2 = pontos_jogador2 + 1
                                                mapa_jogador2[linha1][coluna1] = "x"
                                                print(f"vc acertou {frota[1]} ")
                                                print(exibir_matriz(mapa_jogador2))
                                                pontos_jogador2 = pontos_jogador2 + 1
                                            else:
                                                if mapa_jogador1[linha1][coluna1] == 3:
                                                    pontos_jogador2 = pontos_jogador2 + 1
                                                    mapa_jogador2[linha1][coluna1] = "x"
                                                    print(f"vc acertou {frota[2]}")
                                                    print(exibir_matriz(mapa_jogador2))
                                                    pontos_jogador2 = pontos_jogador2 + 1
                                                else:
                                                    if mapa_jogador1[linha1][coluna1] == 4:
                                                        pontos_jogador2 = pontos_jogador2 + 1
                                                        mapa_jogador2[linha1][coluna1] = "x"
                                                        print(f"vc acertou {frota[3]}")
                                                        print(exibir_matriz(mapa_jogador2))
                                                        pontos_jogador2 = pontos_jogador2 + 1

def sortear():
    pontos_jogador2= 0
    linha= randint(0,8)
    coluna= randint(0,8)
    if mapa_jogador1[linha][coluna]==0:
        mapa_jogador2[linha][coluna]= "~"
        print("TIRO NA AGUA")
        print(exibir_matriz(mapa_jogador2))
    else:
        if mapa_jogador1[linha][coluna]==1:
            mapa_jogador2[linha][coluna] = "x"
            print(f"VC ACERTOU {frota[0]}")
            print(exibir_matriz(mapa_jogador2))
            pontos_jogador2 = pontos_jogador2 + 1
        else:
            if mapa_jogador1[linha][coluna] == 2:
                mapa_jogador2[linha][coluna] = "x"
                print(f"VC ACERTOU {frota[1]}")
                print(exibir_matriz(mapa_jogador2))
                pontos_jogador2 = pontos_jogador2 + 1
            else:
                if mapa_jogador1[linha][coluna] == 3:
                    mapa_jogador2[linha][coluna] = "x"
                    print(f"VC ACERTOU {frota[1]}")
                    print(exibir_matriz(mapa_jogador2))
                    pontos_jogador2 = pontos_jogador2 + 1

                else:
                    if mapa_jogador1[linha][coluna] == 4:
                        mapa_jogador2[linha][coluna] = "x"
                        print(f"VC ACERTOU {frota[4]}")
                        print(exibir_matriz(mapa_jogador2))
                        pontos_jogador2 = pontos_jogador2 + 1

#variaveis
dimensao= 13
matriz = []

# posicionar  frota
frota=["NAVIO 2UN", "SUBMARINO 3UN", "PORTA_AVIÔES", "FRAGATA"]
frota_posicao=["HORIZONTAL","VERTICAL","HORIZONTAL","VERTICAL"]
#jogo
mapa_jogador1=criar_mapa(dimensao)
mapa_jogador2=criar_mapa(dimensao)
jogador1 = 1
jogador2 = 2

pontos_jogador1 =0
pontos_jogador2 = 0

iniciar_jogo()



