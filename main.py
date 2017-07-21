#!/usr/bin/python
# -*- coding: utf-8 -*-


import module
import sys
import tool

module_test=module.ModuleTest()
device_tool=tool.TestTool()


def startTest(count):
    try:
        for i in range(count):
            temp=str(i)
            device_tool.print_log('***********第'+temp+'次测试*********')
            module_test.run_test()
            device_tool.print_log('***********第'+temp+'次结束*********')
    except BaseException:
        device_tool.print_exception_info()
        device_tool.write_log_to_file()
    device_tool.write_log_to_file()


if __name__=='__main__':
    if len(sys.argv)==1:
        startTest(1)
        print('默认执行一次')
    else:
        count=int(sys.argv[1])
        startTest(count)