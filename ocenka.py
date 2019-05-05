import mysql.connector
import ast
from PyQt5 import QtCore, QtGui, QtWidgets
def MyConvertor(mydata):
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)
    return tuple(map(cvt,mydata))
class Ui_MainWindow(object):
    def menu(self):
        os.system("python main.py")
    def LoadData(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="oop"
        )
        cursor = con.cursor()
        cursor.execute("SELECT `ocenka` FROM `ocenka` WHERE 1")
        data=cursor.fetchall()
        for row in data:
            self.AddTable(MyConvertor(row))
        cursor.close()
    def AddTable(self,columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition,i,QtWidgets.QTableWidgetItem(str(column)))
    def InsertData(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="oop"
        )
        ocenka = self.lineEdit_2.text()
        cursor = con.cursor()
        cursor.execute("INSERT INTO ocenka(ocenka)"
                            "VALUES('%s')" % (''.join(ocenka),
                                                  ))
        con.commit()
        #self.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 130, 161, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 260, 501, 251))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.InsertData)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 210, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.LoadData)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 80, 151, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.menu)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Оценка"))
        self.pushButton.setText(_translate("MainWindow", "Внести в базу"))
        self.pushButton_2.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_3.setText(_translate("MainWindow", "Вернутся в меню"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

