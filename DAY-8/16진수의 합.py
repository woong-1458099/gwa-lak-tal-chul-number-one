T = int(input())

for tc in range (1, T + 1):
    N = int(input())  # 16진수 문자열 길이
    hex_str = input().strip() # 16 진수 -> hex 

    # str.strip() : 문자열 앞뒤(좌우)에 있는 공백 문자를 제거해 준다.
    # " A3 A3 A3 "  -> ["A3", "A3", "A3" ]
    # str.split() : 문자열 전체를 하나로 다루는 메서드 리스트로 쪼개지지
    # 않고 문자열 자체만 정리 , 앞뒤 공백 제거할 때 사용

    total = 0 # 합을 구하는 변수
    for ch in hex_str:
        total += int(ch, 16)  # 16 진수 -> 10 진수 변환

    print(f"#{tc} {total}")

