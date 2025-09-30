# A 도시에는 E 개의 일방통행 도로 구간이 있으며, 각 구간이 만나는
# 연결지점에는 0부터 N번까지의 번호가 붙어있다.
# 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마
# 인지 출력하는 프로그램을 만드시오
# 시작과 끝의 연결 지점 번호, 구간의 길이가 주어질 때, 0번 지점에서
# N번 지점까지 이동하는데 걸리는 최소한의 거리가 얼마인지 출력
# s, e, w  s : 구간 시작 s, 구간의 끝 지점 e, 구간 거리 w


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
