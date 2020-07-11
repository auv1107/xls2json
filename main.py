# coding=utf-8

import sys
import getopt
from xls2json.xls2json import *
import json

if __name__ == '__main__':
    xls = Xls2Json()
    xls.setConfig(
        Config().start(1).end(-1)
        .values([(0, 'click_time'), (1, 'create_time')])
        .value(2, 'pay_time')
        .value(3, 'balance_time')
        .value(5, 'item_id')
        .value(6, 'pic')
        .value(7, 'title')
        .value(11, 'price')
        )
    res = xls.toJson('test.xls')
    print ('json %s' % json.dumps(res))