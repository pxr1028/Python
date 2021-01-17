import time
scale = 50
print("\033[1;34;47mQ-system正在启动中，请稍等\033[0m".center(scale // 2,"-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = "▋" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end = "")
    time.sleep(0.2)
print("\n"+"加载完成".center(scale // 2,"-"))
# coding=gbk
                                 
print('\033[1;34;43m 欢迎使用Q-system5.02版本，本系统基于Python开发,本次更新内容：优化字体显示，修复部分bug\033[0m')
print('请先登录')
# 编写一个输入用户名及密码的程序，正确则显示登陆成功，
# 如果用户名密码为空，则显示用户名或密码为空，请重新输入；错误则显示输错；超过三次，则无法再输入。
name_t = "pxr"
ps = "pxr20081028"
count = 1
while count <= 3:
    name = input("请输入用户名：")
    password = input("请输入密码：")
    name_b = bool(name)  #转化布尔值，以此判断输入是否为空，下行同
    password_b = bool(password)
    count = count +1
    if password == ps and name==name_t:
        print("登陆成功")
        break
    elif count == 4: #判断输入次数
        print("\033[1;31;40m超过三次，系统锁定\033[0m")
        quit()
    elif name_b == False or password_b == False:
        print("\033[1;31;40m用户名或密码不能为空，请输入用户名及密码。\033[0m")
 
    else:
        print("\033[1;31;40m用户名及密码错误，请重新登陆！\033[0m")
        
        
print('系统:请完善你的个人信息以便系统做出判断')
input()
print('系统:操作指引：按回车键进行下一步操作')
input()
str1 = input("系统:请输入你的班级 \n")

str2 = input("系统:请输入你的学号 \n")

# 提示用户输入想使用的功能
print("输入想使用的功能：1、备忘录；2、智商测试；3、计算机；4、考试分数测试;5、日历")

# 获取用户输入的功能
choice = input("输入你的选择(1/2/3/4):")

#如果是1
if choice == '1':
	print('欢迎使用备忘录功能')

import pickle
class Memo:
    def __init__(self,name,thing,date):
        self._id = 0
        self.name = name
        self.thing = thing
        self.date = date
    def talk(self):
        self._id += 1
        self.name = input('name:')
        self.thing = input('thing:')
        self.date = input('date:')
        one = {'id':self.id,'name':self.name,'thing':self.thing,'date':self.date}
        R.add(one)
    @property
    def id(self): # 只读
        return self._id

class MemoAdmin:
    """管理记录"""
    def __init__(self,memo_list,dir):   # 初始化数据
        self.dir = dir
        self.memo_list = memo_list
    def welcome(self):
        print('欢迎使用小侣AI备忘录'.center(50,'-'))
        for k,v in self.dir.items():
            print(f'{k}:{v}')         # 打印选择选项
        select = input('请选择你的操作选项 (示例 1)：')
        return select
    def add(self,one):    # 增加方法
        self.memo_list.append(one)
        R.query()
        print('增加成功')
    def dele(self):    # 删除方法
        temp = input('请选择你将要删除的记录（示例 1或者2或者3 ）:')
        self.memo_list.pop(int(temp)-1)
        print('删除成功')
        R.query()
    def modify(self):   # 修改方法
        temp1 = input('请输入你要修改的记录（示例 1或者2或者3）:')
        temp2 = input(f'你要修改的记录是{self.memo_list[int(temp1)-1]}，请输入要修改的值（示例：name:zhangsan）:')
        temp3 = temp2.split(':')
        self.memo_list[int(temp1)-1][temp3[0]] = temp3[1]   # 列表中找出嵌套的字典key和value
        print('修改成功')
        R.query()
    def save(self):   # 数据保存在文件内
        with open('db.pkl','wb') as f:
            f.write(pickle.dumps(memo_list))
            print('保存成功')
    def load(self):   # 下载文件
        with open('db.pkl','rb') as f:
            data = pickle.loads(f.read())
            print(data)
            print('下载成功')
    def query(self):   # 查询所有数据
        i = 0
        for k in memo_list:
            i += 1
            print(f'项目{i}{k}')

memo_list = []
dir = {'1':'Add',
        '2':'Dele',
        '3':'Modify',
        '4':'Query',
        '5':'Save',
        '6':'Load'
        }
L = Memo('周杰伦','明天来广州','2018')
R = MemoAdmin(memo_list,dir)
while True:
    t = R.welcome()
    if t == '1':
        L.talk()
    elif t == '2':
        R.dele()    
    elif t == '3':
        R.modify()
    elif t == '4':
        R.query()
    elif t == '5':
        R.save()
    elif t == '6':
        R.load()
    else:
        print('结束')
        break
# 提示用户输入想使用的功能
print("输入想使用的功能：1、备忘录；2、智商测试；3、计算机；4、考试分数测试;5、日历")

#如果是2
if choice == '2':
    print('系统:我可以告诉你你现在的智商（按回车键查看）')
input()
import random 

# 产生 1 到 100 的一个整数型随机数
print( random.randint(1,100 )  ) 

# 提示用户输入想使用的功能
print("输入想使用的功能：1、备忘录；2、智商测试；3、计算机；4、考试分数测试;5、日历")

#如果是3
if choice == '3':
    print('系统：本次更新新增日历功能，诚邀您使用')
input()
# Filename : test.py
# author by : www.runoob.com
 
# 引入日历模块
import calendar
 
# 输入指定年月
yy = int(input("请输入年份: "))
mm = int(input("请输入月份: "))
 
# 显示日历
print(calendar.month(yy,mm))
input()

input()   
print('系统:想知道你考试大概能考几分吗？（本数据为系统测量，会存在误差，纯属娱乐）')
import random
 
# 产生 85 到 100 的一个整数型随机数
print( random.randint(85,100) )   
input()
print('系统:你知道我的开发者是谁吗？')
input()
print('系统:pxr')
input()
# 提示用户输入想使用的功能
print("输入想使用的功能：1、备忘录；2、智商测试；3、计算机；4、考试分数测试;5、日历")

print('系统:我还是一个计算机呢！不信你试试看')

# 打印标题
print("计算器")

# 通过用户输入获取运算的第一个数
num1 = int(input("输入第一个数字: "))
# 通过用户输入获取运算的第二个数
# 默认是字符串需要用int把字符转换为数组
num2 = int(input("输入第二个数字: "))

# 提示用户输入运算符
print("输入运算：1、相加；2、相减；3、相乘；4、相除")

# 获取用户输入的运算符号
choice = input("输入你的选择(1/2/3/4):")

# 如果是1
if choice == '1':
   print(num1,"+",num2,"=", num1+num2)
# 如果2
elif choice == '2':
   print(num1,"-",num2,"=", num1-num2) 
elif choice == '3':
   print(num1,"×",num2,"=", num1*num2) 
elif choice == '4':
   print(num1,"÷",num2,"=", num1/num2)
# 其他都是非法的
else:
   print("错误")
   
 
print('系统:这是Q-system5.02版本的全部内容，感谢您的使用，再见！')
quit()