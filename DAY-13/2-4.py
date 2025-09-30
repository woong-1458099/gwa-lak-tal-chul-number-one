# 2-4. 다음 길이가 20인 1차원 배열 arr안에 서로 대칭인 부분 중 가장 길이가 긴 부분은 얼마인지 구해보세요.
N = 20 
arr = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0]

max_len = 1 # 최소 길이 1 ( 자기 자신 )
center = 0  # 중심

for i in range(N):
    radius = 0  # 중심에서의 길이 ( c- radius -> 왼 c + radius -> 오 )
    while True:
        Left = i - radius
        Right = i + radius
        
        if Left < 0 or Right >= N:  # 범위를 벗어나면 중단
            break

        if arr[Left] != arr[Right]:  # ! 로 대칭 표현, 양옆이 다르면 대칭이 아닌거니까 중단
            break

        cur_len = 2 * radius + 1  # 길이 갱신
        if cur_len > max_len:
            max_len = cur_len
            center = i
        
        radius += 1    # radius = radius + 1

print(max_len)