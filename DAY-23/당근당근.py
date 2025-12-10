# 문제를 어떻게 접근해야 할까
# 우선은 핵심 요구사항을 뽑는다
# “당근을 크기 순서대로 정리해서 3개의 상자에 나누되, 각 상자엔 같은 크기의 당근만 들어야 하고, 비어있는 상자는 없어야 하며, 세 상자의 당근 개수 차이가 최소가 되어야 한다.”
# 당근 크기 -> 리스트로 표현,   비어있는 상자 없음 -> 세 그룹 모두 원소 >1
# 같은 크기끼리 묶기 -> 정렬이 기본 전제 carrots.sort() 로 시작
# 상자가 3개니까, 첫 번째 구간 끝 인덱스 = i , 두 번째 구간 끝 인덱스 = j
 
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    carrots = sorted(list(map(int, input().split()))) # sorted -> 정렬
    # ex) N=5, 입력 : 1 1 1 2 3 -> 정렬 후: [1, 1, 1, 2, 3]
    ans = float('inf')  # 최소 차이 초기값
    possible = False    # 포장 가능 여부 플래그
 
    # i: 첫 번째 구간 끝
    for i in range(N - 2):
        # 같은 크기의 당근이 구간 경계에 걸리면 불가능
        if carrots[i] == carrots[i + 1]:
            continue
 
        # j: 두 번째 구간 끝
        for j in range(i + 1, N - 1):
            if carrots[j] == carrots[j + 1]:
                continue
 
            # 각 상자별 크기 (개수)
            small = i + 1
            medium = j - i
            large = N - 1 - j
 
            # 비어있는 상자 체크
            if small == 0 or medium == 0 or large == 0:
                continue
 
            # 세 상자 크기 차이 계산
            diff = max(small, medium, large) - min(small, medium, large)
 
            ans = min(ans, diff)
            possible = True
 
    if possible:
        print(f"#{tc} {ans}")
    else:
        print(f"#{tc} -1")