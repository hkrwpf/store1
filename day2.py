import random
ran = random.randint(0, 80)
i = 0
money = 500
while money >= 100 or i < 3:
    num = int(input("请输入一个数字"))
    i += 1
    money = money - 100
    if num == ran:
        money += 10
        print("OK")
    elif num > ran:
        print("猜大了")
    else:
        print("猜小了")
        break
