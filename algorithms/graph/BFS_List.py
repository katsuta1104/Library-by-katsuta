INF = 10**46

def bfs_list(graph):
    #graphは隣接リスト表現
    #頂点0からの最短距離を返す
  
    dist = [INF]*N
    dist[0] = 0
    
    from collections import deque
    
    visited = set()
    visited.add(0)
    queue = deque()
    
    for a in graph[0]:
        queue.append((a,1))
        visited.add(a)
    
    while queue:
        now_ver ,now_dis = queue.popleft()
        
        dist[now_ver] = now_dis
        
        for next in graph[now_ver]:
            if next not in visited:
                queue.append((next,now_dis+1))
                visited.add(next)
    
    return dist
