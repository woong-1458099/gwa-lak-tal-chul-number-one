T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    A = [input().split() for _ in range(N)]

    # 회전 행렬 만들기
    rot90 = [[A[N-1-j][i] for j in range(N)] for i in range(N)]
    rot180 = [[A[N-1-i][N-1-j] for j in range(N)] for i in range(N)]
    rot270 = [[A[j][N-1-i] for j in range(N)] for i in range(N)]

    print(f"#{tc}")
    for i in range(N):
        # 각 회전 결과에서 i번째 행을 문자열로 붙여 출력
        row90 = ''.join(rot90[i])
        row180 = ''.join(rot180[i])
        row270 = ''.join(rot270[i])
        print(row90, row180, row270)
