import random

num = int(input("type the test number here: "))

def is_prime(num):
    #calculate m
    coprime = num - 1
    m = coprime / 2

    print(f"initial coprime is: {m}")
    while m % 2 == 0:
        m = m / 2
        print(f"Coprime new iteration is {m}")
    else:
        print(f"coprime is: {m}")

    a = random.randint(1, int(coprime))
    print(f"a is chosen to be {a}")
    bmultiple = (a ** m)
    print(f"b multiple is {bmultiple}")

    bfactor = bmultiple % num

    b = int(bfactor)
    print(f"bfactor is: {b}")

    if b == 1:
        print(f"{num} is not a prime number")
    elif bfactor == -1:
        print(f"{num} is probably a prime number")
    else:
        print(f"{b} is not fully resolved")

        #while b != 1 and b != -1:

            # b = int((b ** 2) % num)
            # print(f"current iteration is {b}")













is_prime(num)