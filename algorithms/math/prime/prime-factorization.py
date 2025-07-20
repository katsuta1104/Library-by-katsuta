def prime_factorization(n):
    #6k±1の範囲のみ探索することで定数倍を改善……しているはず。
    #実際、10**10 - 10**10 + 10**5までの時間を測ると、純粋な√n全探索では2090msかかっていたところを、732msまで短縮している。
    #時間計算量はO(√N)
    
    L = []
    while n % 2 == 0:
        L.append(2)
        n //= 2
        
    while n % 3 == 0:
        L.append(3)
        n//= 3
    
    i = 5
    while i**2 <= n and n != 1:
        while n % i == 0:
            L.append(i)
            n //= i
        
        i += 2
            
        while n % i == 0:
            L.append(i)
            n //= i
            
        i += 4
    
    if n != 1:
        L.append(n)
    return L
