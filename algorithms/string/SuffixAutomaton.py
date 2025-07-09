#verify-https://judge.yosupo.jp/submission/298588
class SuffixAutomaton:
    def __init__(self):
        self.size = 1
        self.last = 0
        
        #各ノード毎
        self.st_next = [{}] #次の文字への遷移
        self.st_len = [0]   #最大長
        self.st_link = [-1] #suffix-link
    
    def push(self,ch):
        #追加
        cur = self.size
        self.size += 1
        self.st_len.append(self.st_len[self.last]+1)
        self.st_link.append(0)
        self.st_next.append({})
        
        p = self.last
        while p >= 0 and ch not in self.st_next[p]:
            self.st_next[p][ch] = cur
            p = self.st_link[p]
        
        if p == -1:
            #同じ遷移なし
            self.st_link[cur] = 0
        else:
            q = self.st_next[p][ch]
            if self.st_len[p] + 1 == self.st_len[q]:
                #長さが一緒だった場合
                self.st_link[cur] = q
            else:
                #クローンを作る
                clone = self.size
                self.size += 1
                self.st_len.append(self.st_len[p]+1)
                self.st_link.append(self.st_link[q])
                self.st_next.append(self.st_next[q].copy())
                
                while p >= 0 and self.st_next[p].get(ch) == q:
                    self.st_next[p][ch] = clone
                    p = self.st_link[p]
                self.st_link[q] = self.st_link[cur] = clone
        self.last = cur
