# 파리 퇴치 문제의 변형판
# 태양광 판넬 크기 N , 렌즈 크기 M
# 판넬 N x N , 렌즈 M x M

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    panel = [list(map(int, input().split())) for _ in range(N)]
    lens = [list(map(int, input().split())) for _ in range(M)]

    # 새로운 판넬의 크기
    new_size = N - M + 1
    new_panel = [[0] * new_size for _ in range(new_size)]

    # 렌즈를 올려서 계산
    for i in range(new_size):
        for j in range(new_size):
            total = 0
            for p in range(M):
                for q in range(M):
                    total += panel[i+p][j+q] + lens[p][q]

            new_panel[i][j] = total
    
    print(f"#{tc}")
    for row in new_panel:
        print(*row)