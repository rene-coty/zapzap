from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/view/ui/about_page.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(439, 505)
        About.setWindowTitle("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(About)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=About)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 439, 505))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_app = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.name_app.setFont(font)
        self.name_app.setObjectName("name_app")
        self.verticalLayout.addWidget(self.name_app)
        self.desc_app = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc_app.setFont(font)
        self.desc_app.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.desc_app.setObjectName("desc_app")
        self.verticalLayout.addWidget(self.desc_app)
        self.version_app = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.version_app.setFont(font)
        self.version_app.setObjectName("version_app")
        self.verticalLayout.addWidget(self.version_app)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.btnLeanMore = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLeanMore.sizePolicy().hasHeightForWidth())
        self.btnLeanMore.setSizePolicy(sizePolicy)
        self.btnLeanMore.setObjectName("btnLeanMore")
        self.verticalLayout_2.addWidget(self.btnLeanMore)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.btnReportIssue = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnReportIssue.sizePolicy().hasHeightForWidth())
        self.btnReportIssue.setSizePolicy(sizePolicy)
        self.btnReportIssue.setObjectName("btnReportIssue")
        self.verticalLayout_3.addWidget(self.btnReportIssue)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.label_4 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(20, 129, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        
        self.label.setText(_("About"))
        self.name_app.setText(_("ZapZap"))
        self.desc_app.setText(_("WhatsApp Web for Linux"))
        self.version_app.setText(_("Version {id} (Official compilation)"))
        self.label_2.setText(_("Lean more"))
        self.label_3.setText(_("See more about Zapzap on our website."))
        self.btnLeanMore.setText(_("Lean more"))
        self.label_5.setText(_("Report issue"))
        self.label_6.setText(_("Report a problem or make your suggestion."))
        self.btnReportIssue.setText(_("Report issue"))
        self.label_4.setText(_("GNU General Public License v3.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QWidget()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec())
