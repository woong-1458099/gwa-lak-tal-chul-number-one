# ------------------------------------------------------------
# 유향 그래프에서 시작 정점 S부터 도착 정점 G까지
# "정점을 한 번씩만 방문하는(단순 경로)" 경로의 개수를 세는 코드
# - DFS + 백트래킹(visited 표시했다가 되돌리기) 사용
# - graph[u]에는 u -> v 방향 인접 정점들이 들어감 (유향 그래프)
# ------------------------------------------------------------

def dfs(start, end):
    global count                 # 전역 변수 count(찾은 경로 수)를 사용하겠다는 선언
    visited[start] = 1           # 현재 정점 start를 방문 처리 (이번 경로에서 재방문 금지)

    if start == end:             # 목적지(end)에 도착했다면
        count += 1               # 유효한 단순 경로 1개 발견
        return                   # 더 내려갈 필요 없이 반환

    # 현재 정점에서 나가는 모든 간선(다음 정점들)을 순회
    for next in graph[start]:
        if visited[next] == 0:   # 아직 이번 경로에서 방문하지 않은 정점만 진행
            visited[next] = 1    # 방문 표시
            dfs(next, end)       # 다음 정점으로 계속 탐색 (재귀 호출)
            visited[next] = 0    # 백트래킹: 다른 분기/경로를 위해 방문 표시 되돌리기


T = int(input())                 # 테스트 케이스 개수

for tc in range(1, T+1):
    N, E = map(int, input().split())   # N: 정점 수(1..N), E: 간선 수
    arr = list(map(int, input().split()))  # 간선들이 (u v) 쌍으로 2*E개 들어옴 (u->v)
    S, G = map(int, input().split())   # S: 시작 정점, G: 도착 정점

    graph = [[] for _ in range(N + 1)] # 인접 리스트 초기화 (1..N 사용, 0은 미사용)

    count = 0                           # S -> G 단순 경로 개수 초기화

    # 간선 배열 arr을 (u, v) 쌍으로 끊어서 인접 리스트에 추가
    for i in range(0, len(arr), 2):
        u = arr[i]                      # 간선의 시작 정점
        v = arr[i+1]                    # 간선의 도착 정점
        graph[u].append(v)              # 유향 간선 u -> v 등록 (무향이면 v->u도 추가해야 함)

    visited = [0] * (N + 1)             # 방문 배열 (0: 미방문, 1: 방문)
    dfs(S, G)                           # DFS 시작: S에서 G까지 탐색하며 경로 수 세기

    print(f'#{tc} {count}')             # 테스트 케이스 번호와 함께 경로 개수 출력
