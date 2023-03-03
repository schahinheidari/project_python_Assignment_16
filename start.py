import standard
import advance
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *



class Window(QMainWindow, QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('project_python_Assignment_16/start.ui', None)
        self.ui.show()

        self.ui.BtnStd.clicked.connect(self.standard)
        self.ui.BtnAdv.clicked.connect(self.advance)
        self.ui.ExitBtn.clicked.connect(self.ui.close)


    def standard(self):
        self.addClass = standard.standardClass(self)

    def advance(self):
        self.addClass = advance.advanceClass(self)


app = QApplication([])
screen = Window()
screen.show()

app.exec_()