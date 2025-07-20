def eratosthenes(max_value):
    #エラトステネスの篩を利用して素数を列挙する
    primes = [True] * (max_value + 1)
    primes[0] = primes[1] = False
    for i in range(2,int(max_value**0.5)+1):
        if primes[i]:
            for j in range(i**2,max_value+1,i):
                primes[j] = False
    
    return [i for i in range(2,max_value+1) if primes[i]]
