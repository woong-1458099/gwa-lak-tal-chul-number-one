T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N X N 크기의 단어 퍼즐, 특정 길이 K를 갖는 단어

    arr = [list(map(int, input().split())) for _ in range(N)]   # 1 단어가 들어갈 수 있는 칸

    total = 0           # 길이가 K인 경우
    for i in range(N):  # 행우선 순회 i행, 열우선 순회 i열
        cnt_row = 0         # 가로로 연속한 1
        cnt_col = 0         # 세로로 연속한 1
        for j in range(N):
            if arr[i][j]:   # 가로로 1인 경우
                cnt_row += 1
            else:           # 0인 경우
                if cnt_row == K:    # 연속한 1이 K (길이 K인 단어에 딱 맞음)
                    total += 1
                cnt_row = 0     # 연속한 1의 개수 초기화. 인덴트 주의!!!
            if arr[j][i]:   # 세로로 1인 경우
                cnt_col += 1
            else:           # 0인 경우
                if cnt_col == K:    # 연속한 1이 K (길이 K인 단어에 딱 맞음)
                    total += 1
                cnt_col = 0     # 연속한 1의 개수 초기화. 인덴트 주의!!!
        if cnt_row == K:  # 행이 1로 끝난 경우. 인덴트 주의!!!
            total += 1
        if cnt_col == K:  # 열이 1로 끝난 경우. 인덴트 주의!!!
            total += 1
    print(f'#{tc} {total}')