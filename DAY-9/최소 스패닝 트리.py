# Kruskal + Union-Find (요약)
# - Kruskal 알고리즘: 모든 간선을 가중치 오름차순으로 정렬한 뒤,
#   가장 가벼운 간선부터 선택하여 사이클이 생기지 않으면 MST에 포함.
# - Union-Find: 서로소 집합 자료구조를 이용해 두 정점이 같은 연결요소(집합)에 있는지 빠르게 검사하고 합침.
# - 최적화: 경로 압축(path compression) + union by rank 를 사용하면 거의 상수에 가까운 시간으로 동작.
# - 시간복잡도: 간선 정렬 O(E log E) + Union-Find 오브 연산들 ≈ O(α(V)) 이므로 주어진 한도(V<=100k, E<=200k)에 적합.
# - 주의: 입력 정점 번호를 1..V로 가정(문제 대부분이 1-indexed). 0-index인 경우 약간 수정 필요.

import sys                                  # 표준입출력 및 빠른 입력을 위해 sys 모듈 불러오기
input = sys.stdin.readline                  # 입력 속도 향상을 위해 input 변수 재정의

# find 함수: 경로 압축을 포함한 대표(root) 찾기
def find(x):                                # 함수 정의: x의 대표(루트)를 반환
    while parent[x] != x:                   # 루트가 될 때까지 반복
        parent[x] = parent[parent[x]]       # 경로 압축: 조부모를 직접 가리키게 하여 트리 높이 감소
        x = parent[x]                       # 한 단계 위로 이동
    return x                                # 최종 루트 반환

# union 함수: 두 집합을 합침 (union by rank)
def union(a, b):                            # 함수 정의: a와 b의 집합을 합치고 성공 여부 반환
    ra = find(a)                            # a의 루트 찾기
    rb = find(b)                            # b의 루트 찾기
    if ra == rb:                            # 이미 같은 집합이면 합칠 필요 없음
        return False                        # 합치지 않음, False 반환
    # rank(깊이 비율) 를 이용해 낮은 쪽을 높은 쪽에 붙임
    if rank_arr[ra] < rank_arr[rb]:         # ra의 rank가 더 작으면
        parent[ra] = rb                     # ra를 rb 아래로 붙임
    elif rank_arr[ra] > rank_arr[rb]:       # ra의 rank가 더 크면
        parent[rb] = ra                     # rb를 ra 아래로 붙임
    else:                                   # rank가 같으면
        parent[rb] = ra                     # rb를 ra 아래로 붙이고
        rank_arr[ra] += 1                   # ra의 rank를 1 증가
    return True                             # 합치기 성공, True 반환

# 테스트케이스 수 읽기
T = int(input().strip())                    # 테스트케이스  T

for tc in range(1, T + 1):                  # 각 테스트케이스 반복
    V, E = map(int, input().split())        # 정점 개수 V, 간선 개수 E 읽기 

    edges = []                              # 간선 정보를 담을 리스트 초기화
    for _ in range(E):                      # E개의 간선 정보를 입력받음
        A, B, C = map(int, input().split()) # 정점 A, 정점 B, 가중치 C 읽기
        edges.append((C, A, B))             # (가중치, 정점A, 정점B) 형태로 저장 -> 가중치 기준 정렬 용이

    edges.sort()                            # 간선들을 가중치 오름차순으로 정렬

    parent = [i for i in range(V + 1)]      # 부모 테이블 초기화: 0..V (1-indexed 사용), parent[i]=i
    rank_arr = [0] * (V + 1)                # rank(트리 높이) 초기화 배열

    mst_weight = 0                          # MST 총 가중치 누적 변수 초기화
    cnt = 0                                 # 선택한 간선 수 (V-1이 되면 종료)

    for w, a, b in edges:                   # 가중치가 작은 간선부터 순회
        if union(a, b):                     # a와 b가 다른 집합이면 합치고 True 반환
            mst_weight += w                 # 선택된 간선의 가중치를 누적
            cnt += 1                        # 선택한 간선 수 증가
            if cnt == V - 1:                # MST 완성 조건 (정점이 V개면 간선은 V-1개)
                break                       # 반복문 종료

    print(f"#{tc} {mst_weight}")            
