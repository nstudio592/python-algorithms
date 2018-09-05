def triangularNumbers(n):
    print("n", "\t", "triangle")
    print("---", "\t", "--------")
    for i in range(1, n+1):
        print(i, "\t", i*(i + 1) // 2)

triangularNumbers(5)
