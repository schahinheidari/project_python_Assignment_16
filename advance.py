from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from math import sin, cos, tan, sqrt, radians

class advanceClass(QMainWindow, QWidget):
    def __init__(self):
        super(advanceClass, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load('project_python_Assignment_16/advance.ui', None)
        self.ui.show()
        self.label = ''


        self.ui.btnSum.clicked.connect(lambda: self.operation('sum'))
        self.ui.btnSub.clicked.connect(lambda: self.operation('sub'))
        self.ui.btnMul.clicked.connect(lambda: self.operation('mul'))
        self.ui.btnDiv.clicked.connect(lambda: self.operation('div'))
        self.ui.btnClear.clicked.connect(lambda: self.operation('rem'))
        self.ui.btnPourcent.clicked.connect(lambda: self.operation('pour'))
        self.ui.btnPower.clicked.connect(lambda: self.operation('pow'))
        self.ui.btnSin.clicked.connect(lambda: self.operation('sin'))
        self.ui.btnCos.clicked.connect(lambda: self.operation('cos'))
        self.ui.btnTan.clicked.connect(lambda: self.operation('tan'))
        self.ui.btnCot.clicked.connect(lambda: self.operation('cot'))
        self.ui.btnSqrt.clicked.connect(lambda: self.operation('sqrt'))

        self.ui.btnNeg.clicked.connect(self.negativeMeth)
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
        elif op == 'sin':
            self.label = 'Sin'
        elif op == 'cos':
            self.label = 'Cos'
        elif op == 'tan':
            self.label = 'Tan'
        elif op == 'cot':
            self.label = 'Cot'
        elif op == 'sqrt':
            self.label = '√'

    
    def functionPoint(self):
        for i in self.ui.textBox.text():
            if '.' not in self.ui.textBox.text():
                self.ui.textBox.setText(self.ui.textBox.text() + '.')
    
    def negativeMeth(self):
        self.ui.textbox.setText(str(-1 * float(self.ui.textbox.text())))
        
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
        elif self.label == 'Sin':
            res = sin(radians(self.num2)) 
        elif self.label == 'Cos':
            res = cos(radians(self.num2))
        elif self.label == 'Tan':
            res = tan(radians(self.num2))
        elif self.label == 'Cot':
            res = ((cos/sin)(radians(self.num2)))
        elif self.label == '√':
            res = sqrt(radians(self.num2))
               
        self.ui.textBox.setText(str(res))


app = QApplication([])
window = advanceClass()

app.exec_()