from PySide6.QtWidgets import QApplication, QDialog, QMainWindow
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class HelloWorld(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('standard.ui', None)
        self.ui.show()
        self.label = ''

        self.ui.btnSum.clicked.connect(lambda: self.operation('sum'))
        self.ui.btnSub.clicked.connect(lambda: self.operation('sub'))
        self.ui.btnMul.clicked.connect(lambda: self.operation('mul'))
        self.ui.btnDiv.clicked.connect(lambda: self.operation('div'))
        self.ui.btnRemove.clicked.connect(lambda: self.operation('rem'))
        self.ui.btnPourcent.clicked.connect(lambda: self.operation('pour'))
        self.ui.btnPower.clicked.connect(lambda: self.operation('pow'))
        self.ui.btnEqual.clicked.connect(self.equal)

        self.ui.btn1.clicked.connect(lambda: self.functionNum('1'))
        self.ui.btn2.clicked.connect(lambda: self.functionNum('2'))
        self.ui.btn3.clicked.connect(lambda: self.functionNum('3'))
        self.ui.btn4.clicked.connect(lambda: self.functionNum('4'))
        self.ui.btn5.clicked.connect(lambda: self.functionNum('5'))
        self.ui.btn6.clicked.connect(lambda: self.functionNum('6'))
        self.ui.btn7.clicked.connect(lambda: self.functionNum('7'))
        self.ui.btn8.clicked.connect(lambda: self.functionNum('8'))
        self.ui.btn9.clicked.connect(lambda: self.functionNum('9'))
        self.ui.btn0.clicked.connect(lambda: self.functionNum('0'))
        self.ui.btnPoint.clicked.connect(self.functionPoint)

    def functionNum(self, digit):
        for d in digit:
            self.ui.textBox.setText(self.ui.textBox.text() + d)

    def operation(self, op):
        self.num = float(self.ui.textBox.text())
        self.ui.textBox.setText('')
        if op == 'sum':
            self.label = '+'
        elif op == 'sub':
            self.label = '-'
        elif op == 'mul':
            self.label = '*'
        elif op == 'div':
            self.label = '/'
        elif op == 'rem':
            self.ui.textBox.setText('')
            self.label = 'AC'
        elif op == 'pour':
            self.label = '%'
        elif op == 'pow':
            self.label = '^2'
    
    def functionPoint(self):
        for i in self.ui.textBox.text():
            if '.' not in self.ui.textBox.text():
                self.ui.textBox.setText(self.ui.textBox.text() + '.')
        
    def equal(self): 
        self.num2 = float(self.ui.textBox.text())
        if self.label == '+':
                res = self.num + self.num2
        elif self.label == '-':
                res = self.num - self.num2
        elif self.label == '*':
                res = self.num * self.num2
        elif self.label == '/':
            if self.num2 == 0:
                res = 'Division by Zero'
            else:
                res = self.num / self.num2
        elif self.label == 'AC':
            res = self.ui.textBox.setText('')
        elif self.label == '%':
            res = self.num2 / 100
        elif self.label == '^2':
            res = self.num ** 2
               
        self.ui.textBox.setText(str(res))



app = QApplication([])
window = HelloWorld()

app.exec_()


