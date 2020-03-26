#UI Packages
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys

#SNAP Interfacing
import extractor
import matplotlib.pyplot as plt
 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(381, 239)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(80, 10, 191, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Xtract = QtWidgets.QLabel(self.frame)
        self.Xtract.setGeometry(QtCore.QRect(60, 5, 81, 21))
        self.Xtract.setObjectName("Xtract")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 60, 271, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileSelect = QtWidgets.QLabel(self.layoutWidget)
        self.fileSelect.setObjectName("fileSelect")
        self.horizontalLayout.addWidget(self.fileSelect)
        self.selectButton = QtWidgets.QPushButton(self.layoutWidget)
        self.selectButton.setObjectName("selectButton")
        self.horizontalLayout.addWidget(self.selectButton)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 120, 271, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileSelected = QtWidgets.QLabel(self.layoutWidget1)
        self.fileSelected.setObjectName("fileSelected")
        self.horizontalLayout_2.addWidget(self.fileSelected)
        self.fileName = QtWidgets.QLabel(self.layoutWidget1)
        self.fileName.setText("")
        self.fileName.setObjectName("fileName")
        self.horizontalLayout_2.addWidget(self.fileName)
        self.status = QtWidgets.QLabel(Dialog)
        self.status.setGeometry(QtCore.QRect(170, 160, 51, 20))
        self.status.setText("")
        self.status.setObjectName("status")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(200, 190, 158, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        self.selectButton.clicked.connect(self.browseFile)
        self.pushButton.clicked.connect(self.runAlgo)
        self.pushButton_2.clicked.connect(self.exitApp)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def browseFile(self):
        fname = QFileDialog.getOpenFileName(None, 'Open file', "./","SAFE files (*.safe)")

        if fname[0]:
            self.fileName.setText(fname[0])   

    def runAlgo(self):
        self.status.setText("Processing")
        fName = self.fileName.text()
        stat , img = extractor.tiffCreation(fName)
        self.status.setText(stat)
        plt.imshow(img)
        plt.title("Orginal Image")
        plt.show()
        
        self.status.setText("Extracting Land area")
        stat , land = extractor.landMask(fName)
        self.status.setText(stat)
        plt.imshow(land)
        plt.title("Land area image")
        plt.show()

        self.status.setText("Extracting Sea area")
        stat , sea = extractor.seaMask(fName)
        self.status.setText(stat)
        plt.imshow(sea)
        plt.title("Sea area image")
        plt.show()

        self.status.setText("Completed")

    def exitApp(self):
        sys.exit(1)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Xtract.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Xtract</span></p></body></html>"))
        self.fileSelect.setText(_translate("Dialog", "Select a .safe file :"))
        self.selectButton.setText(_translate("Dialog", "Browse"))
        self.fileSelected.setText(_translate("Dialog", "Selected file :"))
        self.pushButton.setText(_translate("Dialog", "Run"))
        self.pushButton_2.setText(_translate("Dialog", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
