def sequence(n):
    '''print 3n+1 sequence, starting at n and terminating @ 1'''
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n) #prints one at the end

sequence(5)
