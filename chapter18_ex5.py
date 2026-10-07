known = {}
def binomial_coeff(n, k):
    '''Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number of successes

    returns: int
    '''
    return 0 if n == 0 and k != 0 else 1 if k == 0 else known[(n, k)] if (n, k) in known else known.setdefault((n, k), binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1))

binomial_coeff(10, 4)    