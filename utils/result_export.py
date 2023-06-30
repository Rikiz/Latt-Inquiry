#!/usr/bin/env python
# coding=utf-8

import os
from pandas import DataFrame

keys = []

class Exporter(object):
    """docstring for Exporter"""
    def __init__(self, filename = "result.csv"):
        super(Exporter, self).__init__()
        self._filename = filename
        self.reset_result()

    def reset_result(self):
        if os.path.exists(self._filename):
            os.remove(self._filename)


    def append_to_result(self, address, longtitude, latitude):
        mode = "w"
        if os.path.exists(self._filename):
            mode = "a"
        add_row_frame = DataFrame({u'地址':[address],u'经度':[longtitude],u'维度':[latitude]})
        add_row_frame.to_csv(self._filename, mode=mode, encoding='utf-8',header=0,index=None)  #含中文，需要改变编码方式；保存在同级目录下


