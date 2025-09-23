# NxN 비용 행렬에서
# 각 "행(공장)"에서 하나씩 "열(제품)"을 골라
# 세로(같은 제품) 중복 없이 총 비용의 최소값을 구한다.

def find_min_sum(row, current_sum):
    """row번째 공장부터 배정하며 최소 비용을 갱신하는 백트래킹 함수"""
    global min_sum

    # 가지치기: 지금까지의 합이 이미 최소값 이상이면 더 볼 필요 없음
    if current_sum >= min_sum:
        return

    # 모든 공장에 제품 배정을 끝냈다면 최소값 갱신
    if row == N:
        min_sum = current_sum
        return

    # row번째 공장에 배정할 제품(col)을 하나씩 시도
    for col in range(N):
        if not visited[col]:            # 아직 배정 안 된 제품만 선택
            visited[col] = True         # 제품 col 배정
            find_min_sum(row + 1, current_sum + cost[row][col])
            visited[col] = False        # 백트래킹(원상복구)

# ===== 메인 =====
T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    cost = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')  # 최소 비용 초기값(아주 크게)
    visited = [False] * N   # 각 제품이 이미 배정되었는지 표시

    find_min_sum(0, 0)      # 0번 공장부터 시작, 현재 합 0

    print(f"#{tc} {min_sum}")
