T = int(input())

for tc in range(1, T +1):
    N = int(input())  # 농장의 크기 N , 항상 홀수
    farm = [list(map(int, input().strip())) for _ in range(N)]  # 리스트로 입력받음 예를들어서 N이 5이고 한 줄이 14032 이면 리스트 [1,4,0,3,2]로 변환

    total = 0
    mid = N // 2

    for i in range(N):
        if i <= mid:
            start = mid - i
            end = mid + i   # 행 i가 중앙 행보다 위쪽이면, 마름모 폭이 점점 넓어진다
        
        else:
            start = i - mid  # 행 i 가 중앙보다 아래쪽이면, 마름모 폭이 점점 좁아진다.
            end = (N -1) - (i - mid)

        for j in range(start, end + 1):  #range(start, stop) , range(stop) , range(start, stop, step)
            total += farm[i][j]   # end +1 -> range에서 끝 미포함

    print(f"#{tc} {total}")