T = int(input())  # 첫 줄에 노선 수 T 가 주어짐 (1<= T <= 50)

def drive(K,N):
    # K : 한번 충전시 이동 가능한 정류장 개수
    # N : 마지막 도착 정류장 번호

    # return 값 == 0 : 버스가 마지막 정류장에 도착하지 못함
    # return 값 > 0 : 버스가 마지막 정류장에 도착했다.

    last = 0 # 마지막에 충전한 위치
    bus = K # 버스가 최대로 움직인 위치 (초기값은 한번 최대로 이동)
    count = 0 # 충전 횟수, 시작충전은 횟수 제외

    # 버스 위치가  N보다 작으면 계속 움직여라.
    while bus < N:
        # 현재 위치에 충전기가 있는지 확인
        # 없으면 다시 한칸씩 돌아오기

        while stop_list[bus] == 0:
            bus -= 1
            if bus == last:
                return 0
        #stop_list[bus] == 1 인 곳을 만나면 반복 중단
        # 더 갈 수 있다는 것을 의미
        # 마지막 충전 위치 현재 위치로 기록
        last = bus
        # 충전했으니 충전횟수 + 1
        count += 1
        #  충전했으니 k칸 쭉 땡기기
        bus += K

    # 반복이 종료되면 충전횟수 return
    return count


    # return값 == 0 : 버스가 마지막 정류장에 도착하지못함
    # return값 > 0 : 버스가 마지막 정류장에 도착했다.
for tc in range(1,T+1):
    #  tc는 테스트 케이스 번호, 1부터 시작

    # 입력이 한줄에 3개가 들어온다는게 고정이면
    # 변수도 3개 준비해놓으면 된다.
    K, N, M = map(int, input().split())
    # K : 1번충전시 이동가능한 정류장 수
    # N : 마지막 도착 정류장 번호
    # M : 충전기 개수

    # 충전기가 있는 정류장 번호 리스트
    charger_list = list(map(int, input().split()))


    # 정류장 리스트
    stop_list = [0] * N
    # stop_list[1] == 1 : 1번 정류장에는 충전기가 있다.
    # stop_list[2] == 0 : 2번 정류장에는 충전기가 없다.

    # 충전기가 있는 정류장 번호를 확인
    for x in charger_list:
        # x번 정류장에는 충전기가 있다고 표시
        stop_list[x] = 1

    answer = drive(K, N)
    print(f"#{tc} {answer}")

    
    # 문제는 크게 두 가지 과정으로 나눌 수 있다.
    # 첫 번째 : 버스의 운행 자체를 코딩으로 나타냄
    # 두 번째 : 버스가 몇번의 충전을 해야 도착할 수 있는지 ( 첫번째 과정에서 K,N,M의 변수 3 가지 를 사용)
    # K, N 은고정값  X  , M 은 고정값