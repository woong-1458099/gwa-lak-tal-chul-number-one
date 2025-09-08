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