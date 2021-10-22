from ddt import ddt
from ddt import unpack
from ddt import data
from unittest import TestCase
from bank import bank_addUser

da = [
    ["wmn","123456","china","河北省","中山西路","s001",6000,1],
    ["wmn","123456","china","河北省","中山西路","s001",6000,2],
    ["rzc","123456","china","河北省","中山西路","s005",6000,1],
]

@ddt
class TestBank(TestCase):

    for i in range(96):
        name = "wpf" + str(i)
        da.append([name,"123456","china","河北省","中山西路","s005",6000,1])
    da.append(["ld","123456","china","河北省","中山西路","s005",6000,3])

    @data(*da)
    @unpack
    def testAdduser(self,a,b,c,d,e,f,g,h):
        result = bank_addUser(a,b,c,d,e,f,g)
        self.assertEqual(h,result)








