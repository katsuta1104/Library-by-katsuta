#隣接リスト形式のDFS。グリッドは非対応。

import sys
sys.setrecursionlimit(2*10**5)
visited = set()
def dfs_list(graph,now):
    global visited
    visited.add(now)
    
    for next in graph[now]:
        if next not in visited:
            dfs_list(graph,next)
