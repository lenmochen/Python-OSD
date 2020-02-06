#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
license: "MIT License"
description: "判斷是否為回文日程式(簡易版)。"
"""

slist = "\n請輸入檢查日期，例如:2020年1月13日，輸入20200113: "
stag = "+"*20
print("\n" +stag +"程式開始" +stag )
while True:
    search_date = input( slist )
    print ("\n將查詢日期：",search_date)
    chk_status = input("是否正確(y/n)：")
    if ( chk_status == "y" or chk_status == "Y" ):
        print("\n開始進行檢查作業...",end='')
        search_date_year = search_date[:4]
        search_date_mday = search_date[-1:-5:-1]
        if search_date_year == search_date_mday:
            print("當天是回文日")
        else:
            print("不是回文日")
        print("\n" +stag +"程式結束" +stag)
        break
    elif ( chk_status == "n" or chk_status == "N" ):
        continue
    else:
        print("\n***需選擇 y|n ，請需重新輸入***\n")


__author__ = "icoingithink <icoingithink@gmail.com>"
__copyright__ = "Copyright 2020, 海獅程式開源教材-Python"
__license__ = "MIT License"
__description__ = "判斷是否為回文日程式(簡易版)。"