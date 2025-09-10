T = int(input())
 
for tc in range(1, T + 1):
    # N : 물웅덩이 길이
    # K : 개구리 최대 점프 칸 수
    N, K = map(int, input().split())
 
    # 물웅덩이 정보 1부터 시작하도록 0을 맨 왼쪽에 추가
    pond = [0] + list(map(int, input().split()))
 
    # 개구리의 현재 위치, 처음에는 위치 = 1 에서 시작한다
    frog = 1
 
    # 개구리의 위치가 N보다 작으면 점프 가능
    while frog < N:
        # 다음에 점프할 위치
        next = frog
        # 개구리가 점프 가능한 범위 1 ~ K
        for i in range(1, K + 1):
            # i만큼 점프한 위치가 물웅덩이를 벗어나면
            # 물웅덩이의 길이가 최대 이동 거리
            if frog + i > N:
                next = N
                break
 
            # 다음에 i만큼 점프한 위치에 나뭇잎이 있다면 점프 가능
            if pond[frog + i] == 1:
                # 점프 위치 변경
                next = frog + i
                break
        else:
            # 반복문이 중단된적이 없다면 점프할곳을 찾지 못한것
            # 현재 위치 + K 가 마지막 점프위치가 되고 점프 종료
            frog = frog + K
            break
 
        # 다음 위치를 현재위치로 최신화
        frog = next
 
    print(f"#{tc} {frog}")