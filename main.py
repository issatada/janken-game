import random
import time

WAIT_TIME = 1
JANKEN_LISTS = {"グー": 0, "チョキ": 1, "パー": 2}

for HANDS in JANKEN_LISTS.items()

print("じゃんけんゲーム　スタート！")

time.sleep(WAIT_TIME)
print(JANKEN_LISTS)
print("グー=0", "チョキ=1", "パー=2")
USER_HAND = int(input("0.1.2の中から選ぼう！"))
print(f"君は{JANKEN_LISTS[USER_HAND]}を選んだよ")

time.sleep(WAIT_TIME)

COMPUTER_HANDS = random.randrange(0, 2)
print(f"コンピューターは{JANKEN_LISTS[COMPUTER_HANDS]}を選んだよ")

time.sleep(WAIT_TIME)

result = (USER_HAND - COMPUTER_HANDS) % 3
WIN = int(2)
ROSE = int(1)

if result == WIN:
    print("あなたの勝ち！")

elif result == ROSE:
    print("あなたの負け。\nもう一1戦!")

else:
    print("あいこ\nもう1戦！")
