# i번째부터 j 개의 돌을 i번째 돌의 색으로 바꿔놓는다.



T = int(input())

for tc in range(1, T+1):
    N = int(input())  # N 개의 돌

N,M = map(int, input().split())  # N개의 돌, M 개의 줄
stones = list(map(int,input().split()))

for _ in range(M):

    i,j = map(int, input().split())

    color = stones[i-1]

    for k in range(i-1, min(i-1+j, N)):
        stones[k] = color


print(f"#{tc} {' '.join(map(str, stones))}")



T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N개의 돌, M개의 뒤집기 연산
    stones = list(map(int, input().split()))  # 초기 돌 상태
    
    for _ in range(M):
        i, j = map(int, input().split())  # i번째 돌부터 j개 뒤집기
        color = stones[i-1]
        for k in range(i-1, min(i-1+j, N)):
            stones[k] = color

    # 인덱스를 이용해서 하나씩 출력
    print(f"#{tc}", end=' ')  # 테스트 케이스 번호 출력, 같은 줄 유지
    for idx in range(N):
        print(stones[idx], end=' ')  # 각 돌 출력, 공백 추가
    print()  # 한 줄 끝나면 줄바꿈