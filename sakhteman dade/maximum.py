def max(lst):
    x = lst[0]
    for i in range (1 , len(lst)):
        if lst[i] > x :
            x = lst[i]
    return x
