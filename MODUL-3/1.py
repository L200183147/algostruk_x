
A = [[2,5],[6,9]]
B = [[4,6],[3,7]]

#a
def check(A):
    for i in range(len(A)):
        if len(A[0]) == len(A[i]):
            print(A)
        else:
            print('error')
            break
        
#b
def size(matrix):
    return("Matrix size = " + str(len(matrix)) +" x "+ str(len(matrix[0])))

#c
def plus(A,B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j] + B[i][j], end = ' '),
        print()

#d
def multiply(A,B):
    C = []
    for i in range(0, len(C)):
        row = []
        for j in range(0, len(A[0])):
            total = 0
            for k in range(0, len(A)):
                total = total + (A[i][C] * B[C][j])
            row.append(total)
        a.append(row)

    for i in range(0, len(C)):
        for j in range(0, len(C[0])):
            print (C[i][j], end=' ')
        print()

#e
def determinan(matrix):
    if len(matrix) == len(matrix[0]):
        bil = [x for x in range(len(matrix))]
        jum = 0
        for i in range(len(matrix)):
            total = 1
            for x in range(len(matrix)):
                total *= matrix[x][bil[x]]
            bil += [bil.pop(0)]
            jum += total
        bil2 = [x for x in range(len(matrix))]
        bil.reverse()
        jum2 = 0
        for i in range(len(matrix)):
            total2 = 1
            for x in range(len(matrix)):
                total2 *= matrix[x][bil2[x]]
            bil2 += [bil2.pop()]
            jum2 += total2
        print(total-total2)
        return ""
    else:
        print("Matriks must type 'Square Matrix' ")
        
check(A)
size(A)
plus(A,B)
multiply(A,B)
determinan(A)


