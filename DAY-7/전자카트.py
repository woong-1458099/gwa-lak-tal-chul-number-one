# def dfs(now, visited, cost):
#     global min_cost

#     # 가지치기 ( 이미 최소값 보다 크면 더 볼 필요 없음)
#     if cost >= min_cost:
#         return
    
#     # 모든 구역 방문했다면 사무실로 돌아가기
#     if visited == (1 << N) -1: # 모든 비트가 1이면 모든 구역 방문
#         min_cost = min(min_cost, cost + e[now][0])
#         return
    
#     # 다음 방문할 구역 고르기
#     for nxt in range(N):
#         if not visited & (1 << nxt):
#             dfs(nxt, visited | (1 << nxt), cost + e[now][nxt])

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     e = [list(map(int, input().split())) for _ in range(N)]

#     min_cost = float('inf')
#     dfs(0, 1, 0)

#     print(f"#{tc} {min_cost}")

from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]

    min_cost = float('inf')