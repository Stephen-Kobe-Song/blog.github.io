import os
filename = 'student.txt'


def insert():
    student_list = []
    while True:
        id = input('请输入你的id（1001）：')
        if not id :
            break
        name = input('请输入你的姓名：')
        if not name:
            break

        try:
            english = int(input('请输入你的英语成绩'))
            Python = int(input('请输入你的Python成绩'))
            Java = int(input('请输入你的Java成绩'))

        except:
            print("您的输入不合法，请重新输入！")
            continue

        student = {'id': id, 'name': name, 'english': english, 'python': Python, 'java': Java}
        student_list.append(student)
        answer = input('请问是否继续添加：（y/n）:\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print('学生信息录入完毕')


def save(lst):
    try:
        sut_txt = open(filename, 'a', encoding='utf-8')
    except:
        sut_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        sut_txt.write(str(item) + '\n')

    sut_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = int(input('按id查找请输入1，按姓名查找请输入2：'))
            if mode == 1:
                id = input('请输入id：')
            elif mode == 2:
                name = input('请输入姓名！')
            else:
                print('您的输入有误！请重新输入。')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                for item in rfile:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    if name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('请问是否继续操作？（Y/N）\n')
            if answer == 'y' or answer =='Y':
                continue
            else:
                break

        else:
            print('未保存任何学员信息！')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有找到学生信息！')
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}\t'
    for item in lst:
        print(format_data.format(item.get('id'), item.get('name'), item.get('english'),
                                 item.get('python'), item.get('java'), int(item.get('english'))
                                 + int(item.get('python')) + int(item.get('java'))))


def delete():
    while True:
        student_id = input('请输入你要删除的id:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True

                    if flag:
                        print(f'id为{student_id}已被删除')
                    else:
                        print(f'没有找到id为{student_id}的信息')
            else:
                print('无任何学生的信息')
                break
            show()
            answer = input('是否继续删除？（y/n)\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学生id：')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生相关信息，可以进行修改了。')
                while True:
                    try:
                        d['name'] =input('请输入姓名：')
                        d['english'] = input('请输入英语成绩：')
                        d['python'] = input('请输入python成绩：')
                        d['java'] = input('请输入Java成绩：')
                    except:
                        print('您的输入有误，请重新输入')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！')
            else:
                wfile.write(str(d))
        answer = input('是否继续删除？（y/n）:\n')
        if answer == 'y' or answer == 'Y':
            modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
    else:
        print('暂时没有数据！！！')
        return
    asc_or_desc = int(input('请选择升序降序（0.升序，1.降序）：'))
    if asc_or_desc == 0:
        asc_or_desc_bool = False
    elif asc_or_desc == 1:
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入！')
        sort()
    mode = int(input('选择按什么排序（1，按英语成绩排序。2，按python成绩。3.按Java成绩排序。0，按总成绩排序：'))
    if mode == 1:
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == 2:
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == 3:
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == 0:
        student_new.sort(key=lambda x: int(x['java'])+int(x['python']) +int(x['english']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误！')
        sort()

    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('未录入学生信息！')

    else:
        print('暂未保存学生信息！')


def show():
    student_list = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_list.append(eval(item))
            if student_list:
                show_student(student_list)
    else:
        print('暂时没有学生数据！！！')

def main():
    while True:
        menu()
        choice = int(input('请选择你要的功能:'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定选择推出么？(y/n):')
                if answer == 'y' or answer == 'Y':
                    print('感谢您的使用!')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('=============================学生管理系统===================================')
    print('------------------------------功能菜单--------------------------------------')
    print('\t\t\t\t\t\t 1. 录入学生信息')
    print('\t\t\t\t\t\t 2. 查找学生信息')
    print('\t\t\t\t\t\t 3. 删除学生信息')
    print('\t\t\t\t\t\t 4. 修改学生信息')
    print('\t\t\t\t\t\t 5. 排序')
    print('\t\t\t\t\t\t 6. 统计学生总数')
    print('\t\t\t\t\t\t 7. 显示学生信息')
    print('\t\t\t\t\t\t 0. 退出')


if __name__ == '__main__':
    main()