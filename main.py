#!/usr/bin/python
# -*- coding: utf-8 -*-

import search
import tool
import module

search_test=search.SearchTest()
device_tool=tool.TestTool()
module_test=module.ModuleTest()


if __name__=='__main__':
    module_test.init_activity()
    search_test.open_search()