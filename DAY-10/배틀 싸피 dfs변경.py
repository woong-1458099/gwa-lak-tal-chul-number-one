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
from collections import deque

# 방향 정의 (오른쪽, 아래, 왼쪽, 위)
DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
MOVE_CMDS = {0: "R A", 1: "D A", 2: "L A", 3: "U A"}
FIRE_CMDS = {0: "R F", 1: "D F", 2: "L F", 3: "U F"}
START_SYMBOL = 'M'
TARGET_SYMBOL = 'X'
WALL_SYMBOL = {'R', 'W'}  # 바위, 물은 절대 못 지나감

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
            if grid[nr][nc] in WALL_SYMBOL:  # 바위, 물에 막힘
                break
    return False, -1

# 경로 탐색 알고리즘 (Stage 4까지 가능)
def bfs(grid, start, target, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (r, c), actions = queue.popleft()

        # ✅ 사거리 3 안에 X가 보이면 바로 FIRE
        ok, d = can_fire(r, c, target, grid)
        if ok:
            return actions + [FIRE_CMDS[d]]

        # 4방향 탐색
        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in wall and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

    return []

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
