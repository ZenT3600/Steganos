import time
import sys

from colored import fg, attr
from PyQt5 import QtWidgets, QtGui

from base import Ui_MainWindow
from Logic import SteganoMode, BlatantMode


class Logger:
    @staticmethod
    def info(msg):
        print(f"{fg(225) + attr(1)}[{time.strftime('%Y-%m-%d %H:%M.%S', time.localtime())}] (Info) --> {attr(0) + fg(225)}{msg}{fg(0)}")

    @staticmethod
    def debug(msg):
        print(f"{fg(40) + attr(1)}[{time.strftime('%Y-%m-%d %H:%M.%S', time.localtime())}] (Debug) --> {attr(0) + fg(40)}{msg}{fg(0)}")

    @staticmethod
    def warning(msg):
        print(f"{fg(220) + attr(1)}[{time.strftime('%Y-%m-%d %H:%M.%S', time.localtime())}] (Warning!) --> {attr(0) + fg(220)}{msg}{fg(0)}")

    @staticmethod
    def error(msg):
        print(f"{fg(9) + attr(1)}[{time.strftime('%Y-%m-%d %H:%M.%S', time.localtime())}] (!Error!) --> {attr(0)+ fg(9)}{msg}{fg(0)}")


class Ui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)

        Logger.info("Loaded GUI blueprint")
        self.setWindowIcon(QtGui.QIcon("key.png"))
        self.show()

        self.encrypt = self.findChild(QtWidgets.QPushButton, "encrypt")
        self.decrypt = self.findChild(QtWidgets.QPushButton, "decrypt")

        self.text = self.findChild(QtWidgets.QLineEdit, "text")
        self.key = self.findChild(QtWidgets.QLineEdit, "key")
        self.image = self.findChild(QtWidgets.QLineEdit, "image")

        self.radius_constant = self.findChild(QtWidgets.QSpinBox, "radius_constant_spinbox")
        self.avg_radius_constant = self.findChild(QtWidgets.QSpinBox, "avg_radius_constant_spinbox")
        self.max_rejects_constant = self.findChild(QtWidgets.QSpinBox, "max_rejects_constant_spinbox")

        self.blatant_radiobtn = self.findChild(QtWidgets.QRadioButton, "mode_button_1")
        self.steganos_radiobtn = self.findChild(QtWidgets.QRadioButton, "mode_button_2")
        Logger.info("Referenced useful widgets")

        self.encrypt.clicked.connect(self.encryptRoutine)
        self.decrypt.clicked.connect(self.decryptRoutine)
        self.findChild(QtWidgets.QAction, "actionHelp").triggered.connect(self.help)
        self.findChild(QtWidgets.QAction, "actionContact").triggered.connect(self.contact)
        Logger.info("Connected widget events")

    def contact(self):
        self.showDialog(QtWidgets.QMessageBox.Information,
                        "Steganos - Contacts",
                        "Website: www.matteoleggio.it\n"
                        "Instagram: @zent3600\n"
                        "Reddit: u/ZenT3600\n"
                        "Telegram: @ZenT3600")

    def help(self):
        self.showDialog(QtWidgets.QMessageBox.Information,
                        "Steganos - Help",
                        "Steganos\n"
                        "Hidden in plain sight\n"
                        "\n"
                        "----------\n"
                        "\n"
                        "Modes:\n"
                        "-----\n"
                        "Blatant --> Colored pixels on black background\n"
                        "Steganos --> Actual hidden image\n"
                        "\n\n"
                        "Settings (Only touch if experienced):\n"
                        "-----\n"
                        "Radius Constant --> The safe radius between every encrypted pixel\n"
                        "Avg. Radius Constant --> The radius to get the estimated average color of a pixel from\n"
                        "Max Rejects --> The max number of times the program can be rejected before giving up")

    def showDialog(self, icon, title, body):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(icon)
        msg.setText(body)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def encryptRoutine(self):
        Logger.info("Entered encrypting routine")
        try:
            Logger.debug(f"Image: {self.image.text()}\n"
                         f"\t\t\tKey: {self.key.text()}\n"
                         f"\t\t\tText: {self.text.text()}")
            Logger.debug(f"Image Type: {type(self.image.text())}\n"
                         f"\t\t\tKey Type: {type(self.key.text())}\n"
                         f"\t\t\tText Type: {type(self.text.text())}")
            Logger.debug(f"Settings: {self.max_rejects_constant.value()}\n"
                         f"\t\t\t{self.radius_constant.value()}\n"
                         f"\t\t\t{self.avg_radius_constant.value()}")

            if self.text.text():
                if self.blatant_radiobtn.isChecked():
                    Logger.info("Blatant mode selected")
                    c = BlatantMode.Steganos()
                else:
                    Logger.info("Stegano mode selected")
                    if not self.key.text():
                        Logger.warning("No key given")
                        self.showDialog(QtWidgets.QMessageBox.Warning,
                                        "Error!",
                                        f"No key given")
                        return
                    if self.avg_radius_constant.value() > self.radius_constant.value():
                        self.showDialog(QtWidgets.QMessageBox.Warning,
                                        "Error!",
                                        f"Avg. Radius Constant can't be higher than Radius Constant")
                        return

                    c = SteganoMode.Steganos(str(self.image.text()), str(self.key.text()),
                                                int(self.max_rejects_constant.value()),
                                                int(self.radius_constant.value()),
                                                int(self.avg_radius_constant.value()))

                file = c.cypherRoutine(self.text.text())
                Logger.debug(f"Generated file: {file}")

                self.showDialog(QtWidgets.QMessageBox.Information, "Success!", f"New Hidden Image: {file}")
            else:
                Logger.warning("No text given")
                self.showDialog(QtWidgets.QMessageBox.Warning,
                                "Error!",
                                f"No text given")
        except Exception as e:
            self.showDialog(QtWidgets.QMessageBox.Critical, "Critical!", f"Error: {e}")
        
    def decryptRoutine(self):
        Logger.info("Entered decrypting routine")
        try:
            Logger.debug(f"Image: {self.image.text()}\n"
                         f"\t\t\tKey: {self.key.text()}\n"
                         f"\t\t\tText: {self.text.text()}")
            Logger.debug(f"Image Type: {type(self.image.text())}\n"
                         f"\t\t\tKey Type: {type(self.key.text())}\n"
                         f"\t\t\tText Type: {type(self.text.text())}")
            Logger.debug(f"Settings: {self.max_rejects_constant.value()}\n"
                         f"\t\t\t{self.radius_constant.value()}\n"
                         f"\t\t\t{self.avg_radius_constant.value()}")

            if self.blatant_radiobtn.isChecked():
                Logger.info("Blatant mode selected")
                if not self.image.text():
                    Logger.warning("No image given")
                    self.showDialog(QtWidgets.QMessageBox.Warning,
                                    "Error!",
                                    f"No image given")
                    return
                c = BlatantMode.Steganos(self.image.text())
            else:
                Logger.info("Stegano mode selected")
                if not self.key.text():
                    Logger.warning("No key given")
                    self.showDialog(QtWidgets.QMessageBox.Warning,
                                    "Error!",
                                    f"No key given")
                    return
                if self.avg_radius_constant.value() > self.radius_constant.value():
                    self.showDialog(QtWidgets.QMessageBox.Warning,
                                    "Error!",
                                    f"Avg. Radius Constant can't be higher than Radius Constant")
                    return

                c = SteganoMode.Steganos(str(self.image.text()), str(self.key.text()),
                                            int(self.max_rejects_constant.value()),
                                            int(self.radius_constant.value()),
                                            int(self.avg_radius_constant.value()))

            text = c.decipherRoutine()
            Logger.debug(f"Hidden text: {text}")

            self.showDialog(QtWidgets.QMessageBox.Information, "Success!", f"Text: {text}")
        except Exception as e:
            self.showDialog(QtWidgets.QMessageBox.Critical, "Critical!", f"Error: {e}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
