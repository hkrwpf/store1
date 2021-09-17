shop = (
    ["机械革命", 15000],
    ["劳力士手表", 200000],
    ["Iphone 12X plus", 12000],
    ["lenovo PC", 6000],
    ["HUA WEI WATCH", 1200],
    ["OPPO R15", 2000],
    ["Mac PC", 15000],
    ["辣条", 2.5],
    ["老干妈", 13]
)

money = input("请输入您的余额：")
money = int(money)

mycart = []

i = 0
while i <= 20:
    for key, value in enumerate(shop):
        print(key, value)
    chose = input("请输入您想要的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        if chose > 6:
            print("您输入的商品不存在！别瞎弄！")
        else:
            if money < shop[chose][1]:
                print("对不起，穷鬼，您的钱不够！请到其他超时买东西去！")
            else:
                mycart.append(shop[chose])
                money = money - shop[chose][1]
                print("恭喜，成功添加购物车！您的余额还剩￥：", money)
    elif chose == "q" or chose == "Q":
        print("拜拜了，您嘞！欢迎下次光临！")
        break
    else:
        print("对不起，您输入有误，请重新输入！")
    i = i + 1
print("以下是您的购物小票，请拿好：")
for key, value in enumerate(mycart):
    print(key, value)
print("本次余额还剩：￥", money)
