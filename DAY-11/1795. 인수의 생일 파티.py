from heapq import heappop, heappush

def dijkstra(start, graph, N):
    """
    다익스트라: 시작 정점 start에서 모든 정점까지의 최단 거리 배열을 구해 반환
    - graph[u] = [(v, w), ...] : u -> v 간선, 가중치 w (단방향)
    - N: 정점 개수 (정점 번호 1..N 사용)
    """
    INF = float('inf')              # 도달 불가를 나타내는 충분히 큰 값
    dist = [INF] * (N + 1)          # dist[i] = start에서 i까지의 최단 거리
    dist[start] = 0                 # 시작점까지 거리는 0
    pq = [(0, start)]               # 우선순위 큐(최소 힙): (현재까지의 비용, 정점)

    while pq:
        d, now = heappop(pq)        # 가장 짧은 거리 상태를 꺼냄
        if d > dist[now]:           # 이미 더 짧은 경로로 방문한 적 있으면 스킵
            continue
        # now에서 갈 수 있는 모든 간선 relax
        for nxt, cost in graph[now]:
            nd = d + cost           # now를 거쳐 nxt로 가는 새로운 비용
            if nd < dist[nxt]:      # 더 짧으면 갱신
                dist[nxt] = nd
                heappush(pq, (nd, nxt))  # 힙에 푸시
    return dist


T = int(input())                    # 테스트 케이스 수
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())    # N: 정점 수, M: 간선 수, X: 모이는 집(정점)
    graph = [[] for _ in range(N + 1)]     # 원본 그래프 (X -> i 거리용)
    reverse_graph = [[] for _ in range(N + 1)]  # 역방향 그래프 (i -> X 거리용)

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))            # 정방향 간선 u -> v (가중치 w)
        reverse_graph[v].append((u, w))    # 역방향 간선: v에서 u로 (원본의 반대)

    # X에서 각 정점 i까지 최단 거리 (X -> i)
    dist_from_X = dijkstra(X, graph, N)

    # 각 정점 i에서 X까지 최단 거리 (i -> X) = 역그래프에서 X -> i
    dist_to_X = dijkstra(X, reverse_graph, N)

    # 왕복 거리의 최댓값 계산: max_i { (i->X) + (X->i) }
    max_dist = 0
    for i in range(1, N + 1):
        # 문제 조건상 모든 정점 간 이동 가능하다고 했으니 INF 체크는 생략 가능
        max_dist = max(max_dist, dist_from_X[i] + dist_to_X[i])

    print(f"#{tc} {max_dist}")      # 테스트케이스 번호와 함께 정답 출력
