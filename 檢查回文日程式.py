#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
author: "icoding.ithink <icoding.ithink@gmail.com>"
copyright: "Copyright 2020, 海獅程式開源教材-Python"
license: "MIT License"
description: "判斷所輸入的日期，是否為回文日？"
"""

slist = "輸入檢查日期，例如:2020年1月13日，輸入20200113: "
stag = "="*20
print("\n" +stag +"程式開始" +stag )
search_date = input( slist )

while True:
    print ("\n將查詢日期：",search_date)
    chk_status = input("是否正確(y/n)：")
    
    #輸入日期正確流程
    if ( chk_status == "y" or chk_status == "Y" ):
        print("\n開始進行檢查作業...",end='')
        search_date_year = search_date[:4]
        search_date_mday = search_date[-1:-5:-1]
        if search_date_year == search_date_mday:
            print(" << 是回文日 >>")
        else:
            print(" << 不是回文日 >>")
        break
    
    #輸入日期錯誤流程
    elif ( chk_status == "n" or chk_status == "N" ):
        print ("\n重來一次：")
        search_date = input( slist )
    
    #輸入非y或n的流程
    else:
        print("\n◎ 請選擇 y|n")

print("\n" +stag +"程式結束" +stag)