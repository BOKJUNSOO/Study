row,col = map(int, input().split())
arr = [[] for _ in range(row)]
for i in range(row):
    arr[i] = list(map(int, input()))
visited = [[False] * col for _ in range(row)]
count = 1
def dfs(x,y):
    global count
    if x <= -1 or y <=-1 or x>= row or y>=col:
        return
    if arr[x][y] == 1 and visited[x][y] == False:
        count += 1
        arr[x][y] = 0
        visited[x][y] = True
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        if x == row-1 and y == col-1:
            print(count)
            return
dfs(0,0)