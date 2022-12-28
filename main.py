import random

u=(1,2,3)
print('''じゃんけんゲーム　スタート！"

グー=0, チョキ=1, パー=2''')
u = int(input("0.1.2の中から選ぼう！"))
print(f"君は{u}を選んだよ")

for n in range(1):
      c = random.randrange(0,2)
      print(f"コンピューターは{c}を選んだよ")

i = (u-c) % 3

if i == 1:
      print("あなたの負け")

elif i ==2:
      print("あなたの勝ち！")

else:
      print("あなたの負け")