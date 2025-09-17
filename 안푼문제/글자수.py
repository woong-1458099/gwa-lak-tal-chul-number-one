# 두 개의 문자열 str1과 str2가 주어진다. 
# 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
# 그 중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
# 딕셔너리 사용 가능

T = int(input())
for tc in range(1, T + 1):
    
    str1 = list(input())
    str2 = list(input())
    
    
    total_cnt = []
    
    for i in str1:
        counter = 0
        for j in str2:
            if i == j:
                counter += 1
        total_cnt.append(counter)


    max_k = 0
    for i in total_cnt:
        if i > max_k:
            max_k = i

    print(f"#{tc} {max_k}")
