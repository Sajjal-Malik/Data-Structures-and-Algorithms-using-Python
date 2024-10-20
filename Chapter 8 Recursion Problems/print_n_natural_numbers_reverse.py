def print_N_Numbers(n):
    if n > 0:
        print(n, end=' ')
        print_N_Numbers(n-1)


print_N_Numbers(10)
