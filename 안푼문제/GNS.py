# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 이게 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아
# 작은 수부터 차례로 정렬하여 출력하는 프로그램 작성
# 테스트 켕스 길이, 단어의 갯수 -> 

T = int(input())
for tc in range(1, T + 1):
    tc_num, N = input().split()   # 예: "#1 10"
    N = int(N)                    # 문자열 → 정수 변환
    arr = input().split()         # 실제 데이터 (길이 N개)

    # 숫자 문자열의 순서 (고정)
    num_words = ["ZRO", "ONE", "TWO", "THR", "FOR", 
                 "FIV", "SIX", "SVN", "EGT", "NIN"]

    # 카운트 배열 준비
    count = [0] * len(num_words)

    # 등장 횟수 세기
    for word in arr:
        for i in range(len(num_words)):
            if word == num_words[i]:
                count[i] += 1
                break

    # 출력
    print(tc_num)   # 테스트케이스 번호 출력
    for i in range(len(num_words)):
        print((num_words[i] + " ") * count[i], end="")
    print()
