#!/usr/bin/python
# -*- coding: utf-8 -*-

import tool as Tool
import search
import practice
import mime
import market
import traceback


COMPONENT_ACTIVITY_PATH = 'com.bbk.videosearchstudy/.ResultFragmentActivity'


class ModuleTest(object):
    def __init__(self):
        self.tool = Tool.TestTool()
        self.MonkeyRunner = Tool.MonkeyRunner
        self.search=search.SearchTest()
        self.market=market.MarketTest()
        self.practice = practice.QuestionLibraryTest()
        self.mime =  mime.MineTest()

    def init_activity(self):
        self.tool.print_log('进入智能答疑')
        self.tool.start_activity(COMPONENT_ACTIVITY_PATH)
        self.MonkeyRunner.sleep(1)


    def open_search_question(self):
        self.tool.print_log('进入搜题模块')
        self.tool.touch_view('id/main_bottom_search_id')
        self.MonkeyRunner.sleep(1)

    def open_pratise_question(self):
        self.MonkeyRunner.sleep(1)
        self.tool.print_log('进入刷题模块')
        self.tool.touch_view('id/main_bottom_pratise_id')
        self.MonkeyRunner.sleep(1)

    def open_question_market(self):
        self.tool.print_log('进入题库模块')
        self.tool.touch_view('id/main_bottom_tk_id')
        self.MonkeyRunner.sleep(1)

    def open_mime(self):
        self.tool.print_log('进入我的模块')
        self.tool.touch_view('id/main_bottom_me_id')
        self.MonkeyRunner.sleep(1)

    def __start_search(self):
        self.open_search_question()
        self.search.start_test()
        self.MonkeyRunner.sleep(2)

    def __start_market(self):
        self.open_question_market()
        self.market.start_test()
        self.MonkeyRunner.sleep(2)

    def __start_pratise(self):
        self.open_pratise_question()
        self.practice.start_test()
        self.MonkeyRunner.sleep(2)
        pass

    def __start_mime(self):
        self.open_mime()
        self.mime.start_test()
        self.MonkeyRunner.sleep(2)
        pass
        

    def run_test(self):
        try:
            self.init_activity()
            #搜题模块
            # self.__start_search()

            #刷题模块
            # self.__start_pratise()

            #题库模块
            # self.__start_market()

            #我的模块
            # self.tool.write_log_to_file()
            self.__start_mime()

        except BaseException:
            self.tool.print_log(traceback.format_exc())
            self.tool.write_log_to_file()


    def exit(self):
        self.exit()

