from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 271)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 131, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.formLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 70, 331, 25))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 331, 16))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 130, 331, 131))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(160, 10, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 40, 191, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def insertkategori(self):
        try:
            # Membuat koneksi ke database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan"
            )
            cursor = mydb.cursor()

            # Mendapatkan data dari input
            idkat = self.lineEditId.text()
            namekat = self.lineEditName.text()

            # Menyusun query SQL
            sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
            val = (idkat, namekat)

            # Menjalankan query dan menyimpan data
            cursor.execute(sql, val)
            mydb.commit()

            # Menampilkan pesan sukses
            self.labelResult.setText("Data Kategori Berhasil Disimpan")

            # Mengosongkan input
            self.lineEditId.setText("")
            self.lineEditName.setText("")

        except mc.Error as e:
            # Menampilkan pesan error
            self.labelResult.setText(f"Data Kategori Gagal Disimpan: {str(e)}")

    def loadkategori(self):
        try:
            # Membuat koneksi ke database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan"
            )
            mycursor = mydb.cursor()

            # Menjalankan query untuk mendapatkan data kategori
            mycursor.execute("SELECT * FROM kategori ORDER BY id ASC")
            result = mycursor.fetchall()

            # Mengosongkan tabel
            self.tableWidget.setRowCount(0)

            # Memasukkan data ke dalam tabel
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            # Menampilkan pesan sukses
            self.labelResult.setText("Data Kategori Berhasil Ditampilkan")

        except mc.Error as err:
            # Menampilkan pesan error
            self.labelResult.setText(f"Data Kategori Gagal DiLoad: {str(err)}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ID Kategori"))
        self.label_2.setText(_translate("Form", "Nama Kategori"))
        self.pushButton.setText(_translate("Form", "Insert Data"))
        self.label_3.setText(_translate("Form", "Text Label"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Kategori"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nama Kategori"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
