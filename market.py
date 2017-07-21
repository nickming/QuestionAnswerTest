#!/usr/bin/python
# -*- coding: utf-8 -*-

import base
import random

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
        child_width_half=33
        pop_x=698
        pop_y=157
        self.tool.touch_point(pop_x+child_width_half,pop_y-child_width_half)
        self.sleep(1)
        pop_listview_count=self.tool.get_children_count('id/pop_suject_list')
        self.sleep(2)
        if pop_listview_count==0:
            self.tool.touch_point(pop_x+child_width_half,pop_y-child_width_half)
        elif pop_listview_count>0:
            for i in range(1,pop_listview_count+1):
                self.tool.touch_point(734,122)
                self.sleep(1)
                self.tool.touch_point(pop_x+i*child_width_half,pop_y+i*child_width_half)
                self.sleep(2)
        else:
            self.tool.touch_point(pop_x+child_width_half,pop_y-child_width_half)

        self.tool.touch_point(pop_x+child_width_half,pop_y-child_width_half)
        self.tool.touch_point(pop_x+child_width_half,pop_y-child_width_half)
        self.sleep(1)
        
        ##测试删除按钮
        self.print_log('测试删除按钮')
        self.tool.touch_view('id/delete_button')
        self.sleep(1)
        count=self.tool.get_children_count('id/myXListView')
        print(count)
        self.sleep(2)
        # self.tool.get_childview('id/myXListView',[0,0,0])




        #测试下拉刷新以及上拉加载
        self.tool.drag(370,270,370,650,1,10)
        self.sleep(1)

        print(count)



    def start_test(self):
        self.print_log('******搜索题库测试开始******')
        self.test_my_answers()
        self.sleep(1)
        self.test_collection()
        self.print_log('******搜索题库测试完成******')
