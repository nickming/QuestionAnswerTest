#!/usr/bin/python
# -*- coding: utf-8 -*-

import tool as Tool
import base


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



    def test_keyboard(self):
        self.tool.touch_view('id/quiz_ime')


