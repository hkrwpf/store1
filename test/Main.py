from HTMLTestRunner import HTMLTestRunner
import unittest
import os
from threading import Thread

class test(Thread):
    pattern = ""
    file = ""
    def run(self) -> None:
        tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern=self.pattern)

        runner = HTMLTestRunner.HTMLTestRunner(
            title="HKR系统测试报告",
            description="HKR系统登录测试",
            verbosity=1,
            stream=open(file=self.file, mode="w+", encoding="utf-8")
        )

        runner.run(tests)

r1 = test()
r1.pattern = "TestLogin.py"
r1.file = "hkr.html"
r1.start()

r2 = test()
r2.pattern = "TEST.py"
r2.file = "gai.html"
r2.start()

















