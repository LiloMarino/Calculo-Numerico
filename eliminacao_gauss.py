import pandas as pd
import numpy as np

# Carrega a matriz a partir de um arquivo Excel
matriz = pd.read_excel("matriz.xlsx", header=None).values

# Converte as colunas para o tipo de dados float
matriz = matriz.astype(float)


# Função para realizar a eliminação de Gauss com pivotamento
def eliminacao_gauss_pivotamento(matriz: np.ndarray):
    n = len(matriz)
    for i in range(n):
        print(f"Passo {i+1}:")
        # Encontra o pivô para a coluna atual
        max_index = i
        for j in range(i + 1, n):
            if abs(matriz[j, i]) > abs(matriz[max_index, i]):
                max_index = j
        # Troca as linhas se necessário
        if max_index != i:
            matriz[[i, max_index]] = matriz[[max_index, i]]

        for idx in range(i + 1):
            print(matriz[:, idx])
        # Eliminação de Gauss
        for j in range(i + 1, n):
            fator = matriz[j, i] / matriz[i, i]
            print(f"{matriz[j]} - {fator} * L{i+1}")
            matriz[j] -= fator * matriz[i]

    return matriz


# Realiza a eliminação de Gauss com pivotamento
matriz_resultante = eliminacao_gauss_pivotamento(matriz)

# Resolução do sistema
x = np.zeros(len(matriz_resultante))
for i in range(len(matriz_resultante) - 1, -1, -1):
    x[i] = (
        matriz_resultante[i, -1] - np.dot(matriz_resultante[i, i + 1 : -1], x[i + 1 :])
    ) / matriz_resultante[i, i]

# Imprime a solução
print("Solução:")
print(x.view())
