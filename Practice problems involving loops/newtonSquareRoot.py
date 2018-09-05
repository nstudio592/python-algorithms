def newtonSquare(n):
    '''newton's method of determing square roots'''
    approx = 0.5 * n
    better = 0.5 * (approx + n/approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + n/approx)
    return approx

print(newtonSquare(10))
