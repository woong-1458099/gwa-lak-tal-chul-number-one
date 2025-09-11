T = int(input())

# idx : 단계, 이문제에서는 공장의 번호
# selected : 내가 지금까지 생산한 제품 번호 모음
# now_cost : 현재 단계까지 선택한 공장들의 비용 합
# idx번 공장에서 생산할 제품을 고르는 것
def perm(idx, selected, now_cost):
    global min_cost
    

    # 가지치기를 하면 불필요한 연산을 줄일 수 있다. 
    # 현재 단계까지 계산한 비용 now_cost가
    # 이전에 내가 계산한 최소 비용 min_cost 보다 큰 경우, 답이 될 가능성이 없다.
    # 더 이상 탐색할 필요 없이 현재의 재귀 호출을 즉시 종료(return) 하여 불필요한 연산을 줄인다 
    if now_cost >= min_cost:
        return
    
    
    # 종료 조건
    if idx == N: # N개의 공장이니까 N-1번까지 idx N번 공장은 없음 따라서 return
        # 원래 코드에서는 min_cost = min(now_cost, min_cost)였지만,
        # 가지치기 로직 덕분에 now_cost는 항상 min_cost보다 작으므로 바로 할당해도 됨
        min_cost = now_cost
        return
    # 재귀 호출(다음단계)
    # idx번 공장에서 생산할 제품을 선택
    # 선택할 수 있는 가지 수 최대 N개
    # 0~ idx-1 번 공장에서 생산했던 제품은 선택 불가
    # 제품 번호 j
    for j in range(N):
        # idx 번 공장에서 j번 제품 생산  , 모든 경우의 수를 하나씩 탐색하겠다는 의미
        if j not in selected:
            # j번 제품을 이전에 생산한 적이 없으면 해보자
            selected.append(j)
            # j번 제품을 idx번 공장에서 생산했으니 비용 추가
            # new_cost 변수가 정의되지 않았던 부분 수정
            # 다음 재귀 호출에 누적된 비용을 바로 전달
            perm(idx + 1, selected, now_cost + arr[j][idx])
            # j번 제품 생산 기록 취소
            selected.pop()
            # perm 함수 호출이 끝나고 이 줄로 돌아왔다는 것은 , j번 제품 경로 안의 탐색이 끝났음을 의미
            # selected.pop()은 방금 추가했던 j번 제품을 리스트에서 제거하여, 다음 for반복문 (j+1 일 때)에서 selected 리스트가 깨끗한 상태로 유지되도록 한다.
for tc in range(1, T + 1):
    # 제품 / 공장 개수
    N = int(input())

    # 생산비용 표
    # arr[i][j] => i번 제품을 j 번 공장에서 생산하는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 (최소) 값
    min_cost = 15 * 100

    # 공장순서는 고정 시켜놓고 제품 순서만 바꿔서 순열을 만들고
    # 공장에서 생산하는 제품의 생산 비용을 모두 계산해서 합친 후 그 중 최소를 구하면 된다.
    
    perm(0,[],0) # perm(idx+1, selected, new_cost)
    # 현재 어떤 공장에서 제품을 생산할지 나타내는 인덱스 idx = 0:
    # 지금까지 어떤 제품들이 생산되었는지 저장하는 리스트 selsected = []
    # 현재까지 누적된 생산 비용 now_cost - 0
    # " 0 번 공장에서 부터 시작해서, 아직 선택된 제품이 없는 상태에서, 현재까지의 비용은 0으로 두고 탐색을 시작해라"
    

    print(f"#{tc} {min_cost}")