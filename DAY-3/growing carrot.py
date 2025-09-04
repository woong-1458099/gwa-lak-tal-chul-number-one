# 당근의 크기가 커지다니 참으로 신기한 부분
# 흠 연속으로 커지는 구간의 길이를 찾으면 될듯
# 앞의 당근 크기보다 크면 길이 +1 , 아니면 길이 1로 초기화
# max_len 갱신해서 가장 긴 길이 저장
# 다 확인 한 뒤에 max_len 출력

T = int(input())

for tc in range(1, T+1):
    N = int(input())  # 당근 개수
    carrots = list(map(int, input().split()))  # 당근 크기 리스트 !!!!

    max_len = 1  # 최소 길이 1
    cur_len = 1  # 연속으로 증가하는 구간 길이 

    for i in range(1, N):  #range(start, stop)
        if carrots[i] > carrots[i -1]:  # carrots[i] -> 현재 위치 당근 크기 , carrots[i-1] -> 바로 이전 당근 크기 
            # 현재 당근 크기가 이전 당근 크기보다 크면이라는 뜻인데 연속 증가는 바로 이전 원소보다 커야 한다는 뜻
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        else:
            cur_len = 1
    
    print(f"#{tc} {max_len}")