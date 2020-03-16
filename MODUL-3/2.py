#a
def buatNol(m, n):
    """using two inputs"""
    matrix = [[0 for j in range(m)] for i in range(n)]
    print(matrix)

def BuatNol(m):
    """using one input"""
    n = m
    matrix = [[0 for j in range(m)] for i in range(n)]
    print(matrix)


#b
def buatIdentitas(m):
    """Identity Matrix"""
    n = m
    matrix = [[1 if j == i else 0 for j in range(m)] for i in range(n)]
    print(matrix)

#check
buatNol(3,5)
BuatNol(3)
buatIdentitas(4)
