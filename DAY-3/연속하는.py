T = int(input())  # 테스트케이스 개수 입력
 
for tc in range(1, T + 1):
    N = int(input())  # 수열의 길이
    sequence = input().strip()  # 0과 1로 된 문자열 입력
     
    max_count = 0  # 지금까지 나온 연속 1의 최대 길이
    current_count = 0  # 현재 연속된 1의 개수
     
    for bit in sequence:
        if bit == '1':  # 1이면 연속 카운트 증가
            current_count += 1
            max_count = max(max_count, current_count)  # 최댓값 갱신
        else:  # 0이면 연속이 끊김
            current_count = 0
     
    print(f"#{tc} {max_count}")