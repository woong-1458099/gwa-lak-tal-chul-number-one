T = int(input())  # 테스트 케이스 개수 입력

# 상하좌우 이동을 위한 방향 벡터
dr = [-1, 1, 0, 0]   # 행 변화량 (U, D, L, R)
dc = [0, 0, -1, 1]   # 열 변화량 (U, D, L, R)

# 방향 상수 정의 (인덱스와 매칭하기 쉽게)
U = 0
D = 1
L = 2
R = 3

# 좌표가 맵 안에 있는지 확인하는 함수
def in_range(r, c):
    return 0 <= r < h and 0 <= c < w

# 탱크 이동 함수
def move(r, c, d):
    m[r][c] = "."   # 현재 탱크 위치를 빈칸으로 바꿈
    nr, nc = r + dr[d], c + dc[d]  # 이동할 좌표 계산
    # 맵 범위 안이고, 이동할 위치가 평지('.')라면 이동
    if in_range(nr, nc) and m[nr][nc] == ".":
        r, c = nr, nc
    m[r][c] = tanks[d]  # 이동한 위치에 탱크 방향 기호 표시
    return r, c

# 탱크 모양 (탱크 방향에 따라 출력되는 문자)
tanks = ["^", "v", "<", ">"]   # 상, 하, 좌, 우
# 입력되는 명령어 문자와 방향 인덱스 매칭
dirs = ["U", "D", "L", "R"]

# 각 테스트 케이스 실행
for tc in range(1, T + 1):
    h, w = map(int, input().split())  # 맵의 높이(h), 너비(w)

    # 맵 정보 입력 (문자열을 리스트로 저장)
    m = [list(input()) for _ in range(h)]

    # 탱크 초기 위치와 방향 찾기
    r, c = 0, 0   # 탱크 위치
    d = -1        # 탱크 방향
    for i in range(h):
        for j in range(w):
            if m[i][j] in tanks:   # 탱크 모양 중 하나라면
                d = tanks.index(m[i][j])  # 현재 방향 저장
                r, c = i, j               # 탱크 좌표 저장

    l = int(input())        # 명령어 개수 입력
    commands = input()      # 명령어 문자열 입력

    # 명령어 하나씩 실행
    for o in commands:
        if o in dirs:  # 이동 명령 (U, D, L, R)
            d = dirs.index(o)     # 방향 갱신
            r, c = move(r, c, d)  # 이동 수행
        else:  # 발사 명령 (S)
            sr, sc = r, c  # 포탄 발사 시작 위치
            while in_range(sr, sc):  # 맵을 벗어나기 전까지 계속 진행
                if m[sr][sc] == "*":  # 벽돌벽('*')이면 파괴
                    m[sr][sc] = "."
                    break
                elif m[sr][sc] == "#":  # 강철벽('#')이면 막히고 멈춤
                    break
                # 포탄 직진 (현재 방향 d로 계속 이동)
                sr = sr + dr[d]
                sc = sc + dc[d]

    # 결과 출력
    print(f"#{tc}", end=" ")
    for i in range(h):
        print(*m[i], sep="")
