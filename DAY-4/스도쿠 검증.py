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

    