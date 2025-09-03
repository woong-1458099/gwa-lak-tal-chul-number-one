T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):
    N = int(input())  # N 입력
    seen = set()      # 지금까지 본 숫자들을 저장할 집합
    k = 0             # 몇 번 양을 셌는지 (배수 카운트)

    # 0~9 숫자가 다 나올 때까지 반복
    while len(seen) < 10:
        k += 1
        number = k * N  # k번째 N의 배수
        for digit in str(number):  # number ex)2590 -> str(number) ex)"2590" 이러면 '2','5','9','0,' 하나씩 꺼낼 수 있음
            seen.add(digit)        # 집합에 추가 (중복 자동 처리) append 쓰면 중복생길 수 있음

    print(f"#{tc} {k*N}")  # k번째 배수 번호 출력