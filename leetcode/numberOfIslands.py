class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        mark = [[True for x in range(col)] for x in range(row)]
         
        res  = 0
         
        q = []
         
        for i in range(0,row):
            for j in range(0, col):
                if grid[i][j] == '1' and mark[i][j] == True:
                    q.append([i,j])
                    mark[i][j] = False
                    while q:
                        ii = q[0][0]
                        jj = q[0][1]
                        q.pop(0)
                         
                        if ii+1 < len(grid) and grid[ii+1][jj] == '1' and mark[ii+1][jj] == True:
                            q.append([ii+1, jj])
                            mark[ii+1][jj] = False
                        if jj+1 < len(grid[0]) and grid[ii][jj+1] == '1' and mark[ii][jj+1] ==True:
                            q.append([ii, jj+1])
                            mark[ii][jj+1] = False
                        if ii-1 >= 0 and grid[ii-1][jj] == '1' and mark[ii-1][jj] == True:
                            q.append([ii-1, jj])
                            mark[ii-1][jj] = False
                        if jj-1 >=0 and grid[ii][jj-1] == '1' and mark[ii][jj-1] == True:
                            q.append([ii, jj-1])
                            mark[ii][jj-1] = False
                    res += 1       
                         
        return res