#!/usr/bin/python
# -*- coding: utf-8 -*-

import tool as Tool
import base
import random
import os


class MineTest(base.BaseTest):

    def __init__(self):
        super(MineTest, self).__init__()

    def open_practice(self):
        self.print_log('选择「 我的 」模块')
        self.tool.touch_view('id/main_bottom_me_id') # 点击我的
        self.sleep(3)

    def __rotate_avatar(self):
        self.print_log('点击头像')
        self.tool.touch_view('id/person_photo')
        self.sleep(1)
        self.tool.touch_point(385, 987)  #点击旋转
        self.sleep(1)
        self.tool.touch_point(109, 212)  #点击区域外，退出此弹框

    def __change_info(self):
        self.tool.touch_view('id/person_changename')

        self.sleep(1)
        self.print_log('修改名字')
        self.tool.input_content()
        list = [366, 436]
        x_selected = random.sample(list, 1)
        print('random touch x：', x_selected[0])

        self.sleep(1)
        self.print_log('修改性别')
        self.tool.touch_point(x_selected[0], 373)

        self.sleep(1)
        self.print_log('修改年级')
        self.tool.touch_view('id/person_gradearrorw')
        self.tool.drag(378, 513, 378, 92, 1, 10)
        self.sleep(1)
        self.tool.touch_point(370, 518)
        self.sleep(1)
        self.tool.touch_point(109, 212)  # 点击区域外，退出此弹框
        self.sleep(1)
        self.tool.touch_point(729, 65)   #点击确认修改
        self.tool.print_log('修改个人信息成功')

    def __check_activity(self):
        self.print_log('查看活动')
        self.sleep(1)
        self.tool.touch_point(89, 510)   #点击活动
        self.sleep(1)
        self.back()

    def __write_suggestion(self):
        self.sleep(1)

        self.print_log('进入意见反馈')
        self.tool.touch_point(120, 700)

        self.print_log('填写建议')
        for i in range(3):
            os.system('adb shell input text \"helloworld!\"')

        self.tool.touch_point(89, 375)   #点击添加图片
        self.sleep(3)
        self.print_log('选择图片')
        count = self.tool.get_children_count('id/grideview')
        if count > 0:
            self.tool.touch_point(83, 186)
            self.sleep(2)
        else:
            tool.printLog('无图片')
            tool.back()

        self.print_log('填写联系方式')
        self.tool.touch_point(85, 521)   #点击添加练习方式
        os.system('adb shell input text \"123456\"')

        self.tool.print_log('提交反馈')
        self.tool.touch_point(384, 609)

        self.sleep(4)
        if self.tool.is_component_exist('id/dialog_btn_ok'):
            self.tool.touch_point(382, 581)
            self.print_log('意见反馈模块执行完毕')
        else:
            self.back()

    def __set_setting(self):
        self.sleep(1)
        self.tool.touch_point(360, 800)  #点击设置
        self.print_log('开始设置')
        self.sleep(1)
        self.tool.drag(730, 179, 666, 179, 1, 10)  #切换消息声音提示
        self.tool.drag(666, 179, 730, 179, 1, 10)
        self.sleep(1)
        self.tool.drag(730, 305, 666, 305, 1, 10)  #切换难题反馈
        self.tool.drag(666, 305, 730, 305, 1, 10)
        self.sleep(1)
        self.tool.touch_point(332, 449)
        self.sleep(1)
        self.tool.touch_point(332, 449)
        self.sleep(1)
        self.back()

    def start_test(self):
        self.__start_mime_test()

    # 开始执行本模块相关测试方法
    def __start_mime_test(self):
        self.print_log('******「 我的 」模块测试开始******')
        self.__rotate_avatar()
        self.sleep(1)
        self.tool.touch_point(730, 62)
        self.__change_info()
        self.__check_activity()
        self.__write_suggestion()
        self.__set_setting()
        self.print_log('******「 我的 」模块测试结束******')

