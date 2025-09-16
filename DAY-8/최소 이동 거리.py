from heapq import heappop, heappush

def dijkstra(start):
    # 최단거리 테이블 초기화
    distance = [INF] * (N + 1)
    distance[start] = 0
    
    # (현재까지의 거리, 노드번호) 저장할 우선순위 큐
    pq = []
    heappush(pq, (0, start))

    while pq:
        dist, now = heappop(pq)

        # 이미 처리된 더 짧은 경로가 있으면 스킵
        if distance[now] < dist:
            continue

        # 인접한 노드들 확인
        for cost, nxt in graph[now]:
            new_dist = dist + cost
            if new_dist < distance[nxt]:
                distance[nxt] = new_dist
                heappush(pq, (new_dist, nxt))

    return distance


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())   # N: 노드 개수, E: 간선 개수

    INF = float('inf')
    graph = [[] for _ in range(N + 1)]

    # 간선 정보 입력
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))   # (비용, 목적지) 형태로 저장

    # 0번 노드에서 시작한다고 가정
    dist_table = dijkstra(0)

    # N번 노드까지의 최단 거리 출력
    print(f"#{tc} {dist_table[N]}")
