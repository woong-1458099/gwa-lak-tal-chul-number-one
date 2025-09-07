# 당근의 크기가 커지다니 참으로 신기한 부분
# 흠 연속으로 커지는 구간의 길이를 찾으면 될듯
# 앞의 당근 크기보다 크면 길이 +1 , 아니면 길이 1로 초기화
# max_len 갱신해서 가장 긴 길이 저장
# 다 확인 한 뒤에 max_len 출력

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 당근 개수 ( 정수로 나타내야 되서 int )
    carrots = list(map(int,input().split())) # 당근 크기 리스트



   

    max_len = 1  # 연속으로 커지지 않는 경우 구간의 최소 길이는 1이다
                 # 만약 max_len을 0으로 두고 시작하면 최소 길이가 "0"이 나오게 된다.
    current_len = 1  # 연속으로 증가하는 구간 길이 

    for i in range(1, N):
        if carrots[i] > carrots[i-1]:

      #range(start, stop)
          # carrots[i] -> 현재 위치 당근 크기 , carrots[i-1] -> 바로 이전 당근 크기 
            # 현재 당근 크기가 이전 당근 크기보다 크면이라는 뜻인데 연속 증가를 의미
            
            current_len += 1
            if current_len > max_len:
                max_len = current_len

        else:
            current_len = 1

    print(f"#{tc} {max_len}")