# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 697)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(251, 489))
        self.tabWidget.setMaximumSize(QtCore.QSize(251, 16777215))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupSetting = QtWidgets.QGroupBox(self.tab)
        self.groupSetting.setGeometry(QtCore.QRect(10, 10, 221, 110))
        self.groupSetting.setMinimumSize(QtCore.QSize(221, 110))
        self.groupSetting.setMaximumSize(QtCore.QSize(221, 110))
        self.groupSetting.setObjectName("groupSetting")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupSetting)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelFruit = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelFruit.setObjectName("labelFruit")
        self.horizontalLayout.addWidget(self.labelFruit)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupSetting)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 60, 199, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushWifi = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushWifi.setObjectName("pushWifi")
        self.horizontalLayout_3.addWidget(self.pushWifi)
        self.labelWifi = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.labelWifi.setObjectName("labelWifi")
        self.horizontalLayout_3.addWidget(self.labelWifi)
        self.groupCurve = QtWidgets.QGroupBox(self.tab)
        self.groupCurve.setGeometry(QtCore.QRect(10, 130, 221, 211))
        self.groupCurve.setMinimumSize(QtCore.QSize(221, 211))
        self.groupCurve.setMaximumSize(QtCore.QSize(221, 211))
        self.groupCurve.setObjectName("groupCurve")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupCurve)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 201, 168))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelScanTimes = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelScanTimes.setMaximumSize(QtCore.QSize(16777215, 28))
        self.labelScanTimes.setObjectName("labelScanTimes")
        self.horizontalLayout_2.addWidget(self.labelScanTimes)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(20)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushDetection = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushDetection.setObjectName("pushDetection")
        self.verticalLayout_2.addWidget(self.pushDetection)
        self.pushOriginal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushOriginal.setObjectName("pushOriginal")
        self.verticalLayout_2.addWidget(self.pushOriginal)
        self.pushDerivative = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushDerivative.setObjectName("pushDerivative")
        self.verticalLayout_2.addWidget(self.pushDerivative)
        self.pushIntegral = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushIntegral.setObjectName("pushIntegral")
        self.verticalLayout_2.addWidget(self.pushIntegral)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 350, 221, 261))
        self.tableWidget.setMinimumSize(QtCore.QSize(221, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(221, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupLine_1 = QtWidgets.QGroupBox(self.tab_2)
        self.groupLine_1.setGeometry(QtCore.QRect(10, 10, 221, 141))
        self.groupLine_1.setObjectName("groupLine_1")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupLine_1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 181, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelLineWidth_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelLineWidth_1.setObjectName("labelLineWidth_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelLineWidth_1)
        self.horizontalSlider_1 = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1.setObjectName("horizontalSlider_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_1)
        self.labelColor_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelColor_1.setObjectName("labelColor_1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelColor_1)
        self.comboColor_1 = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboColor_1.setObjectName("comboColor_1")
        self.comboColor_1.addItem("")
        self.comboColor_1.addItem("")
        self.comboColor_1.addItem("")
        self.comboColor_1.addItem("")
        self.comboColor_1.addItem("")
        self.comboColor_1.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboColor_1)
        self.checkVisible_1 = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkVisible_1.setChecked(True)
        self.checkVisible_1.setObjectName("checkVisible_1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkVisible_1)
        self.groupLine_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupLine_2.setGeometry(QtCore.QRect(10, 170, 221, 141))
        self.groupLine_2.setObjectName("groupLine_2")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupLine_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 181, 101))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.labelLineWidth_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.labelLineWidth_2.setObjectName("labelLineWidth_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelLineWidth_2)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.formLayoutWidget_3)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_3)
        self.labelColor_2 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.labelColor_2.setObjectName("labelColor_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelColor_2)
        self.comboColor_2 = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.comboColor_2.setObjectName("comboColor_2")
        self.comboColor_2.addItem("")
        self.comboColor_2.addItem("")
        self.comboColor_2.addItem("")
        self.comboColor_2.addItem("")
        self.comboColor_2.addItem("")
        self.comboColor_2.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboColor_2)
        self.checkVisible_2 = QtWidgets.QCheckBox(self.formLayoutWidget_3)
        self.checkVisible_2.setChecked(True)
        self.checkVisible_2.setObjectName("checkVisible_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkVisible_2)
        self.groupLine_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupLine_3.setGeometry(QtCore.QRect(10, 330, 221, 141))
        self.groupLine_3.setObjectName("groupLine_3")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupLine_3)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 181, 101))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.labelLineWidth_3 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.labelLineWidth_3.setObjectName("labelLineWidth_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelLineWidth_3)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.formLayoutWidget_4)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.horizontalSlider_4)
        self.labelColor_3 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.labelColor_3.setObjectName("labelColor_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelColor_3)
        self.comboColor_3 = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.comboColor_3.setObjectName("comboColor_3")
        self.comboColor_3.addItem("")
        self.comboColor_3.addItem("")
        self.comboColor_3.addItem("")
        self.comboColor_3.addItem("")
        self.comboColor_3.addItem("")
        self.comboColor_3.addItem("")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboColor_3)
        self.checkVisible_3 = QtWidgets.QCheckBox(self.formLayoutWidget_4)
        self.checkVisible_3.setChecked(True)
        self.checkVisible_3.setObjectName("checkVisible_3")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkVisible_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Data = QtWidgets.QAction(MainWindow)
        self.actionSave_Data.setObjectName("actionSave_Data")
        self.actionSave_Graph = QtWidgets.QAction(MainWindow)
        self.actionSave_Graph.setObjectName("actionSave_Graph")
        self.actionLine = QtWidgets.QAction(MainWindow)
        self.actionLine.setObjectName("actionLine")
        self.actionUsage = QtWidgets.QAction(MainWindow)
        self.actionUsage.setObjectName("actionUsage")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCopyright = QtWidgets.QAction(MainWindow)
        self.actionCopyright.setObjectName("actionCopyright")
        self.actionWi_Fi_Setting = QtWidgets.QAction(MainWindow)
        self.actionWi_Fi_Setting.setObjectName("actionWi_Fi_Setting")
        self.menuSave.addAction(self.actionSave_Data)
        self.menuSave.addAction(self.actionSave_Graph)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuSettings.addAction(self.actionLine)
        self.menuSettings.addAction(self.actionWi_Fi_Setting)
        self.menuHelp.addAction(self.actionUsage)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCopyright)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.checkVisible_1.clicked.connect(self.checkVisible_1.click)
        self.checkVisible_2.clicked.connect(self.checkVisible_2.click)
        self.checkVisible_3.clicked.connect(self.checkVisible_3.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "水果光谱检测"))
        self.groupSetting.setTitle(_translate("MainWindow", "Setting"))
        self.labelFruit.setText(_translate("MainWindow", "Fruit"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Apple"))
        self.pushWifi.setText(_translate("MainWindow", "Wi-Fi"))
        self.labelWifi.setText(_translate("MainWindow", "unconnected"))
        self.groupCurve.setTitle(_translate("MainWindow", "Curve"))
        self.labelScanTimes.setText(_translate("MainWindow", "ScanTimes"))
        self.pushDetection.setText(_translate("MainWindow", "Spectral Detection"))
        self.pushOriginal.setText(_translate("MainWindow", "Original Time"))
        self.pushDerivative.setText(_translate("MainWindow", "Derivative Time"))
        self.pushIntegral.setText(_translate("MainWindow", "Integral Time"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Energy"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Carbohydrates"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "-Sugars"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Protein"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sodium"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Per 100g"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "检测"))
        self.groupLine_1.setTitle(_translate("MainWindow", "Line1"))
        self.labelLineWidth_1.setText(_translate("MainWindow", "Width"))
        self.labelColor_1.setText(_translate("MainWindow", "Color"))
        self.comboColor_1.setItemText(0, _translate("MainWindow", "Black"))
        self.comboColor_1.setItemText(1, _translate("MainWindow", "Gray"))
        self.comboColor_1.setItemText(2, _translate("MainWindow", "White"))
        self.comboColor_1.setItemText(3, _translate("MainWindow", "Red"))
        self.comboColor_1.setItemText(4, _translate("MainWindow", "Green"))
        self.comboColor_1.setItemText(5, _translate("MainWindow", "Blue"))
        self.checkVisible_1.setText(_translate("MainWindow", "Visible"))
        self.groupLine_2.setTitle(_translate("MainWindow", "Line2"))
        self.labelLineWidth_2.setText(_translate("MainWindow", "Width"))
        self.labelColor_2.setText(_translate("MainWindow", "Color"))
        self.comboColor_2.setItemText(0, _translate("MainWindow", "Green"))
        self.comboColor_2.setItemText(1, _translate("MainWindow", "Black"))
        self.comboColor_2.setItemText(2, _translate("MainWindow", "Gray"))
        self.comboColor_2.setItemText(3, _translate("MainWindow", "White"))
        self.comboColor_2.setItemText(4, _translate("MainWindow", "Red"))
        self.comboColor_2.setItemText(5, _translate("MainWindow", "Blue"))
        self.checkVisible_2.setText(_translate("MainWindow", "Visible"))
        self.groupLine_3.setTitle(_translate("MainWindow", "Line3"))
        self.labelLineWidth_3.setText(_translate("MainWindow", "Width"))
        self.labelColor_3.setText(_translate("MainWindow", "Color"))
        self.comboColor_3.setItemText(0, _translate("MainWindow", "Red"))
        self.comboColor_3.setItemText(1, _translate("MainWindow", "Black"))
        self.comboColor_3.setItemText(2, _translate("MainWindow", "Gray"))
        self.comboColor_3.setItemText(3, _translate("MainWindow", "White"))
        self.comboColor_3.setItemText(4, _translate("MainWindow", "Green"))
        self.comboColor_3.setItemText(5, _translate("MainWindow", "Blue"))
        self.checkVisible_3.setText(_translate("MainWindow", "Visible"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "设置"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_Data.setText(_translate("MainWindow", "Save Data"))
        self.actionSave_Graph.setText(_translate("MainWindow", "Save Graph"))
        self.actionLine.setText(_translate("MainWindow", "Line Setting"))
        self.actionUsage.setText(_translate("MainWindow", "Usage"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionCopyright.setText(_translate("MainWindow", "Copyright"))
        self.actionWi_Fi_Setting.setText(_translate("MainWindow", "Wi-Fi Setting"))
