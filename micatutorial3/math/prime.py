

def is_prime(n):
    '''Check if number is prime.
    
    Parameters
    ----------
    n: int
        Number to test if prime.
        
    Returns
    -------
    bool
        True is number is prime and False otherwise.
        
    '''
    for factor in range(2, n // 2 + 1):
        if n % factor == 0:
            return False
    return True

def compute_primes(n):
    ''' Compute primes numbers from 1 to `n`.
    
    Parameters
    ----------
    n : int
        Try numbers from 1 to `n`.

    Returns
    -------
    list
        List of prime numbers in range [1, `n`]
    '''
    
    primes = []
    for i in range(1, n):
        if is_prime(i):
            primes.append(i)  
    return primes

