import random
import time

print("じゃんけんゲーム　スタート！")

time.sleep(1)

janken_list = ["グー", "チョキ", "パー"]
print("グー=0, チョキ=1, パー=2")
u = int(input("0.1.2の中から選ぼう！"))
print(f"君は{janken_list[u]}を選んだよ")

time.sleep(1)

c = random.randrange(0,2)
print(f"コンピューターは{janken_list[c]}を選んだよ")

time.sleep(1)

reselts=[0,1,2]

reselt = (u-c) % 3

if reselt == 2:
      print("あなたの勝ち！")

elif reselt == 1:
      print("あなたの負け。\nもう一1戦!")

else:
      print("あいこ\nもう1戦！")
