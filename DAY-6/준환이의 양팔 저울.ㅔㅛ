T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counterweights = list(map(int, input().split()))
    counterweights.sort(reverse=True)
    fact = [1] * (N + 1)
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i
    pow2 = [1] * (N + 1)
    for i in range(1, N + 1):
        pow2[i] = pow2[i - 1] * 2
 
    used = [0] * N
    total = sum(counterweights)
 
    def dfs(i, left, right, rem):
        # i: 올린 개수, left/right: 각 접시에 올린 합, rem: 남은 무게 합
        if i == N:
            return 1
 
        if left >= right + rem:
            left_cnt = N - i
            return fact[left_cnt] * pow2[left_cnt]
 
        res = 0
        for k in range(N):
            if used[k] == 0:
                w = counterweights[k]
                used[k] = 1
                rem2 = rem - w
 
                # 왼쪽에 올리기: 항상 가능
                res += dfs(i + 1, left + w, right, rem2)
 
                # 오른쪽에 올리기: 올리고도 right ≤ left 유지
                if right + w <= left:
                    res += dfs(i + 1, left, right + w, rem2)
 
                used[k] = 0
        return res
 
    ans = dfs(0, 0, 0, total)
    print(f'#{tc} {ans}')