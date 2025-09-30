# 초간단 BFS 풀이 (+1, -1, *2, -10)
# 아이디어: 한 번의 연산 = 거리 1칸. 가장 먼저 M에 도달한 거리 = 최소 연산 횟수.
# 범위 조건: 중간 결과 포함 1..1_000_000 벗어나면 버림.

from collections import deque


MAXV = 1_000_000  # 값 상한

T = int(input().strip())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 이미 같으면 0 (문제는 N!=M이라 안 오지만 안전용)
    if N == M:
        print(f"#{tc} 0")
        continue

    visited = [False] * (MAXV + 1)  # 방문 체크(중복 탐색 방지)
    q = deque()
    q.append((N, 0))                # (현재 값, 사용한 연산 횟수)
    visited[N] = True

    ans = -1
    while q:
        x, d = q.popleft()

        # 다음으로 갈 수 있는 4가지 연산 결과를 순서대로 만들기
        for nx in (x + 1, x - 1, x * 2, x - 10):
            if nx == M:             # 목표에 도달하면 지금보다 1번 더 한 것
                ans = d + 1
                q.clear()           # 더 볼 필요 없이 바로 탈출
                break
            if 1 <= nx <= MAXV and not visited[nx]:
                visited[nx] = True
                q.append((nx, d + 1))

    print(f"#{tc} {ans}")
