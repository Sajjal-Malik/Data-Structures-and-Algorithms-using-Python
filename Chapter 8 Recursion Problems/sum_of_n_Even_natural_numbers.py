def sum_Even_n_Numbers(n):
    if n == 2:
        return n
    return 2 * n + sum_Even_n_Numbers(n - 1)

print(sum_Even_n_Numbers(10))