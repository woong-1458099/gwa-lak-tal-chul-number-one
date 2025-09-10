def quick_sort(arr, left, right):
     
    if left >= right:
        return
 
    # 피벗(pivot) 선택
    #  보통 배열의 첫 번째, 마지막, 혹은 중간 값을 사용
    #   여기서는 '구간의 맨 앞 원소'를 피벗으로 사용
   
    pivot = left   # 피벗의 인덱스
    i = left + 1   # 왼쪽에서 오른쪽으로 이동하는 포인터
    j = right      # 오른쪽에서 왼쪽으로 이동하는 포인터
 
    # ----------------------------
    # 피벗을 기준으로 양쪽에서 값 비교 및 교환
    #   i: 피벗보다 큰 값을 찾을 때까지 오른쪽으로 이동
    #   j: 피벗보다 작은 값을 찾을 때까지 왼쪽으로 이동
    #   만약 i < j라면 두 값을 교환
 
    while i <= j:
        # i가 피벗보다 큰 값에 도달할 때까지 오른쪽으로 이동
        while i <= j and arr[i] <= arr[pivot]:
            i += 1
        # j가 피벗보다 작은 값에 도달할 때까지 왼쪽으로 이동
        while i <= j and arr[j] >= arr[pivot]:
            j -= 1
        # 두 값이 엇갈리지 않았다면 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 피벗과 j 위치의 값을 교환
    #    - 이렇게 하면 피벗 기준으로
    #      왼쪽은 피벗보다 작은 값들,
    #      오른쪽은 피벗보다 큰 값들로 분할됨
 
    arr[pivot], arr[j] = arr[j], arr[pivot]
 
 
    # 분할 정복 (Divide & Conquer)
    # 왼쪽 구간 [left ~ j-1] 재귀적으로 정렬
    # 오른쪽 구간 [j+1 ~ right] 재귀적으로 정렬
 
    quick_sort(arr, left, j - 1)   # 왼쪽 부분 배열 정렬
    quick_sort(arr, j + 1, right)  # 오른쪽 부분 배열 정렬
 
T = int(input())  # 테스트 케이스 수 입력
for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기 입력
    arr = list(map(int, input().split()))  # 배열 입력 받기
 
    # 퀵 정렬 실행 (배열 전체 범위)
    quick_sort(arr, 0, N - 1)
 
    # 정렬 완료 후, N//2번째 값 출력
    print(f"#{tc} {arr[N//2]}")