import numpy as np
from scipy import stats
import math
from scipy.stats import chi2
import statistics
from statsmodels.stats.weightstats import ztest

def calcularSigMedia(dados, media_hipotese, alpha=0.05 ):
    if len(dados) < 2: 
        raise ValueError("A amostra deve conter pelo menos 2 dados para realizar o teste t.")
    estatistica_t , p_valor = stats.ttest_1samp(dados, media_hipotese)
    p_valor = float(p_valor)
    # realiza o teste t para uma amostra, comparaando os dados fornecidos com a média hipotética

    rejeita_h0 = p_valor < alpha 
    return { "estatistica_t" : estatistica_t, "p_valor" : p_valor, "rejeita_hipotese" : rejeita_h0 }

def testeMediaZ(amostra:list, hipNula:float, rejeita_hipotese:float):
    if (len(amostra) < 2):
        raise ValueError("As amostras devem ter ao menos duas observações")
    teste = ztest(amostra, value=hipNula, ddof=1) 
    # executa o teste Z com a amostra, valor de hipótese nula e grau de liberdade n-1
    return { "p_valor": teste[1], "stat_z": teste[0], "rejeita_hipotese": teste[1] < rejeita_hipotese}
    # teste[0] contém o valor Z, teste[1] contém o valor P

def testeProporcao(amostra:list, observacao:float, hipNula:float, rejeita_hipotese:float):
    if (len(amostra) < 2):
        raise ValueError("As amostras devem ter ao menos duas observações")
    n = len(amostra) # número de observações
    proporcaoInicial = amostra.count(observacao)/n # proporção de ocorrências da observação desejada
    stat_z = (proporcaoInicial-hipNula)/(math.sqrt((hipNula*(1-hipNula))/n)) # fórmula de hipótese de proporção
    valor_p = 1-stats.norm.cdf(stat_z) # obtenção do valor P normalizado em Z

    # retorna valor P, valor normalizado Z e se a decisão do teste (rejeitada ou não)
    return { "p_valor": float(valor_p), "stat_z": stat_z, "rejeita_hipotese": bool(valor_p < rejeita_hipotese)}


def testeQuiQuadrado(amostra: list, sigma2_0: float, alpha: float):
    n = len(amostra)
    # Variância amostral (usa n-1 no denominador)
    s2 = statistics.variance(amostra)

    # Estatística Qui-Quadrado
    chi_calc = (n - 1) * s2 / sigma2_0

    # Graus de liberdade
    gl = n - 1

    # Valores críticos (teste bilateral)
    chi_inf = chi2.ppf(alpha / 2, gl)
    chi_sup = chi2.ppf(1 - alpha / 2, gl)
    p_esquerda = chi2.cdf(chi_calc, gl)
    p_direita = 1 - p_esquerda

    p_valor = 2 * min(p_esquerda, p_direita)

    return { "s2": s2, "chi_calc": chi_calc, "chi_inf": chi_inf, "chi_sup": chi_sup, "p_valor": p_valor }

def testeDuasVariancias(amostra1: list, amostra2: list):
    if len(amostra1) < 2 or len(amostra2) < 2:
        raise ValueError("As amostras devem ter ao menos duas observações")
    var1 = np.var(amostra1, ddof=1)
    var2 = np.var(amostra2, ddof=1)
    
    return max(var1, var2) / min(var1, var2)