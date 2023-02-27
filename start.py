from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('start.ui', None)
        self.ui.show()

        self.ui.rBtnStd.clicked.connect(self.standard)
        self.ui.rBtnAdv.clicked.connect(self.advance)
        self.ui.ExitBtn.clicked.connect(self.btnExin)
        self.ui.OkBtn.clicked.connect(self.btnExin)


    def standard(self):
        self.loader = QUiLoader()
        self.ui = self.loader.load('standard.ui', None)
        self.ui.show()

    def advance(self):
        self.loader = QUiLoader()
        self.ui = self.loader.load('advance.ui', None)
        self.ui.show()
    
    def btnExin(self):
        self.close()




app = QApplication([])
screen = Window()
screen.show()

app.exec_()