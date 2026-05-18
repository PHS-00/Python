def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
def fatorialIt(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial