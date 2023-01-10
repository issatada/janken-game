import random
import time

WAIT_TIME = 1
JANKEN_LISTS = {0: "グー", 1: "チョキ", 2: "パー"}
WIN = 0
DRAW = 0
LOSE = 0

print("""
じゃんけんゲーム　スタート！
3回勝負だよ！
""")

time.sleep(WAIT_TIME)

while True:
    print(JANKEN_LISTS)
    USER_HAND = int(input("0.1.2の中から選ぼう！"))
    print(f"君は{JANKEN_LISTS[USER_HAND]}を選んだよ")

    time.sleep(WAIT_TIME)

    COMPUTER_HANDS = random.randrange(0, 2)
    print(f"コンピューターは{JANKEN_LISTS[COMPUTER_HANDS]}を選んだよ")

    time.sleep(WAIT_TIME)

    result = (USER_HAND - COMPUTER_HANDS) % 3

    if result == 2:
        WIN = WIN + 1

    elif result == 1:
        LOSE = LOSE + 1

    else:
        DRAW = DRAW + 1

    print(f"{WIN}勝　{LOSE}敗　{DRAW}引き分け")

    if WIN == 3:
        print("あなたの勝ち！おめでとう！")
        break

    elif LOSE == 3:
        print("あなたの負け。")
        break

    elif DRAW == 3:
        print("引き分け")
        break

