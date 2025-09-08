# 1.
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

    
# 2.
    T = int(input())

def solve():
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))

    stops = [0] * (N + 1) # [0] -> 0이라는 값을 가진 요소 하나를 만들고 * (N+1) 이 리스트를 N+1번 반복하면 결과적으로 [0, 0, 0, ...] 와 같이 0으로 채워진 리스트를 만드는데, 이 리스트의 총 길이는 N+1이다.
    							# 버스 정류장은 1번부터 N번까지 있지만 파이썬 리스트의 인덱스는 0부터 시작한다. 따라서 1번정류장을 stops[1]에 N 번 정류장을 stops[N}에 매핑하려면, 리스트의 크기가 N+1 이 되어야 한다.
    for c in chargers: # chargers 리스트에 담긴 충전기 위치들을 stops 리스트에 표시하는 역할
        stops[c] = 1  # stops 리스트에서 충전기가 있는 위치의 값은 1로, 충전기가 없는 위치는 0으로 표시된다 . ㄷㄷ

    current_pos = 0 # 버스의 현재 위치 0번 정류장(출발지)에서 출발하므로 시작 위치를 0으로 설정
    charge_count = 0 # 충전횟수를 세는 변수를 0으로 초기화. 아직 한 번도 충전하지 않았기 때문

    while current_pos + K < N: # 버스가 종점(N)에 도착하지 않았을 때만 계속 실행 K : 한번 충전으로 갈 수 있는 최대 거리, current_pos : 현재 버스가 있는 위치
        # 최대 거리 K 만큼 이동
        next_pos = current_pos + K

        # 최대 거리에서 가장 가까운 충전소를 찾음
        found_charger = False # 충전소를 찾았는지 여부를 표시하는 boolean 변수. 초기에는 찾지 못했기 떄문에 False 로 설정
        while next_pos > current_pos: # 버스가 최대한 갈 수 있는 거리 (next_pos) 부터 뒤로 한 칸씩 이동하면서 충전소를 찾는다. 루프의 조건은 버스가 현재 위치까지 오기 전까지만 탐색한다는 뜻
            if stops[next_pos] == 1: # 혀재 위치(next_pos)에 충전소가 있는지 확인, 만약 충전소가 있다면 (1로 표시되어 있다면) 
                current_pos = next_pos # 벗의 현재 위치를 이 충전소로 옮긴다.
                charge_count += 1 # 충전 횟수를 1 증가시킨다.
                found_charger = True # 충전소를 찾았으니 True로 변경하고
                break # 충전소를 찾았으니 더 이상 탐색할 필요가 없어 루프를 빠져나온다.
            next_pos -= 1 # 충전소가 없을 경우, 한 칸 뒤로 이동하여 다시 탐색

        # 다음 충전소로 갈 수 없을 때 , 예외상황을 처리하기 위한 코드
        if not found_charger: # 충전소를 못찾음 -> 버스가 최대한 갈 수 있는 거리 (K) 내에 충전소가 없음. 버스는 더 이상 앞으로 나아갈 수 없고, 종점까지 도착하는 것이 불가능
            return 0 # return 0 을 실행하여 solve 함수를 즉시 종료하고 0을 반환 -> 문제의 조건상, 버스가 종점에 도달할 수 없으면 충전횟수(answer)는 0이 되어야 한다.
    
    return charge_count # 지금까지 누적된 총 충전 횟수를 반환 -> 버스가 종점까지 가기 위해 최소한으로 충전해야 했던 횟수

for tc in range(1, T + 1): 
    result = solve() # 테스트 케이스의 수만큼 solve() 함수를 반복 실행하고 결과를 출력하는 역할
    print(f"#{tc} {result}")
