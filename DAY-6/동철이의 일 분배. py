# 테스트 케이스 수 입력
T = int(input().strip())

for tc in range(1, T + 1):
    # N: 직원 수, 즉 해야 할 일 수
    N = int(input().strip())
    # P[i][j]: i번 직원이 j번 일을 성공할 확률(퍼센트)
    P = [list(map(int, input().split())) for _ in range(N)]

    # DP 배열 크기: 2^N
    # dp[mask] = mask 상태에서 배정된 일들에 대해 최대 성공 확률 곱
    size = 1 << N
    dp = [0.0] * size
    dp[0] = 1.0  # 초기 상태: 아무 일도 배정되지 않음, 확률 곱은 1

    # mask: 어떤 일이 이미 배정되었는지를 비트로 표현
    for mask in range(size):
        # 현재 상태의 확률이 0이면 스킵
        if dp[mask] == 0.0:
            continue

        # mask에서 배정된 일 수 = 다음으로 배정할 직원 인덱스
        # Python 3.10 이상이면 bit_count() 사용 가능, 아니면 bin(mask).count('1') 사용
        if hasattr(mask, "bit_count"):
            k = mask.bit_count()   # 다음 배정할 직원(0-based)
        else:
            k = bin(mask).count("1")

        # 다음 배정할 직원이 아직 N명 미만이면
        for j in range(N):
            # j번 일이 아직 배정되지 않은 경우
            if not (mask & (1 << j)):
                # 새로운 상태: j번 일을 배정
                newmask = mask | (1 << j)
                # 성공 확률 곱 계산
                prob = dp[mask] * (P[k][j] / 100.0)
                # 기존 dp[newmask]보다 크면 갱신
                if prob > dp[newmask]:
                    dp[newmask] = prob

    # 모든 일이 배정된 상태: mask = (1<<N)-1
    # 퍼센트 단위로 변환
    result_percent = dp[size - 1] * 100.0
    # 소수점 6자리까지 반올림 출력
    print(f"#{tc} {result_percent:.6f}")
