#!/usr/bin/python
# -*- coding: utf-8 -*-

import tool as Tool
from com.android.monkeyrunner import MonkeyRunner

class BaseTest(object):

    def __init__(self):
        self.tool=Tool.TestTool()

    def print_log(self,content):
        self.tool.print_log(content)

    def sleep(self,time):
        MonkeyRunner.sleep(time)

    def back(self):
        self.tool.back()

    def start_test(self):
        pass
