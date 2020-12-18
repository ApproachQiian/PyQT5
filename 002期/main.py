import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Create AnimeFaces With DCGan!')
        self.resize(1290, 861)
        self.setWindowIcon(QIcon(r'E:\pycharm_Projects\科研实践\dataset\images\favicon.ico'))

        # 设置绘图窗口
        self.figure = plt.figure(facecolor='#FFD7C4', figsize=(600, 600))
        self.canvas = FigureCanvas(self.figure)

        # 设置生成图像按钮
        self.show_image_btn = QPushButton('生成图像', Window)
        self.show_image_btn.setGeometry(250, 620, 131, 41)
        self.show_image_btn.clicked.connect(self.draw_image)

    def draw_image(self):
        x = range(10)
        y = [random.random() for _ in range(10)]
        plt.clf()
        plt.plot(x, y)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
