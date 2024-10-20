def n_Even_Numbers(n):
    if n > 0:
        n_Even_Numbers(n-1)
        print(2*n, end=' ')


n_Even_Numbers(10)
