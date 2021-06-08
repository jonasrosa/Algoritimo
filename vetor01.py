nomes_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" ]
maximo_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mes = int (input ("Digite o número do mês:"))
if mes <1 or mes > 12:
    print ("Mês inválido")
else:
    print (f"Nome do mês = {nomes_meses [mes - 1]}")
    print (f"Quantidade de dias = {maximo_dias [mes - 1]}")