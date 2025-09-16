T = int(input())
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    long = 0  # 가장 긴 구조물 길이 기록
 
    # 행(가로) 검사
    for i in range(N):
        running = 0  # 길이 누적
        for j in range(M):
            if arr[i][j] == 1:
                running += 1
            else:
                if running > long:
                    long = running
                running = 0
        # 행이 끝난 뒤 마지막 갱신
        if running > long:
            long = running
 
    # 열(세로) 검사
    for j in range(M):
        running = 0
        for i in range(N):
            if arr[i][j] == 1:
                running += 1
            else:
                if running > long:
                    long = running
                running = 0
        # 열이 끝난 뒤 마지막 갱신
        if running > long:
            long = running
 
    # 최대값이 1일 경우 0으로      처리
    if long == 1:
        long = 0

    print(f"#{tc} {long}")
 