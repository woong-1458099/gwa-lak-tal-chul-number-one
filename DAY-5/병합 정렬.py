# start 에서 end 까지 정렬하는 함수
def merge_sort(start, end):
    global cnt  # 전역변수
    # 1. 종료 조건
    # 더 이상 분할이 불가능 할 때 까지
    if start == end - 1:
        # 길이가 1이면 분할 불가능
        return start, end
 
    # 2. 재귀 호출
    # 두 부분으로 나누고 합칠 때 정렬
    # 두 부분으로 나누는 기준 가운데 위치
    mid = (start + end) // 2
 
    # 왼쪽범위 정렬해 , mid 미포함
    left_s, left_e = merge_sort(start, mid)
 
    # 오른쪽범위 정렬해
    right_s, right_e = merge_sort(mid, end)
     
    # 왼쪽 마지막 원소 > 오른쪽 마지막 원소 이면 cnt 증가
    if arr[left_e - 1] > arr[right_e - 1]:
        cnt += 1
 
    # 합치면 된다.
    merge(left_s, left_e, right_s, right_e)
 
    # 합치고 나면 정렬 완료
    return start, end
 
# 주어진 범위(왼쪽, 오른쪽)으 리스트를 합치는 함수
def merge(left_s, left_e, right_s, right_e):
    # 왼쪽 범위의 제일 작은 원소의 인덱스
    l = left_s
    # 오른쪽 범위의 제일 작은 원소의 인덱스
    r = right_s
 
    # 결과로 만들어낼 배열의 길이
    N = right_e - left_s
 
    result = [0] * N
 
    # result 의 위치를 가리키는 인덱스
    idx = 0
 
    # 정렬(합치기) 시작
    # 왼쪽에서 가장 작은거, 오른쪽에서 가장 작은거
    # 둘중에 작은거 선택해서 result 의 idx 위치에 놓으면된다. idx += 1
 
    # 1. 비교할 왼쪽, 오른쪽이 둘다 남아있는 경우
    while l < left_e and r < right_e:
        if arr[l] <= arr[r]:
            # 왼쪽과 오른쪽 중에 작은거 놓기
            result[idx] = arr[l]
            l += 1
             
        else:
            result[idx] = arr[r]
            r += 1
        idx += 1
 
    # 2. 왼쪽 부분이나 오른쪽 부분에만 남아있는 경우
 
    # 2-1. 오른쪽만 남아있는 경우
    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1
 
    # 2-2. 왼쪽만 남아있는 경우
    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1
 
    # 정렬이 완료된 범위 ( left_s ~ right_e)를 원본에 반영
    for i in range(N):
        arr[left_s + i] = result[i]
 
 
# 메인 실행부
T = int(input())  # 테스트케이스 개수 입력
for tc in range(1, T + 1):
    N = int(input())  # 정수 개수
    arr = list(map(int, input().split()))  # 정렬 대상 리스트
    cnt = 0  # 조건 만족 횟수 저장 변수
 
    # 병합 정렬 실행
    merge_sort(0, N)
 
    # 출력: 정렬된 리스트에서 중간값과 cnt
    print(f"#{tc} {arr[N//2]} {cnt}")
