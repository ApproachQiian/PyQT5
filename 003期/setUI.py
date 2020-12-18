import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGroupBox, QTextEdit, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUI()
        self.show()

    def setupUI(self):
        self.resize(1290, 861)
        self.setWindowTitle('Create AnimeFaces With DCGan!')
        self.setWindowIcon(QIcon(r'E:\pycharm_Projects\科研实践\dataset\images\favicon.ico'))

        self.figure = plt.figure(figsize=(600, 600), facecolor='#FFD7C4')
        self.canvas = FigureCanvas(self.figure)

        self.draw_image_btn = QPushButton('生成图像', self)
        self.draw_image_btn.setGeometry(250, 620, 131, 41)

        self.clear_image_btn = QPushButton('清除图像', self)
        self.clear_image_btn.setGeometry(40, 720, 137, 39)

        self.extract_feature_btn = QPushButton('提取特征', self)
        self.extract_feature_btn.setGeometry(185, 720, 137, 39)

        self.save_image_btn = QPushButton('保存图像', self)
        self.save_image_btn.setGeometry(329, 720, 137, 39)

        self.exit_app_btn = QPushButton('退出程序', self)
        self.exit_app_btn.setGeometry(473, 720, 137, 39)
        self.exit_app_btn.clicked.connect(self.close)
        self.groupBox = QGroupBox('图像处理信息', self)
        self.groupBox.setStyleSheet(' border:1px solid #bfd1eb;background:#f3faff')
        self.groupBox.setGeometry(670, 20, 571, 711)
        self.textEdit = QTextEdit(self)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(700, 50, 521, 671)
        self.textEdit.setPlaceholderText('图像信息显示....')
        self.textEdit.setStyleSheet(" border:1px solid #adcd3c;background:#F2FDDB")
        self.clear_console_button = QPushButton('清除信息', self)
        self.clear_console_button.setGeometry(920, 750, 121, 41)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '退出程序', "真的要退出程序吗QAQ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
