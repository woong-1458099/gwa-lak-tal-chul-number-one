# 크루스칼은 상호배타집합(유니온파인드) 를 통해서 사이클의 유무 파악

# V : 정점의 개수
# E : 간선의 개수
V, E = map(int, input().split())

#  크루스칼은 간선정보만 리스트로 저장
edges = []

for i in range(E):
    # s, e : 정점번호
    # w : 가중치
    s, e, w = map(int, input().split())
    edges.append((s, e, w))


# 가중치는 튜플의 2번인덱스니까 2번 인덱스 원소를 기준으로 정렬
edges.sort(key=lambda x:x[2])

# 크루스칼은 상호배타집합(유니온파인드) 를 통해서 사이클의 유무 파악
# make_set

p = [i for i in range(V)]


# x번 정점의 대표를 찾는 연산
def find_set(x):
    if p[x] == x:
        return x
    
    # x의 부모한테서 다시 대표를 찾아올라간다.
    p[x] = find_set(p[x]) # 경로압축
    return p[x]


# x가 속한 집합과 y가 속한 집합을 합치는 연산
def union(x,y):
    king_x = find_set(x)
    king_y = find_set(y)

    # x와 y 이 두 정점이 속한 집합의 대표가 같으면
    # 하나의 MST안에 속해있는거다.
    # 이거를 또 추가해버리면 사이클이 생기게 된다.
    if king_x == king_y:
        return
    
    p[king_y] = king_x

# 크루스칼 알고리즘은 인덱스 0번부터 차례대로 확인 ( 정렬이 되어있음 )
# 0번 인덱스에 있는 간선 => 가중치가 최소인 간선

for s, e, w in edges:
    # s, e 사이를 있는 간선의 가중치가 w인데
    # s, e 가 한 집합에 속해있다면, 이 간선을 추가하면 사이클이 생긴다. => MST X
    # s, e 가 한 집합에 속해있지 않다면 이 간선을 추가해도 사이클이 안생긴다. MST 0
    if find_set(s) != find_set(e):
        # s랑 e가 속한 집합을 합친다.
        union(s, e)
        print(s, e, w)
        # 간선 개수 +1
        e_cnt += 1
        # 가중치 합
        min_w += w
        # 이 간선을 추가하고 내가 지금까지 선택한 간선 개수 == V-1이면 완성 !
        if e_cnt == V - 1:
            break

print(f"최소비용 : {min_w}")