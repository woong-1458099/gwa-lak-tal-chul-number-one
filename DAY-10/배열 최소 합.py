def find_min_sum(row, current_sum):
    global min_sum
    
    # 가지치기: 현재 합이 이미 찾은 최소 합보다 크면 탐색 중단
    if current_sum >= min_sum:
        return
    
    # 종료 조건: 모든 행에 대해 숫자를 선택했을 때
    if row == N:
        min_sum = current_sum
        return
    
    # 재귀 호출: 현재 행에서 선택할 열을 탐색
    for col in range(N):
        # 해당 열이 아직 사용되지 않았다면
        if not visited[col]:
            visited[col] = True  # 열 사용 처리
            find_min_sum(row + 1, current_sum + arr[row][col])
            visited[col] = False # 백트래킹: 열 사용 해제

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    min_sum = float('inf')  # 최소 합을 무한대로 초기화
    visited = [False] * N    # 열 방문 여부 체크
    
    find_min_sum(0, 0)
    
    print(f"#{tc} {min_sum}")



#       문제 조건	                              코드 부분	                                   설명
# 한 줄(row)에서 하나씩 숫자를 골라야 한다	    find_min_sum(row+1, ...)	row를 하나씩 증가시키며 다음 행에서 숫자를 선택
# 같은 열(column)에서는 두 개 이상 선택 불가	visited[col] 배열	특정 열을 이미 선택했으면 다시 선택하지 못하도록 체크
# 최소 합을 구해야 한다	                       min_sum 변수	전역 최소 합을 저장하면서 더 작은 값이 나오면 갱신
# 불필요한 탐색 줄이기	                       if current_sum >= min_sum: return	이미 최소 합보다 큰 경우는 가지치기 (탐색 중단)
# 모든 행에서 숫자를 선택한 경우	            if row == N:	N행 모두 선택했을 때 현재 합으로 최소값 갱신
# 입력: T개의 테스트 케이스	                    T = int(input())
#                                              for tc in range(1, T+1):	여러 테스트 케이스를 처리
# 입력: N×N 배열	                           arr = [list(map(int, input().split())) for _ in range(N)]	N줄의 배열을 읽어서 2차원 리스트로 저장
# 출력: #테스트번호 최소합	                    print(f"#{tc} {min_sum}")	문제의 출력 형식에 맞게 결과 출력