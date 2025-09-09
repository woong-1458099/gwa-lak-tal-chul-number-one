T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 컨테이너 수, M: 트럭 수
    weight = list(map(int, input().split()))  # 컨테이너 무게
    truck = list(map(int, input().split()))   # 트럭 적재용량

    # 내림차순 정렬 (큰 것부터 매칭)
    weight.sort(reverse=True)
    truck.sort(reverse=True)

    total = 0  # 옮긴 화물 총 무게
    idx = 0    # 현재 컨테이너 인덱스

    for t in truck:  # 큰 트럭부터 순회
        while idx < N:
            if weight[idx] <= t:  # 트럭이 컨테이너를 실을 수 있으면
                total += weight[idx]
                idx += 1
                break  # 다음 트럭으로 이동
            else:
                idx += 1  # 현재 트럭에 못 싣는 컨테이너면 다음 컨테이너 확인

    print(f"#{tc} {total}")
