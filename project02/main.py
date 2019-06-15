# _*_ coding: utf-8 _*_
import random
import tkinter.messagebox
import tkinter.dialog
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
from string import digits
from pystrich.ean13 import EAN13Encoder
import qrcode

from assist import *

root = tkinter.Tk()
# 隐藏主窗口从而弹出的只有对话框
root.withdraw()

# 初始化数据
number = "1234567890"
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
allis = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"


def main_menu():
    print('''
    **********************************************************************************
    *                          企业编码生成系统
    **********************************************************************************
    *    1. 生成6位数字防伪编码（213563型）
    *    2. 生成9位系列 产品数字防伪编码（879-335439型）
    *    3. 生成25位混合产品序列号(B2R12-N7TE8-9IET2-FE35O-DW2K4型)
    *    4. 生成含数据分析功能的防伪编码(5A61M0583D2)
    *    5. 智能批量生成带数据分析功能的防伪码
    *    6. 后续补加生成防伪码(5A61M0583D2)
    *    7. EAN-13条形码批量生成
    *    8. 二维码批量输出          
    *    9. 企业粉丝防伪码抽奖
    *    0. 退出系统
    **********************************************************************************
    *    说明：通过数字键盘选择菜单
    **********************************************************************************
    ''')


def main():
    while True:
        main_menu()

        choice = input("输入您要操作的选项：")
        # 验证输入是否为合法的数字
        choice = input_validate(choice)

        if choice == '1':
            # 生成防伪码
            generate_code1(str(choice))
        elif choice == '2':
            # 生成9位系列产品数字防伪码
            generate_code2(choice)
        elif choice == '3':
            # 生成25位混合产品序列号
            generate_code3(choice)
        elif choice == '4':
            # 生成含有数据分析功能的防伪编码
            generate_code4(choice)
        elif choice == '5':
            # 批量生成带数据分析功能的防伪码
            generate_code5(choice)
        elif choice == '6':
            # 后续补加生成防伪码
            generate_code6(choice)
        elif choice == '7':
            # 批量生成条形码
            generate_code7(choice)
        elif choice == '8':
            # 批量生成二维码
            generate_code8(choice)
        elif choice == '0':
            # 退出系统
            print("正在退出系统")
            break
        else:
            continue


def input_validate(instr):
    """
    验证输入是否为数字
    :param instr:
    :return:
    """
    if len(instr) == 0 or len(instr) > 1 or instr == '9':
        print("必须输入0~8的数字，请重新输入。")
        return '9'
    if not str.isdigit(instr):
        print("必须输入数字，请重新输入。")
        return '9'
    else:
        return instr


def generate_code1(choice):
    """
    生成6位防伪码
    :param choice:
    :return:
    """
    in_count = input_box("请输入要生成的防伪码的数量：", 1, 0)
    while in_count == 0:
        in_count = input_box("请输入要生成的防伪码的数量：", 1, 0)

    str_list = []
    for i in range(int(in_count)):
        rand_str = ''
        for j in range(6):
            rand_str += random.choice(number)
        rand_str = rand_str + '\n'
        str_list.append(rand_str)

    write_file(str_list, "generate_code" + str(choice) + ".txt", "", "已生成防伪码共计：", "str_code")


def generate_code2(choice):
    """
    生成9位系列产品防伪码
    :param choice:
    :return:
    """
    order_start = input("请输入系列产品的数字起始号（3位）")
    while int(order_start) == 0:
        order_start = input("请输入系列产品的数字起始号（3位）")

    order_count = input_box("请输入系列产品的数量：", 1, 0)
    while int(order_count) < 1 or int(order_count) > 999:
        order_count = input_box("请输入系列产品的数量：", 1, 0)

    in_count = input_box("请输入要生成的每个系列产品的防伪码数量", 1, 0)

    str_list = []
    for i in range(int(order_count)):
        for j in range(int(in_count)):
            temp_str = ''
            for k in range(6):
                temp_str += random.choice(number)
            str_list.append(str(int(order_start) + i) + temp_str + '\n')
    write_file(str_list, "generate_code" + str(choice) + ".txt", "", "已生成9位系列产品防伪码共计：", "str_code")


def generate_code3(choice):
    """
    生成25位混合产品序列号
    :param choice:
    :return:
    """
    in_count = input_box("请输入要生成的25位混合产品序列号的数量：", 1, 0)
    while int(in_count) == 0:
        in_count = input_box("请输入要生成的25位混合产品序列号的数量：", 1, 0)

    str_list = []
    for i in range(int(in_count)):
        temp_str = ''
        for j in range(25):
            temp_str = temp_str + random.choice(letter)

        temp_code = temp_str[:5] + "-" + temp_str[5:10] + "-" + temp_str[10:15] + "-" + temp_str[15:20] + "-" + temp_str[20:25] + "\n"
        str_list.append(temp_code)

    write_file(str_list, "generate_code" + str(choice) + ".txt", "", "已生成25位混合防伪码共计：", "str_code")


def generate_code4(choice):
    in_type = input_box("请输入数据分析编号（3位字母）", 2, 3)
    while not str.isalpha(in_type) or len(in_type) != 3:
        in_type = input_box("请输入数据分析编号（3位字母）", 2, 3)

    in_count = input_box("请输入要生成带数据分析功能的防伪码数量：", 1, 0)
    while int(in_count) == 0:
        in_count = input_box("请输入要生成带数据分析功能的防伪码数量：", 1, 0)

    ffcode(in_count, in_type, "", choice)


def ffcode(count, type_str, is_message, choice):
    """
    生成含数据分析功能防伪编码函数
    :param count: 要生成的防伪码数量
    :param type_str: 用于数据分析的字符串
    :param is_message: 在输出完毕后是否显示提示信息，'no' 则不显示
    :param choice: 设置输出的文件名称
    :return:
    """
    str_list = []
    for i in range(int(count)):
        # 取得三个字母中的第一个字母，并转为大写，区域分析码
        str_pro = type_str[0].upper()
        # 取得三个字母中的第二个字母，并转为大写，颜色分析码
        str_type = type_str[1].upper()
        # 取得三个字母中的第三个字母，并转为大写，版本分析码
        str_class = type_str[2].upper()

        temp_str = random.sample(number, 3)
        sequence_str = sorted(temp_str)

        letter_one = ''
        for j in range(9):
            letter_one += random.choice(number)

        sim = str(letter_one[0:int(sequence_str[0])]) + str_pro
        sim = sim + str(letter_one[int(sequence_str[0]):int(sequence_str[1])]) + str_type
        sim = sim + str(letter_one[int(sequence_str[1]):int(sequence_str[2])]) + str_class
        sim = sim + str(letter_one[int(sequence_str[2]):9]) + "\n"

        str_list.append(sim)

    write_file(str_list, type_str + "generate_code" + str(choice) + ".txt", is_message, "生成含数据分析功能的防伪码共计：", "str_code")


def generate_code5(choice):
    """
    利用文件批量生成带数据分析功能的防伪码
    :param choice:
    :return:
    """
    default_dir = os.path.join(os.getcwd(), 'auto_code.mri')

    file_path = askopenfilename(filetypes=[("Text file", "*.mri")], title=u"请选择智能批处理文件：", initialdir=(os.path.expanduser(default_dir)))
    code_list = openfile(file_path)
    code_list = code_list.split("\n")
    print(code_list)

    for item in code_list:
        count_str = item.split(",")[0]
        type_str = item.split(",")[1]
        ffcode(count_str, type_str, "no", choice)


def generate_code6(choice):
    """
    补充生成防伪码
    :param choice:
    :return:
    """
    default_dir = r'add_generate_code5.txt'
    file_path = askopenfilename(title=u'请选择已生成的防伪码文件', initialdir=(os.path.expanduser(default_dir)))
    code_list = openfile(file_path)
    code_list = code_list.split("\n")
    code_list.remove("")
    str_set = code_list[0]
    remove_digits = str_set.maketrans("", "", digits)

    res_letter = str_set.translate(remove_digits)
    nres_letter = list(res_letter)
    str_pro = nres_letter[0]
    str_type = nres_letter[1]
    str_class = nres_letter[2]

    nres_letter = str_pro.replace(''''', '').replace(''''', '') + str_type.replace(''''', '').replace(''''', '') + str_class.replace(''''', '').replace(''''', '')
    card = set(code_list)

    tkinter.messagebox.showinfo("提示", "之前的防伪码共计：" + str(len(card)))
    root.withdraw()

    in_count = input_box("请输入补充的防伪码数量：", 1, 0)

    str_list = []
    for i in range(int(in_count) * 2):
        temp_str = random.sample(number, 3)
        sequence_str = sorted(temp_str)
        add_count = len(card)
        str_one = ""
        for j in range(9):
            str_one = str_one + random.choice(number)

        sim = str(str_one[0:int(sequence_str[0])]) + str_pro
        sim = sim + str(str_one[int(sequence_str[0]):int(sequence_str[1])]) + str_type
        sim = sim + str(str_one[int(sequence_str[1]):int(sequence_str[2])]) + str_class
        sim = sim + str(str_one[int(sequence_str[2]):9]) + "\n"

        card.add(sim)

        if len(card) > add_count:
            str_list.append(sim)
            add_count = len(card)
        if len(str_list) >= int(in_count):
            print(len(str_list))
            break

    write_file(str_list, nres_letter + "new_code" + str(choice) + ".txt", nres_letter, "生成补充防伪码共计：", "code_add")


def generate_code7(choice):
    """
    生成条形码
    :param choice:
    :return:
    """
    main_id = input_box("请输入EN13的国家代码（3位）", 1, 0)
    while int(main_id) < 1 or len(main_id) != 3:
        main_id = input_box("请输入EN13的国家代码（3位）", 1, 0)

    com_id = input_box("请输入企业代码（4位）", 1, 0)
    while int(com_id) < 1 or len(com_id) != 4:
        com_id = input_box("请输入企业代码（4位）", 1, 0)

    in_count = input_box("请输入要生成的条形码数量：", 1, 0)
    while int(in_count) == 0:
        in_count = input_box("请输入要生成的条形码数量：", 1, 0)

    mkdir("barcode")
    for i in range(int(in_count)):
        str_one = ''
        for j in range(5):
            str_one = str_one + str(random.choice(number))
        barcode = main_id + com_id + str_one
        # 计算条形码的校验位
        even_sum = int(barcode[1]) + int(barcode[3]) + int(barcode[5]) + int(barcode[7]) + int(barcode[9]) + int(barcode[11])
        odd_sum = int(barcode[0]) + int(barcode[2]) + int(barcode[4]) + int(barcode[6]) + int(barcode[8]) + int(barcode[10])

        check_bit = int((10 - (even_sum * 3 + odd_sum) % 10) % 10)
        barcode = barcode + str(check_bit)
        encoder = EAN13Encoder(barcode)
        encoder.save("barcode\\" + barcode + ".png")


def generate_code8(choice):
    """
    批量生成二维码
    :param choice:
    :return:
    """
    in_count = input_box("请输入要生成的12位数字的二维码数量：", 1, 0)
    while int(in_count) == 0:
        in_count = input_box("请输入要生成的12位数字的二维码数量：", 1, 0)

    mkdir("qrcode")
    for i in range(int(in_count)):
        str_one = ''
        for j in range(12):
            str_one += str(random.choice(number))
        encoder = qrcode.make(str_one)
        encoder.save("qrcode\\" + str_one + ".png")


if __name__ == '__main__':
    main()
