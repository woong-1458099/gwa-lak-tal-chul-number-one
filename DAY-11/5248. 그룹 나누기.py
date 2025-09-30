# 같은 조 개수 세기 (유니온-파인드 간단 버전)
# - 쌍 (a, b)가 나오면 a와 b의 집합을 union으로 합친다.
# - 마지막에 대표(root)가 서로 다른 집합의 개수가 "조"의 개수.


def read_k_ints(k):
   
    acc = []
    while len(acc) < k:
        acc += list(map(int, input().split()))
    return acc[:k]

def find(x):
   
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로를 절반으로 압축
        x = parent[x]
    return x

def union(a, b):
    
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if ra < rb:
        parent[rb] = ra
    else:
        parent[ra] = rb

def solve():
    T = int(input().strip())
    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        nums = read_k_ints(2 * M)      # a1 b1 a2 b2 ... aM bM

        # 부모 배열 초기화: 처음엔 각자 자기 자신이 대표
        global parent
        parent = [i for i in range(N + 1)]

        # 모든 신청 쌍 union
        for i in range(0, 2 * M, 2):
            a, b = nums[i], nums[i + 1]
            union(a, b)

        # 대표의 종류 수 = 조의 개수
        groups = set(find(i) for i in range(1, N + 1))
        print(f"#{tc} {len(groups)}")

if __name__ == "__main__":
    solve()
