# 정곤이의 꿈
def is_monotone(num):
    s = str(num)
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:  # 앞자리보다 작아지면 단조 증가 아님
            return False
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_val = -1  # 단조 증가 수 없으면 -1 출력

    # 모든 쌍 확인 (브루트포스)
    for i in range(N):
        for j in range(i + 1, N):
            product = arr[i] * arr[j]
            if is_monotone(product):
                max_val = max(max_val, product)

    print(f"#{tc} {max_val}")
