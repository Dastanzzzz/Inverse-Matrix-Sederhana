import numpy as np

def inverse_matrix(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return "Matriks tidak memiliki invers (determinannya nol)."

if __name__ == "__main__":
    n = int(input("Masukkan ukuran matriks (n x n): "))
    print("Masukkan elemen matriks secara baris per baris:")
    matrix = []
    for i in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    matrix = np.array(matrix)
    print("Matriks awal:")
    print(matrix)
    
    print("Matriks Invers:")
    print(inverse_matrix(matrix))
