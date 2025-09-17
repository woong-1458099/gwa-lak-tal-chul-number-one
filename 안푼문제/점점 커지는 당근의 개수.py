# 연속으로 당근의 크기가 커진 경우 그 개수를 알려준다.
# 당근의 크기가 수확한 순서로 주어질 때, 연속으로 커지는 당근의 갯수는 최대 얼마인지 
# 연속으로 커지지 않는 경우 구간의 최소 길이는 1

T = int(input())
for tc in range(1, T+1):
    carrots = list(map(int, input().split()))
    N = int(input())
    
    count_len = 1
    max_len = 1

    for i in range(1, N):
        if carrots[i] > carrots[i-1]:
            count_len += 1

            if count_len > max_len:
                max_len = count_len

        else:
            count_len = 1

    print(f"#{tc} {max_len}")
            


# T = int(input())  # 테스트 케이스 T
# for tc in range(1, T+1):  # 테스트 케이스 돌림
#     N = int(input())  # 당근의 개수 N (정수 이므로 int)
#     carrots = list(map(int, input().split()))  # 당근 리스트
        
#     max_len = 1 # 최소 길이 1 이게 어떠한 경우라도 연속으로 커지는 구간의 길이는 최소 1은 된다는 가정하에 안전한 초기값을 설정한 것
#     cur_len = 1 # 현재 길이 1 , 연속으로 커지지 않는 경우 구간의 최소 길이는 1
        
#     for i in range(1, N):
#         if carrots[i] > carrots[i-1]: # 인덱스 값에서 현재 당근 크기가 바로 이전 당근 크기보다 크면 이라는 뜻인데 -> 연속증가를 의미한다.
#             cur_len += 1 # cur_len +1 = cur_len 이전 당근 보다 크니까 1더해서 길이를 세는 카운터 역할
#             if cur_len > max_len :
#                 max_len = cur_len  # 현재 당근의 길이가 최대 길이보다 크면 현재 당근의 길이가 최대 길이이다.
#         else:  
#             cur_len = 1  # 아니면 1로 나옴
        
#     print(f"#{tc} {max_len}")
        
                