T = int(input())  # 테스트케이스 개수

for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]  # 9x9 스도쿠 입력
    valid = 1  #  유효하면 1, 아니면 0 , 1 = True, 0 = False
    
    # 1. 행 검사
    for row in sudoku:
        if len(set(row)) != 9:  # 중복이 있으면 길이가 9가 안 됨
            valid = 0
            break
    
    # 2. 열 검사
    if valid:  # 행에서 이미 틀리면 더 검사 안 해도 됨
        for col in range(9):
            column = [sudoku[row][col] for row in range(9)]
            if len(set(column)) != 9:
                valid = 0
                break
    
    # 3. 3x3 격자 검사
    if valid:
        for i in range(0, 9, 3):       # 0, 3, 6 (start, stop, step) start는 포함되는 값이고, stop은 포함되지 않음
            for j in range(0, 9, 3):   # 0, 3, 6 (step : 증가(양수) 또는 감소(음수) 간격)
                block = []
                for x in range(3):
                    for y in range(3):
                        block.append(sudoku[i + x][j + y])
                if len(set(block)) != 9:
                    valid = 0
                    break
    
    print(f"#{tc} {valid}")

#     T = int(input())

# for tc in range(1, T + 1):
#     N = 9
#     sudoku = [list(map(int, input().split())) for _ in range(N)]

#     # 일단 잘 되어 있다고 생각
#     answer = 1

#     for i in range(N):
#         # 행
#         row_set = set()
#         # 열
#         col_set = set()
#         for j in range(N):
#             # 숫자 9개씩 넣기
#             row_set.add(sudoku[i][j])
#             col_set.add(sudoku[j][i])

#         # 행검사, 열검사 set는 중복을 허용하지 않으므로 빠짐없이 9개가 들어있어야함
#         if len(row_set) != N or len(col_set) != N:
#             answer = 0

#     # 3 * 3
#     for i in range(0, N, 3):
#         for j in range(0, N, 3):
#             box_set = set()
#             for r in range(i, i + 3):
#                 for c in range(j, j + 3):
#                     box_set.add(sudoku[r][c])

#             # print(i,j, box_set)
#             if len(box_set) != N:
#                 answer = 0

#     print(f"#{tc} {answer}")


    