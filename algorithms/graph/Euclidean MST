#ユークリッド最小全域木をscipyを用いて解くライブラリ
#Cpythonでの動作が前提
#verify-https://judge.yosupo.jp/submission/285923
#verify-https://atcoder.jp/contests/abc181/submissions/65825323

from scipy.spatial import Delaunay,QhullError

class UnionFind:
    def __init__(self,n):
        self.parents = [-1]*n
        self.sz = [1]*n
    
    def find(self,x):
        while self.parents[x] != -1:
            self.parents[x] = self.find(self.parents[x])
            x = self.parents[x]
        return x
    
    def union(self,u,v):
        self.find(v)
        ru = self.find(u)
        rv = self.find(v)
        
        if ru == rv:
            return False
        
        if self.sz[ru] > self.sz[rv]:
            ru,rv = rv,ru
        
        self.parents[ru] = rv
        self.sz[rv] += self.sz[ru]
        
        return True


def solve():
    N = int(input())
    coords = [tuple(map(int,input().split())) for _ in range(N)]
    
    dic = {}
    uf = UnionFind(N)
    
    for i,p in enumerate(coords):
        if p not in dic:
            dic[p] = [i]
        else:
            dic[p].append(i)
        
    for lst in dic.values():
        for a,b in zip(lst,lst[1:]):
            uf.union(a,b)
            print(a,b)
    
    unique = []
    rep = {}
    for p,lst in dic.items():
        u = lst[0]
        rep[u] = len(unique)
        unique.append((coords[u][0],coords[u][1],u))
    M = len(unique)
    
    delaunay_edges = set()
    
    if M >= 3:
        pts = [(x,y) for x,y,_ in unique]
        try:
            tri = Delaunay(pts)
        except QhullError:
            try:
                tri = Delaunay(pts,qhull_options = "QJ")
            except QhullError:
                tri = None
        
        if tri != None:
            for simplex in tri.simplices:
                for i in range(3):
                    a = unique[simplex[i]][2]
                    b = unique[simplex[(i+1)%3]][2]
                    
                    if a > b:
                        a,b = b,a
                    delaunay_edges.add((a,b))
    
    
    
    
    if (not delaunay_edges and M >= 3) or M < 3:
        pts = [(x,y,idx) for x,y,idx in unique]
        for u,v in zip(pts,pts[1:]):
            a,b = u[2],v[2]
            if a > b:
                a,b = b,a
            delaunay_edges.add((a,b))
    
    
    
    edge_list = []
    for a,b in delaunay_edges:
        dx = coords[a][0] - coords[b][0]
        dy = coords[a][1] - coords[b][1]
        w = dx**2 + dy**2
        edge_list.append((a,b,w))
    edge_list.sort(key = lambda x:x[-1])
    
    used = 0
    for a,b,w in edge_list:
        if uf.union(a,b):
            print(a,b)
            used += 1
            
            if used == N-1:
                break
            
solve()
