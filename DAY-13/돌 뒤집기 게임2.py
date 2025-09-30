T = int(input())  # 테스트 케이스 수를 입력받음

for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 돌 개수(배열 길이), M: 뒤집기 연산의 횟수
    stones = list(map(int, input().split()))  # 초기 돌 상태(0 또는 1로 구성된 길이 N의 배열)
    
    # M번의 연산을 차례대로 수행
    for p in range(M):
        i, j = map(int, input().split())  # i: 중심 위치(1-indexed), j: 확장 가능한 최대 거리(반지름 같은 의미)
        i -= 1  # 파이썬 리스트는 0-index이므로, 문제에서 1-index로 준 i를 0-index로 변환

        # k를 1부터 j까지 늘려가며, 중심 i를 기준으로 양옆으로 k칸 떨어진 두 칸(left/right)을 비교
        for k in range(1, j+1):
            left = i - k   # 중심에서 왼쪽으로 k칸
            right = i + k  # 중심에서 오른쪽으로 k칸

            # 인덱스가 범위를 벗어나면 더 이상 확장 불가 -> 반복 중단
            if left < 0 or right >= N:
                break
            
            # 양끝이 "대칭" 조건(같은 값)일 때만 둘 다 뒤집음
            if stones[left] == stones[right]:
                # 같으면 둘 다 뒤집기 (비트 XOR 1: 0->1, 1->0)
                stones[left] ^= 1
                stones[right] ^= 1
            # else:
            #     (현재 코드는 다르면 아무것도 하지 않고 다음 k로 넘어감.
            #      만약 "대칭이 깨지는 순간 더 확장도 중단"이 의도라면 여기서 break 하는 편이 맞다.)
                # break

    # 최종 결과를 그대로 출력(리스트 형태). 문제 포맷에 따라 공백으로 출력하려면 수정 필요.
    print(f"#{tc} {stones}")

    # ^ : 두 비트가 다르면 1, 같으면 0  XOR 이네 ..


    # a ^= b 는 a = a ^ b 와 같아

    # x ^= 1 동작

    # x = 0 일 때 -> 0 ^ 1 = 1

    # x = 1 일 때 -> 1 ^ 1 = 0
    # stones[left] 값이 0이면 1로 바뀌고, 1 이면 0으로 바뀜. 즉 좌우 돌 색을 반대로 뒤집는다는 뜻

