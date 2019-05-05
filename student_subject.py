from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox
import mysql.connector
import ast
import sys
ids =''
idd =''
ido=''
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
        cursor.execute("SELECT `student_id`, `subject_id`, `ocenka_id` FROM `subject_student` WHERE 1")
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
        global ids
        global idd
        global ido
       # fio = self.lineEdit.text()
        #date = self.lineEdit_2.text()
        #kaf = self.lineEdit_3.text()
        cursor = con.cursor()
        cursor.execute("INSERT INTO subject_student(student_id,subject_id,ocenka_id)"
                            "VALUES('%s','%s','%s')" % (''.join(ids),
                                                        ''.join(idd),
                                                        ''.join(ido),
                                                        ))
        con.commit()
        #self.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combo = QComboBox(self.centralwidget)
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="oop"
        )
        cursor = con.cursor()
        cursor.execute("SELECT `student_name` FROM `student` WHERE 1")
        result = cursor.fetchall()
        for row in result:
            self.combo.addItems(row)
            con.commit()
        self.combo.activated[str].connect(self.onActivatedStudent)
        self.combo.setGeometry(QtCore.QRect(60, 100, 161, 21))
        self.combo1 = QComboBox(self.centralwidget)
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="oop"
        )
        cursor = con.cursor()
        cursor.execute("SELECT `subject_name` FROM `subject` WHERE 1")
        result = cursor.fetchall()
        for row in result:
            self.combo1.addItems(row)
            con.commit()
        self.combo1.activated[str].connect(self.onActivatedStudentSubject)
        self.combo1.setGeometry(QtCore.QRect(60, 130, 161, 21))
        self.combo2 = QComboBox(self.centralwidget)
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="oop"
        )
        cursor = con.cursor()
        cursor.execute("SELECT `ocenka` FROM `ocenka` WHERE 1")
        result = cursor.fetchall()
        for row in result:
            self.combo2.addItems(row)
            con.commit()
        self.combo2.activated[str].connect(self.onActivatedStudentOcenka)
        self.combo2.setGeometry(QtCore.QRect(60, 160, 161, 21))
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 260, 501, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["Номер студента", "Номер дицсиплины", "Номер оценки"])
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
    def onActivatedStudent(self, text):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="oop"
        )
        cursor = con.cursor()
        cursor.execute("select `student_id` from `student` where `student_name`='%s'"%text)
        result = cursor.fetchall()
        newrez= ','.join(map(str,result))
        rez = newrez.replace(",","")
        rez1 = rez.replace(")", "")
        rez2= rez1.replace("(", "")
        global ids
        ids = rez2
        #print(rez2)
        con.close()
    def onActivatedStudentSubject(self, text):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="oop"
        )
        cursor = con.cursor()
        cursor.execute("select `subject_id` from `subject` where `subject_name`='%s'"%text)
        result = cursor.fetchall()
        newrez= ','.join(map(str,result))
        rez = newrez.replace(",","")
        rez1 = rez.replace(")", "")
        rez2= rez1.replace("(", "")
        global idd
        idd = rez2
        #print(rez2)
        con.close()
    def onActivatedStudentOcenka(self, text):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="oop"
        )
        cursor = con.cursor()
        cursor.execute("select `ocenka_id` from `ocenka` where `ocenka`='%s'"%text)
        result = cursor.fetchall()
        newrez= ','.join(map(str,result))
        rez = newrez.replace(",","")
        rez1 = rez.replace(")", "")
        rez2= rez1.replace("(", "")
        global ido
        ido = rez2
        #print(rez2)
        con.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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

