def find_min_sum(row, current_sum):
    global min_sum
    
    # 가지치기: 현재 합이 이미 찾은 최소 합보다 크면 탐색 중단
    if current_sum >= min_sum:
        return
    
    # 종료 조건: 모든 행에 대해 숫자를 선택했을 때
    if row == N:
        min_sum = current_sum
        return
    
    # 재귀 호출: 현재 행에서 선택할 열을 탐색
    for col in range(N):
        # 해당 열이 아직 사용되지 않았다면
        if not visited[col]:
            visited[col] = True  # 열 사용 처리
            find_min_sum(row + 1, current_sum + arr[row][col])
            visited[col] = False # 백트래킹: 열 사용 해제

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    min_sum = float('inf')  # 최소 합을 무한대로 초기화
    visited = [False] * N    # 열 방문 여부 체크
    
    find_min_sum(0, 0)
    
    print(f"#{tc} {min_sum}")