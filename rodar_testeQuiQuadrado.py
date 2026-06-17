from calculos import testeQuiQuadrado
from time import time

dados = input(
    "Digite os valores da amostra separados por virgula: "
)

amostra = [float(x) for x in dados.split(',')] # Converte os valores para float



# Variância populacional hipotética (H0)
sigma2_0 = float( input("Digite a variância hipotética (σ²₀): ") )

start = time()
resultado = testeQuiQuadrado(amostra, sigma2_0, 0.05)

# Exibição dos resultados
# ------------------------------------------
print("\n===== Resultados =====")
print(f"Tamanho da amostra (n): {len(amostra)}")
print(f"Variância amostral (s²): {resultado['s2']:.4f}")
print(f"Qui-quadrado calculado: {resultado['chi_calc']:.4f}")
print(f"Qui-quadrado crítico inferior: {resultado['chi_inf']:.4f}")
print(f"Qui-quadrado crítico superior: {resultado['chi_sup']:.4f}")

# Decisão
# ------------------------------------------
if resultado['chi_calc'] < resultado['chi_inf'] or resultado['chi_calc'] > resultado['chi_sup']:
    print("\nDecisão: Rejeitar H0")
    print("Há evidências de que a variância é diferente da hipótese.")
else:
    print("\nDecisão: Não Rejeitar H0")
    print("Não há evidências suficientes para afirmar que a variância é diferente.")
print(f"\np-valor = {resultado['p_valor']:.6f}")
end = time()
print(f"Tempo de execução: {(end - start)}")