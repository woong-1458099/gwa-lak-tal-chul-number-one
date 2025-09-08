T = int(input())

for tc in range(1, T+1):
    # 화물 도크 이용 신청서 N개
    N = int(input())

    # (작업시작시간, 작업종료시간) 형태의 입력이 N줄
    work_list = [list(map(int, input().split()))for _ in range(N)]

    #  위에 있는 리스트를 끝나는 시간(e)를 기준으로
    #  끝나는 시간이 빠른것이 앞으로 오도록 정렬
    # 끝나는시간 기준 오름차순 정렬
    work_list.sort(key=lambda e: e[1])

    # 최대 작업의 개수
    cnt = 0

    # 작업 종료 시간이 빠른것부터 선택
    # 현재 작업의 시작 시간이 si라고 하면
    # 이전 작업의 끝난시간 ei-1 보다 현재 작업시작시간이 크거나 같아야한다.

    # 이전 작업 끝난시간
    last_end = 0

    for i in range(N):
        # i번 작업의 시작시간, 종료시간
        start = work_list[i][0]
        end = work_list[i][1]

    # for start, end in work_list: 이래 써도 됨
    # i 번작업은 이전 작업의 끝시간보다
    # i번 작업의 시작시간이 크거나 같아야 한다
    if start >= last_end:
        # 이 작업을 고른다
        cnt += 1
        # 이 작업이 끝나는 시간을 갱신
        last_end = end

print(f"#{tc} {cnt}")