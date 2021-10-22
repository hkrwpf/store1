from ddt import ddt
from ddt import data
from ddt import unpack
from bank import bank_takeMoney
from unittest import TestCase

da = [
    [6202238790, 123456, 1000, 1],
    [6225600169, 852746, 1000, 2],
    [6209848313, 123456, 6001, 3],
    [6209848313, 123456, 6000, 0],
    [6225600169, 123456, 5999, 0],
    [6225600169, 123456, -1, 3],
    [6225600169, 123456, 0, 0],
    [6225600169, 123456, 1, 0]
]
# 钱不够3、密码不对2、账号不存在1、成功0
@ddt
class TestBank(TestCase):

    @data(*da)
    @unpack
    def testtakemoney(self,a,b,c,d):
        result = bank_takeMoney(a,b,c)
        self.assertEqual(d,result)





