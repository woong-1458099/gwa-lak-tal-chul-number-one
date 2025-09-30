# 종료조건/가지치기 설명 주석:
# - N명의 모든 점원을 고려했을 때:
#   • 목표 높이 B 이상이면 더 이상 쌓을 필요가 없음 → 현재 높이로 정답 후보 갱신 후 반환
# - 가지의 수(재귀 분기):
#   • 현재 사람을 탑에 포함시키는 경우
#   • 포함시키지 않는 경우

def recur(idx, total_height):
    
    # idx: 현재 고려 중인 사람(인덱스)
    # total_height: 지금까지 선택한 사람들의 키 합(현재까지 탑 높이)
    # 전역변수:
    #   - min_answer: B 이상으로 달성한 높이 중 '최소 높이'(초과 최소)
    #   - N, B, heights: 문제 입력
   
    global min_answer

    # 1 종료 & 가지치기 조건 
    # 현재 높이가 B 이상이면 목표 달성 → 더 확장할 필요가 없음(추가로 쌓으면 더 커져서 손해)
    if total_height >= B:
        # 이미 찾은 답과 비교하여 더 작은 높이(즉, B를 가장 적게 초과한/딱 맞춘 값)로 갱신
        if total_height < min_answer:
            min_answer = total_height
        return  # 반드시 리턴해서 탐색 종료(가지치기)

    # 모든 사람(N명)을 다 고려했다면 더 이상 선택할 사람이 없으므로 종료
    if idx == N:
        return

    # 2 재귀 분기(현재 idx 사람을 포함할지/말지) 

    #  현재 사람을 탑에 포함시키는 경우: total_height에 heights[idx]를 더함
    recur(idx + 1, total_height + heights[idx])

    #  현재 사람을 포함시키지 않는 경우: 높이 변동 없이 다음 사람으로
    recur(idx + 1, total_height)
    # 두 가지 경우를 모두 탐색하여 min_answer를 갱신
  
    

T = int(input())  # 테스트 케이스 수 입력

for tc in range(1, T + 1):
    N, B = map(int, input().split())           # N: 사람 수, B: 목표 높이(최소로 달성해야 할 기준)
    heights = list(map(int, input().split()))  # 각 사람의 키(양의 정수)

    # '아직 답을 못 찾은 상태'를 나타내기 위해 무한대에 가까운 큰 값으로 초기화
    # float('inf')는 파이썬에서 수학적 "무한대"를 표현하는 특수한 실수 값
    min_answer = float('inf')

    # 0번째 사람부터, 현재 높이 0에서 시작
    recur(0, 0)

    # min_answer가 B 이상이므로, '초과분'은 (min_answer - B)
    # 문제 출력 포맷에 맞춰 테스트 케이스 번호와 함께 출력
    print(f'#{tc} {min_answer - B}')
