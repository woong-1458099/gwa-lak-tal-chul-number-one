def binary_search(A, target):
    
    #리스트 A에서 값 target을 이진 탐색으로 찾되, 탐색 과정에서 왼쪽-오른쪽 구간을 번갈아 선택해야만 True 반환. (같은 방향 연속 선택은 실패 처리)
     
    left = 0
    right = len(A) - 1
    last_dir = 0  # 직전에 이동한 방향 기록 (0: 없음, -1: 왼쪽, 1: 오른쪽)
 
    while left <= right:
        mid = (left + right) // 2  # 중앙 인덱스
 
        if A[mid] == target:
            # 찾는 값 발견 -> 조건 만족
            return True
 
        elif A[mid] < target:
            # target이 오른쪽 구간에 있음
            if last_dir == 1:   # 이전에도 오른쪽이면 실패
                return False
            last_dir = 1        # 직전 방향을 오른쪽으로 기록
            left = mid + 1      # 오른쪽으로 탐색 구간 이동
 
        else:
            # target이 왼쪽 구간에 있음
            if last_dir == -1:  # 이전에도 왼쪽이면 실패
                return False
            last_dir = -1       # 직전 방향을 왼쪽으로 기록
            right = mid - 1     # 왼쪽으로 탐색 구간 이동
 
    # 끝까지 탐색했는데 값이 없는 경우
    return False
 
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N: A의 원소 수, M: B의 원소 수
    A = list(map(int, input().split()))  # 탐색 대상 배열
    B = list(map(int, input().split()))  # 찾고 싶은 값들
 
    A.sort()  # 이진 탐색 전 반드시 정렬
 
    res = 0  # 조건 만족하는 B 원소 개수
    for target in B:
        if binary_search(A, target):
            res += 1
 
    print(f'#{test_case} {res}')