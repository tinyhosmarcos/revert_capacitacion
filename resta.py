# funcion de resta de matrices

def resta(A,B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[0])):
            C[i].append(A[i][j] - B[i][j])
    return C