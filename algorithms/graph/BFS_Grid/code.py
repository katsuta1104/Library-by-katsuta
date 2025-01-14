INF = 10**46
def bfs_grid(grid,start,goal):
    """
    登場する変数
    H …… 縦幅
    W …… 横幅
    start …… 初めの地点[x,y]
    goal …… 終わりの地点[y,x]
    grid …… [.]が移動可能,[#]が移動不可
    visited …… すでに移動した座標を保持するset
    
    startからgoalまでの最短距離を返す。移動不可な場合はINFを返す。
    """
    from collections import deque
    
    queue = deque()
    dire = [(0,1),(1,0),(0,-1),(-1,0)]
    
    x,y = start
    gx,gy = goal
    visited = set()
    visited.add((x,y))
    
    for dx,dy in dire:
        nx = x+dx
        ny = y+dy
        
        if 0<= nx < H and 0<= ny < W:
            if grid[nx][ny] == ".":
                queue.append((nx,ny,1))
                visited.add((nx,ny))
    
    while queue:
        x,y,dis = queue.popleft()
        
        if x == gx and y==gy:
            return dis
        
        for dx,dy in dire:
            nx = x+dx
            ny = y+dy
            
            if 0<= nx < H and 0<= ny < W:
                if grid[nx][ny] == "." and (nx,ny) not in visited:
                    queue.append((nx,ny,dis+1))
                    visited.add((nx,ny))
    
    return INF
