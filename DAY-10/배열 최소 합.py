# NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
# 조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
 # 예를 들어 다음과 같이 배열이 주어진다.
# 2  1  2
# 5  8  5
# 7  2  2
# 이 경우 1, 5, 2를 고르면 8로 최소가 된다.


# [입력]
#  첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
#  다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

 
# [출력]
#  각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.



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
            visited[col] = True  # 열 사용 처리 -> 이번 행에서 col(열)을 선택했다는 흔적을 남김
            find_min_sum(row + 1, current_sum + arr[row][col])  # 재귀 : 다음 행 (row+1)로 내려가서, 지금까지의 합에 이번에 고른 값을 더해 계속 탐색 -> 이번선택을 확정하고 그 다음 단계로 진행 하는 부분
            visited[col] = False # 백트래킹: 방금 선택했던 열을 원상복구 -> 바로 다음 반복에서 다른 열을 선택해보려면, 이전 선택의 흔적을 지워야 함

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