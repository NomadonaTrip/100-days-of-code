import random

num = int(input("type the test number here: "))



def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    # find a value of k for which num-1 = m*(2^k) and m is an odd number.
    j = num - 1
    k = 0
    while j % 2 == 0:
        j // 2
        k += 1

    m = j / (2 ** k)
    print(f"m is {m}, k is {k}")

is_prime(num)















is_prime(num)