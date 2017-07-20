#!/usr/bin/python
# -*- coding: utf-8 -*-

import tool as Tool

COMPONENT_ACTIVITY_PATH = 'com.bbk.videosearchstudy/.ResultFragmentActivity'


class ModuleTest(object):
    def __init__(self):
        self.tool = Tool.TestTool()
        self.MonkeyRunner = Tool.MonkeyRunner

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

    def exit(self):
        self.exit()

