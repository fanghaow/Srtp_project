from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import numpy as np
import time
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import (QEvent, QTimer, Qt)
from PyQt5.QtGui import QPainter
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

data_x = None; data_y = None; N_n = 0;
C_x = -0.5; C_y = 0; D_d = 1.5;

class Myfigure(FigureCanvas):
    def __init__(self):
        self.fig = plt.figure(facecolor='#FFD7C4')  # 可选参数,facecolor为背景颜色
        self.axes = self.fig.subplots() #也可以用add_subplot
        FigureCanvas.__init__(self, self.fig) #初始化激活widget中的plt部分

    def Draw(self):
        global C_x, C_y, D_d
        plt.imshow(self.draw_mandlbrot(C_x, C_y, D_d, 400, 400))
        self.draw()
        self.fig.canvas.mpl_connect('button_press_event', self.on_press) #如果不使用canvas.mpl_connect的话将不能激活event中的xdata和ydata以及inaxes，这里为相对axes的坐标
        # pos = plt.ginput(3)
        # print(pos)

    def draw_mandlbrot(self, cx, cy, d, width=400, length=400): #生成.png图片颜色暂时为黄和蓝两种
        if width >= length:
            dx = d; dy = d*width/length #比例缩放，使其看起来依然是一个长宽比为1:1的图形
        else:
            dy = d; dx = d*length/width
        x0, x1, y0, y1 = cx - dx, cx + dx, cy - dy, cy + dy
        x = np.arange(x0, x1, (x1 - x0) / length).reshape(1, length)
        y = np.arange(y0, y1, (y1 - y0) / width ).reshape( width, 1)
        c = x + y*1j

        def iter_point(c):
            z = c
            for i in range(1, 100):
                if abs(z) > 2: break
                z = z * z + c
            return i

        start = time.process_time()
        mandelbrot = np.frompyfunc(iter_point, 1, 1)(c).astype(np.float)
        print("time = ", time.process_time() - start)
        return mandelbrot

    # def mousePressEvent(self, event): #如果只重载这个方法那么无法获得xdata,ydata
    #     global data_x, data_y
    #     # data_x = event.pos().x()
    #     # data_y = event.pos().y()
    #     # print(data_x, ',', data_y)
    #

    def on_press(self,event):
        global data_x, data_y, N_n, C_x, C_y, D_d
        N_n += 1
        data_x = event.xdata
        data_y = event.ydata
        print('you pressed', N_n, 'times,', event.xdata, event.ydata)

        C_x = C_x + (data_x-200)/200 * D_d  #计算新的中心点坐标
        C_y = C_y + (data_y-200)/200 * D_d
        D_d = 0.5**(N_n) * D_d #计算新的范围，0.5为放大倍数

        plt.imshow(self.draw_mandlbrot(C_x, C_y, D_d, 400, 400))
        self.draw()
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)


class Main_window(QWidget):
    def __init__(self):
        super(Main_window, self).__init__()

        # QWidget
        self.figure = Myfigure()
        self.setWindowTitle('Mandlort_Calculater')
        self.fig_ntb = NavigationToolbar(self.figure, self) #注意，记得指向figure的FigureCanvas
        self.button_draw = QPushButton("绘图")
        self.button_draw.setFont(QFont( "Roman times" , 10 ,  QFont.Bold))
        self.label = QLabel('')
        self.label.setFont(QFont( "Roman times" , 8 ,  QFont.Bold))
        timer = QTimer(self)  #设置一个定时器用来刷新label显示的坐标
        timer.timeout.connect(self.time_Event)
        timer.start(1000)
        # 连接事件
        self.button_draw.clicked.connect(self.figure.Draw)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.figure)
        layout.addWidget(self.fig_ntb)
        layout.addWidget(self.button_draw)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def time_Event(self):
        data_xy = str(C_x)+','+str(C_y)
        self.label.setText(data_xy)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Main_window()
    ui.show()
    sys.exit(app.exec_())
