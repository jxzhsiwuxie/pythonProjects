# _*_ coding: utf-8 _*_
import os
import tkinter
import tkinter.messagebox
import tkinter.dialog
import tkinter.filedialog


def mkdir(path):
    """
    自定义用于生成文件夹的函数
    :param path: 文件夹路径
    :return: None
    """
    exists = os.path.exists(path)
    if not exists:
        os.mkdir(path)


def openfile(filename):
    """
    自定义读取文件内容函数
    :param filename: 文件名
    :return: 文件内容
    """
    f = open(file=filename, mode='r')
    f_list = f.read()
    f.close()
    return f_list


def input_box(tips, in_type, length):
    """
    输入验证
    :param tips: 提示文字
    :param in_type: 限制输入类型，1 表示输入大于0的数字，2表示输入字母，3表示数字
    :param length: 输入信息长度，当类型为 1 时，输入数字长度无限制，这个参数无效，当类型为 2 或者 3 时才有效
    :return: 如果通过验证则返回输入的信息，否则返回 '0'
    """
    instr = input(tips)
    if len(instr) != 0:
        if in_type == 1:
            if str.isdigit(instr):
                if instr == '0':
                    print("输入值为0，请重新输入！")
                    return "0"
                else:
                    return instr
            else:
                print("输入类型不对，请重新输入！")
                return "0"
        if in_type == 2:
            if str.isalpha(instr):
                if len(instr) != length:
                    print("必须输入{}个字母，请重新输入！".format(length))
                    return '0'
                else:
                    return instr
            else:
                print("输入类型不对，请重新输入！")
                return "0"
        if in_type == 3:
            if str.isdigit(instr):
                if len(instr) != length:
                    print("必须输入{}个数字，请重新输入！".format(length))
                    return '0'
                else:
                    return instr
            else:
                print("输入类型不对，请重新输入！")
                return "0"
    else:
        print("输入为空，请重新输入！")
        return "0"


def write_file(str_list, filename, show_tips, tips,  dir_name):
    """
    将列表中的文字写入文件中
    :param str_list: 文字列表
    :param filename: 写入的文件名
    :param show_tips: 是否显示提示文字
    :param tips: 显示的提示文字
    :param dir_name: 文件夹名
    :return:
    """
    mkdir(dir_name)
    data_file = dir_name + '\\' + filename

    file = open(data_file, 'w')
    for line in str_list:
        file.write(line)
    file.close()

    if show_tips != 'no':
        tkinter.messagebox.showinfo("提示", tips + str(len(str_list)) + '\n 防伪码文件存放位置：' + data_file)
