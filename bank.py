import random
from DBUtils import update
from DBUtils import select

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


def getRandom():
    li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
    global string
    string = ""
    for i in range(8):
        string = string + li[int(random.random() * len(li))]
    return string
def bank_adduser(username, password, country, province, street, door, money):
    sql1 = "select count(*) from user"
    param1 = []
    data1 = select(sql1, param1)
    if data1[0][0] > 100:
        return 3

    sql2 = "select * from user where username = %s"
    param2 = [username]
    data2 = select(sql2, param2)
    if len(data2) != 0:
        return 2

    sql3 = "insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
    param3 = [getRandom(), username, password, country, province, street, door, money, bank_name]
    update(sql3, param3)
    return 1
def addUser():
    username = input("用户名")
    password = int(input("密码"))
    country = input("居住地址：1.国家：")
    province = input("省份")
    street = input("街道")
    door = input("门牌号")
    money = int(input("银行卡余额"))

    statue = bank_adduser(username, password, country, province, street, door, money)
    if statue == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")
    elif statue == 2:
        print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif statue == 1:
        print("开户成功，以下是您的开户信息")
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
        print(info % (username, password, string, country, province, street, door, money, bank_name))

def savemoney():
    account = input("请输入您的账号：")
    m = int(input("请输入您要存的金额："))
    sql1 = "select * from user where account = %s"
    param1 = [account]
    data1 = select(sql1, param1)
    if data1[0][0] == account:
        sql2 = "update user set money = money + %s where account = %s"
        param2 = [m, account]
        update(sql2, param2)
        print("存款成功，以下是您的个人信息")
        sql3 = "select account,username,money from user where account = %s"
        param3 = [account]
        data3 = select(sql3, param3)
        print(data3)
    else:
        print("您的账号错误！")

def takemoney():
    account = input("请输入您的账号：")
    sql1 = "select * from user where account = %s"
    param1 = [account]
    data1 = select(sql1, param1)
    if data1[0][0] == account:
        password = int(input("请输入您的密码："))
        if data1[0][2] == password:
            q = int(input("请输入您要取的金额："))
            if data1[0][7] >= q:
                sql2 = "update user set money = money - %s where account = %s"
                param2 = [q, account]
                update(sql2, param2)
                sql3 = "select account,username,money from user where account = %s"
                param3 = [account]
                data3 = select(sql3, param3)
                print(data3)
            else:
                print("您账户金额不足！")
        else:
            print("您输入的密码错误！")
    else:
        print("您输入的账号不存在！")


def givemoney():
    account = input("请输入您的账号：")
    sql1 = "select * from user where account = %s"
    param1 = [account]
    data1 = select(sql1, param1)
    if data1[0][0] == account:
        account2 = input("请输入要转账的账号：")
        password = int(input("请输入您账号的密码："))
        if data1[0][2] == password:
            sql2 = "select * from user where account = %s"
            param2 = [account2]
            data2 = select(sql2, param2)
            if data2[0][0] == account2:
                z = int(input("请输入您要转账的金额："))
                if data1[0][7] >= z:
                    sql3 = "update user set money = money - %s where account = %s and password = %s"
                    param3 = [z, account, password]
                    update(sql3, param3)
                    sql4 = "update user set money = money + %s where account = %s"
                    param4 = [z, account2]
                    update(sql4, param4)
                    print("转账成功！以下是您的个人信息：")
                    sql5 = "select account,username,money from user where account = %s"
                    param5 = [account]
                    data5 = select(sql5, param5)
                    print(data5)
                else:
                    print("您账户的金额不足！")
            else:
                print("您要转账的账户不存在！")
        else:
            print("您输入的密码错误！")
    else:
        print("您输入的账号不存在！")


def selectUser():
    account = input("请输入您要查询的账号：")
    sql = "select * from user where account = %s "
    param = [account]
    data = select(sql, param)
    if data[0][0] == account:
        password = int(input("请输入要查询账号的密码："))
        if data[0][2] == password:
            sql1 = "select account, username, money from user where account = %s "
            param1 = [account]
            data1 = select(sql1, param1)
            print(data1)
        else:
            print("您输入的密码错误！")
    else:
        print("您输入的账号不存在！")



while True:
    welcome()
    chose = input("请选择您要办理的业务号：")
    if chose == "1":
        addUser()
    elif chose == "2":
        savemoney()
    elif chose == "3":
        takemoney()
    elif chose == "4":
        givemoney()
    elif chose == "5":
        selectUser()
    elif chose == "6":
        print("欢迎下次光临！")
        break
    else:
        print("输入错误！请重新输入！")


