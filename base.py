# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steganos.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(250, 30, 301, 94))
        self.title.setMinimumSize(QtCore.QSize(301, 0))
        self.title.setObjectName("title")
        self.subtitile = QtWidgets.QLabel(self.centralwidget)
        self.subtitile.setGeometry(QtCore.QRect(240, 120, 321, 46))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.subtitile.setFont(font)
        self.subtitile.setObjectName("subtitile")
        self.text = QtWidgets.QLineEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(80, 200, 550, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.key = QtWidgets.QLineEdit(self.centralwidget)
        self.key.setGeometry(QtCore.QRect(80, 240, 550, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.key.setFont(font)
        self.key.setObjectName("key")
        self.image = QtWidgets.QLineEdit(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(80, 280, 550, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.image.setFont(font)
        self.image.setObjectName("image")
        self.key_label = QtWidgets.QLabel(self.centralwidget)
        self.key_label.setGeometry(QtCore.QRect(640, 240, 34, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.key_label.setFont(font)
        self.key_label.setObjectName("key_label")
        self.text_label = QtWidgets.QLabel(self.centralwidget)
        self.text_label.setGeometry(QtCore.QRect(637, 200, 34, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.text_label.setFont(font)
        self.text_label.setObjectName("text_label")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(640, 280, 93, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.image_label.setFont(font)
        self.image_label.setObjectName("image_label")
        self.mode_button_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.mode_button_1.setGeometry(QtCore.QRect(90, 350, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.mode_button_1.setFont(font)
        self.mode_button_1.setObjectName("mode_button_1")
        self.mode_button_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.mode_button_2.setGeometry(QtCore.QRect(90, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.mode_button_2.setFont(font)
        self.mode_button_2.setChecked(True)
        self.mode_button_2.setObjectName("mode_button_2")
        self.mode_label = QtWidgets.QLabel(self.centralwidget)
        self.mode_label.setGeometry(QtCore.QRect(90, 330, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mode_label.setFont(font)
        self.mode_label.setObjectName("mode_label")
        self.settings_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_label.setGeometry(QtCore.QRect(270, 322, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.settings_label.setFont(font)
        self.settings_label.setObjectName("settings_label")
        self.radius_constant_slider = QtWidgets.QSlider(self.centralwidget)
        self.radius_constant_slider.setEnabled(True)
        self.radius_constant_slider.setGeometry(QtCore.QRect(280, 360, 160, 20))
        self.radius_constant_slider.setMinimum(1)
        self.radius_constant_slider.setMaximum(20)
        self.radius_constant_slider.setProperty("value", 10)
        self.radius_constant_slider.setOrientation(QtCore.Qt.Horizontal)
        self.radius_constant_slider.setObjectName("radius_constant_slider")
        self.radius_constant_label = QtWidgets.QLabel(self.centralwidget)
        self.radius_constant_label.setGeometry(QtCore.QRect(460, 350, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radius_constant_label.setFont(font)
        self.radius_constant_label.setObjectName("radius_constant_label")
        self.avg_radius_constant_slider = QtWidgets.QSlider(self.centralwidget)
        self.avg_radius_constant_slider.setGeometry(QtCore.QRect(280, 390, 160, 20))
        self.avg_radius_constant_slider.setMinimum(1)
        self.avg_radius_constant_slider.setMaximum(20)
        self.avg_radius_constant_slider.setProperty("value", 9)
        self.avg_radius_constant_slider.setOrientation(QtCore.Qt.Horizontal)
        self.avg_radius_constant_slider.setObjectName("avg_radius_constant_slider")
        self.avg_radius_constant_label = QtWidgets.QLabel(self.centralwidget)
        self.avg_radius_constant_label.setGeometry(QtCore.QRect(460, 380, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.avg_radius_constant_label.setFont(font)
        self.avg_radius_constant_label.setObjectName("avg_radius_constant_label")
        self.max_rejects_constants_slider = QtWidgets.QSlider(self.centralwidget)
        self.max_rejects_constants_slider.setGeometry(QtCore.QRect(280, 420, 160, 20))
        self.max_rejects_constants_slider.setMinimum(25000)
        self.max_rejects_constants_slider.setMaximum(100000)
        self.max_rejects_constants_slider.setProperty("value", 50000)
        self.max_rejects_constants_slider.setSliderPosition(50000)
        self.max_rejects_constants_slider.setOrientation(QtCore.Qt.Horizontal)
        self.max_rejects_constants_slider.setObjectName("max_rejects_constants_slider")
        self.max_rejects_constant_label = QtWidgets.QLabel(self.centralwidget)
        self.max_rejects_constant_label.setGeometry(QtCore.QRect(460, 410, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.max_rejects_constant_label.setFont(font)
        self.max_rejects_constant_label.setObjectName("max_rejects_constant_label")
        self.encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt.setGeometry(QtCore.QRect(430, 480, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.encrypt.setFont(font)
        self.encrypt.setObjectName("encrypt")
        self.decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt.setGeometry(QtCore.QRect(260, 480, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.decrypt.setFont(font)
        self.decrypt.setObjectName("decrypt")
        self.radius_constant_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.radius_constant_spinbox.setGeometry(QtCore.QRect(650, 360, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.radius_constant_spinbox.setFont(font)
        self.radius_constant_spinbox.setMinimum(1)
        self.radius_constant_spinbox.setMaximum(20)
        self.radius_constant_spinbox.setProperty("value", 10)
        self.radius_constant_spinbox.setObjectName("radius_constant_spinbox")
        self.avg_radius_constant_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.avg_radius_constant_spinbox.setGeometry(QtCore.QRect(650, 390, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.avg_radius_constant_spinbox.setFont(font)
        self.avg_radius_constant_spinbox.setMinimum(1)
        self.avg_radius_constant_spinbox.setMaximum(20)
        self.avg_radius_constant_spinbox.setProperty("value", 9)
        self.avg_radius_constant_spinbox.setObjectName("avg_radius_constant_spinbox")
        self.max_rejects_constant_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.max_rejects_constant_spinbox.setGeometry(QtCore.QRect(650, 420, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.max_rejects_constant_spinbox.setFont(font)
        self.max_rejects_constant_spinbox.setMinimum(25000)
        self.max_rejects_constant_spinbox.setMaximum(100000)
        self.max_rejects_constant_spinbox.setProperty("value", 50000)
        self.max_rejects_constant_spinbox.setObjectName("max_rejects_constant_spinbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.help_menu = QtWidgets.QMenuBar(MainWindow)
        self.help_menu.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.help_menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.help_menu.setAutoFillBackground(False)
        self.help_menu.setDefaultUp(False)
        self.help_menu.setNativeMenuBar(True)
        self.help_menu.setObjectName("help_menu")
        self.menuHelp = QtWidgets.QMenu(self.help_menu)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.help_menu)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionContact)
        self.help_menu.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.mode_button_1.clicked.connect(self.settings_label.hide)
        self.mode_button_1.clicked.connect(self.radius_constant_slider.hide)
        self.mode_button_1.clicked.connect(self.radius_constant_label.hide)
        self.mode_button_1.clicked.connect(self.avg_radius_constant_slider.hide)
        self.mode_button_1.clicked.connect(self.avg_radius_constant_label.hide)
        self.mode_button_1.clicked.connect(self.max_rejects_constants_slider.hide)
        self.mode_button_1.clicked.connect(self.max_rejects_constant_label.hide)
        self.mode_button_2.clicked.connect(self.settings_label.show)
        self.mode_button_2.clicked.connect(self.radius_constant_slider.show)
        self.mode_button_2.clicked.connect(self.radius_constant_label.show)
        self.mode_button_2.clicked.connect(self.avg_radius_constant_slider.show)
        self.mode_button_2.clicked.connect(self.avg_radius_constant_label.show)
        self.mode_button_2.clicked.connect(self.max_rejects_constants_slider.show)
        self.mode_button_2.clicked.connect(self.max_rejects_constant_label.show)
        self.mode_button_2.clicked.connect(self.key_label.show)
        self.mode_button_1.clicked.connect(self.key_label.hide)
        self.mode_button_1.clicked.connect(self.key.hide)
        self.mode_button_2.clicked.connect(self.key.show)
        self.radius_constant_spinbox.valueChanged['int'].connect(self.radius_constant_slider.setValue)
        self.radius_constant_slider.valueChanged['int'].connect(self.radius_constant_spinbox.setValue)
        self.avg_radius_constant_spinbox.valueChanged['int'].connect(self.avg_radius_constant_slider.setValue)
        self.avg_radius_constant_slider.valueChanged['int'].connect(self.avg_radius_constant_spinbox.setValue)
        self.max_rejects_constant_spinbox.valueChanged['int'].connect(self.max_rejects_constants_slider.setValue)
        self.max_rejects_constants_slider.valueChanged['int'].connect(self.max_rejects_constant_spinbox.setValue)
        self.mode_button_1.clicked.connect(self.radius_constant_spinbox.hide)
        self.mode_button_1.clicked.connect(self.avg_radius_constant_spinbox.hide)
        self.mode_button_1.clicked.connect(self.max_rejects_constant_spinbox.hide)
        self.mode_button_2.clicked.connect(self.radius_constant_spinbox.show)
        self.mode_button_2.clicked.connect(self.avg_radius_constant_spinbox.show)
        self.mode_button_2.clicked.connect(self.max_rejects_constant_spinbox.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.text, self.key)
        MainWindow.setTabOrder(self.key, self.image)
        MainWindow.setTabOrder(self.image, self.mode_button_1)
        MainWindow.setTabOrder(self.mode_button_1, self.mode_button_2)
        MainWindow.setTabOrder(self.mode_button_2, self.radius_constant_slider)
        MainWindow.setTabOrder(self.radius_constant_slider, self.avg_radius_constant_slider)
        MainWindow.setTabOrder(self.avg_radius_constant_slider, self.max_rejects_constants_slider)
        MainWindow.setTabOrder(self.max_rejects_constants_slider, self.encrypt)
        MainWindow.setTabOrder(self.encrypt, self.decrypt)
        MainWindow.setTabOrder(self.decrypt, self.radius_constant_spinbox)
        MainWindow.setTabOrder(self.radius_constant_spinbox, self.avg_radius_constant_spinbox)
        MainWindow.setTabOrder(self.avg_radius_constant_spinbox, self.max_rejects_constant_spinbox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steganos - v1.0.0"))
        self.title.setText(_translate("MainWindow", "Steganos"))
        self.subtitile.setText(_translate("MainWindow", "Hidden in plain sight"))
        self.text.setPlaceholderText(_translate("MainWindow", "Lorem ipsum dolor sit amet"))
        self.key.setPlaceholderText(_translate("MainWindow", "Password"))
        self.image.setPlaceholderText(_translate("MainWindow", "C:\\Users\\matte\\Images\\image.png"))
        self.key_label.setText(_translate("MainWindow", "Key"))
        self.text_label.setText(_translate("MainWindow", "Text"))
        self.image_label.setText(_translate("MainWindow", "Image Path"))
        self.mode_button_1.setText(_translate("MainWindow", "Blatant"))
        self.mode_button_2.setText(_translate("MainWindow", "Steganos"))
        self.mode_label.setText(_translate("MainWindow", "Mode:"))
        self.settings_label.setText(_translate("MainWindow", "Settings:"))
        self.radius_constant_label.setText(_translate("MainWindow", "Radius Constant"))
        self.avg_radius_constant_label.setText(_translate("MainWindow", "Avg. Radius Constant"))
        self.max_rejects_constant_label.setText(_translate("MainWindow", "Max Rejects Constant"))
        self.encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.menuHelp.setTitle(_translate("MainWindow", "?"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))
