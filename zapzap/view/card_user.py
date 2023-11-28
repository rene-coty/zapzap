from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/card_user.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CardUser(object):
    def setupUi(self, CardUser):
        CardUser.setObjectName("CardUser")
        CardUser.resize(320, 84)
        CardUser.setMinimumSize(QtCore.QSize(320, 0))
        CardUser.setStyleSheet("")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(CardUser)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(parent=CardUser)
        self.frame.setMinimumSize(QtCore.QSize(320, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.icon = QtWidgets.QLabel(parent=self.frame)
        self.icon.setMinimumSize(QtCore.QSize(32, 32))
        self.icon.setMaximumSize(QtCore.QSize(32, 32))
        self.icon.setText("")
        self.icon.setScaledContents(True)
        self.icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 0, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(parent=self.frame)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.btnDisable = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDisable.sizePolicy().hasHeightForWidth())
        self.btnDisable.setSizePolicy(sizePolicy)
        self.btnDisable.setMinimumSize(QtCore.QSize(30, 30))
        self.btnDisable.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btnDisable.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnDisable.setText("")
        self.btnDisable.setObjectName("btnDisable")
        self.gridLayout.addWidget(self.btnDisable, 0, 2, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDelete.sizePolicy().hasHeightForWidth())
        self.btnDelete.setSizePolicy(sizePolicy)
        self.btnDelete.setMinimumSize(QtCore.QSize(30, 30))
        self.btnDelete.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnDelete.setText("")
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout.addWidget(self.btnDelete, 0, 3, 1, 1)
        self.showNotifications = QtWidgets.QCheckBox(parent=self.frame)
        self.showNotifications.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.showNotifications.setChecked(True)
        self.showNotifications.setObjectName("showNotifications")
        self.gridLayout.addWidget(self.showNotifications, 1, 2, 1, 2)
        self.key = QtWidgets.QLabel(parent=self.frame)
        self.key.setText("")
        self.key.setObjectName("key")
        self.gridLayout.addWidget(self.key, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_3.addWidget(self.frame)

        self.retranslateUi(CardUser)
        QtCore.QMetaObject.connectSlotsByName(CardUser)

    def retranslateUi(self, CardUser):
        
        CardUser.setWindowTitle(_("Form"))
        self.name.setPlaceholderText(_("Enter the user name"))
        self.showNotifications.setText(_("On"))
        self.label.setText(_("Show notifications"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CardUser = QtWidgets.QWidget()
    ui = Ui_CardUser()
    ui.setupUi(CardUser)
    CardUser.show()
    sys.exit(app.exec())
