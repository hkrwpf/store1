from threading import Thread
import time

baket = 0
count1 = 0
class cooker(Thread):
    def run(self) -> None:
        global baket
        global count1
        count_end = 0
        while 1:
            if baket < 500:
                baket += 1
                count1 += 1
                count_end = 0
            else:
                time.sleep(3)
                count_end += 1
                if count_end > 100:
                    print("总共制做了",count1,"个汉堡")
                    break

class patron(Thread):
    username = ""
    def run(self) -> None:
        global baket
        money = 10000
        count = 0
        while 1:
            if money > 0:
                if baket > 0:
                    baket -= 1
                    money -= 5
                    count += 1
                else:
                    time.sleep(3)
            else:
                print(self.username,"买了",count,"个汉堡")
                break

c1 = cooker()
c2 = cooker()
c3 = cooker()
c1.start()
c2.start()
c3.start()
p1 = patron()
# p1.username = "李四"
p1.username = (input("请输入姓名："))
p1.start()
p2 = patron()
# p2.username = "李环境"
p2.username = (input("请输入姓名："))
p2.start()
p3 = patron()
# p3.username = "李安徽科技"
p3.username = (input("请输入姓名："))
p3.start()
p4 = patron()
# p4.username = "李安居客和"
p4.username = (input("请输入姓名："))
p4.start()
p5 = patron()
# p5.username = "李暗黑风"
p5.username = (input("请输入姓名："))
p5.start()
p6 = patron()
# p6.username = "李AFK"
p6.username = (input("请输入姓名："))
p6.start()

