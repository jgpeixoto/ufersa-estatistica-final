from calculos import testeMediaZ
from time import time
def rodar_testeZ():
    print("---Teste de Hipótese para uma Média (Teste Z)---")
    #recebe os dados da amostra do usuário
    entrada = input("Digite os valores da amostra separados por vírgula: ")
    amostra = [float(x) for x in entrada.split(",") ]
    #recebe a média que deseja-se testar
    media_teste = float(input("Digite a média a ser testada (Hipótese Nula): ") )
    start = time()
    try:
        resultado = testeMediaZ(amostra, media_teste, 0.05)
        print(f"Estatística t: {resultado[ 'stat_z' ]:.4f}") 
        print(f"Valor p: {resultado[ 'p_valor' ]:.4f}") 
        print(f"Rejeita Hipótese Nula: {resultado[ 'rejeita_hipotese' ]}") 
    except ValueError as e:
        print(f"Erro: {e}")
    if resultado['rejeita_hipotese']:
        print("A hipótese nula foi rejeitada")
        print(f"A média da amostra é significativamente diferente de {media_teste}")
    else:
        print("A hipótese nula não foi rejeitada")
        print(f"Não há evidências suficientes para afirmar que a média é diferente de {media_teste}.")
    end = time()
    print(f"Tempo de execução: {(end - start)}")
rodar_testeZ()