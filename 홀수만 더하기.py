T = int(input())   # 테스트 케이스 개수 입력

for t in range(1, T + 1):      # 1부터 T까지 반복
    numbers = list(map(int, input().split()))  # 10개의 수 입력
    odd_sum = 0

    for num in numbers:
        if num % 2 == 1:       # 홀수인지 확인
            odd_sum += num     # 홀수면 합계에 추가

    print(f"#{t} {odd_sum}")   # 출력 형식 맞추기
