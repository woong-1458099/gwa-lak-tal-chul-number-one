T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N개의 돌, M개의 뒤집기 연산
    stones = list(map(int, input().split()))  # 초기 돌 상태
    
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1

        for k in range(1, j+1):
            left = i -k
            right = i + k

            if left < 0 or right >= N:
                break
            
            if stones[left] == stones[right]:
                # 같으면 둘 다 뒤집기
                stones[left] ^= 1  # 0->1, 1->0
                stones[right] ^= 1

    print(f"#{tc}", *stones)

    # ^ : 두 비트가 다르면 1, 같으면 0
    
    # a ^= b 는 a = a ^ b 와 같아

    # x ^= 1 동작

    # x = 0 일 때 -> 0 ^ 1 = 1

    # x = 1 일 때 -> 1 ^ 1 = 0
    # stones[left] 값이 0이면 1로 바뀌고, 1 이면 0으로 바뀜. 즉 좌우 돌 색을 반대로 뒤집는다는 뜻

