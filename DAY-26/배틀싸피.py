# while queue:
#     (r, c), actions = queue.popleft()

#     for d, (dr, dc) in enumerate(DIRS):
#         nr, nc = r + dr, c + dc
#         if (nr, nc) == target:
#             return actions + [FIRE_CMDS[d]]

#     for d, (dr, dc) in enumerate(DIRS):
#         nr, nc = r + dr, c + dc

#         if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in wall and (nr, nc) not in visited:
#             visited.add((nr, nc))
#             queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

# return []

# 일타싸피는 좌표 바꾸는거 -1로 바꾸는 거였던가