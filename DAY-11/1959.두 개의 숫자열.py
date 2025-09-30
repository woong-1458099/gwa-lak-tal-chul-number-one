# N 개의 숫자로 구성된 숫자열 Ai와 M 개의 숫자로 구성된 숫자열 Bj
# Ai나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다. 단 더 긴 쪽의 양끝을 벗어나서는 안 된다.
# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 길이가 짧은 배열 -> A , 길이가 긴 배열 -> B
    if N > M:
        N, M = M, N
        A, B = B, A

    max_m = float('-inf')
    # A를 B위에서 왼쪽 -> 오른쪽으로 한 칸씩 슬라이딩
    for i in range(M - N + 1):
        s = 0
        for j in range(N):   
            s += A[j] * B[j + 1]  # 마주보는 원소들 곱의 합
        if s > max_m:
            max_m = s

    
    print(f"#{tc} {max_m}")
             