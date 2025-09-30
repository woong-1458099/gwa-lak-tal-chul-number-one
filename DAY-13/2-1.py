# 2-1. 다음 길이가 10인 1차원 배열 arr 안에 가로로 1이 연속으로 있는 부분 중 가장 길이가 긴 부분은 얼마인지 구해보세요. print(7) 하면 사망
N = 10
arr = [1, 0, 1, 1, 1, 1, 1, 1, 1, 0]

max_len = 0
cnt_len = 0

for i in arr:
    if i == 1:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 0

print(max_len)