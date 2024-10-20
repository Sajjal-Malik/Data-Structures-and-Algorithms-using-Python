def n_Odd_Numbers(n):
    if n > 0:
        n_Odd_Numbers(n-1)
        print(2*n-1, end=' ')


n_Odd_Numbers(10)
