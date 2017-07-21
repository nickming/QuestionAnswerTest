#!/usr/bin/python
# -*- coding: utf-8 -*-

import tool as Tool
import base
import random
import os


class SearchTest(base.BaseTest):
    MODE_CAMERA = 1
    MODE_KEYBOARD = 2

    def __init__(self):
        super(SearchTest,self).__init__()
        self.mode=self.MODE_CAMERA

    def open_search(self):
        self.print_log('进入搜索页面')
        self.sleep(2)
        self.tool.touch_view('id/main_search_id_parent')
        self.sleep(1)

    def test_camera(self):
        self.print_log('进入拍照模块')
        self.sleep(2)
        self.tool.touch_view('id/quiz_camera')
        self.sleep(2)
        self.print_log('进行拍照')
        self.sleep(2)
        self.tool.touch_view('id/capture_image_button')
        self.print_log('进行上下拖动')
        self.tool.drag(500, 370, 500, 233, 0.5, 10)
        self.sleep(2)
        self.tool.drag(500, 233, 500, 370, 0.5, 10)
        self.sleep(2)
        self.tool.drag(500, 370, 350, 370, 0.5, 10)
        self.sleep(2)
        self.tool.drag(350, 370, 500, 370, 0.5, 10)
        self.sleep(2)
        self.print_log('进行旋转操作')
        for i in range(0, 4):
            self.tool.touch_point(960, 63)
            self.sleep(2)
        self.print_log('进行保存操作')
        self.sleep(2)
        self.tool.touch_point(960, 384)
        self.sleep(2)
        self.__handle_search_result()
        self.sleep(1)
        self.print_log('相机模块测试完成')

    def __handle_search_result(self):
        self.sleep(5)
        while self.tool.is_component_visiable('id/search_questionresult_progressbar'):
            self.print_log('搜索中...')
        else:
            pass

        if self.tool.is_component_exist('id/answer_content_wv'):
            self.__handle_success()
        else:
            self.__handle_failed()

    def __handle_success(self):
        self.print_log('搜索成功')
        self.print_log('上下左右滑动')
        self.tool.drag(373, 678, 373, 311, 0.5, 10)
        self.sleep(2)
        self.tool.drag(373, 311, 373, 678, 0.5, 10)
        self.sleep(2)
        self.tool.drag(645, 350, 125, 350, 0.5, 1)
        self.sleep(2)
        self.tool.drag(125, 350, 645, 350, 0.5, 1)
        self.sleep(2)

        self.print_log('点击纠错按钮')
        self.tool.touch_point(567, 195)
        self.sleep(2)
        os.system('adb shell input text \"helloworld\" ')
        self.sleep(1)
        self.tool.touch_point(157, 160)
        self.sleep(1)
        self.tool.touch_point(520, 600)
        self.sleep(3)

        self.print_log('点击收藏')
        self.tool.touch_point(689, 195)
        self.sleep(2)
        self.print_log('进入巩固练习模块')
        self.sleep(2)
        if self.tool.is_component_visiable('id/consolidate_questions_btn'):
            self.tool.touch_view('id/consolidate_questions_btn')
            self.sleep(3)
            if self.tool.is_component_visiable('id/consolidate_questions_webview_root'):
                self.print_log('巩固模块进行拖动以及随机点击操作')
                for k in range(1, 5):
                    self.sleep(0.5)
                    self.tool.drag(373, 678, 373, 311, 0.5, 10)
                    self.sleep(1)
                    ran_x = random.randint(0, 768)
                    ran_y = random.randint(147, 800)
                    self.tool.touch_point(ran_x, ran_y)
                self.back()
        self.sleep(2)
        # 循环滑动至底部
        self.print_log('循环往下滑动并且点击')
        # 在webview的范围内随机点击30次操作
        self.print_log('点击操作开始')
        for i in range(1, 20):
            self.sleep(2)
            if self.tool.is_component_visiable('id/videoviewcontain'):
                self.print_log('进入视频播放界面')
                self.sleep(20)
                self.print_log('点击操作结束')
                self.back()
                self.sleep(2)
                break
            else:
                print('点击了')
                ran_x = random.randint(0, 768)
                ran_y = random.randint(147, 800)
                self.tool.drag(373, 678, 373, 311, 0.5, 10)
                self.tool.touch_point(ran_x, ran_y)
        self.print_log('点击操作结束')
        self.back()

    def __handle_failed(self):
        if self.tool.is_component_visiable('id/search_questionresult_errorimage'):
            self.print_log('传输数据出现问题')
            self.back()
            self.sleep(2)
            if self.mode == self.MODE_CAMERA:
                self.test_camera()
            else:
                self.back()
        else:
            self.print_log('网络出错')
            self.back()
            self.sleep(2)

    def test_keyboard(self):
        self.sleep(2)
        self.tool.touch_view('id/quiz_ime')
        self.print_log('进入键盘输入模块')
        self.sleep(1)
        os.system('adb shell input text \"hello\"')
        self.sleep(2)
        self.tool.touch_view('id/search')
        self.__handle_search_result()
        self.print_log('键盘测试模块完成')
        self.back()

    def start_test(self):
        self.__start_search_test()

    def __start_search_test(self):
        self.print_log('******搜索模块测试开始******')
        self.open_search()
        self.sleep(1)
        self.test_camera()
        self.sleep(2)
        self.test_keyboard()
        self.sleep(2)
        self.back()
        self.print_log('******搜索模块测试完成******')
