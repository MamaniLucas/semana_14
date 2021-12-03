def parimp(n):
    return True if n % 2 == 0 else False


def imppar(n):
    return True if n % 2 != 0 else False


def parlist(a):
    newlist = []
    for i in a:
        if i % 2 == 0:
            newlist.append(i)
    print(newlist)


def mayor(n):
    return max(n)


def funcion_suma(n):
    return sum(n)


def funcion_prod(n):
    producto = 1
    for i in n:
        producto *= i
    return producto


def fibonacci(n):
    a = 0
    b = 1
    fibo = [0, 1]
    for k in range(n-2):
        c = a + b
        a = b
        b = c
        fibo.append(b)
    return fibo


def sumafibonacci(n):
    a = 0
    b = 1
    fibo = [0, 1]
    for k in range(n-2):
        c = a + b
        a = b
        b = c
        fibo.append(b)
    return sum(fibo)


def factorial(n):
    a = 1
    b = 1
    while b <= n:
        a *= b
        b += 1
    return a
