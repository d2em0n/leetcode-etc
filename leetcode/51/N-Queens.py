class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def atacked(x, y, f):
            f[x][y] = 1
            for i in range(0, n):
                if i != y : f[x][i] = -1
                if i != x : f[i][y] = -1
            i = 1
            while x + i < n and y + i < n:
                f[x+i][y+i] = -1
                i += 1
            i = 1
            while x + i < n and y - i >= 0:
                f[x + i][y - i] = -1
                i += 1
            return f


        def resultConverter(f):
            result = []
            str = ""
            for x in range(n):
                str = ""
                for y in range(n):
                    if f[x][y] > 0:
                        str += "Q"
                    else:
                        str += (".")
                result.append(str)
            return result


        def positions(f, i):
            free = []
            for j in range(n):
                if f[i][j] == 0:
                    free.append(j)
            return free

        def solve(f, i, n, results):
            pos = positions(f, i)
            if n -1 == i and len(pos) == 1:
                f[i][pos[0]] =1
                result = resultConverter(f)
                results.append(result)
                return
            if len(pos) == 0:
                return
            
            for p in pos:
                fi = [[f[i][j] for j in range(n)] for i in range(n)]
                fi = atacked( i, p , fi)
                solve(fi, i+1, n, results)

        results = []
        if n == 1: return [["Q"]]
        f = []
        for i in range(n):
            f.append([0] * n)
        solve(f, 0, n, results)

        return results        
            