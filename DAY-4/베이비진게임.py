
# card_count = [0] * 10

# card = [1,1,1,4,5,6]

# for i in range(6):
#     # i번 카드의 등장 횟수를 1 증가
#     card_count[card[i]] += 1

#     #탐욕적인 방법으로 babygin 판단
# for i in range(10):
#     #숫자 i 카드를 보고
#     #숫자 i 카드가 3 장 이상 => triplet

#     if card_count[i] >=3:
#         print("triple")

#     #숫자 i 카드, i+1 카드, i+2 3장 다 1장 이상씩 있다면 => run
#     elif i < 8 and card_count[i] > 0 and card_count[i+1] > 0 and card_count[i+2] > 0:
#         print("run")
        

        def check(card_count):
    # triplet 확인
    for i in range(10):
        if card_count[i] >= 3:
            return True

    # run 확인
    for i in range(8):  # i, i+1, i+2 확인 가능
        if card_count[i] > 0 and card_count[i+1] > 0 and card_count[i+2] > 0:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    p1_count = [0] * 10  # 플레이어1 카드 카운트
    p2_count = [0] * 10  # 플레이어2 카드 카운트
    winner = 0

    for i in range(12):
        card = cards[i]

        if i % 2 == 0:   # 짝수 → 플레이어1 차례
            p1_count[card] += 1
            if check(p1_count):
                winner = 1
                break
        else:            # 홀수 → 플레이어2 차례
            p2_count[card] += 1
            if check(p2_count):
                winner = 2
                break

    print(f"#{tc} {winner}")
