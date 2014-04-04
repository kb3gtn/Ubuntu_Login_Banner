#!/usr/bin/env python3

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QToolTip, QDesktopWidget


class Login_popup(QDialog):
    def __init__(self):
        super(Login_popup, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Login Popup")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resize(1024, 450)
        self.setMinimumSize(QtCore.QSize(800, 400))
        self.setMaximumSize(QtCore.QSize(1400, 600))
        self.setBaseSize(QtCore.QSize(1024, 450))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.setFont(font)
        self.setSizeGripEnabled(True)
        self.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_display = QtWidgets.QTextBrowser(self)
        self.textBrowser_display.setDocumentTitle("")
        self.textBrowser_display.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser_display.setSource(QtCore.QUrl("file:///etc/login_banner.html"))
        self.textBrowser_display.setOpenLinks(False)
        self.textBrowser_display.setObjectName("textBrowser_display")
        self.verticalLayout.addWidget(self.textBrowser_display)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Decline = QtWidgets.QPushButton(self)
        self.pushButton_Decline.setMinimumSize(QtCore.QSize(128, 64))
        self.pushButton_Decline.setMaximumSize(QtCore.QSize(256, 64))
        self.pushButton_Decline.setObjectName("pushButton_Decline")
        self.horizontalLayout.addWidget(self.pushButton_Decline)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_Accept = QtWidgets.QPushButton(self)
        self.pushButton_Accept.setMinimumSize(QtCore.QSize(128, 40))
        self.pushButton_Accept.setMaximumSize(QtCore.QSize(256, 64))
        self.pushButton_Accept.setObjectName("pushButton_Accept")
        self.horizontalLayout.addWidget(self.pushButton_Accept)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Set default result to decline.. catch (X) being pressed on window.
        self.setResult(0)

        self.retranslateUi()
        self.pushButton_Accept.clicked.connect(self.Accept)
        self.pushButton_Decline.clicked.connect(self.Decline)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.pushButton_Accept, self.pushButton_Decline)
        self.setTabOrder(self.pushButton_Decline, self.textBrowser_display)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Login Popup"))
        self.textBrowser_display.setPlaceholderText(_translate("self", "Login Message here..."))
        self.pushButton_Decline.setText(_translate("self", "DECLINE"))
        self.pushButton_Accept.setText(_translate("self", "ACCEPT"))


    def Accept(self):
        self.close()
        QtCore.QCoreApplication.exit(0)

    def Decline(self):
        self.close()
        QtCore.QCoreApplication.exit(-1)

def main():

    app = QApplication( sys.argv )
    w = Login_popup()
    
    # center widget on screen
    sg = QDesktopWidget().screenGeometry();
    w.move( (sg.width() / 2) - ( w.width()/2) , (sg.height() / 2) - (w.height()/2))

    w.show()
    sys.exit( app.exec_())

if __name__ == '__main__':
    main()

