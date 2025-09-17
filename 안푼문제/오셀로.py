import sys
sys.stdin = open("input.txt")

def in_range(n, r, c):                  # 범위 n 안에서 탐색
    return 0 <= r < n and 0 <= c < n

def hor(board, r, c, color):            # 
    n = len(board)
    opp = 2 if color == 1 else 1

# right
captured = []
cc = c + 1
while in_range(n, r, cc) and board[r][cc] == opp:
    captured.append((r, cc))
    cc += 1
if in_range(n, r, cc) and board[r][cc] == color:
    for rr, cc in captured:
        board[rr][cc] = color

# left
captured = []
cc = c - 1
while in_range(n, r, cc) and board[r][cc] == opp:
    captured.append((r, cc))
    cc -= 1
if in_range(n, r, cc) and board[r][cc] == color:
    for rr, cc in captured:
        board[rr][cc] = color
def ver(board, r, c, color):
    n = len(board)
    opp = 2 if color == 1 else 1

# down
captured = []
rr = r + 1
while in_range(n, rr, c) and board[rr][c] == opp:
    captured.append((rr, c))
    rr += 1
if in_range(n, rr, c) and board[rr][c] == color:
    for rr, cc in captured:
        board[rr][cc] = color

# up
captured = []
rr = r - 1
while in_range(n, rr, c) and board[rr][c] == opp:
    captured.append((rr, c))
    rr -= 1
if in_range(n, rr, c) and board[rr][c] == color:
    for rr, cc in captured:
        board[rr][cc] = color
def diag(board, r, c, color):
    n = len(board)
    opp = 2 if color == 1 else 1
    dirs = [(-1,-1), (-1,1), (1,-1), (1,1)]  # 2nd 1st 3rd 4th

for dr, dc in dirs:
    captured = []
    rr, cc = r + dr, c + dc
    while in_range(n, rr, cc) and board[rr][cc] == opp:
        captured.append((rr, cc))
        rr += dr
        cc += dc
    if in_range(n, rr, cc) and board[rr][cc] == color:
        for cr, cc in captured:
            board[cr][cc] = color
t = int(input())
for tc in range(1, 1 + t):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]

# 초기 배치
mid = n // 2
board[mid][mid] = 2
board[mid-1][mid-1] = 2
board[mid-1][mid] = 1
board[mid][mid-1] = 1

for _ in range(m):
    x, y, color = map(int, input().split())
    r, c = y-1, x-1  # 입력은 1-index
    board[r][c] = color  # 돌 놓기

    hor(board, r, c, color)
    ver(board, r, c, color)
    diag(board, r, c, color)

black = sum(row.count(1) for row in board)
white = sum(row.count(2) for row in board)
print(f"#{tc} {black} {white}")


----------------------------------------------------------------------


T =int(input())

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

for tc in range(1, T+1):
    # 게임판 크기 N
    # 내가 돌을 놓는 횟수 M
    N, M = map(int, input().split())

    # 게임판 만들기 N*N
    # board[i][j] == 0 : 돌이 없는 상태
    # board[i][j] == 1 : 돌이 없는 상태
    # board[i][j] == 2 : 돌이 없는 상태
    board = [[0] * N for _ in range(N)]

    # 게임판 처음에 백돌과 흑돌을 2개씩 놓고 시작
    # 백돌

    board[N // 2 - 1][N // 2 - 1] = board[N//2][N//2] = 2
    # 흑돌
   
    board[N // 2 - 1][N // 2] = board[N//2][N//2-1] = 1

    # 돌을 놓는 작업을 M번 한다.
    for i in range(M):
        # 놓을 돌의 위치 정보, 색
        # 문제에서 사용하는 좌표값이 내 생각과 맞는가?
        c, r, color = map(int, input().split())

        r -= 1
        c -= 1

        # r, c 위치에 돌 놓기
        board[r][c] = color

        # (r, c) 위치 기준으로 8방향 델타 탐색
        for d in range(8):
            # d방향으로 뻗어나간 칸의 개수k
            # 다른 색 돌을 기억할 위치
            
            mem = []
            for k in range(1, N):
                # d 방향으로 k칸 뻗어나간 위치 계산
                # 현재위치 기준 d 방향으로 k 칸 뻗어나감
                nr = r + dr[d] * k
                nc = c + dc[d] * k


                # 보드의 크기를 벗어난 경우
                if not (0<= nr < N and 0<= nc < N):
                    break

                # 돌이 없는 경우
                elif board[nr][nc] == 0:
                    break
                
                # 다른색 돌인 경우
                elif board[nr][nc] != color:
                    # 다른 색 돌들은 나중에 뒤집을 수도 있으니
                    # 리스트에 넣어사 저장해둔다.
                    mem.append((nr, nc))

                # 같은색 돌인 경우
                elif board[nr][nc] == color:
                    # 지금까지 만난 다른 색 돌을 모두 뒤집어서
                    # 내 색으로 맞춘다.
                    while mem: 
                        rr, rc = mem.pop()
                        board[rr][rc] = color

                    break # 같은색 돌을 만나서 바꿨으면 더이상 진행X

    # 돌 놓기를 다 했으면 흰돌의 개수와 검은돌의 개수 세기
    w = 0
    b = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                 b += 1
            elif board[i][j] == 2:
                 w += 1

        print(f"#{tc} {b} {w}")