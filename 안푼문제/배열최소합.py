def find_min_sum(row, current_sum):
    global min_sum


    if current_sum >= min_sum:
        return
    # 가지치기 : 현재 합이 이미 찾은 최소 합보다 크면 탐색 중단


    if row == N:
        min_sum = current_sum
        return
    # 종료 조건 : 모든 행에 대해 숫자를 선택했을 때


   # 재귀 호출: 현재 행에서 선택할 열을 탐색
    for col in range(N):
        # 해당 열이 아직 사용되지 않았다면
        if not visited[col]:
            visited[col] = True  # 열 사용 처리 -> 이번 행에서 col(열)을 선택했다는 흔적을 남김
            find_min_sum(row + 1, current_sum + arr[row][col])  # 재귀 : 다음 행 (row+1)로 내려가서, 지금까지의 합에 이번에 고른 값을 더해 계속 탐색 -> 이번선택을 확정하고 그 다음 단계로 진행 하는 부분
            visited[col] = False # 백트래킹: 방금 선택했던 열을 원상복구 -> 바로 다음 반복에서 다른 열을 선택해보려면, 이전 선택의  흔적을 지워야 함

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')
    visited = [False] * N
    find_min_sum = 0
    
    print(f"#{tc} {min_sum}")
