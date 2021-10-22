from ddt import ddt
from ddt import data
from ddt import unpack
from unittest import TestCase
from bank import bank_transformMoney
# a转出账号b转入账号c转出密码d转出金额
# 1账号不存在2密码错误3余额不足0成功
da = [
    [6225600169,6209848313,123456,-1,3],
    [6225600169,6209848313,123456,0,0],
    [6225600169,6209848313,123456,1,0],
    [6225600169,6202238790,123456,1000,1],
    [6202238790,6209848313,123465,1000,1],
    [6225600169,6209848313,456789,1000,2],
    [6225600169,6209848313,123456,6000,3]
]
@ddt
class TestBank(TestCase):
    @data(*da)
    @unpack
    def testtransformmoney(self,a,b,c,d,e):
        result = bank_transformMoney(a,b,c,d)
        self.assertEqual(e,result)


