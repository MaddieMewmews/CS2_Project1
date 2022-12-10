from PyQt6 import *
from view import *

class Controller(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__tiprate = 1.10
        self.__foodamt = 0.00
        self.__drinkamt = 0.00
        self.__dessertamt = 0.00
        self.setupUi(self)
        self.pushButton_2.clicked.connect(lambda: self.submit())
        self.pushButton.clicked.connect(lambda: self.clear())
        self.radioButton.clicked.connect(lambda: self.ten())
        self.radioButton_2.clicked.connect(lambda: self.fifteen())
        self.radioButton_3.clicked.connect(lambda: self.twenty())
        self.doubleSpinBox.valueChanged.connect(lambda: self.food())
        self.doubleSpinBox_2.valueChanged.connect(lambda: self.drink())
        self.doubleSpinBox_3.valueChanged.connect(lambda: self.dessert())


    def submit(self):
        subtotal=self.__foodamt+self.__drinkamt+self.__dessertamt
        subtaxed=subtotal*1.10
        taxamt=subtotal*0.10
        subtipped=subtaxed*self.__tiprate
        tipamt= subtaxed*(self.__tiprate-1)
        result=(f"SUMMARY\n\nFood:  ${self.__foodamt:.2f}\nDrink:   ${self.__drinkamt:.2f}\nDessert:    ${self.__dessertamt:.2f}\nTax:  ${taxamt:.2f}\nTip:  ${tipamt:.2f}\n\nTOTAL:    ${subtipped:.2f}")
        self.textEdit.setText(result)

    def clear(self):
        self.__tiprate = 1.10
        self.__foodamt = 0.0
        self.__drinkamt = 0.0
        self.__dessertamt = 0.0
        self.doubleSpinBox.setValue(0.00)
        self.doubleSpinBox_2.setValue(0.00)
        self.doubleSpinBox_3.setValue(0.00)
        self.radioButton.setChecked(True)
        self.textEdit.clear()

    def ten(self):
        self.__tiprate = 1.10
    def fifteen(self):
        self.__tiprate = 1.15
    def twenty(self):
        self.__tiprate = 1.20
    def food(self):
        self.__foodamt = self.doubleSpinBox.value()
    def drink(self):
        self.__drinkamt = self.doubleSpinBox_2.value()
    def dessert(self):
        self.__dessertamt = self.doubleSpinBox_3.value()
