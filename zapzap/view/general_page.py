from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/general_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_General(object):
    def setupUi(self, General):
        General.setObjectName("General")
        General.resize(370, 432)
        General.setMinimumSize(QtCore.QSize(0, 0))
        General.setWindowTitle("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(General)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=General)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.general_scrollArea = QtWidgets.QWidget()
        self.general_scrollArea.setGeometry(QtCore.QRect(0, 0, 370, 432))
        self.general_scrollArea.setMinimumSize(QtCore.QSize(250, 0))
        self.general_scrollArea.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.general_scrollArea.setObjectName("general_scrollArea")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.general_scrollArea)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.general_scrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.general_scrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.general_scrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.start_system = QtWidgets.QCheckBox(parent=self.general_scrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_system.sizePolicy().hasHeightForWidth())
        self.start_system.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_system.setFont(font)
        self.start_system.setObjectName("start_system")
        self.verticalLayout.addWidget(self.start_system)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(parent=self.general_scrollArea)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(parent=self.general_scrollArea)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.keepBackground = QtWidgets.QCheckBox(parent=self.general_scrollArea)
        self.keepBackground.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.keepBackground.setChecked(True)
        self.keepBackground.setObjectName("keepBackground")
        self.gridLayout.addWidget(self.keepBackground, 0, 1, 1, 1)
        self.labelWayland = QtWidgets.QLabel(parent=self.general_scrollArea)
        self.labelWayland.setObjectName("labelWayland")
        self.gridLayout.addWidget(self.labelWayland, 1, 0, 1, 1)
        self.wayland = QtWidgets.QCheckBox(parent=self.general_scrollArea)
        self.wayland.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.wayland.setObjectName("wayland")
        self.gridLayout.addWidget(self.wayland, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.line_3 = QtWidgets.QFrame(parent=self.general_scrollArea)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.general_scrollArea)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.checkSpellChecker = QtWidgets.QCheckBox(parent=self.general_scrollArea)
        self.checkSpellChecker.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.checkSpellChecker.setChecked(True)
        self.checkSpellChecker.setObjectName("checkSpellChecker")
        self.gridLayout_2.addWidget(self.checkSpellChecker, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.comboSpellChecker = QtWidgets.QComboBox(parent=self.general_scrollArea)
        self.comboSpellChecker.setObjectName("comboSpellChecker")
        self.verticalLayout_2.addWidget(self.comboSpellChecker)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(parent=self.general_scrollArea)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnOpenSWhatsapp = QtWidgets.QPushButton(parent=self.general_scrollArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(55)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenSWhatsapp.sizePolicy().hasHeightForWidth())
        self.btnOpenSWhatsapp.setSizePolicy(sizePolicy)
        self.btnOpenSWhatsapp.setMinimumSize(QtCore.QSize(150, 0))
        self.btnOpenSWhatsapp.setObjectName("btnOpenSWhatsapp")
        self.verticalLayout_3.addWidget(self.btnOpenSWhatsapp)
        self.label_5 = QtWidgets.QLabel(parent=self.general_scrollArea)
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.scrollArea.setWidget(self.general_scrollArea)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(General)
        QtCore.QMetaObject.connectSlotsByName(General)

    def retranslateUi(self, General):
        
        self.label.setText(_("General"))
        self.label_2.setText(_("Login"))
        self.label_3.setText(_("Start ZapZap with the system"))
        self.start_system.setText(_("Off"))
        self.label_6.setText(_("Hide on close"))
        self.keepBackground.setText(_("On"))
        self.labelWayland.setText(_("Wayland window system"))
        self.wayland.setText(_("Off"))
        self.label_4.setText(_("SpellChecker"))
        self.checkSpellChecker.setText(_("On"))
        self.btnOpenSWhatsapp.setText(_("Whatsapp Web Settings"))
        self.label_5.setText(_("Open the WhatsApp Web Settings panel on the selected account."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    General = QtWidgets.QWidget()
    ui = Ui_General()
    ui.setupUi(General)
    General.show()
    sys.exit(app.exec())
