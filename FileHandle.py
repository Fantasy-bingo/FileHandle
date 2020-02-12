#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：Boyce Chen
@Date   ：2020-01-10 23:22
@Desc   ：
=================================================="""
import os
import time
import shutil
from ReadJson import read_json
from CommFunc import handle_choose, getTime
from pathlib import Path  # 此模块用于兼容Mac平台和Windows NT平台

if os.name == "nt":
    os.system("")  # 解决Windows的cmd下，颜色不显示问题


class MyFile:
    def __init__(self, src_path, paste_path, postfix):
        self.handle_path = src_path
        self.paste_path = Path(paste_path)
        self.postfix = postfix

    def count_file(self, _count_path):
        num = 0
        for roots, dirs, files in os.walk(_count_path):
            for file in files:
                name = os.path.splitext(file)[0]
                if file == "Thumbs.db" or name == "":  # 去除Thumbs.db和以.开头的隐藏文件
                    continue
                else:
                    num += 1

        return num

    def _copy_file(self, src_path):
        """
        拷贝文件函数，原始文件会在新路径的相同层级下
        :param src_path: 原始文件路径
        :return:
        """
        try:
            length = len(src_path.split("\\"))
            target_path = self.paste_path  # 传递MyFile类中初始化的粘贴文件路径

            for i in range(2, length - 1):  # 2020/01/17 当源路径层级少于3级时，这一步会报错，待处理
                target_path = os.path.join(target_path, src_path.split("\\")[i])

            if not os.path.exists(target_path):
                print("\033[1;32;1m|{}|Make 【{}】\033[0m".format(getTime(), target_path))
                os.makedirs(target_path)

        except Exception as e:
            print(e)

        else:  # 未抛异常时，执行拷贝动作
            shutil.copy(src_path, target_path)

    def traversing_file_include_postfix(self, traverse_path):
        """
        回调函数，遍历指定路径下的所有文件和文件夹，符合指定后缀名的文件，将调用_ copy_ file函数进行拷贝。
        :param traverse_path:
        :return:
        """
        if traverse_path == '':
            return False
        try:
            for file_list in os.listdir(traverse_path):
                if '' != file_list[0]:
                    if os.path.isfile(os.path.join(traverse_path, file_list)):
                        src = os.path.join(traverse_path, file_list)
                        extension = os.path.splitext(file_list)[1].lower()  # 匹配扩展名时兼容大小写
                        if extension in self.postfix:  # 包含后缀名
                            self._copy_file(src)
                            print("源文件:{}".format(src))

                    else:
                        self.traversing_file_include_postfix(os.path.join(traverse_path, file_list))
        except Exception as e:
            print(e)
            return False

    def traversing_file_exclude_postfix(self, traverse_path):
        """
        回调函数，遍历指定路径下的所有文件和文件夹，符合指定后缀名的文件，将调用_ copy_ file函数进行拷贝。
        :param traverse_path:
        :return:
        """
        if traverse_path == '':
            return False
        try:
            for file_list in os.listdir(traverse_path):
                if '' != file_list[0]:
                    if os.path.isfile(os.path.join(traverse_path, file_list)):
                        src = os.path.join(traverse_path, file_list)
                        extension = os.path.splitext(file_list)[1].lower()  # 匹配扩展名时兼容大小写
                        if extension not in self.postfix:  # 排除后缀名
                            self._copy_file(src)
                            print("源文件:{}".format(src))

                    else:
                        self.traversing_file_exclude_postfix(os.path.join(traverse_path, file_list))
        except Exception as e:
            print(e)
            return False

    def copy_file_normal(self, traverse_path):
        try:
            for file in os.listdir(traverse_path):
                if '.' != file[0]:
                    src = os.path.join(traverse_path, file)
                    if os.path.isfile(src):
                        self._copy_file(src)
                        print("源文件:{}".format(src))
                    else:
                        self.copy_file_normal(src)
        except Exception as e:
            print(e)
            return False

    def path_is_exist(self):
        check_path = self.paste_path
        if not os.path.exists(check_path):
            return True
        else:
            print("\033[1;31;1m【{}】is already exist,please reconfigure.\033[0m".format(check_path))
            exit(0)


if __name__ == '__main__':
    config_data = read_json()
    if not config_data:  # 判断config_data数据是否有效，如果无效，被调用的read_json函数会返回False，程序直接退出
        exit(0)

    handle_num = handle_choose()
    if handle_num != '0':
        startTime = time.time()
        myfile = MyFile(config_data.get("handle_path"), config_data.get("paste_path"), config_data.get("postfix"))
        if handle_num == '1':
            print("统计文件数量")
            for filepath in myfile.handle_path:
                if "" != filepath:
                    print("\033[0;32;1m||{}||正在统计:【{}】\033[0m".format(getTime(), filepath), end='')
                    file_num = myfile.count_file(Path(filepath))
                    print("\033[0;32;1m【{}】文件总数量:{}\033[0m".format(filepath, str(file_num)))

        elif handle_num == '2':
            print("排除指定后缀类型文件拷贝")
            for handle_path in myfile.handle_path:
                myfile.traversing_file_exclude_postfix(Path(handle_path))
                print("\033[0;32;1m||{}||拷贝的文件保存在{}目录.\033[0m".format(getTime(), myfile.paste_path))

        elif handle_num == '3':
            print("包含指定后缀类型文件拷贝")
            for handle_path in myfile.handle_path:
                myfile.traversing_file_include_postfix(Path(handle_path))
                print("\033[0;32;1m||{}||拷贝的文件保存在{}目录.\033[0m".format(getTime(), myfile.paste_path))

        elif handle_num == '4':
            print("常规拷贝")
            if myfile.path_is_exist():
                for handle_path in myfile.handle_path:
                    myfile.copy_file_normal(handle_path)
                    print("\033[0;32;1m||{}||拷贝的文件保存在{}目录.\033[0m".format(getTime(), myfile.paste_path))

        endTime = time.time()
        print("\033[0;32;1m||{}||总耗时:{:.6}s\033[0m".format(getTime(), str(endTime - startTime)))

    # 输入错误或者是0，则退出程序
    else:
        for i in range(3, -1, -1):
            print('\033[0;35;1mThe program will exit after {} seconds.\033[0m'.format(str(i)), end="", flush=True)
            time.sleep(1)

        exit(0)
