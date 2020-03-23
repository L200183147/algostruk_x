#7
def binSe(a, target):
    low = 0
    high = len(a)
    b = []

    while low < high:
        if a[low] == target:
            b.append(low)
            low+=1
        else:
            low+=1
    return "target berada pada index ke- ", b
