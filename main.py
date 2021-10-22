from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread

class test(Thread):
    pattern = ""
    description = ""
    file = ""
    def run(self) -> None:
        tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern=self.pattern)
        runner = HTMLTestRunner.HTMLTestRunner(
            title="工商银行的测试报告",
            description=self.description,
            verbosity=1,
            stream=open(file=self.file, mode="w+", encoding="utf-8")
        )

        runner.run(tests)

c1 = test()
c1.pattern = "Testbank.py"
c1.description = "这是银行开户测试报告"
c1.file = "工商银行开户.html"
c1.start()

c2 = test()
c2.pattern = "Testbank1.py"
c2.description = "这是银行存钱测试报告"
c2.file = "工商银行存钱.html"
c2.start()

c3 = test()
c3.pattern = "Testbank2.py"
c3.description = "这是银行取钱测试报告"
c3.file = "工商银行取钱.html"
c3.start()

c4 = test()
c4.pattern = "Testbank3.py"
c4.description = "这是银行转账测试报告"
c4.file = "工商银行转账.html"
c4.start()



