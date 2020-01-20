#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：Boyce Chen
@Date   ：2020-01-20 22:11
@Desc   ：提供公共方法
=================================================="""
import time
import os

if os.name == 'nt':
    os.system("")


def handle_choose():
    print("*" * 55)
    print('**\t{:<45}**'.format("1.统计文件数"))
    print('**\t{:<40}**'.format("2.排除指定后缀类型文件拷贝"))
    print('**\t{:<40}**'.format("3.包含指定后缀类型文件拷贝"))
    print('**\t{:<46}**'.format("4.常规拷贝"))
    print('**\t{:<49}**'.format("0.exit"))
    print("*" * 55)

    choice = input("\033[0;36;1mPlease enter the choice:\033[0m")

    if choice in ('0', '1', '2', '3', '4'):
        return choice
    else:
        print("^\033[0;31;1mIncorrect input, please re-enter. \033[0m")
        handle_choose()


def getTime():
    return time.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    print("Current Time:{}".format(getTime()))
    choices = handle_choose()
    if choices:
        if "1" == choices:
            print("{} is selected.".format('1.统计文件数'))
        if "2" == choices:
            print("{} is selected.".format('2.排除指定后缀类型文件拷贝'))
        if "3" == choices:
            print("{} is selected.".format('3.包含指定后缀类型文件拷贝'))
        if "4" == choices:
            print("{} is selected.".format('4.常规拷贝'))
    else:
        print('\r\033[0;35;1mThe program will exit after {} seconds.\033[0m'.format(3))
        time.sleep(3)
