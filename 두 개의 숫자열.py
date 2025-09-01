
#  테스트 케이스 수 입력
T = int(input())  # 테스트 케이스 개수 입력
for tc in range(1, T + 1):
    N, M = map(int, input().split())  
    # N: 첫 번째 배열 길이
    # M: 두 번째 배열 길이
    A = list(map(int, input().split()))  # 첫 번째 배열
    B = list(map(int, input().split()))  # 두 번째 배열

    if N >= M:
        long_arr, short_arr = A, B  # 긴 배열: long_arr, 짧은 배열: short_arr
        L, S = N, M 
    else:                           # 항상 긴 배열을 기준으로 슬라이딩 윈도우 적용 가능
        long_arr, short_arr = B, A  # 첫 번째 배열이 두 번째 배열보다 짧을 때
        L, S = M, N

 
    max_v = -10**10  # 충분히 작은 값으로 초기화 (음수도 고려)

   
    for i in range(L - S + 1):  # 긴 배열에서 짧은 배열을 겹치며 이동
        total = 0  # 현재 위치에서의 곱셈 합 초기화

    
        for j in range(S):
            total += long_arr[i + j] * short_arr[j]
            # long_arr[i+j] 위치와 short_arr[j]를 곱해서 합산

        if total > max_v:
            max_v = total  # 더 큰 값이면 최대값 갱신

    print(f"#{tc} {max_v}")
