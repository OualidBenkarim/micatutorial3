
import numpy as np
import matplotlib.pyplot as plt

def plot_fibo(numbers, **kwargs):
    ''' Plot Fibonacci numbers.
    
    Parameters
    ----------
    numbers : list
        Sequence of Fibonacci numbers.

    kwargs:
        Additional keyword arguments are passed to `plt.scatter`
        
    '''
    
    plt.scatter(range(len(numbers)), numbers, **kwargs)
    plt.xlabel('Rank')
    plt.ylabel('Value')
    

    
# https://jaketae.github.io/study/prime-spirals/    
def _get_coordinate(num):
    return num * np.cos(num), num * np.sin(num)

def plot_primes(numbers, figsize=8, **kwargs):
    ''' Plot prime numbers in spiral.
    
    Parameters
    ----------
    numbers : list
        Sequence of prime numbers.
    
    figsize: int
        Figure size.

    kwargs:
        Additional keyword arguments are passed to `plt.scatter`
        
    '''
    
    nums = np.array(list(numbers))
    x, y = _get_coordinate(nums)
    plt.figure(figsize=(figsize, figsize))
    plt.axis('off')
    plt.scatter(x, y, **kwargs)
    plt.show()

