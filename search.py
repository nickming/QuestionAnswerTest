#!/usr/bin/python
# -*- coding: utf-8 -*-

import tool as Tool
import base
import random


class SearchTest(base.BaseTest):

    def open_search(self):
        self.print_log('进入搜索页面')
        self.tool.touch_view('id/main_search_id_parent')
        self.sleep(1)

    def test_camera(self):
        self.print_log('进入拍照模块')
        self.tool.touch_view('id/quiz_camera')
        self.sleep(4)
        self.print_log('进行拍照')
        self.tool.touch_view('id/capture_image_button')
        self.print_log('进行上下拖动')
        self.tool.drag(500,370,500,233,0.5,10)
        self.sleep(0.5)
        self.tool.drag(500,233,500,370,0.5,10)
        self.sleep(0.5)
        self.tool.drag(500,370,350,370,0.5,10)
        self.sleep(0.5)
        self.tool.drag(350,370,500,370,0.5,10)
        self.sleep(0.5)
        self.print_log('进行旋转操作')
        for i in range(1,4):
            self.sleep(1)
            self.tool.touch_view('id/id_editor_turnright')
        self.print_log('进行保存操作')
        self.tool.touch_view('id/id_save')
        self.sleep(3)
        self.__handle_search_result()



    def __handle_search_result(self):
        while self.tool.is_component_visiable('id/search_questionresult_progressbar'):
            self.print_log('搜索中...')
        else:
            pass
        if self.tool.is_component_exist('id/answer_content_wv'):
            self.__handle_success()
        else:
            pass

    def __handle_success(self):
        self.print_log('搜索成功')
        self.print_log('上下左右滑动')
        self.tool.drag(373,678,373,311,0.5,10)
        self.sleep(0.5)
        self.tool.drag(373,311,373,678,0.5,10)
        self.sleep(0.5)
        self.tool.drag(645,350,125,350,0.5,1)
        self.sleep(0.5)
        self.tool.drag(125,350,645,350,0.5,1)
        self.sleep(2)
        self.print_log('点击纠错按钮')
        self.tool.touch_point(561,196)
        self.sleep(1)
        self.tool.touch_view('id/dialog_correct_mistake_chkbox_result_nowant')
        self.sleep(1)
        Tool.device.type('hello world!')
        self.sleep(1)
        self.tool.touch_view('id/dialog_correct_mistake_btn_submit')
        self.sleep(2)
        self.tool.touch_point('点击收藏')
        self.tool.touch_point(689,195)
        self.sleep(2)
        # 循环滑动至底部
        self.print_log('循环滑动至底部')
        for k in range(1, 10):
            self.sleep(0.5)
            self.tool.drag(373,678,373,311,0.5,10)
        # 在webview的范围内随机点击30次操作
        self.print_log('点击操作开始')
        for i in range(1, 30):
            if self.tool.is_component_visiable('id/videoviewcontain'):
                self.print_log('进入视频播放界面')
                self.sleep(20)
                self.print_log('点击操作结束')
                self.back()
                self.sleep(2)
                break
            else:
                print('点击了')
                ran_x = random.randint(0, 1536)
                ran_y = random.randint(500, 1800)
                self.tool.touch_point(ran_x, ran_y)
        self.print_log('点击操作结束')
        self.back()





    def test_keyboard(self):
        self.tool.touch_view('id/quiz_ime')


