T = int(input())  # 테스트 케이스 문제에서 3개

for tc in range(1, T+1):    # 테스트 케이스 실행

    N = int(input())  # 정수

    portals = list(map(int, input().split()))    

    # input() => 사용자로부터 문자열을 입력받음
    # .split() => 문자열을 공백(스페이스) 기준으로 잘라 리스트를 만든다
    # map(int, ...) => 리스트의 모든 요소에 int()를 적용 즉 문자열 "10", "20", "30" 을 각각 정수 10, 20, 30 으로 바꿔줌
    # list(...) => map 객체는 반복 가능한(iterable) 자료형이라 list()로 감싸주면 실제 리스트로 변환

    N_counter = [0]*N
    # 길이가 N인 리스트를 만들고, 모든 원소를 0으로 초기화
    # N_counter[0] -> 1번 방에 들어간 횟수
    # N_counter[1] -> 2번 방에 들어간 횟수
    M_counter = 0
    # 움직인 횟수를 저장하는 변수 M => Moving
    # 이동할 때마다 M_counter += 1 같은 방식으로 1씩 증가시키면 , 지금까지 몇 번 움직였는지를 알 수 있다.
    Cur_position = 1
    # 현재 내가 있는 위치를 저장하는 변수인데 1번방 부터 시작하기 때문에 =1 로 나타냄
    # counter 는 주로 몇 번 발생했는지 기록하는 용도로 쓴다.

# 조건식이 참 (True) 면 -> 블록 안의 코드 실행
# 무한 루프가 필요할 땐 while True: 를 사용하고 break 로 빠져나옴
while True:
    Cur_position = 1   # 시작할 때 1번 부터 시작하니까 현재 위치를 1로 잡음
    # = : 대입 (값을 저장) , == : 비교(값이 같은지 확인)
    Cur_position += 1  # 1번방에선 무조건 2번방으로 감
    M_counter += 1     # 이동횟수 1 오름

    if (Cur_position > 1) and (N_counter[Cur_position -1] == 0): 
        N_counter[Cur_position -1] = 1
        Cur_position = portals[Cur_position-1]
        M_counter += 1

        # Cur_position >1 : 현재 위치가 1보다 큼
        # N_counter[Cur_position -1] == 0   : 아직 그 방을 방문한 적이 없는 경우
        # Cur_position = portals[Cur_position-1] : 연결된 다음 방으로 이동
        # M_counter += 1 : 이동 횟수 1 증가
        # ---> 아직 안간 방이면 방문 표시하고, 경로에 따라 이동하는 식

    if (Cur_position >1) and (N_counter[Cur_position-1] == 1):
        N_counter[Cur_position -1] = 1
        Cur_position += 1
        M_counter += 1

        # 이미 방문한 방이면 다음 방으로 이동
        # N_counter[Cur_position-1] == 1 : 이미 그 방을 방문한 경우
        
    if Cur_position == N:
        break
        # N에 다다르면 멈춤
