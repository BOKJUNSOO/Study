N,M = map(int,input().split())
visited = [[False] * M for _ in range(N)]

graph = [list(map(int, input().strip())) for _ in range(N)]

count = 1
def dfs(x,y):
    global count
    if 0<=x<N and 0<=y<M:
        if visited[x][y] == False and graph[x][y] ==1 :
            visited[x][y] = True
            count += 1

            dfs(x+graph[x][y],y)
            dfs(x-graph[x][y],y)
            dfs(x,y+graph[x][y])
            dfs(x,y-graph[x][y])

            if x == N-1 and y == M-1:
                print(count)
                return
            
dfs(0,0)