# 둘다 0부터 9까지의 숫자로 이루어진 배열
# 신호에서 0에서 9까지의 숫자들 중 몇개를 제외했을 때 암호와 같으면 그 암호는 신호에 포함된다고 한다.
# 신호가 암호를 포함하면 1 포함하지 않으면 0을 출력하라


T = int(input())

for tc in range(1, T + 1)
# 신호 배열 입력 (ex: 1 3 2 4 5)
signal = list(map(int, input().split()))

# 암호 배열 입력 (ex: 3 4)
code = list(map(int, input().split()))

# 두 배열을 순회할 포인터 변수
i = 0  # signal을 훑는 인덱스
j = 0  # code를 훑는 인덱스

# 신호 전체를 검사하면서 암호가 순서대로 등장하는지 확인한다.
# "부분 수열(subsequence)" 확인 문제
while i < len(signal) and j < len(code):

    # 만약 signal[i] 값이 code[j] 값과 같다면
    # 암호(code)의 다음 숫자를 찾아야 하므로 j를 증가시킨다.
    if signal[i] == code[j]:
        j += 1  # 암호의 다음 숫자를 찾는 단계로 이동

    # signal에서는 항상 다음 요소로 이동해야 하므로 i는 무조건 증가
    i += 1

# 반복이 끝난 후,
# j가 code 길이와 같다면 → code의 모든 숫자를 순서대로 찾았다는 의미 → 포함됨
if j == len(code):
    print(f"#{tc} 1")   # 포함
else:
    print(f"#{tc} 0")   # 불포함