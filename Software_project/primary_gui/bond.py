from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout

from matplotlib import pyplot as plt
import numpy as np
import math
from matplotlib.widgets import Cursor

import sys
from PyQt5 import QtWidgets
from original_11_26_wfh_5 import Ui_MainWindow
#
# global track
# track =0
def picture():
    A0 = 590.8939192
    B1 = 2.303196492
    B2 = -0.0004665871929
    B3 = -0.000007877923077
    B4 = 3.020550598E-08
    B5 = -4.876599743E-11


    def wavelength(i):
        wavelength = A0 + B1 * i + B2 * i ** 2 + B3 * i ** 3 + B4 * i ** 4 + B5 * i ** 5
        return wavelength


    x = [0 for i in range(256)]
    for i in range(256):
        x[i] = wavelength(i)  # 获取wavelength数组数据放入数组x


    # 中文字体设置
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 绘图，设置标签
    fig, ax = plt.subplots(figsize=(8, 6))
    if y==y1:
        ax.set_title("wavelength——强度--one")
    elif y==y2:
        ax.set_title("wavelength——强度--two")
    elif y==y3:
        ax.set_title("wavelength——强度--three")
    ax.set_xlabel("wavelength")
    ax.set_ylabel("强度")  # 如若需要散点简单平滑曲线连接图，只要将scatter改成plot即可 plt.plot(x, y)

    max_i = y.index(max(y))  # 获取y[i]最大值对应的i
    min_i = y.index(min(y))  # 获取y[i]最小值对应的i
    # global width1
    # width = 0.8
    ax.plot(x, y, color=colo, linewidth=width, linestyle='-', label='光谱发生相关曲线')
    ax.axvline(x=x[max_i], ls="-.", c="magenta", linewidth=1.6)  # 添加垂直直线
    ax.axhline(y=max(y), ls="-.", c="magenta", linewidth=1.6, label='最大峰峰值')  # 添加垂直直线
    ax.axvline(x=x[min_i], ls="-.", c="cyan", linewidth=1.6)  # 添加垂直直线
    ax.axhline(y=min(y), ls="-.", c="cyan", linewidth=1.6, label='最大峰峰值')  # 添加垂直直线
    ax.legend(bbox_to_anchor=(0, 1), loc='lower left',
              framealpha=0.5)  # 同时画多条曲线 图例设置参考：https://www.cnblogs.com/lfri/p/12248629.html

    # x、y轴精度设置
    my_x_ticks = np.arange(560, 1160, 20)
    my_y_ticks = np.arange(min(y)-0.1*(max(y)-min(y)), max(y)+0.1*(max(y)-min(y)), (max(y)-min(y))/20)
    plt.xticks(my_x_ticks, rotation=90)
    plt.yticks(my_y_ticks)

    # 网格设置
    plt.grid(b=True,
             color='b',
             linestyle='--',
             linewidth=0.5,
             alpha=0.3,
             axis='both',
             which='both')  # 网格、图例设置参考：https://www.cnblogs.com/zyg123/p/10519588.html


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
        fig.canvas.draw_idle()  # 绘图动作实时反映在图像上


    fig.canvas.mpl_connect('scroll_event', call_back)  # 滚轮移动事件实现反馈


    #
    def on_press(event):
        print("my position:", event.button, event.xdata, event.ydata)


    fig.canvas.mpl_connect('button_press_event', on_press)  # 添加新功能：鼠标点击位置的输出
    #
    h = []
    l = []
    for i in range(1, len(y) - 1):
        if (y[i - 1] < y[i] and y[i + 1] < y[i]):
            h.append(y[i])
        elif (y[i - 1] > y[i] and y[i] > y[i]):
            l.append(y[i])
    if (len(h) == 0):
        h.append(max(y))
    if (len(l) == 0):
        l.append(min(y))
    print("极大值：", h)  # 极大值点
    print("极小值：", l)  # 极小值点

    # 最大值和最小值的获取及标记
    max_peak = max(y)
    min_peak = min(y)
    print("最大值点坐标：({},{})".format(x[max_i], max(y)))
    print("最小值点坐标：({},{})".format(x[min_i], min(y)))
    #
    cursor = Cursor(ax, useblit=True, color='black', linewidth=0.5)  # 鼠标跟随十字架，定义颜色粗细





class MyPyQT_Form(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    # 连接pushbutton与逻辑事件

    def feedback(self):
        # 读取excel
        import xlrd
        excel = xlrd.open_workbook("./1123三次鲸鱼有效数据.xlsx")  # 读取excel文件，相当于打开excel
        sheet = excel.sheet_by_name("Sheet1")  # 通过sheet页的名字，跳转sheet页

        y = [0 for i in range(256)]
        for i in range(256):
            y[i] = sheet.cell_value(2, i)  # sheet.row_values(2)#获取某一行的数据，返回第二行的列表
        print("画图")
        picture()
        plt.show()


    def select1(self,count1 = 0):
        if count1 % 2 == 1:
            global y, y1, y2, y3,colo,width
            colo = 'k'
            width= 0.8
            import xlrd
            excel = xlrd.open_workbook("./1123三次鲸鱼有效数据.xlsx")  # 读取excel文件，相当于打开excel
            sheet = excel.sheet_by_name("Sheet1")  # 通过sheet页的名字，跳转sheet页
            y1 = [0 for i in range(256)]
            for i in range(256):
                y1[i] = sheet.cell_value(0, i)  # sheet.row_values(2)#获取某一行的数据，返回第二行的列表
            y = [0 for i in range(256)]
            y = y1
            picture()
            plt.show()
            count1 += 1
        else:
            plt.close()
            print("曲线1关闭")

    def select2(self,count2 = 0):
        if count2 % 2 == 1:
            global y, y1, y2, y3, colo,width
            colo = 'y'
            width = 0.8
            import xlrd
            excel = xlrd.open_workbook("./1123三次鲸鱼有效数据.xlsx")  # 读取excel文件，相当于打开excel
            sheet = excel.sheet_by_name("Sheet1")  # 通过sheet页的名字，跳转sheet页
            y2 = [0 for i in range(256)]
            for i in range(256):
                y2[i] = sheet.cell_value(1, i)  # sheet.row_values(2)#获取某一行的数据，返回第二行的列表
            y = [0 for i in range(256)]
            y = y2
            picture()
            plt.show()
            count2 += 1
        else:
            plt.close()
            print("曲线2关闭")

    def select3(self,count3 = 0):
        if count3 % 2 == 1:
            global y, y1, y2, y3, colo,width
            colo = 'b'
            width = 0.8
            import xlrd
            excel = xlrd.open_workbook("./1123三次鲸鱼有效数据.xlsx")  # 读取excel文件，相当于打开excel
            sheet = excel.sheet_by_name("Sheet1")  # 通过sheet页的名字，跳转sheet页
            y3 = [0 for i in range(256)]
            for i in range(256):
                y3[i] = sheet.cell_value(2, i)  # sheet.row_values(2)#获取某一行的数据，返回第二行的列表
            y = [0 for i in range(256)]
            y = y3
            picture()
            plt.show()
            count3 += 1
        else:
            plt.close()
            print("曲线3关闭")
    def width1_range(self):
        print(self.horizontalSlider_1.value())
        global width
        width = self.horizontalSlider_1.value() / 100 * 0.8 + 0.8
        plt.close()
        picture()
        plt.show()
    def width2_range(self):
        print(self.horizontalSlider_3.value())
        global width
        width = self.horizontalSlider_3.value() / 100 * 0.8 + 0.8
        plt.close()
        picture()
        plt.show()
    def width3_range(self):
        print(self.horizontalSlider_4.value())
        global width
        width = self.horizontalSlider_4.value() / 100 * 0.8 + 0.8
        plt.close()
        picture()
        plt.show()













    def clicked_track(self,track = 0):

        if track ==0:
            track = 1
        if track%2==1:
            import numpy as np
            import matplotlib
            import matplotlib.pyplot as plt

            # set up matplotlib
            is_ipython = 'inline' in matplotlib.get_backend()
            if is_ipython:
                from IPython import display

            plt.ion()

            def plot_durations(yy):
                plt.figure(3)
                plt.clf()
                plt.subplot(311)
                plt.plot(yy[:, 0])
                plt.subplot(312)
                plt.plot(yy[:, 1])
                plt.subplot(313)
                plt.plot(yy[:, 2])

                plt.pause(0.000001)  # pause a bit so that plots are updated
                if is_ipython:
                    display.clear_output(wait=True)
                    display.display(plt.gcf())
            global xx
            xx= np.linspace(-10, 10, 500)
            yy = []
            for i in range(len(xx)):
                y11 = np.cos(i / (3 * 3.14))
                y22 = np.sin(i / (3 * 3.14)) * i
                y33 = np.sin(i / (3 * 3.14)) * i**2
                yy.append(np.array([y11, y22, y33]))  # 保存历史数据
                plot_durations(np.array(yy))
                print(track)
                track = 2
                if track ==400:
                    break
        else:
            track = 400




    def selectionchange1(self):

        # 标签用来显示选中的文本
        # currentText()：返回选中选项的文本

        # self.btn1.setText(self.comboColor_1.currentText())
        # print('Items in the list are:')
        # 输出选项集合中每个选项的索引与对应的内容
        # count()：返回选项集合中的数目
        print(self.comboColor_1.currentText())
        # for count in range(self.comboColor_1.count()):
        #     print('Item' + str(count) + '=' + self.comboColor_1.itemText(count))
        #     print('current index', 'selection changed', self.comboColor_1.currentText())
        global colo,colo1,colo2,colo3

        if self.comboColor_1.currentText()=='Black':
            colo1 = 'k'
        elif self.comboColor_1.currentText()=='Yellow':
            colo1 = 'y'
        elif self.comboColor_1.currentText()=='Red':
            colo1 = 'r'
        elif self.comboColor_1.currentText()=='Green':
            colo1 = 'g'
        elif self.comboColor_1.currentText()=='Blue':
            colo1 = 'b'
        elif self.comboColor_1.currentText()=='White':
            colo1 = 'w'
        colo = colo1
        plt.close()
        picture()
        plt.show()
    def selectionchange2(self):
        global colo,colo1,colo2,colo3
        if self.comboColor_2.currentText()=='Black':
            colo2 = 'k'
        elif self.comboColor_2.currentText()=='Yellow':
            colo2 = 'y'
        elif self.comboColor_2.currentText()=='Red':
            colo2 = 'r'
        elif self.comboColor_2.currentText()=='Green':
            colo2 = 'g'
        elif self.comboColor_2.currentText()=='Blue':
            colo2 = 'b'
        elif self.comboColor_2.currentText()=='White':
            colo2 = 'w'
        colo = colo2
        plt.close()
        picture()
        plt.show()
    def selectionchange3(self):
        global colo,colo1,colo2,colo3
        if self.comboColor_3.currentText()=='Black':
            colo3 = 'k'
        elif self.comboColor_3.currentText()=='Yellow':
            colo3 = 'y'
        elif self.comboColor_3.currentText()=='Red':
            colo3 = 'r'
        elif self.comboColor_3.currentText()=='Green':
            colo3 = 'g'
        elif self.comboColor_3.currentText()=='Blue':
            colo3 = 'b'
        elif self.comboColor_3.currentText()=='White':
            colo3 = 'w'
        colo = colo3
        plt.close()
        picture()
        plt.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    plt.show()
    sys.exit(app.exec())

