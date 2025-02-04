import parking.service as service
import sys,time,base64
import img.background_rc

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QApplication

from UI.loginpage import Ui_loginpage
from UI.wuqixinxi import Ui_wuqixinxi

from parking.plts import bing_tu_1,bing_tu,zhu_zhuangtu,fee_plt,shiduan
from datetime import datetime
import parking.date0 as date0
import parking.py_echarts as py_echarts

# 有几个页面定义几个class!!!!!!
class login_window(QtWidgets.QMainWindow, Ui_loginpage):  # 定义的loginpageh
    def __init__(self):
        super(login_window, self).__init__()
        self.setupUi(self)  # 创建窗体对象
        self.init()

    def init(self):
        self.denglu.clicked.connect(self.login_button)  # 连接槽..
        self.zhuce1.clicked.connect(self.zhuce1_button)
        self.zhuce_1.clicked.connect(self.zhuce_1_button)
        self.back_login.clicked.connect(self.back_login_button)
        self.shuaxin.clicked.connect(self.shuaxin_button)
    def shuaxin_button(self):
        global VerificationCode
        VerificationCode=date0.generate_captcha_image()
        pixmap = QPixmap(r"Visual/yanzhengma.png")  # 创建相应的QPixmap对象
        self.yanzhengma.setScaledContents(True)  # 设置铺满
        self.yanzhengma.setPixmap(pixmap)  # 显示lena图像
    def login_button(self):
        service.userName = self.username.text()  # 全局变量，记录用户名
        self.userPwd = self.password.text()  # 记录用户密码
        if self.username.text() == "":
            QMessageBox.warning(self, '警告', '账号不能为空，请输入！')
            return None
        if self.password.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
            return None
        if self.lineEdit_4.text() == "":
            QMessageBox.warning(self, '警告', '验证码不能为空，请输入！')
            return None
        if service.userName != "" and self.userPwd != "":  # 判断用户名和密码不为空
            # 根据用户名和密码查询数据
            result = service.query("select * from id where name = %s and password= %s", service.userName,
                                   self.userPwd)
            if len(result) > 0 and self.lineEdit_4.text() == VerificationCode:  # 如果查询结果大于0，说明存在该用户，可以登录

                ww.show()  # 显示登录窗体
                w.close()  # 隐藏当前的登录窗体
            elif len(result) == 0:
                QMessageBox.critical(self, '错误', '账号或密码错误！')
                self.username.clear()
                self.password.clear()
                self.lineEdit_4.clear()
                return None
            elif self.lineEdit_4.text() != VerificationCode:
                QMessageBox.critical(self, '错误', '验证码错误！')
                self.lineEdit_4.clear()
                return None
            else:
                QMessageBox.critical(self, '错误', '错误！')
                self.username.clear()
                self.password.clear()
                self.lineEdit_3.clear()
                return None

    def zhuce_1_button(self):
        result= service.query("select * from pro_user where pas=%s ", self.pro_Password.text())

        if self.new_username.text()=="" or self.new_Password.text()=="" or self.pro_Password.text()=="" or self.new_Password_1.text()=="":
            QMessageBox.warning(self, '警告', '信息不能为空，请输入！')
            return None
        elif len(self.new_Password.text()) < 6:
            QMessageBox.warning(self, '警告', '密码长度不能小于6位，请重新输入！')
            return None
        elif self.new_Password_1.text() != self.new_Password.text():
            QMessageBox.warning(self, '警告', '两次密码不一致，请重新输入！')
            return None
        elif len(result)==0:
            QMessageBox.warning(self, '警告', '管理员验证失败，请重新输入！')
            self.pro_Password.clear()
            return None
        elif len(result)>0 :
            result1 = service.query("select * from id where name = %s ",self.new_username.text())
            if len(result1)>0:
                QMessageBox.warning(self, '警告', '用户名已存在，请重新输入！')
                self.new_username.clear()
                return None
            elif len(result1)==0:
                service.exec("insert into id (name,password) values(%s,%s)",(self.new_username.text(),self.new_Password.text()))
                QMessageBox.information(self, '提示', '注册成功！')
    def zhuce1_button(self):
        self.stackedWidget.setCurrentIndex(1)
    def back_login_button(self):
        self.stackedWidget.setCurrentIndex(0)




class wuqixinxiwindow(QtWidgets.QMainWindow, Ui_wuqixinxi):

    def __init__(self):
        super(wuqixinxiwindow, self).__init__()

        #self.showMaximized()
        self.setupUi(self)  # 创建窗体对象
        self.init()
        #self.query()  # 窗体加载时显示所有数据

        self.wp_information_1.itemClicked.connect(self.getItem)  # 获取选中的单元格数据
        self.btnQuery.clicked.connect(self.query)  # 绑定刷新按钮的单击信号
        self.bindGrade()
        self.wp_Model()
        # 绑定年级下拉列表
        #self.cboxGrade.currentIndexChanged.connect(self.wp_Model)



        # 根据年级绑定班级列表

    def init(self):
        self.query()  # 窗体加载时显示所有数据
        self.query_1()
        self.zhgl.clicked.connect(self.zhgl_button)  # 连接槽
        self.wqtj.clicked.connect(self.wqtj_button)
        self.crkgl.clicked.connect(self.crkgl_button)
        self.qzxx.clicked.connect(self.qzxx_button)
        self.whby.clicked.connect(self.whby_button)
        self.qywqxx.clicked.connect(self.qywqxx_button)
        self.afgl.clicked.connect(self.afgl_button)

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
        self.ciyun.clicked.connect(self.ciyun_button)
        self.shiduan.clicked.connect(self.shiduan_button)



    def shijian_fenbu_button(self):
        zhu_zhuangtu()
        with open("Visual/zhuzhuang_tu.png", "rb") as f:
            encoded_image = base64.b64encode(f.read()).decode()
        html = f"""
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8">
            <title>Local Image</title>
            <style>
              img {{
                width: 100%;
                height: auto;
              }}
            </style>
          </head>
          <body>
            <img id="myImage" src="data:image/png;base64,{encoded_image}">
            <script>
              function resizeImage() {{
                var image = document.getElementById('myImage');
                var container = image.parentElement;
                image.style.width = container.clientWidth + 'px';
              }}
              window.onload = resizeImage;
              window.onresize = resizeImage;
            </script>
          </body>
        </html>
        """
        self.web.setHtml(html)
    def zhoufanmang_button(self):
        bing_tu_1()
        with open("Visual/bing_tu_2.png", "rb") as f:
            encoded_image = base64.b64encode(f.read()).decode()
        html = f"""
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8">
            <title>Local Image</title>
            <style>
              img {{
                width: 100%;
                height: auto;
              }}
            </style>
          </head>
          <body>
            <img id="myImage" src="data:image/png;base64,{encoded_image}">
            <script>
              function resizeImage() {{
                var image = document.getElementById('myImage');
                var container = image.parentElement;
                image.style.width = container.clientWidth + 'px';
              }}
              window.onload = resizeImage;
              window.onresize = resizeImage;
            </script>
          </body>
        </html>
        """
        self.web.setHtml(html)
    def fee_button(self):
        fee_plt()
        with open("Visual/fee.png", "rb") as f:
            encoded_image = base64.b64encode(f.read()).decode()
        html = f"""
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8">
            <title>Local Image</title>
            <style>
              img {{
                width: 100%;
                height: auto;
              }}
            </style>
          </head>
          <body>
            <img id="myImage" src="data:image/png;base64,{encoded_image}">
            <script>
              function resizeImage() {{
                var image = document.getElementById('myImage');
                var container = image.parentElement;
                image.style.width = container.clientWidth + 'px';
              }}
              window.onload = resizeImage;
              window.onresize = resizeImage;
            </script>
          </body>
        </html>
        """

        self.web.setHtml(html)

    def gaofeng_button(self):
        shiduan()

        with open("Visual/shiduan.png", "rb") as f:
            encoded_image = base64.b64encode(f.read()).decode()

        html = f"""
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8">
            <title>Local Image</title>
            <style>
              img {{
                width: 100%;
                height: auto;
              }}
            </style>
          </head>
          <body>
            <img id="myImage" src="data:image/png;base64,{encoded_image}">
            <script>
              function resizeImage() {{
                var image = document.getElementById('myImage');
                var container = image.parentElement;
                image.style.width = container.clientWidth + 'px';
              }}
              window.onload = resizeImage;
              window.onresize = resizeImage;
            </script>
          </body>
        </html>
        """

        self.web.setHtml(html)

    def jiedai_button(self):

        py_echarts.map_0()
        self.web.load(QUrl.fromLocalFile("/Visual/jiedai.html"))
    def ciyun_button(self):

        py_echarts.ciyun()
        self.web.load(QUrl.fromLocalFile("/Visual/ciyun.html"))
    def shiduan_button(self):

        py_echarts.shiduan1()
        self.web.load(QUrl.fromLocalFile("/Visual/shiduan.html"))
    def zonghe_button(self):

        py_echarts.line_bar()

        self.web.load(QUrl.fromLocalFile("/Visual/bar.html"))

    def zonghe_3_button(self):

        py_echarts.pie_web()
        self.web.load(QUrl.fromLocalFile("/Visual/fee_web.html"))

    def get_time_button(self):
        self.in_time.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    def get_time_1_button(self):
        self.out_time_1.setText(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    def dengji_button(self):
        id =self.car_id.text()
        in_time =str(self. in_time.text())
        week_day=date0.get_weekday(in_time)
        Time_period=date0.get_timeperiod(in_time)
        self.result1 = service.exec("insert into car (id, in_time,state,wel,Time_period) values (%s, %s,%s,%s,%s)",
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
            self.result=service.exec(" update car set out_time = %s, state = %s where id = %s",
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
                "select id,in_time,state from car where id=%s and state=%s ",
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
            result = service.query("select * from id where name = %s and password= %s", service.userName,
                                   self.ps_3.text())
            if len(result) > 0:
                result1 = service.exec(" update id set name = %s, password = %s where name = %s",
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
        #self.widget.load(QUrl.fromLocalFile("/Visual/car_num.html"))
        result_0= service.query("select state from car where state=%s",0)
        c = 200
        b = c - len(result_0)
        a = len(result_0)
        self.SubtitleLabel.setText("总车位：" + str(c))
        self.SubtitleLabel_4.setText("占用车位："+str(a))
        self.bq.setText("剩余车位：" + str(b))
        bing_tu(["占用车位", "剩余车位"], [a, b], ['gold', 'lightskyblue'])
        py_echarts.car_use()
        self.widget_21.load(QUrl.fromLocalFile("/Visual/liquid.html"))
        #self.ImageLabel.setPixmap(QPixmap(""))
        #pixmap = QPixmap(r"Visual/bing_tu.png")  # 创建相应的QPixmap对象
        #self.ImageLabel.setScaledContents(True)  # 设置铺满
        #self.ImageLabel.setPixmap(pixmap)
    def crkgl_button(self):
        self.stackedWidget.setCurrentIndex(2)
    def qzxx_button(self):
        self.stackedWidget.setCurrentIndex(3)
        self.query()
    def whby_button(self):
        self.stackedWidget.setCurrentIndex(4)
        py_echarts.map_0()
        self.web.load(QUrl.fromLocalFile("/Visual/jiedai.html"))

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
                "select id,in_time,out_time,Time_period,time,wel ,fee from car where Time_period=%s and state=%s ",
                gname,1)
            # 获取指定枪支信息
        elif cname != "所有" and gname == "所有":
            result = service.query(
                "select id,in_time,out_time,Time_period,time,wel ,fee from car where wel=%s and state=%s",
                cname,1)
        elif cname != "所有" and gname != "所有":
            result = service.query(
                "select id,in_time,out_time,Time_period,time,wel ,fee from car where wel=%s and Time_period=%s and state=%s",
                cname, gname,1)
        elif cname == "所有"and gname == "所有":
            result = service.query(
                "select id,in_time,out_time,Time_period,time,wel ,fee from car where state=%s",1)
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
        id = self.locationID.text()  # 记录选择的大类
        if id != "":

            result2 = service.query(
                "select id,in_time,Time_period,time,wel ,fee from car where state=%s and id=%s ",
                0,id)
        else:
            result2 = service.query(
                "select id,in_time,Time_period,time,wel ,fee from car where state=%s ",0)

        row = len(result2)
        for i in range(row):  # 遍历行
            for j in range(6):  # 遍历列
                if j==3:
                    date_string = result2[i][1]
                    now_time = datetime.now()
                    self.time_0 = now_time - date_string
                    fee=3*(self.time_0.seconds // 3600+1)#一个小时3块
                    self.result1 = service.exec(
                        "update car set time=%s , fee=%s where state = %s and id = %s",
                        (self.time_0,fee, 0,result2[i][0]))
        if id != "":

            result = service.query(
                        "select id,in_time,Time_period,time,wel ,fee from car where state=%s and id=%s ",
                        0, id)
        else:
            result = service.query(
                        "select id,in_time,Time_period,time,wel ,fee from car where state=%s ", 0)

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
            #result = service.query("select Time_period from car_num where we_day=%s",
            #                      self.cboxGrade.currentText())
            class_2 = list(set(result))
            for i in class_2:  # 遍历查询结果
                self.cboxClass.addItem(i[0])





    def getItem(self, item):
        if item.column() == 0:  # 如果单击的是第一列
            self.select = item.text()  # 获取单击的单元格文本
            self.editID.setText(self.select)
            result = service.query("select * from car where id=%s",
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
                "update car set wel = %s, in_time = %s, out_time = %s, Time_period = %s where id = %s",
                (new_wek, new_in_time, new_out_time, new_period, self.editID.text()))
            if result > 0:  # 如果结果大于0，说明修改成功
                self.query()  # 在表格中显示最新数据
                QMessageBox.information(self, '提示', '信息修改成功！')
        except :

            QMessageBox.warning(self, '警告', '修改失败！')


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QtWidgets.QApplication(sys.argv)
    w = login_window()
    ww = wuqixinxiwindow()
    ww.setWindowState(Qt.WindowMaximized)
    w.show()
    sys.exit(app.exec_())

