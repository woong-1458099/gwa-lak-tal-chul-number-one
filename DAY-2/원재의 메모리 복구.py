T = int(input())  # 테스트 케이스 개수

for tc in range(1, T + 1):
    memory = input().strip()  # 원래 메모리 값 걍 째서 나열
    count = 0  # 수정 횟수
    current = "0"  # 처음 상태는 모두 0이니까 시작값도 0

    for bit in memory:
        if bit != current:  # ! -> "같지 않다" 라는 의미의 비교 연산자 지선생 참조
            count += 1
            current = bit  # 이제부터는 이 값으로 덮어씌워짐

    print(f"#{tc} {count}")