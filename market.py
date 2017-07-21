#!/usr/bin/python
# -*- coding: utf-8 -*-

import base
import random
import os

class MarketTest(base.BaseTest):
    
    def __init__(self):
        super(MarketTest,self).__init__()

    def test_my_answers(self):
        self.print_log('进入我的提问模块')
        self.sleep(2)
        #点击了我的提问
        self.tool.touch_point(96,60)
        self.sleep(1)
        #左右滑动操作
        self.print_log('滑动以及切换操作')
        self.tool.drag(645, 350, 125, 350, 0.5, 1)
        self.sleep(2)
        self.tool.drag(125, 350, 645, 350, 0.5, 1)
        self.sleep(2)


    def test_collection(self):
        self.print_log('进入收藏夹模块')
        self.sleep(2)
        #点击了收藏夹
        self.tool.touch_point(282,60)

        #测试分类按钮
        self.print_log('测试分类按钮')
        child_width=66
        pop_x=731
        pop_y=124
        self.tool.touch_view('id/pop_select')
        self.sleep(2)
        pop_listview_count=self.tool.get_children_count('id/pop_suject_list')
        self.sleep(2)
        if pop_listview_count==0:
            self.tool.touch_point(pop_x,pop_y)
        elif pop_listview_count>0:
            for i in range(1,pop_listview_count):
                self.sleep(1)
                if self.tool.is_component_exist('id/pop_suject_list'):
                   pass
                else: 
                    self.tool.touch_view('id/pop_select')
                self.sleep(1)
                self.tool.touch_point(pop_x,pop_y+i*child_width)
                self.print_log('切换了分类')
                self.sleep(1)
        else:
            self.tool.touch_point(pop_x,pop_y)
        self.sleep(2)
        self.tool.touch_view('id/pop_select')
        self.sleep(2)
        self.print_log('点击全部')
        self.tool.touch_point(pop_x,pop_y)
        self.sleep(1)
        
        #测试删除按钮
        self.print_log('测试删除按钮')
        self.tool.touch_view('id/delete_button')
        self.sleep(1)
        self.print_log('选中checkbox')
        self.tool.touch_view('id/checkbox_deletebutton')
        self.sleep(1)
        self.print_log('删除内容')
        self.tool.touch_view('id/delete_sure')
        self.sleep(1)
        ##随机点击内容
        self.print_log('内容测试开始')
        for i in range(5):
            self.print_log('开始随机点击')
            random_x=random.randint(0,768)
            random_y=random.randint(100,946)
            self.sleep(1)
            self.tool.touch_point(random_x,random_y)
            self.sleep(1)
            if self.tool.is_component_exist('id/header_container'):
                self.print_log('进入详细信息页面')
                self.__handle_search_result()
                self.sleep(2)
                self.back()
                break
        self.print_log('内容测试完毕')
        #测试下拉刷新以及上拉加载
        for i in range(3):
            self.print_log('测试下拉刷新')
            self.sleep(1)
            self.tool.drag(370,270,370,650,1,10)

        for i in range(5):
            self.print_log('测试上拉加载')
            self.sleep(1)
            self.tool.drag(370,650,370,270,1,10)
        self.sleep(2)

    #处理搜索结果
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



    def start_test(self):
        self.print_log('******搜索题库测试开始******')
        self.test_my_answers()
        self.sleep(1)
        self.test_collection()
        self.print_log('******搜索题库测试完成******')
