import sys
import random
from PyQt5.QtWidgets import QLabel, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PySide2 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        # init data
        self.oldPos = (0, 0)
        self.setCursor(self.getCursor(False))

        self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
            "Hola Mundo", "Привет мир"]

        # Layout elements
        self.button = QtWidgets.QPushButton("Click me!")

        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        pixmap = QtGui.QPixmap('./assets/hole_1.png')
        self.img = QtWidgets.QLabel()
        self.img.setPixmap(pixmap)


        # layout full
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        #self.layout.addWidget(self.button)
        self.layout.addWidget(self.img)
        self.setLayout(self.layout)


        # actions
        #self.button.clicked.connect(self.magic)





    def getCursor(self, isInversed):
        if(isInversed):
            pm = QtGui.QPixmap('./assets/shovel-mouse-inversed.png')
            pm.scaledToWidth(20)
            pm.scaledToHeight(20)
            return QtGui.QCursor(pm)
        else:
            pm = QtGui.QPixmap('./assets/shovel-mouse.png')
            pm.scaledToWidth(20)
            pm.scaledToHeight(20)
            return QtGui.QCursor(pm)


    def magic(self):
        self.text.setText(random.choice(self.hello))

    def mousePressEvent(self, QMouseEvent):
        self.setCursor(self.getCursor(True))
        print("old", self.oldPos)
        self.setOldPos((QMouseEvent.x(), QMouseEvent.y()))
        print("new",  self.getOldPos())
        print('(', QMouseEvent.x(), ', ', QMouseEvent.y(), ')')


    def mouseReleaseEvent(self, QMouseEvent):
        self.setCursor(self.getCursor(False))
        print("mouseRelease")



    def getOldPos(self):
        return self.oldPos
    def setOldPos(self, newPos):
        self.oldPos = newPos


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)


    widget = MyWidget()
    widget.show()


    sys.exit(app.exec_())