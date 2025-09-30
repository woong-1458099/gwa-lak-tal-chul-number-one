
# find 함수: 경로 압축(Path Compression)을 적용한 대표(root) 찾기
def find(x):
    # parent[x]가 자기 자신이 아니면 루트가 아님 -> 루트를 찾아 올라가며 압축
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 절반 압축(할빙): 조부모를 가리키도록 갱신
        x = parent[x]
    return x

# union 함수: rank(대략 트리 높이) 기준으로 두 집합을 합치기
def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return False  # 이미 같은 집합 -> 이 간선을 선택하면 사이클 -> 채택 X

    # 랭크가 낮은 루트를 높은 루트 밑으로 붙임
    if rank_arr[ra] < rank_arr[rb]:
        parent[ra] = rb
    elif rank_arr[ra] > rank_arr[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank_arr[ra] += 1
    return True  # 합치기 성공 -> 간선 채택

# 테스트케이스 수
T = int(input().strip())

for tc in range(1, T + 1):
    # 입력: 마지막 노드 번호 V, 간선 수 E
    # 정점 집합은 {0, 1, 2, ..., V} -> 정점 개수 = V + 1
    V, E = map(int, input().split())

    edges = []  # (가중치, u, v)
    for _ in range(E):
        A, B, C = map(int, input().split())
        edges.append((C, A, B))

    # 가중치 오름차순 정렬
    edges.sort()

    # Union-Find 준비 (0..V)
    parent = [i for i in range(V + 1)]
    rank_arr = [0] * (V + 1)

    mst_weight = 0  # MST 가중치 합
    cnt = 0         # 선택한 간선 수
    need = V        # 중요: 정점이 V+1개이므로 MST 간선은 정확히 V개

    # Kruskal: 작은 간선부터 사이클이 없을 때 채택
    for w, a, b in edges:
        if union(a, b):
            mst_weight += w
            cnt += 1
            if cnt == need:  # 간선 V개를 고르면 MST 완성
                break

    print(f"#{tc} {mst_weight}")
