import random
i=1
money=500
ran = random.randint(0, 80)
while i<=3 or money<100 :
    num=int(input("请输入一个数字"))
    money=money-100
    i+=1
    if num == ran :
        money+=10
        print("OK")
        break
    elif num > ran :
        print("猜大了")
    else:
        print("猜小了")
    print(money, "￥")
