
def sum_Odd_n_Numbers(n):
    if n == 1:
        return n
    return 2 * n -1 + sum_Odd_n_Numbers(n - 1)

print(sum_Odd_n_Numbers(10))