from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout

from matplotlib import pyplot as plt
import numpy as np
from math import sin
from matplotlib.widgets import Cursor

import sys
from PyQt5 import QtWidgets
from Button_link import Ui_Form
#
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

    #
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 绘图，设置标签
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title("wavelength——强度")
    ax.set_xlabel("wavelength")
    ax.set_ylabel("强度")  # 如若需要散点简单平滑曲线连接图，只要将scatter改成plot即可 plt.plot(x, y)

    max_i = y.index(max(y))  # 获取y[i]最大值对应的i
    min_i = y.index(min(y))  # 获取y[i]最小值对应的i
    ax.plot(x, y, color='b', linewidth=0.8, linestyle='-', label='光谱发生相关曲线')
    ax.axvline(x=x[max_i], ls="-.", c="red", linewidth=1)  # 添加垂直直线
    ax.axhline(y=max(y), ls="-.", c="red", linewidth=1, label='最大峰峰值')  # 添加垂直直线
    ax.axvline(x=x[min_i], ls="-.", c="green", linewidth=1)  # 添加垂直直线
    ax.axhline(y=min(y), ls="-.", c="green", linewidth=1, label='最大峰峰值')  # 添加垂直直线
    ax.legend(bbox_to_anchor=(0, 1), loc='lower left',
              framealpha=0.5)  # 同时画多条曲线 图例设置参考：https://www.cnblogs.com/lfri/p/12248629.html

    # x、y轴精度设置
    my_x_ticks = np.arange(500, 1100, 10)
    my_y_ticks = np.arange(-0.1, 0.1, 0.005)
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





class MyPyQT_Form(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)

    # 连接pushbutton与逻辑事件

    def feedback(self):
        print("画图")


    def select1(self,count1 = 0):
        if count1 % 2 == 1:
            global y, y1, y2, y3
            y1 = [0 for i in range(256)]
            y = [0 for i in range(256)]
            for i in range(256):
                y1[i] = 0.1 * sin(0.1 * i)
            y = y1
            picture()
            # plt.show()
            count1 += 1
        else:
            plt.close()
            print("曲线1关闭")

    def select2(self,count2 = 0):
        if count2 % 2 == 1:
            global y, y1, y2, y3
            y2 = [0 for i in range(256)]
            y = [0 for i in range(256)]
            for i in range(256):
                y2[i] = 0.1 * sin(0.1 * i) ** 2
            y = y2
            picture()
            plt.show()
            count2 += 1
        else:
            plt.close()
            print("曲线2关闭")

    def select3(self,count3 = 0):
        if count3 % 2 == 1:
            global y, y1, y2, y3
            y3 = [0 for i in range(256)]
            y = [0 for i in range(256)]
            for i in range(256):
                y3[i] = 4e-4 * abs(i) * sin(i)
            y = y3
            picture()
            plt.show()
            count3 += 1
        else:
            plt.close()
            print("曲线3关闭")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    plt.show()
    sys.exit(app.exec())

