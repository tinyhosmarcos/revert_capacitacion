# funcion de multiplicacion de matrices

def mult(A,B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            C[i].append(0)
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]
    return C
    