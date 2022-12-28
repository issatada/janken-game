import random
import time

print("じゃんけんゲーム　スタート！")

time.sleep(1)

janken_list = ["グー","チョキ","パー"]
print("グー=0, チョキ=1, パー=2")
u = int(input("0.1.2の中から選ぼう！"))
print(f"君は{janken_list}を選んだよ")

c = random.randrange(0,2)
print(f"コンピューターは{c}を選んだよ")

i = (u-c) % 3

if i == 1:
      print("あなたの負け")

elif i ==2:
      print("あなたの勝ち！")

else:
      print("あいこ\nもう1戦！")