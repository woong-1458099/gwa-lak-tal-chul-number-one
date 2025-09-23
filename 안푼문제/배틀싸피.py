import sys
import socket
from collections import deque

##############################
# 메인 프로그램 통신 변수 정의
##############################
HOST = '127.0.0.1'
PORT = 8747
ARGS = sys.argv[1] if len(sys.argv) > 1 else ''
sock = socket.socket()

##############################
# 메인 프로그램 통신 함수 정의
##############################

# 메인 프로그램 연결 및 초기화
def init(nickname):
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}...')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}'

        return submit(init_command)

    except Exception as e:
        print('[ERROR] Failed to connect. Please check if the main program is waiting for connection.')
        print(e)

# 메인 프로그램으로 데이터(명령어) 전송
def submit(string_to_send):
    try:
        send_data = ARGS + string_to_send + ' '
        sock.send(send_data.encode('utf-8'))

        return receive()
        
    except Exception as e:
        print('[ERROR] Failed to send data. Please check if connection to the main program is valid.')

    return None

# 메인 프로그램으로부터 데이터 수신
def receive():
    try:
        game_data = (sock.recv(1024)).decode()

        if game_data and game_data[0].isdigit() and int(game_data[0]) > 0:
            return game_data

        print('[STATUS] No receive data from the main program.')    
        close()

    except Exception as e:
        print('[ERROR] Failed to receive data. Please check if connection to the main program is valid.')

# 연결 해제
def close():
    try:
        if sock is not None:
            sock.close()
        print('[STATUS] Connection closed')
    
    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')

##############################
# 입력 데이터 변수 정의
##############################
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
my_allies = {}  # 아군 정보. 예) my_allies['M'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문

##############################
# 입력 데이터 파싱
##############################

# 입력 데이터를 파싱하여 각각의 리스트/딕셔너리에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0]) if len(header) >= 1 else 0 # 맵의 세로 크기
    map_width = int(header[1]) if len(header) >= 2 else 0  # 맵의 가로 크기
    num_of_allies = int(header[2]) if len(header) >= 3 else 0  # 아군의 수
    num_of_enemies = int(header[3]) if len(header) >= 4 else 0  # 적군의 수
    num_of_codes = int(header[4]) if len(header) >= 5 else 0  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, len(col)):
            map_data[i][j] = col[j]
    row_index += map_height

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    my_allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0) if len(ally) >= 1 else '-'
        my_allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0) if len(enemy) >= 1 else '-'
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])

# 파싱한 데이터를 화면에 출력
def print_data():
    print(f'\n----------입력 데이터----------\n{game_data}\n----------------------------')

    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()

    print(f'\n[아군 정보] (아군 수: {len(my_allies)})')
    for k, v in my_allies.items():
        if k == 'M':
            print(f'M (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 메가 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(enemies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'X (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])

##############################
# 닉네임 설정 및 최초 연결
##############################
NICKNAME = '기본코드'
game_data = init(NICKNAME)

###################################
# 알고리즘 함수/메서드 부분 구현 시작
###################################

# 출발지와 목적지의 위치 찾기
def find_positions(grid, start_mark, goal_mark):
    rows, cols = len(grid), len(grid[0])
    start = goal = None

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == start_mark:
                start = (row, col)

            elif grid[row][col] == goal_mark:
                goal = (row, col)

    return start, goal

# 경로 탐색 알고리즘
def bfs(grid, start, target, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (r, c), actions = queue.popleft()

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if (nr, nc) == target:
                return actions + [FIRE_CMDS[d]]

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != wall and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

    return []

# 경로 탐색 변수 정의
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = 'R'

# 최초 데이터 파싱
parse_data(game_data)

# 출발지점, 목표지점의 위치 확인
start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)
if not start or not target:
    print("[ERROR] Start or target not found in map")
    close()
    exit()

# 최초 경로 탐색
actions = bfs(map_data, start, target, WALL_SYMBOL)

###################################
# 알고리즘 함수/메서드 부분 구현 끝
###################################

# 반복문: 메인 프로그램 <-> 클라이언트(이 코드) 간 순차로 데이터 송수신(동기 처리)
while game_data is not None:

    ##############################
    # 알고리즘 메인 부분 구현 시작
    ##############################

    # 파싱한 데이터를 화면에 출력하여 확인
    print_data()

    # 이전 경로 탐색 결과가 존재하지 않을 경우 다시 탐색
    if not actions:
        start, target = find_positions(map_data, START_SYMBOL, TARGET_SYMBOL)
        actions = bfs(map_data, start, target, WALL_SYMBOL) if start and target else []

    # 탱크를 제어할 명령어를 output의 값으로 지정(type: string)
    output = actions.pop(0) if actions else 'A'

    # 메인 프로그램에서 명령을 처리할 수 있도록 명령어를 submit()의 인자로 전달
    game_data = submit(output)

    # submit()의 리턴으로 받은 갱신된 데이터를 다시 파싱
    if game_data:
        parse_data(game_data)

    ##############################
    # 알고리즘 메인 구현 끝
    ##############################

# 반복문을 빠져나왔을 때 메인 프로그램과의 연결을 완전히 해제하기 위해 close() 호출
close()


# 기본 logic 코드가 주어 지기 때문에 내가 수정 해야 하는 건 dfs 부분


# stage 4 별 1개 정도 60점짜리 코드
# 경로 탐색 알고리즘
def bfs(grid, start, target, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (r, c), actions = queue.popleft()

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if (nr, nc) == target:
                return actions + [FIRE_CMDS[d]]

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in wall and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

    return []

# 경로 탐색 변수 정의
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = {'R', 'W'}

# 최초 데이터 파싱
parse_data(game_data)


# stage 4 까지 통과 가능
# ===== 사거리 3 발사 가능 여부 체크 =====
def can_fire(r, c, target, dirs, max_range=3):
    """
    현재 위치 (r,c)에서 target을 사거리 max_range 이내로
    직선 방향으로 쏠 수 있는지 확인
    """
    for d, (dr, dc) in enumerate(dirs):
        nr, nc = r, c
        for dist in range(1, max_range + 1):
            nr += dr
            nc += dc
            if (nr, nc) == target:
                return True, d
    return False, -1


# ===== BFS 경로 탐색 =====
def bfs(grid, start, target, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (r, c), actions = queue.popleft()

        # --- 포탑 사거리 3 발사 체크 ---
        fire_ok, direction = can_fire(r, c, target, DIRS, 3)
        if fire_ok:
            return actions + [FIRE_CMDS[direction]]

        # --- 이동 확장 ---
        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] not in wall and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

    return []  # 길 없음

# stage 5 까지 통과 가능
from collections import deque

# ==============================
# 경로 탐색 알고리즘
# ==============================
def in_range(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def can_fire(r, c, target, grid):
    """현재 위치에서 사거리 3 안에 target(X)이 보이면 발사 가능"""
    rows, cols = len(grid), len(grid[0])
    for d, (dr, dc) in enumerate(DIRS):
        nr, nc = r, c
        for step in range(1, 4):  # 1~3칸 직선
            nr += dr
            nc += dc
            if not in_range(nr, nc, rows, cols):
                break
            if (nr, nc) == target:
                return True, d
            if grid[nr][nc] in WALL_SYMBOL:  # 바위, 물은 막힘
                break
    return False, -1

def bfs(grid, start, target, wall, ammo=10):
    """
    Stage 5까지 대응 BFS
    - 사거리 3 발사 가능
    - 나무(T)는 포탄 쏴서 제거 가능 (포탄 소모)
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque([((start[0], start[1], ammo), [])])  # 상태: (행, 열, 남은포탄)
    visited = {(start[0], start[1], ammo)}

    while queue:
        (r, c, bullets), actions = queue.popleft()

        # ✅ 사거리 안에 X 보이면 발사 후 종료
        ok, d = can_fire(r, c, target, grid)
        if ok:
            return actions + [FIRE_CMDS[d]]

        # 4방향 탐색
        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc, rows, cols):
                continue
            cell = grid[nr][nc]

            # 바위, 물은 절대 못 감
            if cell in WALL_SYMBOL:
                continue

            # 나무 처리
            if cell == 'T':
                if bullets <= 0:
                    continue
                new_state = (nr, nc, bullets-1)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, actions + [FIRE_CMDS[d], MOVE_CMDS[d]]))
            else:
                new_state = (nr, nc, bullets)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, actions + [MOVE_CMDS[d]]))

    return []


# ==============================
# 경로 탐색 변수 정의
# ==============================
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = {'R', 'W'}  # 바위, 물은 통과 불가


# ==============================
# 최초 데이터 파싱
# ==============================
parse_data(game_data)


# stage 5 까지 대응 python code
from collections import deque

# ==============================
# 경로 탐색 알고리즘 (Stage 5 대응)
# ==============================
def in_range(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

def can_fire(r, c, target, grid):
    """현재 위치에서 사거리 3 안에 target(X)이 보이면 발사 가능"""
    rows, cols = len(grid), len(grid[0])
    for d, (dr, dc) in enumerate(DIRS):
        nr, nc = r, c
        for step in range(1, 4):  # 1~3칸 직선 탐색
            nr += dr
            nc += dc
            if not in_range(nr, nc, rows, cols):
                break
            if (nr, nc) == target:
                return True, d
            if grid[nr][nc] in WALL_SYMBOL:  # 바위, 물은 막힘
                break
    return False, -1

def bfs(grid, start, target, wall, ammo=10):
    """
    Stage 5까지 대응 BFS
    - 사거리 3 발사 가능
    - 나무(T)는 포탄 쏴서 제거 후 이동
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque([((start[0], start[1], ammo), [])])  # 상태: (행, 열, 남은포탄), 경로
    visited = {(start[0], start[1], ammo)}

    while queue:
        (r, c, bullets), actions = queue.popleft()

        # ✅ 사거리 안에 X 보이면 바로 FIRE
        ok, d = can_fire(r, c, target, grid)
        if ok:
            return actions + [FIRE_CMDS[d]]

        # 4방향 이동
        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc, rows, cols):
                continue
            cell = grid[nr][nc]

            # 바위, 물은 못 지나감
            if cell in WALL_SYMBOL:
                continue

            # 나무 처리
            if cell == 'T':
                if bullets <= 0:
                    continue
                new_state = (nr, nc, bullets - 1)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, actions + [FIRE_CMDS[d], MOVE_CMDS[d]]))
            else:
                new_state = (nr, nc, bullets)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, actions + [MOVE_CMDS[d]]))

    return []


# ==============================
# 경로 탐색 변수 정의
# ==============================
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = {'R', 'W'}  # 바위, 물은 통과 불가


# ==============================
# 최초 데이터 파싱
# ==============================
parse_data(game_data)
