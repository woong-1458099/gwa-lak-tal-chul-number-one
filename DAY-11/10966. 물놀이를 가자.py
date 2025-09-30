# 문제: 각 'L'(땅) 칸이 가장 가까운 'W'(물) 칸으로 가는 최소 이동 횟수의 합
# 핵심 아이디어:
#   - 모든 'W'를 동시에 시작점으로 큐에 넣고 BFS(다중 시작) 1번 수행
#   - dist[r][c] = 해당 칸에서 가장 가까운 'W'까지의 거리
#   - 최종 답 = 모든 'L' 칸에 대해 dist를 합산
#
# 왜 다중 시작 BFS인가?
#   - 'W'가 여러 개 있을 때, 각 칸의 최단 거리는 "가장 가까운 W"까지의 거리
#   - 모든 W에서 동시에 퍼져나가면 한 번의 BFS로 각 칸의 최단 거리를 얻을 수 있음
#   - 시간복잡도 O(N*M) (큐에 각 칸이 최대 한 번 들어감)


import sys
from collections import deque

input = sys.stdin.readline

# 상, 하, 좌, 우 이동 벡터 (문제 조건: 4방향 인접)
DR = (-1, 1, 0, 0)
DC = (0, 0, -1, 1)

def solve():
    T = int(input().strip())
    for tc in range(1, T + 1):
        # N: 행(세로 크기), M: 열(가로 크기)
        N, M = map(int, input().split())

        grid = [input().strip() for _ in range(N)]

        # 거리 배열: 아직 방문 전은 -1로 표시
        dist = [[-1] * M for _ in range(N)]

        # 다중 시작 BFS를 위한 큐
        q = deque()

        # 1) 모든 'W' 칸을 시작점(거리 0)으로 큐에 넣기
        #    - 'W'에서 'W'로의 거리는 0 (자기 자신)
        for r in range(N):
            row = grid[r]
            for c in range(M):
                if row[c] == 'W':
                    dist[r][c] = 0
                    q.append((r, c))

        # 2) BFS 수행: 모든 칸에 대해 가장 가까운 W까지의 최단 거리 채우기
        while q:
            r, c = q.popleft()
            d = dist[r][c]

            for k in range(4):
                nr = r + DR[k]
                nc = c + DC[k]
                # 격자 범위 체크
                if 0 <= nr < N and 0 <= nc < M:
                    if dist[nr][nc] == -1:       # 아직 방문하지 않은 칸만
                        dist[nr][nc] = d + 1     # 현재 거리 + 1
                        q.append((nr, nc))

        # 3) 정답 계산: 'L' 칸들의 dist 합산
        #    - 물 칸('W')의 dist는 0이므로 더해도 영향 없음
        total = 0
        for r in range(N):
            row = grid[r]
            for c in range(M):
                if row[c] == 'L':
                    # 문제 보장상 적어도 하나의 W가 있으므로 dist는 항상 채워짐
                    total += dist[r][c]

        print(f"#{tc} {total}")

if __name__ == "__main__":
    solve()
