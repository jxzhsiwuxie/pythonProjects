# _*_ coding: utf-8 _*_

import re
from operations import *


# 主函数
def main():
    in_system = True
    while in_system:
        show_menu.show()

        option = input('请选择：')
        option_str = re.sub(r'\D', '', option)

        if option_str in [str(x) for x in range(8)]:
            option_int = int(option_str)

            if option_int == 0:
                print('您已推出学生信息管理系统。')
                in_system = False
            elif option_int == 1:
                insert.insert()
            elif option_int == 2:
                search.search()
            elif option_int == 3:
                delete.delete()
            elif option_int == 4:
                update.update()
            elif option_int == 5:
                sort.sort()
            elif option_int == 6:
                total.total()
            elif option_int == 7:
                show_menu.show()
            else:
                continue




