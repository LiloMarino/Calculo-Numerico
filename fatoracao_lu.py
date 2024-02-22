import numpy as np
import pandas as pd

# Carrega a matriz a partir de um arquivo Excel
matriz = pd.read_excel("matriz.xlsx", header=None).values

# Converte as colunas para o tipo de dados float
matriz = matriz.astype(float)


def fatoracao_lu(matriz : np.ndarray):
    # Obter o tamanho da matriz
    linhas, colunas = matriz.shape

    print("Número de linhas:", linhas)
    print("Número de colunas:", colunas)

    # Defina o tamanho da matriz
    if linhas != colunas:
        raise ValueError(f"A matriz deve ser quadrada ({linhas} x {colunas})")

    n = linhas  

    # Inicialize a matriz U com zeros
    U = np.zeros((n, n))

    # Defina a matriz L como uma matriz diagonal com 1s na diagonal principal
    L = np.eye(n)

    # Exibir as matrizes L e U
    print("Matriz L:")
    print(L)

    print("\nMatriz U:")
    print(U)
    
fatoracao_lu(matriz)
