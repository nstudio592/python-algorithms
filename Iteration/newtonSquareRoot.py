def newtonSquare(n):
    approx = 0.5 * n
    better = 0.5 * (approx + n/approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + n/approx)
        print("Better", better)
    return approx

print("Final Answer:", newtonSquare(25))
