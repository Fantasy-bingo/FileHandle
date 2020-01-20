#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@Author ：Boyce Chen
@Date   ：2020-01-10 23:22
@Desc   ：
=================================================="""
import os
import json


def read_json():
    global _data
    if os.path.exists('./config.json'):
        with open('./config.json', 'r', encoding='utf-8') as fjson:
            _data = json.load(fjson)
            return _data

    else:
        print('\033[0;31;1m>>>ERROR<<<\n{}\033[0m'.format("The config.json file in the current directory doesn't "
                                                          "exist or correct, please check it first.\nThe content "
                                                          "format is shown below:"))
        print("{")
        print("    \"paste_path\": \"the full directory you want to paste\",")
        print("    \"handle_path\": [")
        print("        \"the full directory you want handle\",")
        print("        \"the full directory you want handle\"")
        print("    ],")
        print("    \"postfix\": [")
        print("        \".jpg\",")
        print("    ]")
        print("}")
        return False


if __name__ == '__main__':
    json_data = read_json()

    print(json_data)
