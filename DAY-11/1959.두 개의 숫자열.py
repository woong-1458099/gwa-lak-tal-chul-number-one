T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 길이가 짧은 배열 -> A , 길이가 긴 배열 -> B
    if N > M:
        N, M = M , N
        A, B = B , A

    max_m = float('-inf')
    # A를 B위에서 왼쪽 -> 오른쪽으로 한 칸씩 슬라이딩
    for i in range(M - N + 1):
        s = 0
        for j in range(N):   
            s += A[j] * B[j + 1]  # 마주보는 원소들 곱의 합
        if s > max_m:
            max_m = s

    
    print(f"#{tc} {max_m}")
             