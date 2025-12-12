# 스위치 개수 입력 (1 ~ 100)
N = int(input())

# 스위치 초기 상태 입력 (0: 꺼짐, 1: 켜짐)
# ex) 0 1 0 1 0 0 0 1
switches = list(map(int, input().split()))

# 학생 수 입력 (1 ~ 100)
M = int(input())

# 학생 수(M)만큼 반복하면서 각 학생의 정보(성별, 받은 수)를 처리
for _ in range(M):
    # gender : 1(남학생), 2(여학생)
    # num    : 학생이 받은 수 (1 이상, N 이하)
    gender, num = map(int, input().split())

    
    # 1. 남학생인 경우 (gender == 1)
   
    if gender == 1:
        # 남학생은 자신이 받은 수의 "배수 번호" 스위치를 모두 토글한다.
        # 스위치 번호는 1부터 시작이므로, 인덱스는 i + 1 로 맞춰서 확인.
        for i in range(N):
            # (i + 1) 이 num 의 배수이면 상태 변경
            if ((i + 1) % num) == 0:
                # 현재 값 0 -> 1, 1 -> 0 으로 토글
                # (switches[i] + 1) % 2 는 0,1을 번갈아가며 바꿈
                switches[i] = (switches[i] + 1) % 2

   
    # 2. 여학생인 경우 (gender == 2)
    
    elif gender == 2:
        # 여학생은 자신이 받은 번호(num)를 "중심"으로 하는 좌우 대칭 구간을 찾는다.
        # 리스트 인덱스로 쓰려면 0-based 로 바꿔야 하므로 -1 해준다.
        idx = num - 1

        # i는 중심에서부터 얼마나 떨어진 거리인지 나타내는 변수
        # i = 1부터 시작해서, 왼쪽(idx - i)과 오른쪽(idx + i)를 계속 비교
        for i in range(1, N - 1):
            # 왼쪽과 오른쪽 인덱스 계산
            l, r = idx - i, idx + i

            # 1) 범위 안에 있는지 확인 (0 <= l, r < N)
            # 2) 좌우 스위치 상태가 같은지 확인
            if l >= 0 and r < N and switches[l] == switches[r]:
                # 두 스위치 상태가 같으면, 양쪽 스위치를 동시에 토글
                # (switches[r] + 1) % 2 의 값을 양쪽에 같이 대입
                switches[l] = switches[r] = (switches[r] + 1) % 2
            else:
                # 범위를 벗어나거나, 좌우 상태가 다르면 대칭이 깨지는 순간이므로 즉시 종료
                break

        # 마지막으로, 중심 스위치(idx)도 토글해야 한다.
    
        switches[idx] = (switches[idx] + 1) % 2


# 최종 스위치 상태 출력
#  -> 한 줄에 최대 20개씩 출력

for i in range(N // 20 + 1):
    # 슬라이싱으로 20개씩 잘라서 출력
    # ex) N = 30 이면
    #  i = 0 -> switches[0:20]
    #  i = 1 -> switches[20:40]
    print(*switches[20 * i : 20 * (i + 1)])
