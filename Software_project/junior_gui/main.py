import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Mainwindow
import xlwt
from datetime import datetime
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QFileDialog, QTextEdit, QAction
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

####################### 头代码 #######################
from matplotlib import pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtWidgets
from matplotlib.widgets import Cursor
import xlrd
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets

system = 0

class Myfigure(FigureCanvas):
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 4), facecolor='#FFD7C4')
        FigureCanvas.__init__(self, self.fig) #初始化激活widget中的plt部分

    def change_sys(self):
        # o represents 'windows', 1 represents 'mac'
        global system
        system = 1 - system
        print('切换系统成功！！！')
        # Ui_MainWindow().textEdit.setText('切换系统成功！！')

    def GIF(self):
        plt.rcParams['font.family']='SimHei'
        plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False
        fig, ax = self.fig, self.ax
        try:
            # y1 = []
            # for i in range(1000):
            #     y1.append(np.sin(i/10))
            #     ax.cla()
            #     ax.set_title("Data")
            #     ax.set_xlabel("Time/s")
            #     ax.set_ylabel("Strength")
            #     ax.set_xlim(0, (i+1)*1.5)
            #     ax.set_ylim(-1, 1)
            #     ax.grid()
            #     ax.plot(y1, color='b', linewidth=0.8, linestyle='-', label='快乐曲线')
            #     ax.legend(loc='best')
            #     plt.pause(1e-1)
            #     self.draw()
            y = list(range(100))
            ax.plot(y)
            self.fig.draw()
            print('nihao')
        except:
            print(Exception)


    def drawing(self):
        A0 = 590.8939192; B1 = 2.303196492; B2 = -0.0004665871929; B3 = -0.000007877923077; B4 = 3.020550598E-08; B5 = -4.876599743E-11
        x = [(A0 + B1 * i + B2 * i ** 2 + B3 * i ** 3 + B4 * i ** 4 + B5 * i ** 5) for i in range(256)]

        # 读取excel
        excel = xlrd.open_workbook(r"光谱仪正确的鲸鱼数据.xls")  # 读取excel文件，相当于打开excel
        sheet = excel.sheet_by_name("Sheet1")  # 通过sheet页的名字，跳转sheet页

        # 获取数据
        y = [sheet.cell_value(0,i) for i in range(256)]

        ############ python_to_arduino ###############
        # import serial  # 导入serial库
        #
        # ser = serial.Serial('COM7', baudrate=9600, bytesize=8, parity='N', stopbits=1,
        #                     timeout=0.01)  # 打开端口，每一秒返回一个消息 ,设置自己的串口
        #
        # demo1 = b"G"  # 将0转换为ASCII码方便发送
        # demo2 = b"1"  # 同理
        # # try模块用来结束循环（靠抛出异常）
        # try:
        #     for i in range(1):
        #         # 通过电脑端给arduino发送起始命令：'G'
        #         c = input('请输入指令:')
        #         c = ord(c)  # 将c转换为UTF-8标准数字
        #         if (c == 48):
        #             ser.write(demo1)  # ser.write在于向串口中写入数据
        #         if (c == 49):
        #             ser.write(demo2)
        #         time = 0
        #         data = []
        #
        #         # 开始从arduino接收数据
        #         while(data == []): #直到读到有效数据才停止循环
        #             a = ser.readline()
        #
        #             if(str(a,encoding='gbk')!='' and str(a,encoding='gbk')!='\r\n'):
        #                 data.append(str(a,encoding='gbk'))
        #             time += 1
        #             if time >= 1000:
        #                 print('运行%d次，次数过多，未能读到数据' % (time))
        #                 break
        #         yy = data[0].split(',') # 将字符型数据分割成字符型列表
        #         y = [int(i) for i in yy if i.isdigit()] # 保存整型数据于y中
        #         y.append(sum(y)/255)
        #         print('运行第%d次，读取到数据:'%(time),y)
        #         print(len(y))
        # except Exception as e:
        #     print(e)
        #     ser.close()  # 抛出异常后关闭端口
        ##############################

        # matplotlib设置字体
        global system
        if system == 0:
            plt.rcParams['font.family']='SimHei'
            plt.rcParams['font.sans-serif']=['SimHei']
            plt.rcParams['axes.unicode_minus']=False
        else:
            plt.rcParams['font.sans-serif']=['Arial Unicode MS']  #mac中文显示方法，跟换字体文件名字可以更改显示出的文字类型
            plt.rcParams['axes.unicode_minus']=False

        # 设置标签
        fig, ax = self.fig, self.ax
        ax.set_title("wavelength——强度")
        ax.set_xlabel("wavelength")
        ax.set_ylabel("强度")  # 如若需要散点简单平滑曲线连接图，只要将scatter改成plot即可 plt.plot(x, y)

        max_i = y.index(max(y)); min_i = y.index(min(y))    # 获取y[i]最大、最小值对应的i
        ax.plot(x, y, color='b', linewidth=0.8, linestyle='-', label='光谱发生相关曲线')
        ax.axvline(x=x[max_i], ls="-.", c="red", linewidth=1)  # 添加垂直直线
        ax.axhline(y=max(y), ls="-.", c="red", linewidth=1, label='最大峰峰值')  # 添加垂直直线
        ax.axvline(x=x[min_i], ls="-.", c="green", linewidth=1)  # 添加垂直直线
        ax.axhline(y=min(y), ls="-.", c="green", linewidth=1, label='最大峰峰值')  # 添加垂直直线
        ax.legend(bbox_to_anchor=(0, 1), loc='lower left',
                  framealpha=0.5)  # 同时画多条曲线 图例设置参考：https://www.cnblogs.com/lfri/p/12248629.html

        # x、y轴精度设置
        my_x_ticks = np.arange(560, 1160, 20)
        my_y_ticks = np.arange(min(y) - (max(y) - min(y)) * 0.1, max(y) + (max(y) - min(y)) * 0.1, (max(y) - min(y)) / 20)
        plt.xticks(my_x_ticks, rotation=90)
        plt.yticks(my_y_ticks)

        # 网格设置
        plt.grid(b=True, color='b', linestyle='--', linewidth=0.5, alpha=0.3, axis='both', which='both')  # 网格、图例设置参考：https://www.cnblogs.com/zyg123/p/10519588.html

        # 鼠标滚轮移动实现图像放缩 参考：https://matplotlib.org/users/event_handling.html
        def call_back(event):
            axtemp = event.inaxes
            x_min, x_max = axtemp.get_xlim()
            y_min, y_max = axtemp.get_ylim()
            xfanwei = (x_max - x_min) / 10
            yfanwei = (y_max - y_min) / 10
            if event.button == 'up':
                axtemp.set(xlim=(x_min + xfanwei, x_max - xfanwei))
                axtemp.set(ylim=(y_min + yfanwei, y_max - yfanwei))
                # print('up')
            elif event.button == 'down':
                axtemp.set(xlim=(x_min - xfanwei, x_max + xfanwei))
                axtemp.set(ylim=(y_min - yfanwei, y_max + yfanwei))
                # print('down')
            Myfigure.fig.canvas.draw_idle()  # 绘图动作实时反映在图像上
        self.fig.canvas.mpl_connect('scroll_event', call_back)  # 滚轮移动事件实现反馈

        # 鼠标点击事件
        def on_press(event):
            print("my position:", event.button, event.xdata, event.ydata)

        self.fig.canvas.mpl_connect('button_press_event', on_press)  # 添加新功能：鼠标点击位置的输出
        # cursor = Cursor(ax, useblit=True, color='black', linewidth=0.5)  # 鼠标跟随十字架，定义颜色粗细
        # plt.show()
        self.draw()
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)

    def on_press(self,event):
        pass
        self.draw()
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
#############################################

def openfile(): # 打开文件
    fname = QFileDialog.getOpenFileName(QMainWindow(),'打开文件','/',('Txt files (*.txt)'))  # fname = ('C:/Users/23573/Desktop/树莓派配置.txt', 'All Files (*)')
    print(fname)
    if fname[0]:
        try:
            f = open(fname[0], 'r', encoding="utf-8")
            with f:
                data = f.read()
                ui.textEdit.setText(data)
        except:
            ui.textEdit.setText("打开文件失败，可能是文件内型错误")

def savefile(): # 保存excel文件
    fname = QFileDialog.getSaveFileName(QMainWindow(), "文件保存", "./", ("Excel Files (*.xls)"))
    print(fname)
    wavelength = list(range(256))
    data = [float(i) for i in (np.arange(0, 20, 256) + np.random.random((256, 1)))]
    style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',
                         num_format_str='#,##0.00')  # ’Times New Roman‘ 字体，红色
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')  #
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet1')
    ws.write(0, 0, '波长', style0)
    ws.write(0, 1, '反射率', style0)
    ws.write(0, 2, '时间', style0)
    ws.write(0, 3, '计算量', style0)
    for i in range(256):
        ws.write(i + 1, 0, 1, style0)
        ws.write(i + 1, 1, data[i])
        ws.write(i + 1, 2, datetime.now())
        ws.write(i + 1, 3, xlwt.Formula('A' + str(i + 1) + '+' + 'B' + str(i + 1)))

    wb.save(fname[0])

def about(self):  # 关于
    # print('about')
    QtWidgets.QMessageBox.about(QMainWindow(), "About",
                                """embedding_in_qt5.py example
Copyright 2005 Florent Rougon, 2006 Darren Dale, 2015 Jens H Nielsen

This program is a simple example of a Qt5 application embedding matplotlib
canvases.

It may be used and modified with no restriction; raw copies as well as
modified versions may be distributed without limitation.

This is modified from the embedding in qt4 example to show the difference
between qt4 and qt5"""
                                    )



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # textEdit
    ui.actionAbout.triggered.connect(about)
    ui.actionOpen.triggered.connect(openfile)
    ui.actionSave_Data.triggered.connect(savefile)
    ui.pushButton.clicked.connect(Myfigure.change_sys)
    ui.pushButton_2.clicked.connect(Myfigure.GIF)
    # ui.pushButton_2.clicked.connect(Myfigure.drawing)
    #
    sys.exit(app.exec_())
