import sys
import xlwt
from datetime import datetime
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QFileDialog, QTextEdit, QAction, QGridLayout
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtCore import QTimer, pyqtSlot, QThread

####################### Head code #######################
# import my web data module
from Web_project.grepper import Web_data
from Mainwindow import Ui_MainWindow
import serial
import xlrd
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
import cv2
# global variables
system = 0

class Myplot(FigureCanvas):
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
        # o : 'windows', 1 : 'mac'
        global system
        system = 1 - system
        print('Transform operational system sucessfully!!')

    def on_press(self,event):
        pass
        self.draw()
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)

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
        # set a suprise
        # img = cv2.imread('smile.jpg')
        # b, r = img[:, :, 0], img[:, :, 2]
        # img[:, :, 0], img[:, :, 2] = r, b
        # self.axes.imshow(img)
        # self.axes.set_title('不会真的有人觉得我会更新软件吧')

#############################################

class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        self.setupUi(self)
        # ^O^ static_fig can changed to any other function
        # self.fig1=static_fig(width=5, height=4, dpi=100)
        self.fig1 = static_fig(width=8, height=6, dpi=108)
        self.fig2 = dynamic_fig(width=8, height=6, dpi=108)
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

    @pyqtSlot()
    def on_Static_plot_clicked(self):
        # self.plot_cos()
        self.fig1.axes.cla()
        self.drawing() # (erase=True)
        self._Static_on = 1
        # self.Start_plot.setEnabled(False)

    global nc
    nc = 1

    def plot_cos(self):
        # print('nc=%d\n' %self.nc)
        global nc
        nc += 1
        self.fig1.axes.cla() # init
        self.t = np.arange(0, 15, 0.1)
        self.y = 2 * nc * self.t - self.t * np.cos(self.t / 2 / np.pi * 1000)
        self.fig1.axes.plot(self.t, self.y)
        self.fig1.axes.set_title("signals", fontsize=18, color='c')
        self.fig1.axes.set_xlabel("delay(s)", fontsize=18, color='c')
        self.fig1.axes.set_ylabel("counts", fontsize=18, color='c')
        self.fig1.draw()

    def drawing(self, erase=False, line_label=1):
        if erase == True:
            self.fig1.axes.cla()
        x, y = load_data('json', line_label)

        # Matplotlib set font
        global system
        if system == 0:
            plt.rcParams['font.family'] = 'SimHei' # windows chinese font
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False
        else:
            plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] # mac chinese font
            plt.rcParams['axes.unicode_minus'] = False

        # set title
        fig, ax = self.fig1, self.fig1.axes
        ax.set_title("Wavelength——Strength")
        ax.set_xlabel("Wavelength")
        ax.set_ylabel("Strength")

        max_i = y.index(max(y)); min_i = y.index(min(y))
        ax.plot(x, y, color=config.line_color, linewidth=config.line_width, linestyle='-', label='Spectral_Curve'+str(line_label))
        ax.axvline(x=x[max_i], ls="-.", c="red", linewidth=1, label='Max_index'+str(line_label))
        ax.axhline(y=max(y), ls="-.", c="red", linewidth=1, label='Max_peak'+str(line_label))  # add horizontal straight line
        ax.axvline(x=x[min_i], ls="-.", c="green", linewidth=1, label='Min_index'+str(line_label))
        ax.axhline(y=min(y), ls="-.", c="green", linewidth=1, label='Min_peak'+str(line_label))  # add vertical straight line
        ax.legend(bbox_to_anchor=(0, 1), loc='lower left',
                  framealpha=0.5)

        # set x、y axis
        my_x_ticks = np.arange(560, 1160, 20)
        my_y_ticks = np.arange(min(y) - (max(y) - min(y)) * 0.1, max(y) + (max(y) - min(y)) * 0.1, (max(y) - min(y)) / 20)
        plt.xticks(my_x_ticks, rotation=90)
        plt.yticks(my_y_ticks)

        # set gird
        plt.grid(b=True, color='b', linestyle='--', linewidth=0.5, alpha=0.3, axis='both', which='both')

        # show
        fig.draw()
        print('Static plot successfully!')

    @pyqtSlot()
    def on_dynamic_plot_clicked(self):
        print('Start dynamic ploting')
        # self.Static_plot.setEnabled(False)
        self.dynamic_plot.setEnabled(False)
        # start update figure every 1s; flag "update_on" : 1 is on and 0 is Off
        self._update_on = 1
        self._timer.timeout.connect(self.update_fig)
        self._timer.start(1000)  # plot after 1s delay

    def update_fig(self):
        self._t += 1
        self._delay_t.append(self._t)
        # new_counts = 2 * self._t - self._t * np.cos(self._t / 2 / np.pi * 1000)
        channel = 50
        new_counts = config.mat_data[self._t - 1][channel]
        self._counts.append(new_counts)

        print('Wavelength '+str(channel)+':', self._counts)
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

# My Functions
def openfile():
    fname = QFileDialog.getOpenFileName(QMainWindow(),'打开文件','/', ("Txt files (*.txt);;Excel files (*.xls/*.xlsx);;Json files (*.json);; Csv file (*.csv)" ) )  # fname = ('C:/Users/23573/Desktop/树莓派配置.txt', 'All Files (*)')
    print(fname)
    if fname[0]:
        try:
            f = open(fname[0], 'r', encoding="utf-8")
            with f:
                data = f.read()
                ui.textEdit.setText(data)
        except:
            ui.textEdit.setText("打开文件失败，可能是文件类型错误")

def savefile(): # save excel file
    fname = QFileDialog.getSaveFileName(QMainWindow(), "文件保存", "./", ("Txt files (*.txt);;Excel files (*.xls/*.xlsx);;Json files (*.json);; Csv file (*.csv)"))
    print(fname)
    wavelength = list(range(256))
    data = [float(i) for i in (np.arange(0, 20, 256) + np.random.random((256, 1)))]
    style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',
                         num_format_str='#,##0.00')  # ’Times New Roman‘ red font
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
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

def about():
    QtWidgets.QMessageBox.about(QMainWindow(), "About",
                                """软件版本：1.0.1
        作者：王芳豪、王雪帆、陈丁佳
        日期：2020.05.01
        目标：测量水果255分辨率光谱数据，运行模型，得出水果糖度预测结果
        功能：检测实时光谱波段数据，多光谱曲线对比，自训练模型，云端数据保存与预测
        支持系统：Windows、Mac、Linux
"""
                                    )

def load_data(formula, line_label):
    if formula == 'excel':
        # Formula1 : excel
        A0 = 590.8939192; B1 = 2.303196492; B2 = -0.0004665871929; B3 = -0.000007877923077; B4 = 3.020550598E-08; B5 = -4.876599743E-11
        wavelength = [(A0 + B1 * i + B2 * i ** 2 + B3 * i ** 3 + B4 * i ** 4 + B5 * i ** 5) for i in range(256)]
        excel = xlrd.open_workbook(r"WhaleLike_Data.xls")
        sheet = excel.sheet_by_name("Sheet1")
        strength = [sheet.cell_value(0,i) for i in range(256)]
    elif formula == 'json':
        # Formula2 : json
        wd = Web_data()
        text = wd.web_str()
        wd.json_down()
        data_mat = wd.proceed_json()
        config.updatedata_callback(data_mat)
        wavelength = [i for i in range(1, 257)]
        strength = data_mat[line_label][:]
    elif formula == 'arduino2py':
        # Formula3 : arduino2py
        ser = serial.Serial('COM7', baudrate=9600, bytesize=8, parity='N', stopbits=1,
                            timeout=0.01)  # open a port, return a msg per second, set own serial
        demo1, demo2 = b'G', b'1'  # tf 0 and 1 into bytes(ASCII) so that easily to send
        try:
            for i in range(1):
                # py send arduino start commend ：'G'
                c = input('请输入指令:')
                c = ord(c)  # tf c to UTF-8 universal number
                if (c == 48):
                    ser.write(demo1)  # ser.write write data in serial
                if (c == 49):
                    ser.write(demo2)
                time = 0
                data = []
                # start receive data from arduino
                while(data == []): # loop until read data
                    a = ser.readline()
                    if(str(a,encoding='gbk')!='' and str(a,encoding='gbk')!='\r\n'):
                        data.append(str(a, encoding='gbk'))
                    time += 1
                    if time >= 1000:
                        print('运行%d次，次数过多，未能读到数据' % (time))
                        break
                yy = data[0].split(',') # split my str into list data
                strength = [int(i) for i in yy if i.isdigit()] # save int data into y
                strength.append(sum(strength)/255)
                print('运行第%d次，读取到数据:'%(time), strength)
                print(len(strength))
        except Exception as e:
            print(e)
            ser.close()  # close my serial when get a exception
    print('Wavelength :', wavelength)
    print("strength :", strength)
    return wavelength, strength

def color_change1():
    color_dict = {'Black':'k', 'Gray':'y', 'Red':'r', 'Green':'g', 'Blue':'b', 'White':'w'}
    print('I change line color to :', color_dict[win.comboColor_1.currentText()])
    config.line_color = color_dict[win.comboColor_1.currentText()]
    for index, line in enumerate(win.fig1.axes.get_lines()):
        print('Lines label :', line.get_label())
        if line.get_label() == 'Spectral_Curve'+str(1):
            line.set_color(config.line_color)
            win.fig1.draw()
    pass
def color_change2():
    pass

def line_width1():
    width = win.horizontalSlider_1.value() / 100 * 0.8 + 0.8
    config.line_width = width
    for index, line in enumerate(win.fig1.axes.get_lines()):
        print('Lines label :', line.get_label())
        if line.get_label() == 'Spectral_Curve'+str(1):
            line.set_linewidth(config.line_width)
            win.fig1.draw()
    pass

def visiable1():
    ischecked = win.checkVisible_1.isChecked()
    if ischecked == True:
        win.drawing()
    elif ischecked == False:
        fig, ax = win.fig1, win.fig1.axes
        print('Before :', ax.get_lines())
        ax.cla()
        fig.draw()
        print('After :', ax.get_lines())
    pass

def visiable2():
    ischecked = win.checkVisible_2.isChecked()
    if ischecked == True:
        win.drawing(line_label=2)
    elif ischecked == False:
        fig, ax = win.fig1, win.fig1.axes
        for index, line in enumerate(win.fig1.axes.get_lines()):
            print('Lines label :', line.get_label())
            if line.get_label() in [config.Line_name[i]+str(2) for i in config.Line_name]:
                win.fig1.axes.lines.remove(line)
        fig.draw()
    pass

class MyConfiguration():
    def __init__(self):
        self.line_color = 'b'
        self.line_width = 0.8
        self.mat_data = np.zeros((100, 256))
        self.Line_name = {'title':'Spectral_Curve', 'min_x':'Min_index',\
                          'min_y':'Min_peak', 'max_x':'Max_index', 'max_y':'Max_peak'}

    def updatedata_callback(self, data_mat):
        self.mat_data = data_mat

if __name__ == '__main__':
    config = MyConfiguration()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    # Two windows i create : MainWindow and AppWindow! I just show AppWindow!
    ui.setupUi(MainWindow)
    # MainWindow.show()
    win = AppWindow()
    win.show()
    ###### My functions #######
    win.actionAbout.triggered.connect(about)
    win.actionOpen.triggered.connect(openfile)
    win.actionSave_Data.triggered.connect(savefile)
    win.checkVisible_1.clicked.connect(visiable1) # Don't add () after func, or you will get a Nonetype Error!!!
    win.checkVisible_2.clicked.connect(visiable2)
    # win.checkVisible_3.clicked.connect(visiable3)
    win.comboColor_1.currentTextChanged['QString'].connect(color_change1)
    win.horizontalSlider_1.valueChanged['int'].connect(line_width1)
    # ui.pushButton.clicked.connect(Myplot.change_sys)
    #########################
    sys.exit(app.exec_())
