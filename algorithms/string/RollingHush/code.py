def RollingHush_Pre(strings):
    mod = 2**61 - 1
    d = {chr(i+65): i+1 for i in range(26)}  # 大文字
    d1 = {chr(i+97): i+27 for i in range(26)}  # 小文字
    d.update(d1)
    
    r = len(strings)
    H = [0] * (r + 1)
    B = 10000
    for i in range(1, r+1):
        H[i] = (B * H[i-1] + d[strings[i-1]]) % mod
    return H

def RollingHush(H, l, r):
    mod = 2**61 - 1
    B = 10000
    result = H[r] - (pow(B, r-l+1, mod) * H[l-1] % mod)
    return (result + mod) % mod
