
from Ui_MainWindow import Ui_MainWindow
import Matplot
import Derivative_Culculate
import Lorenz_Culculate

class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)

        self.actionMatplot_Mandelort.triggered.connect(self.Show1)
        self.actionDerivaive_Calculator.triggered.connect(self.Show2)
        self.actionAx3D_Lorenz.triggered.connect(self.Show3)

    def Show1(self):
        self.child_Close()
        self.resize(525,600)
        self.child1 = Matplot.Main_window()
        self.gridLayout.addWidget(self.child1)
        self.child1.show()

    def Show2(self):
        self.child_Close()
        self.resize(525,375)
        self.child2 = Derivative_Culculate.Main_window()
        self.gridLayout.addWidget(self.child2)
        self.child2.show()

    def Show3(self):
        self.child_Close()
        self.resize(525,600)
        self.child3 = Lorenz_Culculate.Main_window()
        self.gridLayout.addWidget(self.child3)
        self.child3.show()

    def child_Close(self):
        try:
            self.child1.close()
            self.child2.close()
            self.child3.close()
            self.gridLayout.removeWidget(self.child1)
            self.gridLayout.removeWidget(self.child2)
            self.gridLayout.removeWidget(self.child3)
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
