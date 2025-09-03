T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
 
    d = {2:0, 3:0, 5:0, 7:0, 11:0} # 딕셔너리, key : 2, 3, 4, 7, 11 -> 소인수
    # value : 0으로 초기화 소인수가 곱해진 수 만큼 더해짐
 
    for num in d.keys():
        while N % num == 0: # N이 num으로 나누어 떨어지는 동안 반복
            d[num] += 1
            N //= num
    print(f"#{tc}", end=" ")
    print(*d.values())