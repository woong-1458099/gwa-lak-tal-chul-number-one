# 입력: T
# 각 테스트케이스: D A B F
# 출력: #t <distance> (절대/상대오차 1e-6 허용)

T = int(input().strip())
for tc in range(1, T + 1):
    # D: 두 기차 전면부 사이 거리
    # A: 기차 A 속력
    # B: 기차 B 속력
    # F: 파리 속력
    D, A, B, F = map(int, input().split())

    # 기차들이 충돌할 때까지 걸리는 시간 = D / (A + B)
    time_until_collision = D / (A + B)

    # 파리가 이동한 거리 = 파리 속력 * 시간
    distance = F * time_until_collision

    # 출력: 요구되는 형식으로 (충분한 소수 자리로 출력)
    print(f"#{tc} {distance:.10f}")
