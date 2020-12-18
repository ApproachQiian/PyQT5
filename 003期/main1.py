import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random


def setupUI():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(1290, 861)
    window.setWindowTitle('编程创造城市001期')

    figure = plt.figure(facecolor='#FFD7C4', figsize=(600, 600))
    canvas = FigureCanvas(figure)

    btn = QPushButton('生成图像', window)
    btn.setGeometry(250, 620, 131, 41)

    btn2 = QPushButton('清除图像', window)
    btn2.setGeometry(40, 720, 137, 39)

    btn3 = QPushButton('提取特征', window)
    btn3.setGeometry(185, 720, 137, 39)

    btn4 = QPushButton('保存图像', window)
    btn4.setGeometry(329, 720, 137, 39)

    btn4 = QPushButton('退出程序', window)
    btn4.setGeometry(473, 720, 137, 39)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    setupUI()
