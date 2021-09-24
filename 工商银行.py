import random
bank = {11584936:  {
        "username": "张三",
        "password": 123456,
        "country": "中国",
        "province": "河北",
        "street": "中兴路",
        "gate": "s002",
        "money": 100}, 15446064: {
        "username": "李四",
        "password": 147258,
        "country": "中国",
        "province": "河北",
        "street": "中兴路",
        "gate": "s008",
        "money": 0}}
bank_name = "中国工商银行昌平回龙观支行"

def welcome():
    print("**********************************")
    print("*       中国工商银行昌平支行         *")
    print("**********************************")
    print("* 1.开户                         *")
    print("* 2.存钱                         *")
    print("* 3.取钱                         *")
    print("* 4.转账                         *")
    print("* 5.查询                         *")
    print("* 6.bye                         *")
    print("**********************************")

# def bank_addUser(account,username,password,country,province,street,gate,money):
#     if len(bank) >= 100:
#         return 3
#
#     if username in bank:
#         return 2
#
#     bank[account] = {
#         "username": username,
#         "password": password,
#         "country": country,
#         "province": province,
#         "street": street,
#         "gate": gate,
#         "money": money,
#         "bank_name": bank_name
#     }
#     return 1

def addUser():
    username = input("请输入您的用户名：")
    password = int(input("请输入您的开户密码："))
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))

    account = random.randint(10000000, 99999999)
    if len(bank) >= 100:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif username in bank:
        print("对不起，该用户已存在！请勿重复开户！")
    else:
        bank[account] = {
            "username": username,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "gate": gate,
            "money": money,
            "bank_name": bank_name
        }
        print("开户成功！以下是您的个人开户信息")
        info = '''
                    ----------个人信息------
                        用户名：%s
                        密码：%s
                        账号：%s
                        地址信息
                            国家：%s
                            省份：%s
                            街道：%s
                            门牌号: %s
                        余额：%s
                        开户行地址：%s
                        ------------------------
                '''
        print(info % (username, password, account, country, province, street, gate, money,
                      bank_name))


    # status = bank_addUser(account, username, password, country, province, street, gate,
    #                       money)
    #
    # if status == 3:
    #     print("对不起，用户库已满，请携带证件到其他银行办理！")
    # elif status == 2:
    #     print("对不起，该用户已存在！请勿重复开户！")
    # elif status == 1:
    #     print("开户成功！以下是您的个人开户信息")
    #     info = '''
    #         ----------个人信息------
    #             用户名：%s
    #             密码：%s
    #             账号：%s
    #             地址信息
    #                 国家：%s
    #                 省份：%s
    #                 街道：%s
    #                 门牌号: %s
    #             余额：%s
    #             开户行地址：%s
    #             ------------------------
    #     '''
    #     print(info % (username, password, account, country, province, street, gate, money,
    #                   bank_name))
    # else:
    #     print("出错了！")
        '''
        把return型全部改为打印
        '''
    # bank1 = {"account": account,
    #     "password": password,
    #     "country": country,
    #     "province": province,
    #     "street": street,
    #     "gate": gate,
    #     "money": money,
    #     "bank_name": bank_name}
    # bank.update(bank1)

def add_money():
    account = int(input('请输入要存款的账号：'))
    if account in bank:
        money = int(input('请输入存款金额：'))
        bank[account]['money'] += money
        info = '''
                用户名：%s
                账号:%s
                余额：%s
                '''
        print(info % (bank[account]['username'], account, bank[account]['money']))
    else:
        print('您输入的账号不存在')

def take_money():
    account = int(input('请输入要取款的账号：'))
    if account in bank:
        password = int(input('请输入密码：'))
        if password == bank[account]['password']:
            money = int(input('请输入取款的金额'))
            if bank[account]["money"] >= money:
                bank[account]['money'] -= money
                info = '''
                        用户名：%s
                        账号：%s
                        余额：%s
                       '''
                print(info % (bank[account]['username'], account, bank[account]['money']))
            else:
                print("余额不足")
        else:
            print("您输入的密码错误")
    else:
        print("您输入的账户不存在")


def give_money():
    account = int(input("请输入您的账号："))
    account1 = int(input("请输入您要转账的账号："))
    if account1 in bank:
        if account in bank:
            password = int(input("请输入您的密码："))
            if password == bank[account]["password"]:
                money = int(input("请输入您要转的金额："))
                if bank[account]["money"] >= money:
                    bank[account]["money"] -= money
                    bank[account1]["money"] += money
                    info = '''
                                账号：%s
                                用户名：%s
                                余额：%s
                                转账账号：%s
                                转账用户名：%s
                                余额：%s
                        '''
                    print(info % (account, bank[account]["username"], bank[account]["money"], account1,
                                  bank[account1]["username"], bank[account1]["money"]))
                else:
                    print("余额不足！")
            else:
                print("密码不正确！")
        else:
            print("账号不存在！")
    else:
        print("账号不存在！")



def demand():
    account = int(input("请输入您的账号："))
    if account in bank:
        password = int(input("请输入密码："))
        if password == bank[account]["password"]:
            info = '''
                ----------个人信息------
                用户名：%s
                密码：%s
                账号：%s
                地址信息
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号: %s
                余额：%s
                开户行地址：%s
                ------------------------
            '''
            print(info % (bank[account]["username"], account, password, bank[account]["country"],
                          bank[account]["province"],  bank[account]["street"], bank[account]["gate"],
                          bank[account]["money"], bank_name))
        else:
            print("密码错误！")
    else:
        print("账号不存在！")

while True:
    welcome()
    chose = input("请选择您要办理的业务号：")
    if chose == "1":
        addUser()
        print(bank)
    elif chose == "2":
        add_money()
    elif chose == "3":
        take_money()
    elif chose == "4":
        give_money()
    elif chose == "5":
        demand()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")