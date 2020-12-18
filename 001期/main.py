import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(500, 300)
    window.setWindowTitle('编程创造城市001期')
    window.show()
    sys.exit(app.exec_())
