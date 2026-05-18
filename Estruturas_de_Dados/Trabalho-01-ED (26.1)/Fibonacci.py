def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:        
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacciIt(n):
    termoN0 = 0
    termoN1 = 1
    for i in range(2,n+1):
        termoNi = termoN0 + termoN1
        termoN0 = termoN1
        termoN1 = termoNi 
    return termoN1