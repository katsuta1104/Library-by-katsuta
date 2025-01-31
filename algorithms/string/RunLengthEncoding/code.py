def runlengthencoding(string):
    #ランレングス圧縮する
    
    before = string[0]
    count = 1
    L = []
    for i in range(1,len(string)):
        if string[i] == before:
            count += 1
        else:
            L.append((before,count))
            before = string[i]
            count = 1
        
    L.append((before,count))
    return L
