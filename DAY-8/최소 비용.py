import heapq   # 우선순위 큐(최소 힙) 사용을 위한 라이브러리

# 이동 방향: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra(N, board):
    INF = float('inf')  # 무한대를 의미 (아직 도달하지 못한 상태)
    dist = [[INF] * N for _ in range(N)]   # 최소 연료 소비량 저장 배열
    dist[0][0] = 0                         # 시작점은 연료 0으로 설정

    # heap 요소: (소모 연료, 현재 행, 현재 열)
    heap = [(0, 0, 0)]  
    
    # 다익스트라 시작
    while heap:
        cost, r, c = heapq.heappop(heap)   # 가장 작은 비용을 가진 노드 꺼내기
        
        # 이미 저장된 최소 비용보다 크면 무시 (더 좋은 경로 있음)
        if dist[r][c] < cost:
            continue

        # 도착지 (N-1, N-1)에 도착하면 바로 종료
        if r == N-1 and c == N-1:
            return cost

        # 4방향 탐색
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]  # 새로운 위치 계산
            if 0 <= nr < N and 0 <= nc < N:   # 보드 범위 확인
                # 이동 비용 계산
                # 기본 1 + (만약 더 높은 곳이면 높이 차이만큼 추가)
                extra = max(0, board[nr][nc] - board[r][c])
                new_cost = cost + 1 + extra

                # 새로 계산한 비용이 기존보다 더 작으면 갱신
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    # 힙에 새로운 경로 추가
                    heapq.heappush(heap, (new_cost, nr, nc))

    # while문이 끝나면 최종 목적지 최소 비용 반환
    return dist[N-1][N-1]

# 메인 실행부
T = int(input())   # 테스트 케이스 개수 입력
for tc in range(1, T+1):
    N = int(input())   # 지도의 크기 N 입력
    board = [list(map(int, input().split())) for _ in range(N)]  # N*N 높이 정보 입력

    ans = dijkstra(N, board)   # 다익스트라 실행
    print(f"#{tc} {ans}")      # 결과 출력
