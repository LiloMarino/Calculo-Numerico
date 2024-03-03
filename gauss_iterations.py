import numpy as np
import pandas as pd


def gauss_jacobi(A: np.ndarray, B: np.ndarray, iterations: int):
    n = len(A)
    X = np.zeros(n, dtype=float)
    for k in range(0, iterations + 1):
        print(f"X{k} = {X}")
        for i in range(n):
            somatorio = 0
            for j in range(n):
                if j != i:
                    somatorio += A[i,j]*X[j]
            X[i] = (B[i,0] - somatorio)/A[i,i]
    return X


def gauss_seidel(A: np.ndarray, B: np.ndarray, iterations: int):
    n = len(A)
    X = np.zeros(n, dtype=float)
    X_OLD = np.zeros(n, dtype=float)
    for k in range(0, iterations + 1):
        print(f"X{k} = {X}")
        for i in range(n):
            somatorio1 = 0
            somatorio2 = 0
            for j in range(n):
                if j < i:
                    somatorio1 += A[i,j]*X[j]
                if j > i:
                    somatorio2 += A[i,j]*X_OLD[j]
            X_OLD[i] = X[i]
            X[i] = (B[i,0] - somatorio1 - somatorio2)/A[i,i]
    return X


if __name__ == "__main__":
    np.set_printoptions(precision=6)   # Definindo a precisão
    A = pd.read_excel("matriz.xlsx", header=None).values
    A = A.astype(float)
    B = pd.read_excel("vetor.xlsx", header=None).values
    B = B.astype(float)
    print("Gauss Jacobi")
    X = gauss_jacobi(A,B,10)
    print(np.dot(A,X))
    print("Gauss Seidel")
    X = gauss_seidel(A,B,10)
    print(np.dot(A,X))