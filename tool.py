#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import time
import random
import stat
import traceback
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer

PATH = lambda p: os.path.abspath(p)

device = mr.waitForConnection()
easy_device = EasyMonkeyDevice(device)
MonkeyRunner=mr
global current_logs
current_logs = ''


class TestTool:
    global current_logs

    # 开启activity
    def start_activity(self, path):
        device.startActivity(component=path)
        # MonkeyRunner.sleep(1)

    # 根据id点击
    def touch_view(self, view_id):
        easy_device.touch(By.id(view_id), MonkeyDevice.DOWN_AND_UP)  # 点击
        # MonkeyRunner.sleep(1)

    # 根据坐标点击
    def touch_point(self, point_x, point_y):
        device.touch(point_x, point_y, MonkeyDevice.DOWN_AND_UP)  # 点击
        # MonkeyRunner.sleep(1)

    # 返回
    def back(self):
        for i in range(0, 1):
            device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)  # 点击返回

    # 退出
    def exit(self):
        for i in range(1, 3):
            device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)  # 点击返回

    # 判断控件是否可见
    def is_component_visiable(self, view_id):
        return easy_device.visible(By.id(view_id))

    # 判断控件是否存在
    def is_component_exist(self, view_id):
        return easy_device.exists(By.id(view_id))

    # 获取控件的文字内容
    def get_component_text(self, viewId):
        return easy_device.getText(By.id(viewId))

    # 注入文本到控件当中
    def set_text(self, view_id, text):
        easy_device.type(By.id(view_id), text)

    # 拖动操作
    def drag(self, startX, startY, endX, endY, duration, step):
        device.drag((startX, startY), (endX, endY), duration, step)

    # 获取当前控件下子控件的数量
    def get_children_count(self, viewId):
        viewer = device.getHierarchyViewer()
        contentview = viewer.findViewById(viewId)
        childs = contentview.children
        return len(childs)

        # 对当前屏幕进行截图

    def take_screenshot(self):
        path = PATH(os.getcwd() + "/screenshot")
        print(path)
        if not os.path.isdir(PATH(os.getcwd() + "/screenshot")):
            os.makedirs(path)
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        MonkeyRunner.sleep(2)
        image = device.takeSnapshot()
        MonkeyRunner.sleep(2)
        image.writeToFile(PATH(path + "/" + timestamp + ".png"), 'png')
        print('执行截图完毕')

    # 获取任意层级的子view
    def get_childview(self, parentId, array):
        hierarchyViewer = device.getHierarchyViewer()
        str_getchildview = "hierarchyViewer.findViewById('" + parentId + "')"
        for index in array:
            str_getchildview += ('.children[' + str(index) + ']')
        exec('child_view=' + str_getchildview)
        return child_view

    def write_log_to_file(self):
        global current_logs
        path = PATH(os.getcwd() + '/logs')
        if not os.path.exists(PATH(os.getcwd() + '/logs')):
            os.makedirs(path)
        filename = time.strftime('%Y-%m-%d-%H:%M:%S-logs.txt', time.localtime(time.time()))
        file = open(os.getcwd() + '/logs/' + filename, 'w+')
        file.write(current_logs)

    def append_logs(self, content):
        global current_logs
        timestamp = time.strftime('[%Y-%m-%d-%H:%M:%S]', time.localtime(time.time()))
        result = timestamp + ': ' + content + '\n'
        current_logs += result
        print(result)

    def print_log(self, content):
        self.append_logs(content)

    def print_exception_info(self):
        self.print_log(traceback.format_exc())

    #调用当前方法必须获得焦点,即键盘弹出,光标显示
    def input_content(self):
        os.system('adb shell input text \"hello world!\"')

