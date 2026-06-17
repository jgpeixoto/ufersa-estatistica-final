from calculos import testeDuasVariancias
from time import time

def rodar_testeDuasVariancias():
    entrada1 = input("Digite os valores da primeira amostra separados por vírgula: ")
    amostra1 = [float(x) for x in entrada1.split(",")]
    entrada2 = input("Digite os valores da segunda amostra separados por vírgula: ")
    amostra2 = [float(x) for x in entrada2.split(",")]
    start = time()
    print("Razão entre as duas variâncias: " + str(testeDuasVariancias(amostra1, amostra2)))
    end = time()
    print(f"Tempo de execução: {(end - start)}")

rodar_testeDuasVariancias()