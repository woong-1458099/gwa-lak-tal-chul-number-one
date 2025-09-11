T = int(input().strip())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    boxes = [0] * (N + 1)   # 1번부터 N번까지 쓰기 위해 N+1 크기로 생성

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            boxes[j] = i    # 범위 [L, R]을 i로 변경

    # 출력 형식 맞추기
    print(f"#{tc}", *boxes[1:])
