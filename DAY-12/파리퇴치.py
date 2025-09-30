# NxN 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미
# MXM 크기의 파리채를 한 번 내려쳐 최대한 많은 파리를 죽이고자 한다. 죽은 파리의 개수를 구하라 !


T = int(input()) # 테스트 케이스 개수 입력
for tc in range(1, T+1): #
    N, M = map(int, input().split())  # N : 배열크기, M : 파리채 크기
    arr = [list(map, int(input().split()))] # N x N 배열 입력

    max_v = 0  # 잡을 수 있는 최대 파리 수 저장하는 변수

    for i in range(N-M+1):  # 세로 방향 시작점
        for j in range(N-M+1):  # 가로 방향 시작점
            cnt = 0
            for p in range(M):  # 파리채 높이만큼
                for q in range(M):  # 파리채 너비만큼
                    cnt += arr[i+p][j+q]  # 현재 (i, j)위치에서 MxM 범위 합

            if max_v < cnt:  # 합이 기존 최대보다 크면 갱신
                max_v = cnt
    
    print(f"#{tc} {max_v}")


# 최솟값 구하는 파리 퇴치
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = float('inf')
    for i in range(N - M + 1):          # 시작 행
        for j in range(N - M + 1):      # 시작 열
            s = 0
            for p in range(M):          # M x M 영역 합
                for q in range(M):
                    s += arr[i+p][j+q]
            if s < min_v:
                min_v = s

    print(f"#{tc} {min_v}")
