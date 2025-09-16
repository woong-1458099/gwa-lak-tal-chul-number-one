T = int(input())

for tc in range(1, T + 1):
    N = int(input())        # 16진수 문자열 길이 
    hex_str = input().strip()

    total = 0
    for ch in hex_str:
        total += int(ch, 16)   # 16진수 -> 10진수 변환

    print(f"#{tc} {total}")

