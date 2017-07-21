#!/usr/bin/python
# -*- coding: utf-8 -*-

import tool as Tool
import base
import random
import os


class QuestionLibraryTest(base.BaseTest):

    def __init__(self):
        super(QuestionLibraryTest, self).__init__()

    def open_practice(self):
        self.print_log('选择刷题模块')
        # self.tool.startActivity('com.bbk.videosearchstudy/.Activity_Two')
        self.tool.touch_point(288, 982) # 点击刷题
        self.sleep(3)
    
    def choose_textbook(self):
        self.print_log("选择做题教材")
        self.sleep(1)
        self.tool.touch_point(398,42)
        # children_count = self.tool.get_children_count('id/gradeGridView')
        # self.print_log("count of children=",children_count)
        # index = random.randint(0, (children_count-1))
        # self.print_log('the random num=', index)
        # childView =  self.tool.getChildView('id/gradeGridView', [index])
        # self.tool.touch_button(childView, 0, 0)
        self.sleep(1)
        # 选择年级
        x_grade = random.randint(135, 758)
        y_grade = random.randint(95, 409)
        # self.print_log("point of x_grade: ", x_grade)
        # self.print_log("point of y_grade: ", y_grade)
        self.tool.touch_point(x_grade, y_grade)
        self.sleep(2)

        # 选择科目
        x_subject = random.randint(135, 758)
        # self.print_log("point of x_subject: ", x_subject)
        # self.print_log("point of y_subject: ", 448)
        self.tool.touch_point(x_subject, 448)
        self.sleep(2)
        # 选择出版社
        x_press = random.randint(135,758)
        # y_press = random.randint(495,643)
        # self.print_log("point of x_press: ", x_press)
        # self.print_log("point of y_press: ", y_press)
        self.sleep(1)
        self.tool.touch_point(x_press, 508)

        # 选择完毕，退出选择框状态
        self.back()

    def check_forcast_core(self):
        self.print_log('查看预测分')
        self.tool.touch_view('id/rank_change')
        self.tool.touch_view('id/rank_change')

    def switch_question_list(self):
        self.print_log('选择章节')
        self.tool.drag(745, 570, 17, 570, 1, 10)
        self.tool.drag(745, 570, 17, 570, 1, 10)
        self.tool.drag(332, 790, 332, 390, 1, 10)
        self.tool.drag(332, 390, 332, 790, 1, 10)

    # 在while循环中不断地点击，直到viewpager消失
    def choose_question(self):
        choose_false = self.tool.is_component_exist('id/pratise_jazzviewpager')
        while choose_false:
            y = random.randint(386,800)
            self.tool.touch_point(363, y)
            self.sleep(1)
            choose_false = self.tool.is_component_exist('id/pratise_jazzviewpager') #当viewpager销毁时，则选择成功
        self.print_log('进入习题')

    def answer_special_question(self):
        for j in range(1, 300):
            y_random = random.randint(92, 910)
            self.tool.touch_point(229, y_random)

    def answer_tool(self):
        self.print_log('点击草稿纸')
        self.tool.touch_point(572, 59)  # touch paper
        self.sleep(2)
        self.tool.drag(332, 790, 332, 390, 1, 10)
        self.sleep(2)
        self.print_log('点击橡皮擦')
        self.tool.touch_point(644, 30)  # touch wipe
        self.sleep(2)
        self.tool.drag(332, 390, 332, 700, 1, 10)
        self.sleep(2)
        self.print_log('点击清除')
        self.tool.touch_point(714, 31)  # touch clean

    def answer_question(self):
        self.sleep(2)
        self.answer_tool()

        if self.tool.is_component_exist('id/draftpaper_hvScrollView'):
            self.back()

        has_not_enter = True
        while has_not_enter:
            self.print_log('习题加载中....')
            self.sleep(1)
            has_not_enter = not self.tool.is_component_exist('id/pratise_question_viewpager') #当viewpager销毁时，则question已经展示
        self.print_log('习题加载成功')

        # 收藏题目
        self.print_log('点击收藏')
        self.tool.touch_point(638, 59)  # touch favorite

        # 纠错反馈
        self.print_log('点击纠错')
        self.tool.touch_point(704, 57)
        self.sleep(2)
        self.tool.input_content()
        self.sleep(1)
        self.tool.touch_point(157, 160)
        self.sleep(1)
        self.tool.touch_point(522, 583)
        self.sleep(3)

        # 查看题目(拿到屏幕下方Indicator个数)
        self.print_log('查看所有题目')
        count_quesiont = self.tool.get_children_count('id/practise_viewGroup')
        drag_count = count_quesiont
        print('count of question = ', drag_count)
        for i in range(1, drag_count):
            self.tool.drag(745, 570, 17, 570, 1, 10)
            print('the num of question: ', i)

        self.sleep(1)

        # 开始答题，返回第一题
        for i in range(1, drag_count):
            self.tool.drag(17, 570, 745, 570, 1, 10)
        self.print_log('返回第一题')

        self.sleep(1)

        self.print_log('开始答题')
        answer_count = drag_count + 1
        for i in range(1, answer_count):
            print("the num of answered:", i)
            self.answer_special_question()
            self.sleep(1)
            self.tool.drag(745, 570, 17, 570, 1, 10)

        self.print_log('再来一组')
        if self.tool.is_component_exist('id/ib_practice_again'):
            self.tool.touch_view('id/ib_practice_again')

        for x in range(1, answer_count):
            print("the num of answered:", x)
            self.answer_special_question()
            self.sleep(1)
            self.tool.drag(745, 570, 17, 570, 1, 10)
        self.back()

    def start_test(self):
        self.__start_search_test()

    def __start_search_test(self):
        self.print_log('******刷题模块测试开始******')
        # question_lib_test = question_library_test()
        self.open_practice()
        self.sleep(1)
        self.choose_textbook()
        self.sleep(1)
        self.check_forcast_core()
        self.sleep(1)
        self.switch_question_list()
        self.sleep(1)
        self.choose_question()
        self.sleep(1)
        self.answer_question()
        self.print_log('******刷题模块测试结束******')


    #     def practice_answered_question(self):
    #     self.print_log('点击错题本')
    #     self.sleep(3)
    #     # self.tool.touch_point(220, 837) #点击错题本
    #     wrong_count_exist = self.tool.is_component_exist('id/wrong_collect')
    #     self.print_log(str(wrong_count_exist))
    #     self.tool.touch_view('id/wrong_collect')
    #
    #     if self.tool.is_component_exist('id/iv_net_error'):
    #         self.print_log('网络出现问题')
    #         self.back()
    #
    #     if self.tool.is_component_exist('id/list'):
    #         self.print_log('选择错题集的第一题')
    #         self.tool.touch_point(150,190)
    #         self.sleep(3)
    #
    #     self.print_log('开始练习易错题')
    #     wrong_count = self.tool.getComponentText("id/tv_pager_indicator")
    #     for i in range(1, wrong_count):
    #         self.print_log('the num of wrong:', i)
    #         self.answer_special_question()
    #         self.tool.drag(745, 570, 17, 570, 1, 10)
    #     self.back()
    #     self.back()

# tool = TestTool()
# self.tool.startActivity('com.bbk.videosearchstudy/.Activity_Two')
# self.sleep(3)
# self.print_log('选择刷题模块')
# self.tool.touch_point(288, 982)
#
# self.sleep(1)
# question_lib_test = question_library_test()
# self.sleep(1)
# question_lib_test.choose_textbook()
# self.sleep(1)
# question_lib_test.check_forcast_core()
# self.sleep(1)
# question_lib_test.switch_question_list()
# self.sleep(1)
# question_lib_test.choose_question()
# self.sleep(1)
# question_lib_test.answer_question()
# self.sleep(3)
# question_lib_test.practice_answered_question()






