
card_count = [0] * 10

card = [1,1,1,4,5,6]

for i in range(6):
    # i번 카드의 등장 횟수를 1 증가
    card_count[card[i]] += 1

    #탐욕적인 방법으로 babygin 판단
for i in range(10):
    #숫자 i 카드를 보고
    #숫자 i 카드가 3 장 이상 => triplet

    if card_count[i] >=3:
        print("triple")

    #숫자 i 카드, i+1 카드, i+2 3장 다 1장 이상씩 있다면 => run
    elif i < 8 and card_count[i] > 0 and card_count[i+1] > 0 and card_count[i+2] > 0:
        print("run")
        