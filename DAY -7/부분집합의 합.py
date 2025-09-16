# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 
# 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
#해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
 #예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
# 1부터 12까지의 숫자를 원소로 가진 집합 A. 
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램 작성
# 해당 하는 부분집합이 없는 경우 0을 출력
# 재귀로 풀어야 할 거 같은데.. 
# 집합 A = {1,2 , ..., 12} 
# N개 뽑아서 합이 K 인지 확인해야 함.
# "이 숫자를 뽑는다" / " 안 뽑는다 " 두 가지 선택을 계속 재귀로 내려가는 방식

# idx : 현재 보고 있는 숫자 (1 ~ 12), cnt : 지금까지 뽑은 원소 개수 , total : 지금까지 뽑은 원소의 합
# N : 목표 원소 개수 , K : 목표 합
def subset(idx, cnt, total, N, K):

    # 첫 번째 조건 : 원소 개수가 N 이고 합이 K 일때
    if cnt == N and total == K:
        return 1
    
    # 두 번째 조건 : 범위를 넘어섰거나 , 이미 원소를 다 선택했는데 조건 만족 못할때
    # 집합 A  {1, 2, ..., 12} 만 다루니까 idx가 13 이상이 되면 더 이상 뽑을 원소가 없음 -> 탐색 끝
    # 목표라 하는 부분집합의 원소 개수는 딱 N개. 따라서 지금까지 고른 원소 개수 (cnt)가 이미 N보다 많으면 실패
    # 지금까지 선택한 원소 합(total)이 이미 목표 합 (K)보다 크면 실패. 뒤에 더 큰 수만 남아 있으니 조건 만족 X
    if idx > 12 or cnt > K or total > K:
        return 0
    
    # 우리가 보고 있는 숫자가 idx 일 떄, 그 숫자르 뽑을 지 말지 두 가지 경우가 항상 존재한다.
    # 매 단계마다 뽑는다 vs 안 뽑는다 로 나눠서 재귀호출을 함
    # 현재 idx를 선택하는 경우
    # 다음 숫자로 넘어가야 하니까 -> idx+1, 원소를 하나 더 골랐으니 -> cnt + 1, 합에도 idx를 더해주니까 total + idx
    pick = subset(idx+1, cnt+1, total + idx, N, K)
    
    # 현재 idx를 선택하지 않는 경우
    # 숫자를 안 뽑았으니 원소 개수(cnt) 와 합(total)은 그대로 두고 idx만 idx + 1 로 넘어감
    not_pick = subset(idx+1, cnt, total, N, K)
    
    # 두 경우의 결과를 더해서 반환 
    # 각 재귀호출은 "조건을 만족하는 부분집합 개수"를 반환하니까, 두 경우를 합치면 전체 경우의 수가 된다.
    return pick + not_pick

T = int(input())
for tc in range(1, T +1) :
    N, K = map(int, input().split())
    ans = subset(1, 0, 0, N, K)  # subset(1, 0, 0, N, K) 는 다음 상태에서 탐색을 시작하라는 뜻
    # 아직 아무것도 고르지 않은 상태에서 1 부터 시작해 N개를 골라 합이 K 가 되는 모든 경우의 수를 세라
    # subset(idx, cnt, total, N, K)
    print(f"#{tc} {ans}")



from itertools import combinations # terable(리스트, 문자열, 집합 등)에서 원소를 중복 없이 뽑는 조합을 만들어 준다 지선생 참조
T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N개 원소, 합 K
    
    A = list(range(1, 13))  # 집합 A = {1~ 12}
    count = 0
    
    # N개의 원소를 뽑는 모든 조합
    for subset in combinations(A, N):
        if sum(subset) == K:
            count += 1
    
    print(f"#{tc} {count}")