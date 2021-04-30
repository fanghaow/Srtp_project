# rom __future__ import division #整数除法 / 变为普通除法
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import numpy as np
from sympy import *
import time
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import (QEvent, QTimer, Qt)
from PyQt5.QtGui import QPainter
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
x_data = 0;y_data = 0;

'''
注意：
1.仅可以求解微分方程
2.输入的时候使用英文输入法，当使用中文输入法的时候会出现不可预知的错误
3.这个demo中，text仅仅只能作为接收信息的工具，不要用来处理信息
ps:给出一个书写需要求解的微分方程的例子：
Derivative(f(x), x) - f(x) + 1等同于df(x)-f(x)+1=0
给出一个书写求解对象的例子：
f(x)
'''

x, y = symbols('x, y', real=True)
f = Function('f')
func = Eq(Derivative(f(x), x) - f(x) + 1, 0)
df = f(x)
func_tmp = ''
df_tmp = ''
ans = dsolve(func, df)
write = ''


class Myfigure(FigureCanvas):
    def __init__(self):
        self.fig = plt.figure(figsize=(4,1))  # 可选参数,facecolor为背景颜色facecolor='#FFD7C4',
        # self.axes = self.fig.subplots() #也可以用add_subplot
        self.axes = self.fig.add_axes([0,0,1,1])
        FigureCanvas.__init__(self, self.fig) #初始化激活widget中的plt部分
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)

    def _print(self):
        global write
        left, width = .25, .5
        bottom, height = .25, .5
        right = left + width
        top = bottom + height
        self.axes.text(0.5 * (left + right), 0.5 * (bottom + top), write,
                       horizontalalignment='center',
                       verticalalignment='center',
                       fontsize=20, color='red',
                       )
        self.axes.set_axis_off()
        self.draw()

    def on_press(self,event):
        global x_data, y_data
        x_data = event.xdata
        y_data = event.ydata
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)

class Main_window(QWidget):
    def __init__(self):
        super(Main_window, self).__init__()

        # QWidget
        self.figure = Myfigure()
        self.setWindowTitle('LaTex display')
        # self.fig_ntb = NavigationToolbar(self.figure, self) #注意，记得指向figure的FigureCanvas
        self.button_text = QPushButton("确认输入")
        self.button_text.setFont(QFont( "Roman times" , 10 ,  QFont.Bold))

        self.text1 = QLineEdit('')
        self.text1.setPlaceholderText('输入需要求解的表达式')
        self.text1.textChanged.connect(self.text_handler1) # 输入数值改变n的大小

        self.text2 = QLineEdit('')
        self.text2.setPlaceholderText('输入需要求解的对象')
        self.text2.textChanged.connect(self.text_handler2)  # 输入数值改变n的大小

        self.label = QLabel('')
        self.label.setFont(QFont( "Roman times" , 8 ,  QFont.Bold))

        timer = QTimer(self)  #设置一个定时器用来刷新label显示的坐标
        timer.timeout.connect(self.time_Event)
        timer.start(1000)
        # 连接事件
        # self.button_draw.clicked.connect(self.figure.Draw)
        self.button_text.clicked.connect(self.but_click)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.text1)
        layout.addWidget(self.text2)
        layout.addWidget(self.figure)
        # layout.addWidget(self.fig_ntb)
        layout.addWidget(self.button_text)
        layout.addWidget(self.label)
        self.setLayout(layout)


    def time_Event(self):
        data_xy = str(x_data)+','+str(y_data)
        self.label.setText(data_xy)

    def text_handler1(self,text):
        global func_tmp
        func_tmp = text

    def text_handler2(self,text):
        global df_tmp
        df_tmp = text

    def but_click(self):
        global x, y, f, func, df, ans, write
        df = eval(df_tmp)
        func = Eq(eval(func_tmp), 0)
        ans = dsolve(func, df)
        write = '$' + ''.join(latex(ans)) + '$'
        print(write)
        self.figure._print()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main_window()
    ui.show()
    sys.exit(app.exec_())

