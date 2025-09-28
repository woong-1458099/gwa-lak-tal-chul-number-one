def f(i,  N, m):
    global max_v
   
    if i == N:
        if max_v < m:
            max_v = m
    elif max_v >= m:
        return
    else: 
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                f(i + 1, N, m * P[i][j]/100)
                used[j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    used = [0] * N
    f(0, N, 1)
    print(f"#{tc} {max_v*100:.6f}")



