# _*_ coding: utf-8 _*_
import re
import os

file_path = r'students.txt'


# 主函数
def main():
    in_system = True
    while in_system:
        show_menu()

        option = input('请选择：')
        option_str = re.sub(r'\D', '', option)

        if option_str in [str(x) for x in range(8)]:
            option_int = int(option_str)

            if option_int == 0:
                print('您已推出学生信息管理系统。')
                in_system = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                update()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show_all()
            else:
                continue


# ################################ 显示操作菜单 ################################
def show_menu():
    print('''
    ╔════════════════════════════════学生信息管理系统════════════════════════════════╗
    ║                                                                                ║
    ║               ════════════════════功能菜单════════════════════                 ║ 
    ║                                                                                ║ 
    ║               1   学生信息录入                                                 ║
    ║               2   查找学生信息                                                 ║
    ║               3   删除学生信息                                                 ║
    ║               4   修改学生信息                                                 ║
    ║               5   排序                                                         ║ 
    ║               6   统计学生人数                                                 ║
    ║               7   显示所有学生信息                                             ║
    ║               0   推出系统                                                     ║
    ║                                                                                ║
    ║               ═════════════════════════════════════════════════                ║
    ║               说明：通过数字键选择菜单                                         ║
    ║                                                                                ║
    ╚════════════════════════════════════════════════════════════════════════════════╝
    ''')


# ################################ 插入学生信息 ################################
def insert():
    student_list = []
    continue_insert = True

    while continue_insert:
        student_id = input(' 请输入 ID 例如：（100）：')
        if not student_id:
            break
        student_name = input('请输入名字：')
        if not student_name:
            break
        try:
            english_score = float(input('请输入英语出成绩：'))
            python_score = float(input('请输入python成绩：'))
            c_score = float(input('请输入c语言成绩：'))
        except ValueError as e:
            print(e)
            print('输入值不是数字，请重新录入信息')
            continue

        # 将输入的学生信息保存到字典中
        student = {'id': student_id, 'name': student_name, 'english': english_score, 'python': python_score, 'c': c_score}
        student_list.append(student)

        continue_mark = input('是否继续添加？（y/n）：')
        if continue_mark == 'y':
            continue_insert = True
        else:
            continue_insert = False

    # 循环结束后将学生列表保存
    save(student_list)
    print('学生信息录入完毕。')


# ################################ 根据学生 ID 或者姓名查找学生信息 ################################
def search():
    continue_mark = True

    # 用于保存查找结果的列表
    query_result = []

    while continue_mark:
        search_id = ''
        search_name = ''

        if os.path.exists(file_path):
            mode = input('按 ID 查询输入1；按姓名查询输入2：')
            if mode == '1':
                search_id = input('输入学生 ID：')
            elif mode == '2':
                search_name = input('输入学生姓名：')
            else:
                print('输入模式错误，请重新输入')
                search()

            with open(file=file_path, mode='r') as file:
                student_list = file.readlines()
                for student in student_list:
                    d = dict(eval(student))
                    if search_id is not '':
                        if d['id'] == search_id:
                            query_result.append(d)
                    elif search_name is not '':
                        if d['name'] == search_name:
                            query_result.append(d)

            # 显示查找到的学生信息
            show_students(query_result)
            # 清空查找到的列表
            query_result.clear()

            input_mark = input('是否继续查找？（y/n）：')
            if input_mark == 'y':
                continue_mark = True
            else:
                continue_mark = False

        else:
            print('暂时还没有学生信息')
            return


# ################################ 根据学生 id 删除一条学生信息 ################################
def delete():
    continue_mark = True
    while continue_mark:

        student_id = input('输入想要删除的学生的 ID：')
        if student_id is not '':
            if os.path.exists(file_path):
                with open(file=file_path, mode='r') as rfile:
                    # 读取全部内容
                    student_old = rfile.readlines()
            else:
                student_old = []

            # 标记是否删除
            ifdel = False
            if student_old:
                with open(file=file_path, mode='w') as wfile:
                    d = {}
                    for student in student_old:
                        d = dict(eval(student))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            # 标记已删除
                            ifdel = True
                    if ifdel:
                        print('ID 为{}的学生已删除...'.format(student_id))
                    else:
                        print('没有找到 ID 为 {} 的学生'.format(student_id))
            else:
                print('暂时还没有学生信息....')
                break

            show_menu()
            input_mark = input('是否继续删除？（y/n）：')
            if input_mark == 'y':
                continue_mark = True
            else:
                continue_mark = False


# ################################ 修改学生信息 ################################
def update():
    show_all()

    # 判断存储文件是否存在
    if os.path.exists(file_path):
        with open(file=file_path, mode='r') as rfile:
            # 读取全部学生
            students_old = rfile.readlines()
    else:
        return

    update_id = input('输入要修改的学生的 ID：')
    with open(file=file_path, mode='w') as wfile:
        for student in students_old:
            d = dict(eval(student))
            if d['id'] == update_id:
                print('找到了这个学生，可以修改他的信息')
                while True:
                    try:
                        d['name'] = input('输入修改后的姓名：')
                        d['english'] = float(input('输入修改后的英语成绩：'))
                        d['python'] = float(input('输入修改后的 python 成绩：'))
                        d['c'] = float(input('输入修改后的 c 语言成绩：'))
                    except Exception as e:
                        print(e)
                        print('输入的信息有误，请重新输入：')
                    else:
                        break

                # 将修改后的字典转为字符串
                student = str(d)

                wfile.write(student + '\n')
                print('修改成功')
            else:
                wfile.write(student)

    continue_mark = input('是否继续修改其他学生信息？（y/n）：')
    if continue_mark == 'y':
        update()


# ################################ 按成绩排序显示 ################################
def sort():
    show_all()

    if os.path.exists(file_path):
        with open(file=file_path, mode='r') as f:
            students_old = f.readlines()
            sorted_list = []
        for student in students_old:
            d = dict(eval(student))
            sorted_list.append(d)

    else:
        return

    asc_or_desc = input('请选择（0升序；1降序）：')
    if asc_or_desc == '0':
        asc_or_desc = False
    elif asc_or_desc == '1':
        asc_or_desc = True
    else:
        print('输入错误，请重新输入')
        sort()

    sort_mode = input('请选择排序方式（1按英语成绩，2按python成绩，3按c语言成绩，0按总成绩）：')
    if sort_mode == '1':
        sorted_list.sort(key=lambda x: x['english'], reverse=asc_or_desc)
    elif sort_mode == '2':
        sorted_list.sort(key=lambda x: x['python'], reverse=asc_or_desc)
    elif sort_mode == '3':
        sorted_list.sort(key=lambda x: x['c'], reverse=asc_or_desc)
    elif sort_mode == '0':
        sorted_list.sort(key=lambda x: x['english'] + x['python'] + x['c'], reverse=asc_or_desc)
    else:
        print('输入错误，请重新输入')
        sort()

    show_students(sorted_list)


# ################################ 显示学生总数 ################################
def total():
    if os.path.exists(file_path):
        with open(file=file_path, mode='r') as f:
            student_list = f.readlines()
            if student_list:
                print('总共有 {} 名学生'.format(len(student_list)))
            else:
                print('还没有录入学生信息')
    else:
        print('还没保存数据')


# ################################ 显示所有学生 ################################
def show_all():
    student_list = []

    if os.path.exists(file_path):
        with open(file=file_path, mode='r') as f:
            students_old = f.readlines()
            for student in students_old:
                student_list.append(eval(student))
        if student_list:
            show_students(student_list)
    else:
        print('暂时还未保存信息')


# ################################ 辅助函数，展示列表中的信息 ################################
def show_students(student_list):
    if not student_list:
        print('没有要显示的学生信息')
        return

    # 定义标题显示格式
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "姓名", "英语成绩", "python成绩", "C语言成绩", "总成绩"))

    # 定义内容显示格式
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in student_list:
        print(format_data.format(
            info.get('id'), info.get('name'), str(info.get('english')),
            str(info.get('python')), str(info.get('c')),
            str(info.get('english') + info.get('python') + info.get('c'))
        ))


# ################################ 辅助函数保存学生信息 ################################
def save(student_list):
    try:
        # 以追加的模式打开文件
        student_txt = open(file=file_path, mode='a')
    except Exception as e:
        # 文件不存在，新创建一个文件并打开
        student_txt = open(file=file_path, mode='w')
    for info in student_list:
        # 按行存储学生信息
        student_txt.write(str(info) + '\n')
    student_txt.close()


if __name__ == "__main__":
    main()
