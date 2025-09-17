T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    best = 0

    # 열  ( 세로 ) 
    for i in range(N):
        running = 0
        for j in range(M):
            if best[i][j] == 1:
                running += 1

            else:
                if running > best:
                    best = running
                running = 0
        if running > best:
            best = running
        

    # 행  ( 가로 )
    for j in range(M):
        running = 0
        for i in range(N):
            if best[i][j] == 1:
                running += 1

            else:
                if running > best:
                    best = running
                running = 0

        if running > best:
            best = running
    if best == 1:
        best = 0

    print(f"#{tc} {best}")
            
            