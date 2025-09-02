T = int(input())  # 첫 줄에서 테스트 케이스 개수 T 입력

for t in range(1, T + 1):  # 테스트 케이스 번호는 1부터 시작
    numbers = list(map(int, input().split()))  
    # 10개의 수를 입력 받아 정수로 변환해 리스트에 저장

    total = 0  # 합계를 저장할 변수
    for num in numbers:      # 리스트에 있는 숫자들을 하나씩 꺼내면서
        total += num         # total에 더하기

    average = total / 10     # 평균 구하기 (합계 ÷ 10)
    result = round(average)  # 소수점 첫째 자리에서 반올림한 정수로 만들기

    print(f"#{t} {result}")  # 문제에서 요구한 출력 형식
