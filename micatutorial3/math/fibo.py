
''' Fibonacci numbers module '''

def fib(n):    # write Fibonacci series up to n
    ''' Print Fibonacci sequence up to `n`.
    
    Parameters
    ----------
    n : int
        Upper bound for Fibonacci seq.

    '''
    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

    
def fib2(n):   # return Fibonacci series up to n
    ''' Compute Fibonacci sequence up to `n`.
    
    Parameters
    ----------
    n : int
        Upper bound for Fibonacci seq.

    Returns
    -------
    list
        Fibonacci numbers.
    '''
    
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

