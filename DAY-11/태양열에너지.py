# 파리 퇴치 문제의 변형판
# 태양광 판넬 크기 N , 렌즈 크기 M
# 판넬 N x N , 렌즈 M x M

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    panel = [list(map(int, input().split())) for _ in range(N)] # N 줄 동안 판넬의 에너지 정보를 입력받아 2차원 리스트로 저장
    lens = [list(map(int, input().split())) for _ in range(M)]  # M 줄 동안 렌즈의 에너지 정보를 입력받아 2차원 리스트로 저장

    # 새로운 판넬의 크기
    new_size = N - M + 1 # 끝이 넘지 않도록 할 수 있는 시작점의 개수 N - M + 1
    new_panel = [[0] * new_size for _ in range(new_size)] # 결과를 담을 새로운 판넬(new_panel)을 0으로 초기화

    # 렌즈를 올려서 계산
    for i in range(new_size):   # i: 시작 행 인덱스(0 ~ N-M)
        for j in range(new_size): # j: 시작 열 인덱스(0 ~ N-M)
            total = 0 # 현재 위치에서의 누적 합(패널+렌즈 합)
            for p in range(M): # p: 렌즈의 행 인덱스(0 ~ M-1)
                for q in range(M):  # q: 렌즈의 열 인덱스(0 ~ M-1)
                    total += panel[i+p][j+q] + lens[p][q]
                    # 같은 상대 위치의 패널 값과 렌즈 값을 더해서 누적
                    # panel[i+p][j+q]: (i,j)를 기준으로 MxM 부분행렬의 원소
                    # lens[p][q]: 렌즈의 해당 칸에서 추가로 모을 수 있는 에너지
            new_panel[i][j] = total  # 계산된 합을 새로운 판넬의 (i, j) 위치에 기록
    
    print(f"#{tc}")
    for row in new_panel:    # 새로운 판넬의 각 행을 공백 구분으로 출력
        print(*row)