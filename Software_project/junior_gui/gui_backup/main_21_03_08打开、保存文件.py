import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import original_11_24_wfh_2
from original_11_24_wfh_2 import Ui_MainWindow
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

class PlotCanvas(FigureCanvas): # matplotlib 嵌入 qt

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        # 清屏
        plt.cla()
        data = [random.random() for i in range(25)]
        # ax = self.figure.add_subplot(111)
        # ax.plot(data, 'r-')
        # ax.set_title('PyQt Matplotlib Example')
        # self.draw()
        print('hello')

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = original_11_24_wfh_2.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # textEdit
    # ui.actionSave_Data.triggered.connect(save_data)
    ui.pushButton.clicked.connect(PlotCanvas.plot)
    ui.actionOpen.triggered.connect(openfile)
    ui.actionSave_Data.triggered.connect(savefile)
    #
    sys.exit(app.exec_())
