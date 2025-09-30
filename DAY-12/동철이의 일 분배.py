def f(i, N, m): # i : 지금 배정할 사람 (행) 인덱스 0 부터 시작해서 N이 되면 전원 배정 완료
                # N : 문제 크기(사람/일의 수). 재귀 깊이의 한계값이자 종료 조건에 씀
                # m : 현재까지 배정한 것들의 확률 곱(누적값). 처음에 1부터 시작해서, 매 배정마다 m *= P[i][j]/100으로 업데이트
    global max_v
   
    if i == N:  # 모든 사람을 다 배정했다면, 현재 곱 m으로 최대값 갱신
        if max_v < m:
            max_v = m

    elif max_v >= m: # 가지치기 : 현재 곱 m이 이미 최대값 이하이면 더 내려가도 이길 수 없으니 중단
        return
    else: 

        for j in range(N): # i번째 사람에게 배정할 일을 고른다 ( 아직 쓰지 않은 열만 )
            if used[j] == 0:
                used[j] = 1

                f(i + 1, N, m * P[i][j]/100) # 확률은 %로 주어졌으니 /100 해서 곱셈
                used[j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]  # % 단위(0~100)
    max_v = 0
    used = [0] * N
    f(0, N, 1)  # i = 0 번쨰 사람부터, 초기 곱 m-1(곱셈 항등원) 로 시작
    print(f"#{tc} {max_v*100:.6f}")  # 내부는 0~1 사이 실수, 출력은 %로 환산



