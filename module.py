#!/usr/bin/python
# -*- coding: utf-8 -*-

import tool as Tool
import search
import pratise
import mime
import market
import traceback


COMPONENT_ACTIVITY_PATH = 'com.bbk.videosearchstudy/.ResultFragmentActivity'


class ModuleTest(object):
    def __init__(self):
        self.tool = Tool.TestTool()
        self.MonkeyRunner = Tool.MonkeyRunner
        self.search=search.SearchTest()

    def init_activity(self):
        self.tool.print_log('进入智能答疑')
        self.tool.start_activity(COMPONENT_ACTIVITY_PATH)
        self.MonkeyRunner.sleep(1)


    def open_search_question(self):
        self.tool.print_log('进入搜题模块')
        self.tool.touch_view('id/main_bottom_search_id')
        self.MonkeyRunner.sleep(1)

    def open_pratise_question(self):
        self.tool.print_log('进入刷题模块')
        self.tool.touch_view('id/main_bottom_pratise_id')
        self.MonkeyRunner.sleep(1)

    def open_question_market(self):
        self.tool.print_log('进入题库模块')
        self.tool.touch_view('id/main_bottom_tk_id')
        self.MonkeyRunner.sleep(1)

    def open_mime(self):
        self.tool.print_log('进入我的模块')
        self.tool.touch_view('id/id/main_bottom_me_id')
        self.MonkeyRunner.sleep(1)

    def run_test(self):
        try:
            self.init_activity()
            #搜题模块
            self.open_search_question()
            self.search.start_search_test()
            self.MonkeyRunner.sleep(2)
            #刷题模块
            #题库模块
            #我的模块
            self.tool.write_log_to_file()
        except BaseException:
            self.tool.print_log(traceback.format_exc())
            self.tool.write_log_to_file()


    def exit(self):
        self.exit()

