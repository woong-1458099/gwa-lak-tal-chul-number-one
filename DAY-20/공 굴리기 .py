T = int(input())

# 각 테스트 케이스마다 반복
for tc in range(1, T + 1):
    # 격자 한 변의 길이 N 입력 (N x N 격자)
    N = int(input())
    
    # N줄에 걸쳐 격자 정보 입력 받기
    # ex) 5
    #    1 2 3 4 5
    #    5 4 3 2 1
    # 이런 식으로 들어오는 걸 2차원 리스트로 저장
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 상, 하, 좌, 우 방향을 나타내는 델타 배열
    # di, dj의 인덱스 0~3이 아래와 같은 방향을 의미:
    # 0: 상(-1, 0), 1: 하(1, 0), 2: 좌(0, -1), 3: 우(0, 1)
    # 이 "순서"가 곧 우선순위(상 → 하 → 좌 → 우)가 됨
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 공을 굴렸을 때, 이동할 수 있는 최대 칸 수를 저장할 변수
    max_count = 0

    # 격자의 모든 칸(i, j)을 "시작 위치"로 한 번씩 다 시도해 보기
    for i in range(N):
        for j in range(N):
            # 현재 공의 위치 (current i, current j)
            ci, cj = i, j
            
            # 현재 시작점에서 공이 이동한 칸 수
            # 시작 칸도 방문 1칸으로 세기 위해 while문 안에서 1씩 증가시키는 방식 사용
            cnt = 0

            # 공을 더 이상 이동할 수 없을 때까지 반복
            while True:
                # 현재 칸에 도착했으므로, 방문 칸 수 +1
                cnt += 1

                # 상하좌우 이웃 중 "갈 수 있는 후보 칸" 중에서
                # 숫자가 가장 작은 칸을 찾기 위한 변수
                # 문제 조건에서 각 칸 값은 1~99라 1000000은 충분히 큰 초기값
                min_num = 1000000

                # 다음에 이동할 위치 (ni, nj)를 저장할 변수
                # 아직 정해지지 않았으므로 None으로 초기화
                next_pos = None

                # 4방향(상, 하, 좌, 우)을 차례대로 확인
                for d in range(4):
                    # 다음 칸의 좌표 계산
                    ni = ci + di[d]
                    nj = cj + dj[d]

                    # 1) 격자 범위 안에 있는지 체크
                    if 0 <= ni < N and 0 <= nj < N:
                        # 2) 현재 칸(matrix[ci][cj])보다 숫자가 더 작은 칸만 이동 가능
                        if matrix[ni][nj] < matrix[ci][cj]:
                            # 3) 그 중에서 가장 작은 숫자를 가진 칸을 선택해야 함
                            #    지금까지 찾은 최소값 min_num보다 더 작으면 갱신
                            if matrix[ni][nj] < min_num:
                                min_num = matrix[ni][nj]
                                next_pos = (ni, nj)
                                # 여기서 방향 우선순위가 자동으로 적용됨:
                                # 같은 값일 경우, 먼저 탐색된 방향(상→하→좌→우)이 유지되기 때문

                # 4방향을 모두 봤는데도 이동 가능한 칸을 못 찾은 경우
                # (즉, 현재 칸보다 작은 숫자의 칸이 상/하/좌/우에 없음)
                if next_pos is None:
                    # 더 이상 이동할 수 없으므로 이동 종료
                    break
                else:
                    # 이동 가능한 다음 칸이 정해졌다면,
                    # 그 칸으로 공의 현재 위치를 갱신
                    ci, cj = next_pos

            # 현재 시작점(i, j)에서 이동한 칸 수(cnt)를
            # 지금까지의 최대 이동 칸 수(max_count)와 비교해서 갱신
            if cnt > max_count:
                max_count = cnt
                # max_count = max(max_count, cnt) 로 써도 동일한 의미

    # 한 테스트 케이스에서 가능한 최대 이동 칸 수를 출력
    # 형식: #테스트케이스번호 값
    print(f"#{tc} {max_count}")