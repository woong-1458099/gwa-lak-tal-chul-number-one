import math

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    for x in range(-N, N + 1):
        max_y = int(math.sqrt(N * N - x * x))  # 가능한 y 최대
        cnt += 2 * max_y + 1                   # -max_y ~ +max_y
    print(f"#{tc} {cnt}")
