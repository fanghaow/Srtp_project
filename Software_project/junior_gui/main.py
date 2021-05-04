import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import Mainwindow
from Mainwindow import Ui_MainWindow
import xlwt
from datetime import datetime
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QFileDialog, QTextEdit, QAction, QGridLayout
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QTimer, pyqtSlot, QThread

####################### Head code #######################
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

class Myplot(FigureCanvas):
    # def __init__(self):
    #     self.fig, self.ax = plt.subplots(figsize=(6, 4), facecolor='#FFD7C4')
    #     FigureCanvas.__init__(self, self.fig) #初始化激活widget中的plt部分
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        # normalized for 中文显示和负号
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # new figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # activate figure window
        # super(Plot_dynamic,self).__init__(self.fig)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        # self.fig.canvas.mpl_connect('button_press_event', self)
        # sub plot by self.axes
        self.axes = self.fig.add_subplot(111)
        # initial figure
        self.compute_initial_figure()

        # size policy
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
    def compute_initial_figure(self):
        pass

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

    def on_press(self,event):
        pass
        self.draw()
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
#############################################
class static_fig(Myplot):
    def __init__(self, *args, **kwargs):
        Myplot.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        x = np.linspace(0, 2 * np.pi, 100)
        y = x * np.sin(x)
        self.axes.plot(x, y)
        self.axes.set_title("signals")
        self.axes.set_xlabel("delay(s)")
        self.axes.set_ylabel("counts")


class dynamic_fig(Myplot):
    def __init__(self, *args, **kwargs):
        Myplot.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        counts = [1, 10]
        delay_t = [0, 1]
        self.axes.plot(delay_t, counts, '-ob')
        self.axes.set_title("signals")
        self.axes.set_xlabel("delay(s)")
        self.axes.set_ylabel("counts")

class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        # ^O^ static_fig can changed to any other function
        # self.fig1=static_fig(width=5, height=4, dpi=100)
        self.fig1 = static_fig(width=5, height=3, dpi=72)
        self.fig2 = dynamic_fig(width=5, height=3, dpi=72)
        # add NavigationToolbar in the figure (widgets)
        self.fig_ntb1 = NavigationToolbar(self.fig1, self)
        self.fig_ntb2 = NavigationToolbar(self.fig2, self)
        # self.Start_plot.clicked.connect(self.plot_cos)
        # add the static_fig in the Plot box
        self.gridlayout1 = QGridLayout(self.groupBox)
        self.gridlayout1.addWidget(self.fig1)
        self.gridlayout1.addWidget(self.fig_ntb1)
        # add the dynamic_fig in the Plot box
        self.gridlayout2 = QGridLayout(self.groupBox_2)
        self.gridlayout2.addWidget(self.fig2)
        self.gridlayout2.addWidget(self.fig_ntb2)
        # initialized flags for static/dynamic plot: on is 1,off is 0
        self._timer = QTimer(self)
        self._t = 1
        self._counts = []
        self._delay_t = []
        self._Static_on = 0
        self._update_on = 0
        # my configuration
        self.line_color = 'b'

    @pyqtSlot()
    def on_Static_plot_clicked(self):
        # self.plot_cos()
        self.drawing()
        self._Static_on = 1
        # self.Start_plot.setEnabled(False)

    global nc
    nc = 1

    def plot_cos(self):
        # print('nc=%d\n' %self.nc)
        global nc
        nc += 1
        self.fig1.axes.cla()
        self.t = np.arange(0, 15, 0.1)
        self.y = 2 * nc * self.t - self.t * np.cos(self.t / 2 / np.pi * 1000)
        self.fig1.axes.plot(self.t, self.y)
        self.fig1.axes.set_title("signals", fontsize=18, color='c')
        self.fig1.axes.set_xlabel("delay(s)", fontsize=18, color='c')
        self.fig1.axes.set_ylabel("counts", fontsize=18, color='c')
        self.fig1.draw()

    def drawing(self):
        self.fig1.axes.cla()
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
        fig, ax = self.fig1, self.fig1.axes
        ax.set_title("wavelength——强度")
        ax.set_xlabel("wavelength")
        ax.set_ylabel("强度")  # 如若需要散点简单平滑曲线连接图，只要将scatter改成plot即可 plt.plot(x, y)

        max_i = y.index(max(y)); min_i = y.index(min(y))    # 获取y[i]最大、最小值对应的i
        ax.plot(x, y, color=self.line_color, linewidth=0.8, linestyle='-', label='光谱发生相关曲线')
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

        fig.draw()  # 展示图片
        print('hahahaha')

    @pyqtSlot()
    def on_dynamic_plot_clicked(self):
        print('start dynamic ploting')
        # self.Static_plot.setEnabled(False)
        self.dynamic_plot.setEnabled(False)
        # start update figure every 1s; flag "update_on" : 1 is on and 0 is Off
        self._update_on = 1
        self._timer.timeout.connect(self.update_fig)
        self._timer.start(1000)  # plot after 1s delay

    def update_fig(self):
        self._t += 1
        print(self._t)
        self._delay_t.append(self._t)
        print(self._delay_t)
        # new_counts=random.randint(100,900)
        new_counts = 2 * self._t - self._t * np.cos(self._t / 2 / np.pi * 1000)
        self._counts.append(new_counts)
        print(self._counts)
        self.fig2.axes.cla()
        self.fig2.axes.plot(self._delay_t, self._counts, '-ob')
        self.fig2.axes.set_title("signals", fontsize=18, color='c')
        self.fig2.axes.set_xlabel("delay(s)", fontsize=18, color='c')
        self.fig2.axes.set_ylabel("counts", fontsize=18, color='c')
        self.fig2.draw()

    @pyqtSlot()
    def on_End_plot_clicked(self):
        if self._update_on == 1:
            self._update_on = 0
            self._timer.timeout.disconnect(self.update_fig)
            self.dynamic_plot.setEnabled(True)
        else:
            pass

    @pyqtSlot()
    def on_Erase_plot_clicked(self):
        self.fig1.axes.cla()
        self.fig1.draw()
        self.fig2.axes.cla()
        self.fig2.draw()
        if self._update_on == 1:
            self._update_on = 0
            self._delay_t = []
            self._counts = []
            self.fig2.axes.cla()
            self.fig2.draw()
            self._timer.timeout.disconnect(self.update_fig)
            self.dynamic_plot.setEnabled(True)
        else:
            pass
        self.Static_plot.setEnabled(True)
        # self.Erase_plot.setEnabled(False)

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
            ui.textEdit.setText("打开文件失败，可能是文件类型错误")

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
def load_data():
    pass

def select1():
    pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # MainWindow.show()

    win = AppWindow()
    win.show()
    # textEdit
    ui.actionAbout.triggered.connect(about)
    ui.actionOpen.triggered.connect(openfile)
    ui.actionSave_Data.triggered.connect(savefile)
    ui.checkVisible_1.clicked.connect(select1)
    # ui.pushButton.clicked.connect(Myplot.change_sys)
    # ui.pushButton_2.clicked.connect(Myplot.GIF)
    # ui.pushButton_2.clicked.connect(Myfigure.drawing)
    #
    sys.exit(app.exec_())
