import datetime

from PyQt5.QtGui import QPixmap
from matplotlib import pyplot as plt
import parking.service as service
from collections import Counter
import numpy as np



# 显示图像在指定的控件中
def show_plot(file_path, control_name):
    pixmap = QPixmap(file_path)  # 加载图像为 QPixmap
    label =control_name  # 获取指定的控件对象
    #label.setPixmap(QPixmap("clear.Visual"))
    label.setPixmap(pixmap)  # 设置 QLabel 的 Pixmap
    label.adjustSize()  # 调整 QLabel 大小以适应图像
    label.setScaledContents(True)  # 让 QLabel 自适应图片大小
def bing_tu( x, y,colors):#,c=0,d=0,e=0,f=0,g=0,h=0
    plt.rcParams['text.color'] = 'black'

    plt.rcParams['figure.figsize']=5,4
    plt.rcParams['font.size'] = 15
    plt.rcParams['font.family'] = 'SimHei'
    plt.pie(y,
            labels=x,  # 设置饼图标签
            colors=colors,# ['gold', 'lightskyblue'],  # 设置饼图颜色
            explode=(0, 0.1),
            autopct='%1.1f%%',
            #shadow=True,
            startangle=90
            )
    plt.title("车位使用率")  # 设置标题

    # 生成图像...
    plt.savefig('./Visual/bing_tu.png',dpi=300)  # 保存图像到文件
    plt.close('all')
def bing_tu_1( ):#,c=0,d=0,e=0,f=0,g=0,h=0
    result = service.query(
        "select wel from car where  state=%s ", 1)

    elements = list(result)
    # 使用 Counter 来统计每个元素的次数
    element_counts = Counter(elements)
    ls = list(element_counts.keys())
    lables=[ls[0][0],ls[1][0],ls[2][0],ls[3][0],ls[4][0],ls[5][0],ls[6][0]]
    sizes = list(element_counts.values())
    plt.rcParams['text.color'] = 'black'

    plt.rcParams['figure.figsize'] = 8, 5
    plt.rcParams['font.size'] = 15
    plt.rcParams['font.family'] = 'SimHei'
    plt.pie(sizes,
            labels=lables,  # 设置饼图标签
            colors= ["#63b2ee","#76da91", "#f8cb7f","#f89588","#7cd6cf","#9192ab","#7898e1"],# ['gold', 'lightskyblue'],  # 设置饼图颜色
            autopct='%1.1f%%',

            startangle=90
            )
    plt.title("周繁忙统计")  # 设置标题
    plt.rcParams['font.size'] = 8
    plt.legend(loc =(-0.5,0))

    # 生成图像...
    plt.savefig('./Visual/bing_tu_2.png',dpi=300)  # 保存图像到文件
    plt.close('all')
def zhu_zhuangtu():
    result = service.query(
        "select time from car where  state=%s ", 1)
    ls = [0, 0, 0, 0, 0, 0]
    # 类统计
    for i in result:
        hours = i[0].total_seconds() / 3600
        if hours < 1:
            ls[0] += 1
        elif 1 <= hours < 2:
            ls[1] += 1
        elif 3 <= hours <= 5:
            ls[2] += 1
        elif 6 <= hours <= 10:
            ls[3] += 1
        elif 11 <= hours <= 12:
            ls[4] += 1
        else:
            ls[5] += 1
    lables = ["一小时以下", "1-2小时", "3-5小时", "6-10小时", "10-12小时", "12小时以上"]
    plt.rcParams['figure.figsize'] = 8, 5
    plt.rcParams['font.size'] = 7
    plt.rcParams['font.family'] = 'SimHei'
    plt.title("停车时长统计")
    plt.bar(lables, ls)
    for x, y in enumerate(ls):
        plt.text(x, y + 20, str(y) + '台', ha='center')
    plt.savefig('./Visual/zhuzhuang_tu.png',dpi=300)
    plt.close('all')
bing_tu_1()

def fee_plt():#使用ax,而不是plt
    x=[]
    y1=[]
    result = service.query(
        "select in_time,fee from car where  state=%s ", 1)
    data = list(result)
    # 创建一个字典来分组日期和费用
    date_dict = {}
    # 遍历数据并计算相同日期的费用总和
    for date, fee in data:
        # 将日期的时间部分设置为0，只保留日期部分
        date = datetime.datetime(date.year, date.month, date.day)
        # 如果日期已经在字典中，就将费用累加
        if date in date_dict:
            date_dict[date] += fee

        # 否则，将日期添加到字典并初始化费用
        else:
            date_dict[date] = fee
    # 打印每个日期对应费用总和
    for date, total_fee in date_dict.items():
        x.append(date)
        y1.append(total_fee)
    fig, ax = plt.subplots(figsize=(8,5))#创建了一个（800*500）的画布
    ax.set_title('收入曲线', fontsize=15,fontfamily ='SimHei')#图名
    ax.set_xlabel('日期', fontsize=10, fontfamily='SimHei', loc='right')
    ax.set_ylabel('收入(元)', fontsize=10, fontfamily='SimHei', loc='top')
    ax.plot(x, y1, label='车次')
    ax.legend( loc=(0.03,0.89))
    plt.savefig('./Visual/fee.png',dpi=300)
    plt.close('all')
def shiduan():
    result = service.query(
        "select Time_period from car where  state=%s ", 1)
    x,y=[],[]
    Time_period = list(result)
    # 创建一个字典来分组日期和费用
    date_dict = {}
    # 遍历数据并计算相同日期的费用总和
    for period in Time_period:
        # 如果日期已经在字典中，就将费用累加
        if period in date_dict:
            date_dict[period] += 1
        # 否则，将日期添加到字典并初始化费用
        else:
            date_dict[period] = 1
    # 打印每个日期对应费用总和
    for Time_period, total_num in date_dict.items():
        x.append(Time_period[0])
        y.append(total_num)
    plt.rcParams['font.family'] = 'SimHei'
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_title('停车时段分布', fontsize=12, fontfamily='SimHei')  # 图名
    ax.pie(y, colors=colors,
           labels=x,
           wedgeprops={"linewidth": 1, "edgecolor": "white"},
           autopct='%1.1f%%',)
    ax.legend(loc =(-0.5,0))

    plt.savefig('./Visual/shiduan.png', dpi=300)
    plt.close('all')
def jiedai():
    x = []
    y1 = []
    result = service.query(
        "select in_time ,fee from car where  state=%s ", 1)
    data = list(result)
    # 创建一个字典来分组日期和费用
    date_num = {}
    # 遍历数据并计算相同日期的费用总和
    for date ,fee in data:
        # 将日期的时间部分设置为0，只保留日期部分
        date =date.strftime("%Y-%m-%d")
        # 如果日期已经在字典中，就将费用累加
        if date in date_num:
            date_num[date] += 1
        # 否则，将日期添加到字典并初始化费用
        else:
            date_num[date] = 1
    # 打印每个日期对应费用总和
    for date, total_num in date_num.items():
        x.append(date)
        y1.append(total_num)
    fig, ax = plt.subplots(figsize=(8, 5))  # 创建了一个（800*500）的画布
    ax.set_title('接待车次曲线', fontsize=15, fontfamily='SimHei')  # 图名
    ax.set_xlabel('日期', fontsize=10, fontfamily='SimHei', loc='right')
    ax.set_ylabel('车次(辆)', fontsize=10, fontfamily='SimHei', loc='top')

    l1, = ax.plot(x, y1, color= "#f89588" ,label='车次')
    ax.legend(handles=[l1, ], labels=[ '车次',], loc=(0.03, 0.89))
    plt.savefig('./Visual/cc.png', dpi=300)
    plt.close('all')

