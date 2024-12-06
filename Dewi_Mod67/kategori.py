from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_Kategori(object):
    def setupUi(self, Kategori):
        # Set properties for main window
        Kategori.setObjectName("Kategori")
        Kategori.resize(478, 249)

        # Horizontal layout widget
        self.horizontalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 441, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        # Horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Push Button (Insert)
        self.pushButtonInsert = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonInsert.clicked.connect(self.insertkategori)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonInsert.setFont(font)
        self.pushButtonInsert.setObjectName("pushButtonInsert")
        self.horizontalLayout.addWidget(self.pushButtonInsert)

        # Vertical layout widget
        self.verticalLayoutWidget = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 10, 281, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        # Vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Line Edit
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        # Line Edit (ID)
        self.lineEditId = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditId.setFont(font)
        self.lineEditId.setObjectName("lineEditId")
        self.verticalLayout.addWidget(self.lineEditId)

        # Line Edit (Name)
        self.lineEditName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.verticalLayout.addWidget(self.lineEditName)

        # Vertical Layout Widget 2
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Kategori)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 151, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")

        # Vertical Layout 2
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Label (ID)
        self.labelId = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelId.setFont(font)
        self.labelId.setObjectName("labelId")
        self.verticalLayout_2.addWidget(self.labelId)

        # Label (Name)
        self.labelName = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.verticalLayout_2.addWidget(self.labelName)

        # Label Result
        self.labelResult = QtWidgets.QLabel(Kategori)
        self.labelResult.setGeometry(QtCore.QRect(10, 220, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)  # Bold font
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")

        # Connect pushButtonInsert to the insertkategori method
        self.pushButtonInsert.clicked.connect(self.insertkategori)

        # Retranslate UI
        self.retranslateUi(Kategori)
        QtCore.QMetaObject.connectSlotsByName(Kategori)

    def insertkategori(self):
        try:
            # Connect to MySQL database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_penjualan"
            )
            cursor = mydb.cursor()

            # Get values from input fields
            idkat = self.lineEditId.text()
            namakat = self.lineEditName.text()

            # Prepare and execute SQL query
            sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
            val = (idkat, namakat)
            cursor.execute(sql, val)
            mydb.commit()

            # Update result label
            self.labelResult.setText("Data Kategori Berhasil Disimpan")

            # Clear input fields
            self.lineEditId.setText("")
            self.lineEditName.setText("")
        except mc.Error as e:
            # Handle error and update result label
            self.labelResult.setText("Data Kategori Gagal Disimpan")

    def retranslateUi(self, Kategori):
        _translate = QtCore.QCoreApplication.translate
        Kategori.setWindowTitle(_translate("Kategori", "Form Kategori"))
        self.pushButtonInsert.setText(_translate("Kategori", "INSERT DATA"))
        self.labelId.setText(_translate("Kategori", "ID Kategori"))
        self.labelName.setText(_translate("Kategori", "Nama Kategori"))
        self.labelResult.setText(_translate("Kategori", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kategori = QtWidgets.QWidget()
    ui = Ui_Kategori()
    ui.setupUi(Kategori)
    Kategori.show()
    sys.exit(app.exec_())