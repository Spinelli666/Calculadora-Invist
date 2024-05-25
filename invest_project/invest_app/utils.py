import numpy as np

def investimento_dinamico(ativos, retorno, risco, B_inicial, T, lambda_valor):
    # ativos: número de ativos
    # retorno: matriz (T, ativos) com os retornos esperados
    # risco: matriz (T, ativos) com as variâncias associadas
    # B_inicial: orçamento inicial
    # T: número de períodos
    # lambda_valor: fator de ponderação do risco

    # Inicialização
    B = np.zeros(T + 1)
    B[0] = B_inicial
    x = np.zeros((T, ativos))

    # Programação Dinâmica
    for t in range(T):
        for i in range(ativos):
            # Cálculo da fração ótima a investir no ativo i no período t
            x[t, i] = (retorno[t, i] - lambda_valor * risco[t, i]) / (2 * lambda_valor * risco[t, i])
            # Garantir que a fração esteja entre 0 e 1
            x[t, i] = max(0, min(1, x[t, i]))
        
        # Atualização do orçamento para o próximo período
        B[t + 1] = B[t] + sum(retorno[t, i] * x[t, i] * B[t] for i in range(ativos))

    # Retorno da estratégia de investimento e evolução do orçamento
    return x, B
