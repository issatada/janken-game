import random
import time

waittime=1
janken_list=["グー", "チョキ", "パー"]

print("じゃんけんゲーム　スタート！")

time.sleep(waittime)

print("グー=0, チョキ=1, パー=2")
userhand= int(input("0.1.2の中から選ぼう！"))
print(f"君は{janken_list[userhand]}を選んだよ")

time.sleep(waittime)

computerhand = random.randrange(0, 2)
print(f"コンピューターは{janken_list[computerhand]}を選んだよ")

time.sleep(waittime)

reselts=(0, 1, 2)
win=str(2)
rose=str(1)

reselt = (userhand-computerhand) % 3


if reselt == win:
      print("あなたの勝ち！")

elif reselt == rose:
      print("あなたの負け。\nもう一1戦!")

else:
      print("あいこ\nもう1戦！")
