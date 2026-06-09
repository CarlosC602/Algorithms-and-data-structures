import math, time

def dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def triangle_cost(p1, p2, p3):
    return dist(p1, p2) + dist(p2, p3) + dist(p1, p3)


def triangulate_recursive(points, i, j, memo=None):
    if memo is None:
        memo = {}
    if j - i < 2:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    min_cost = float('inf')
    for k in range(i+1, j):  
        cost = (triangle_cost(points[i], points[k], points[j])
              + triangulate_recursive(points, i, k, memo)
              + triangulate_recursive(points, k, j, memo))
        if cost < min_cost:
            min_cost = cost

    memo[(i, j)] = min_cost
    return min_cost


def triangulate_dp(points):
    n = len(points)
    dp = [[0.0] * n for _ in range(n)]

    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float('inf')

            for k in range(i+1, j):  
                cost = (triangle_cost(points[i], points[k], points[j])
                      + dp[i][k]   
                      + dp[k][j]) 
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n-1]  

if __name__ == "__main__":
    datasets = [
        [[0,0],[1,0],[2,1],[1,2],[0,2]],
        [[0,0],[4,0],[5,4],[4,5],[2,5],[1,4],[0,3],[0,2]]
    ]
    for idx, pts in enumerate(datasets):
        t0 = time.perf_counter()
        r = triangulate_recursive(pts, 0, len(pts)-1)
        tr = time.perf_counter() - t0
        t0 = time.perf_counter()
        d = triangulate_dp(pts)
        td = time.perf_counter() - t0
        print(f"Zbiór {idx+1}: rec={r:.4f} ({tr*1e6:.1f}µs) | dp={d:.4f} ({td*1e6:.1f}µs)")