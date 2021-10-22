from ddt import ddt
from ddt import unpack
from ddt import data
from unittest import TestCase
from bank import bank_saveMoney


da = [
    [6225600169,1000,True],
    [6225600169,1,True],
    [6225600169,0,True],
    [6209848313,-1,False],
    [6202238790,1000,False]
]

@ddt
class TestBank(TestCase):

    @data(*da)
    @unpack
    def testsavemoney(self,a,c,i):
        result = bank_saveMoney(a,c)
        self.assertEqual(i,result)


