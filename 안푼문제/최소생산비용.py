T = int(input())

def perm(idx, selected, now_cost):
    global min_cost
# idx : 공장의 번호
# selected : 내가 지금까지 생산한 제품 번호 모음
# now_cost : 현재 단계까지 선택한 공장들의 비용 합
# idx번 공장에서 생산할 제품을 고르는 것


    if now_cost >= min_cost:
        return
    # 가지치기 -> 현재 단계 까지 계산한 비용 now_cost가 이전에 내가 계산한 최소 비용 min_cost보다 큰 경우,
    # 답이 될 가능성이 없으므로 현재의 재귀 호출을 return으로 즉시 종료하여 불필요한 연산을 줄인다.
  

    if idx == N:
        min_cost = now_cost
        return
    # 종료 조건 -> N개의 공장이므로 N-1번까지니까 idx N번 공장은 없음 따라서 return


    for j in range(N):
        if j not in selected:
            selected.append(j)
            perm(idx+1, selected, now_cost + arr[j][idx])
            selected.pop()
    # 재귀호출 (다음단계)
    # idx번 공장에서 생산할 제품을 선택 ( 최대 N개까지) , 제품번호 j
    # j 번 제품을 이전에 생산한 적이 없으니 생산해보고 비용추가(new_cost 변수가 정의되지 않았던 부분 수정) perm호출이 끝난 후 , j번 제품 경로 안의 탐색이 끝났으니
    # selected.pop()은 방금 추가했던 j번 제품을 리스트에서 제거하여, 다음 for반복문 (j+1 일 때)에서 selected 리스트가 깨끗한 상태로 유지되도록 한다. -> 다시 시작할거니까 깔끔하게 리스트 비우고 새로 시작

for tc in range(1 , T + 1):

    N = int(input())
    # 제품 / 공장 개수

    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr[i][j] -> i번 제품을 j번 공장에서 생산하는 비용

    min_cost = 15 * 100
    # 문제에서 원하는 최소 값

    perm(0, [], 0)  # perm(idx+1, selected, new_cost)
    # 현재 어떤 공장에서 제품을 생산할지 나타내는 인덱스 idx = 0:
    # 지금까지 어떤 제품들이 생산되었는지 저장하는 리스트 selsected = []
    # 현재까지 누적된 생산 비용 now_cost - 0
    # " 0 번 공장에서 부터 시작해서, 아직 선택된 제품이 없는 상태에서, 현재까지의 비용은 0으로 두고 탐색을 시작해라"
    

    print(f"#{tc} {min_cost}")


# NxN 비용 행렬에서
# 각 "행(공장)"에서 하나씩 "열(제품)"을 골라
# 세로(같은 제품) 중복 없이 총 비용의 최소값을 구한다.

def find_min_sum(row, current_sum):
    """row번째 공장부터 배정하며 최소 비용을 갱신하는 백트래킹 함수"""
    global min_sum, N, cost, visited

    # 가지치기: 지금까지의 합이 이미 최소값 이상이면 더 볼 필요 없음
    if current_sum >= min_sum:
        return

    # 모든 공장에 제품 배정을 끝냈다면 최소값 갱신
    if row == N:
        min_sum = current_sum
        return

    # row번째 공장에 배정할 제품(col)을 하나씩 시도
    for col in range(N):
        if not visited[col]:            # 아직 배정 안 된 제품만 선택
            visited[col] = True         # 제품 col 배정
            find_min_sum(row + 1, current_sum + cost[row][col])
            visited[col] = False        # 백트래킹(원상복구)

# ===== 메인 =====
T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    cost = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')  # 최소 비용 초기값(아주 크게)
    visited = [False] * N   # 각 제품이 이미 배정되었는지 표시

    find_min_sum(0, 0)      # 0번 공장부터 시작, 현재 합 0

    print(f"#{tc} {min_sum}")


