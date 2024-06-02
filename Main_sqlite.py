from datetime import datetime


import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

import parking.service_sqlite as service
import sys
import img.background_rc

import parking.date0 as date0
from UI.loginpage import Ui_loginpage
from UI.wuqixinxi import Ui_wuqixinxi
from qframelesswindow import FramelessWindow
from parking.plts import bing_tu_1,bing_tu,zhu_zhuangtu,fee_plt,shiduan,jiedai
# 有几个页面定义几个class!!!!!!
class login_window(QtWidgets.QMainWindow, Ui_loginpage):  # 定义的loginpageh
    def __init__(self):
        super(login_window, self).__init__()
        self.setupUi(self)  # 创建窗体对象
        self.init()
        self.VerificationCode = "92390"

    def init(self):
        self.denglu.clicked.connect(self.login_button)  # 连接槽..

    def login_button(self):
        service.userName = self.username.text()  # 全局变量，记录用户名
        self.userPwd = self.password.text()  # 记录用户密码
        if self.username.text() == "":
            QMessageBox.warning(self, '警告', '账号不能为空，请输入！')
            return None
        if self.password.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
            return None
        if self.lineEdit_3.text() == "":
            QMessageBox.warning(self, '警告', '验证码不能为空，请输入！')
            return None
        if service.userName != "" and self.userPwd != "":  # 判断用户名和密码不为空
            # 根据用户名和密码查询数据
            result = service.query("select * from id where name = ? and password= ?", service.userName,
                                   self.userPwd)
            if len(result) > 0 and self.lineEdit_3.text() == self.VerificationCode:  # 如果查询结果大于0，说明存在该用户，可以登录
                ww.show()  # 显示主窗体
                w.close()  # 隐藏当前的登录窗体
            elif len(result) == 0:
                QMessageBox.critical(self, '错误', '账号或密码错误！')
                self.username.clear()
                self.password.clear()
                self.lineEdit_3.clear()
                return None
            elif self.lineEdit_3.text() != self.VerificationCode:
                QMessageBox.critical(self, '错误', '验证码错误！')
                self.lineEdit_3.clear()
                return None
            else:
                QMessageBox.critical(self, '错误', '错误！')
                self.username.clear()
                self.password.clear()
                self.lineEdit_3.clear()
                return None
class wuqixinxiwindow(QtWidgets.QMainWindow, Ui_wuqixinxi):

    def __init__(self):
        super(wuqixinxiwindow, self).__init__()
        self.setupUi(self)  # 创建窗体对象
        self.init()
    def init(self):
        self.wp_information_1.itemClicked.connect(self.getItem)  # 获取选中的单元格数据
        self.btnQuery.clicked.connect(self.query)  # 绑定刷新按钮的单击信号
        self.bindGrade()
        self.wp_Model()
        self.zhgl.clicked.connect(self.zhgl_button)  # 连接槽
        self.wqtj.clicked.connect(self.wqtj_button)
        self.crkgl.clicked.connect(self.crkgl_button)
        self.qzxx.clicked.connect(self.qzxx_button)
        self.whby.clicked.connect(self.whby_button)
        self.qywqxx.clicked.connect(self.qywqxx_button)
        self.afgl.clicked.connect(self.afgl_button)
        self.query()  # 窗体加载时显示所有数据
        self.query_1()
        self.wp_information_1.itemClicked.connect(self.getItem)  # 获取选中的单元格数据
        self.genggai.clicked.connect(self.genggai_button)
        self.luru.clicked.connect(self.luru_button)
        self.btnEdit.clicked.connect(self.edit)  # 绑定修改按钮的单击信号
        self.search_1.clicked.connect(self.query_1)
        self.dengji.clicked.connect(self.dengji_button)
        self.dengji_1.clicked.connect(self.dengji_1_button)
        self.get_time.clicked.connect(self.get_time_button)
        self.get_time_1.clicked.connect(self.get_time_1_button)
        self.sel_car.clicked.connect(self.sel_car_button)
        self.shijian_fenbu_2.clicked.connect(self.shijian_fenbu_button)
        self.zhoufanmang_2.clicked.connect(self.zhoufanmang_button)
        self.fee_2.clicked.connect(self.fee_button)  # 绑定修改按钮的单击信号
        self.gaofeng_2.clicked.connect(self.gaofeng_button)
        self.jiedai.clicked.connect(self.jiedai_button)
        self.zonghe_2.clicked.connect(self.zonghe_button)
        self.zonghe_3.clicked.connect(self.zonghe_3_button)

    def shijian_fenbu_button(self):
        self.stackedWidget_2.setCurrentIndex(0)
        zhu_zhuangtu()
        pixmap = QPixmap(r"Visual/zhuzhuang_tu.png")  # 创建相应的QPixmap对象
        self.shijian_fenbu.setScaledContents(True)  # 设置铺满
        self.shijian_fenbu.setPixmap(pixmap)  # 显示lena图像
    def zhoufanmang_button(self):
        self.stackedWidget_2.setCurrentIndex(1)
        bing_tu_1()

        pixmap = QPixmap(r"Visual/bing_tu_2.png")  # 创建相应的QPixmap对象
        self.zhoufanmang.setScaledContents(True)  # 设置铺满
        self.zhoufanmang.setPixmap(pixmap)  # 显示lena图像
    def fee_button(self):
        self.stackedWidget_2.setCurrentIndex(2)
        fee_plt()

        pixmap = QPixmap(r"Visual/fee.png")  # 创建相应的QPixmap对象
        self.fee.setScaledContents(True)  # 设置铺满
        self.fee.setPixmap(pixmap)  # 显示lena图像
    def gaofeng_button(self):
        self.stackedWidget_2.setCurrentIndex(3)
        shiduan()
        pixmap = QPixmap(r"Visual/shiduan.png")  # 创建相应的QPixmap对象
        self.gaofeng.setScaledContents(True)
        self.gaofeng.setPixmap(pixmap)


    def jiedai_button(self):
        self.stackedWidget_2.setCurrentIndex(4)
        jiedai()

        pixmap = QPixmap(r"Visual/cc.png")  # 创建相应的QPixmap对象
        self.jiedaitj.setScaledContents(True)  # 设置铺满
        self.jiedaitj.setPixmap(pixmap)  # 显示lena图像
    def zonghe_button(self):
        self.stackedWidget_2.setCurrentIndex(5)

    def zonghe_3_button(self):
        self.stackedWidget_2.setCurrentIndex(6)

    def get_time_button(self):
        self.in_time.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    def get_time_1_button(self):
        self.out_time_1.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    def dengji_button(self):
        id =self.car_id.text()
        in_time =str(self. in_time.text())
        week_day=date0.get_weekday(in_time)
        Time_period=date0.get_timeperiod(in_time)
        self.result1 = service.exec("insert into car (id, in_time,state,wel,Time_period) values (?, ?,?,?,?)",
                                    (id, in_time,0,week_day,Time_period))
        if self.result1 > 0:  # 如果结果大于0，说明修改成功
            QMessageBox.information(self, '提示', '登记成功！')
            self.car_id.clear()
            self.in_time.clear()
    def dengji_1_button(self):
        self.id1=self.car_id_1.text()
        self.out_time=self.out_time_1.text()
        if self.out_time=="右侧获取时间": #
            QMessageBox.information(self, '提示', '右侧获取时间！')
        elif self.id1=="" or self.out_time==""or len(self.id1)<=5:
            QMessageBox.information(self, '提示', '请检查输入！')
        elif self.id1!="" or self.out_time!="":
            self.result=service.exec(" update car set out_time = ?, state = ? where id = ?",
                                      (self.out_time, 1, self.id1))
            if len(self.result)>0:
                QMessageBox.information(self, '提示', '登记成功！')
            else:
                QMessageBox.information(self, '提示', '登记失败！')
        else:
            QMessageBox.information(self, '提示', '未知错误！')
    def sel_car_button(self):
        id0=self.car_id_1.text()

        if id0 =="" or len(id0)<5:
            QMessageBox.information(self, '提示', 'id最少为五位')
        else:
            result = service.query(
                "select id,in_time,state from car where id=? and state=? ",
                id0, 0)
            if len(result)>0:
                self.in_time_1.setText(str(result[0][1]))
            else:
                QMessageBox.information(self, '提示', '未登记！')
    def genggai_button(self):

        if self.name_1.text() == "" or self.name_2.text() == "":
            QMessageBox.warning(self, '警告', '账号不能为空，请输入！')
            return None
        if self.ps_3.text() == "" or self.ps_2.text() == "" or self.ps_1.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
            return None

        elif self.name_1.text() == service.userName and self.ps_3 != "":
            result = service.query("select * from id where name = ? and password= ?", service.userName,
                                   self.ps_3.text())
            if len(result) > 0:
                result1 = service.exec(" update id set name = ?, password = ? where name = ?",
                                      (self.name_2.text(), self.ps_2.text(), self.name_1.text()))
                if result1 > 0:  # 如果结果大于0，说明修改成功
                    QMessageBox.information(self, '提示', '信息修改成功！')
                    self.name_1.clear()
                    self.name_2.clear()
                    self.ps_3.clear()
                    self.ps_2.clear()
                    self.ps_1.clear()
            elif len(result) == 0:
                QMessageBox.critical(self, '错误', '账号或密码错误！')
                self.name_1.clear()
                self.name_2.clear()
                self.ps_3.clear()
                self.ps_2.clear()
                self.ps_1.clear()
                return None

        else:
            QMessageBox.critical(self, '错误', '错误！')
            self.name_1.clear()
            self.name_2.clear()
            self.ps_3.clear()
            self.ps_2.clear()
            self.ps_1.clear()
            return None

    def luru_button(self):
        print("hhh") # 打开 stackedWidget > page_0
    def zhgl_button(self):
        self.stackedWidget.setCurrentIndex(0)  # 打开 stackedWidget > page_0

    def wqtj_button(self):

        self.stackedWidget.setCurrentIndex(1)
        result_0= service.query("select state from car where state=?",0)
        c = 100
        b = c - len(result_0)
        a = len(result_0)
        self.SubtitleLabel.setText("总车位：" + str(c))
        self.SubtitleLabel_4.setText("占用车位："+str(a))
        self.bq.setText("剩余车位：" + str(b))
        bing_tu(["占用车位", "剩余车位"], [a, b], ['gold', 'lightskyblue'])
        self.ImageLabel.setPixmap(QPixmap(""))
        pixmap = QPixmap(r"Visual/bing_tu.png")  # 创建相应的QPixmap对象
        self.ImageLabel.setScaledContents(True)  # 设置铺满
        self.ImageLabel.setPixmap(pixmap)
    def crkgl_button(self):
        self.stackedWidget.setCurrentIndex(2)
    def qzxx_button(self):
        self.stackedWidget.setCurrentIndex(3)
        self.query()
    def whby_button(self):
        self.stackedWidget.setCurrentIndex(4)
        self.query_1()
    def qywqxx_button(self):
        self.stackedWidget.setCurrentIndex(5)
    def afgl_button(self):
        self.stackedWidget.setCurrentIndex(6)
    def query(self):

        self.wp_information_1.setRowCount(0)  # 清空表格中的所有行
        gname = self.cboxClass.currentText()  # 记录选择的大类
        cname = self.cboxGrade.currentText()  # 记录选择的型号
        if cname == "所有"and gname != "所有":
            result = service.query(
                "select id,in_time,out_time,Time_period,time,wel ,fee from car where Time_period=? and state=? ",
                gname,1)
            # 获取指定枪支信息
        elif cname != "所有" and gname == "所有":
            result = service.query(
                "select id,in_time,out_time,Time_period,time,wel ,fee from car where wel=? and state=?",
                cname,1)
        elif cname != "所有" and gname != "所有":
            result = service.query(
                "select id,in_time,out_time,Time_period,time,wel ,fee from car where wel=? and Time_period=? and state=?",
                cname, gname,1)
        elif cname == "所有"and gname == "所有":
            result = service.query(
                "select id,in_time,out_time,Time_period,time,wel ,fee from car where state=?",1)
        row = len(result)
        self.wp_information_1.setRowCount(row)  # 设置表格行数
        self.wp_information_1.setColumnCount(7)  # 设置表格列数

        # 设置表格的标题名称
        self.wp_information_1.setHorizontalHeaderLabels(['车牌', '驶入时间', '驶出时间', '时段', '停留时间', '星期','费用'])
        for i in range(row):  # 遍历行
            for j in range(7):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.wp_information_1.setItem(i, j, data)
        self.wp_information_1.resizeColumnsToContents()  # 使列宽跟随内容改变
        self.wp_information_1.resizeRowsToContents()  # 使行高度跟随内容改变
        self.wp_information_1.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.wp_information_1.horizontalHeader().setStretchLastSection(True)  # 设置最后一列自动填充容器

    def query_1(self):

        self.TableWidget_3.setRowCount(0)  # 清空表格中的所有行
        self.id = self.locationID.text()  # 记录选择的大类
        if self.id != "":

            result2 = service.query(
                "select id,in_time,Time_period,time,wel ,fee from car where state=? and id=? ",
                0,id)
        else:
            result2 = service.query(
                "select id,in_time,Time_period,time,wel ,fee from car where state=? ",0)

        row = len(result2)
        for i in range(row):  # 遍历行
            for j in range(6):  # 遍历列
                if j==3:
                    date_string = result2[i][1]
                    date_obj = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
                    now_time = datetime.now()
                    self.time_0 = now_time - date_obj
                    fee=3*(self.time_0.seconds // 3600+1)#一个小时3块
                    self.result1 = service.exec(
                        "update car set time=? , fee=? where state = ? and id = ?",
                        (str(self.time_0),fee, 0,str(result2[i][0])))
        if self.id != "":

            result = service.query(
                        "select id,in_time,Time_period,time,wel ,fee from car where state=? and id=? ",
                        0, id)
        else:
            result = service.query(
                        "select id,in_time,Time_period,time,wel ,fee from car where state=? ", 0)

        row = len(result)
        self.TableWidget_3.setRowCount(row)  # 设置表格行数
        self.TableWidget_3.setColumnCount(6)  # 设置表格列数
        # 设置表格的标题名称
        self.TableWidget_3.setHorizontalHeaderLabels(['车牌', '驶入时间', '时段', '计时', '星期', '费用'])
        for i in range(row):  # 遍历行
            for j in range(6):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))
                self.TableWidget_3.setItem(i, j, data)

        self.TableWidget_3.resizeColumnsToContents()  # 使列宽跟随内容改变
        self.TableWidget_3.resizeRowsToContents()  # 使行高度跟随内容改变
        self.TableWidget_3.setAlternatingRowColors(True)  # 使表格颜色交错显示
        self.TableWidget_3.horizontalHeader().setStretchLastSection(True)  # 设置最后一列自动填充容器
    def bindGrade(self):
            self.cboxGrade.clear()  # 清空列表
            self.cboxGrade.addItem("所有")
            result = service.query("select wel from car")
            class_1 =list(set(result))
            for i in class_1:  # 遍历查询结果
                self.cboxGrade.addItem(i[0])


    def wp_Model(self): #下拉列表
            self.cboxClass.clear()  # 清空列表
            self.cboxClass.addItem("所有")  # 增加首选项
            result = service.query("select Time_period from car ")
            #result = service.query("select Time_period from car_num where we_day=?",
            #                      self.cboxGrade.currentText())
            class_2 = list(set(result))
            for i in class_2:  # 遍历查询结果
                self.cboxClass.addItem(i[0])





    def getItem(self, item):
        if item.column() == 0:  # 如果单击的是第一列
            self.select = item.text()  # 获取单击的单元格文本
            self.editID.setText(self.select)
            result = service.query("select * from car where id=?",
                                   self.select)
            self.editName.setText(str(result[0][1]))
            self.editAge.setText(str(result[0][2]))
            self.editPhone.setText(str(result[0][6]))
            self.editAddress.setText(str(result[0][5]))
            self.cboxSex.setText(str(result[0][7]))
        # 获取选中的表格内容

    def edit(self):
        try:
            new_out_time = self.editAge.text()
            new_period = self.cboxSex.text()
            new_wek = self.editAddress.text()
            new_in_time = self.editName.text()
            result = service.exec(
                "update car set wel = ?, in_time = ?, out_time = ?, Time_period = ? where id = ?",
                (new_wek, new_in_time, new_out_time, new_period, self.editID.text()))
            if result > 0:  # 如果结果大于0，说明修改成功
                self.query()  # 在表格中显示最新数据
                QMessageBox.information(self, '提示', '信息修改成功！')
        except :

            QMessageBox.warning(self, '警告', '修改失败！')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = login_window()
    ww = wuqixinxiwindow()
    w.show()

    sys.exit(app.exec_())
