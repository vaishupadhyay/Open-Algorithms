# Uses python3
def calc_fib(n):
    a = 0
    b = 1
    if n < 2:
        return n

    else:
        for i in range(n-1):
            c = a+b
            a = b
            b = c

        return b


n = int(input())
print(calc_fib(n))
