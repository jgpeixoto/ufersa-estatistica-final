from calculos import testeProporcao
from time import time

def rodar_testeProporcao():
    print("---Teste de Hipótese para Proporção---")
    #recebe os dados da amostra do usuário
    entrada = input("Digite os valores da amostra separados por vírgula: ")
    amostra = [float(x) for x in entrada.split(",")]
    #recebe o valor que deseja-se testar
    valorTeste = float(input("Digite o valor cujo proporção deve ser medida: "))
    hipoteseNula = float(input("Digite a proporção a ser testada (Hipótese Nula): "))
    start = time()
    try:
        resultado = testeProporcao(amostra, valorTeste, hipoteseNula, 0.05)
        print(f"Estatística t: {resultado[ 'stat_z' ]:.4f}") 
        print(f"Valor p: {resultado[ 'p_valor' ]:.4f}") 
        print(f"Rejeita Hipótese Nula: {resultado[ 'rejeita_hipotese' ]}")
    except ValueError as e:
        print(f"Erro: {e}")
    end = time()
    print(f"Tempo de execução: {(end - start)}")
rodar_testeProporcao()