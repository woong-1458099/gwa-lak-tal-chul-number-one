T = int(input())  # 테스트 케이스 개수 입력

grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

for t in range(1, T + 1):
    N, K = map(int, input().split())  # N: 학생 수, K : 학점을 알고 싶은 학생 번호
    scores = []  # 각 학생의 총점을 저장할 리스트

    for i in range(N): # 학생 수만큼 반복해서 점수 입력 받기
        mid, final, hw = map(int, input().split())  # 중간, 기말 , 과제 
        total = mid * 0.35 + final * 0.45 + hw * 0.20  # 중간 35% 기말 45% 과제 20%
        scores.append(total)  # 학생 번호는 굳이 필요 없음, 점수만 저장

    target_score = scores[K - 1]  # K번째 학생 점수
    sorted_scores = sorted(scores, reverse=True)  # 내림차순 정렬
    group_size = N // 10 # 10 명씩 같은 학점 

    # K번째 학생 점수가 몇 번째 인덱스인지 찾기
    for i in range(N):
        if sorted_scores[i] == target_score:
            grade_index = i // group_size
            result = grades[grade_index]
            break

    print(f"#{t} {result}")

