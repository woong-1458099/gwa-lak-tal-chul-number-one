# 종료조건: N명의 모든 점원을 고려했을 때
#  - 가지치기: 이미 높이가 B이상이면 더 이상 쌓을 필요 없다
# 가지의 수:
#  - 점원을 탑에 포함 시키는 경우 or 안시키는 경우
def recur(idx, total_height):
    global min_answer

    if total_height >= B:  # 가지치기: B이상이면 더 이상 쌓지 마라
        min_answer = min(min_answer, total_height)
        return

    if idx == N:  # N명을 모두 고려함
        return

    recur(idx + 1, total_height + heights[idx])  # 탑에 포함 시키는 경우
    recur(idx + 1, total_height)  # 탑에 포함 안 시키는 경우


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    # min_answer = 21e8   # 나올 수 있는 최대 범위 (정답이 항상 보장된 경우)
    min_answer = float('inf')  # 나올 수 없다면 최대 값으로
    recur(0, 0)
    print(f'#{tc} {min_answer - B}')
