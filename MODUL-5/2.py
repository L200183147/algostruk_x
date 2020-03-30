a=[1,3,5,7,9]
b=[2,4,6,8,10]

def swap (A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
    
def comb(a,b):
    c=a+b
    n=len(c)
    for i in range(1,n):
        nilai = c[i]
        pos = i
        while pos>0 and nilai<c[pos-1]:
            c[pos]=c[pos-1]
            pos=pos-1
        c[pos] = nilai
    print(c)   
