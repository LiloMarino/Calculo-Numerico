import numpy as np
import pandas as pd

# Carrega a matriz a partir de um arquivo Excel
matriz = pd.read_excel("matriz.xlsx", header=None).values

# Converte as colunas para o tipo de dados float
matriz = matriz.astype(float)


def fatoracao_ldlt(A: np.ndarray):
    """
    Realiza a fatoração LDLt de uma matriz simétrica A.

    Args:
        A (numpy.ndarray): Matriz simétrica de entrada.

    Returns:
        L (numpy.ndarray): Matriz triangular inferior.
        D (numpy.ndarray): Vetor da diagonal.
    """
    
    if not np.array_equal(A, A.transpose()):
        raise ValueError("Matriz não é simétrica")

    n = A.shape[0]
    L = np.zeros_like(A)
    D = np.zeros(n)

    for k in range(n):
        D[k] = A[k, k] - np.dot(L[k, :k], L[k, :k] * D[:k])
        L[k+1:, k] = (A[k+1:, k] - np.dot(L[k+1:, :k], L[k, :k])) / D[k]

    return L, D, L.transpose()


L, D, LT = fatoracao_ldlt(matriz)
print(L)
print(D)
print(LT)
