# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MMH.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1057, 685)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.filenamelabel = QLabel(self.widget_3)
        self.filenamelabel.setObjectName(u"filenamelabel")

        self.horizontalLayout_4.addWidget(self.filenamelabel)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.label)

        self.sizelabel = QLabel(self.widget_4)
        self.sizelabel.setObjectName(u"sizelabel")

        self.horizontalLayout_5.addWidget(self.sizelabel)


        self.verticalLayout_2.addWidget(self.widget_4)


        self.horizontalLayout_3.addWidget(self.frame)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(200, 16777215))
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_getFile = QPushButton(self.widget_2)
        self.btn_getFile.setObjectName(u"btn_getFile")
        self.btn_getFile.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.btn_getFile)

        self.btn_output = QPushButton(self.widget_2)
        self.btn_output.setObjectName(u"btn_output")

        self.horizontalLayout.addWidget(self.btn_output)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.widget)

        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.begin_index = QLineEdit(self.widget_7)
        self.begin_index.setObjectName(u"begin_index")

        self.horizontalLayout_7.addWidget(self.begin_index)

        self.end_index = QLineEdit(self.widget_7)
        self.end_index.setObjectName(u"end_index")

        self.horizontalLayout_7.addWidget(self.end_index)

        self.btn_filter = QPushButton(self.widget_7)
        self.btn_filter.setObjectName(u"btn_filter")

        self.horizontalLayout_7.addWidget(self.btn_filter)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.matrix_table = QTableWidget(self.widget_6)
        self.matrix_table.setObjectName(u"matrix_table")

        self.verticalLayout_3.addWidget(self.matrix_table)


        self.horizontalLayout_6.addWidget(self.widget_6)

        self.tabWidget = QTabWidget(self.widget_5)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_9 = QVBoxLayout(self.tab_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea = QScrollArea(self.tab_7)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 152, 388))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_9 = QWidget(self.scrollAreaWidgetContents)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_5 = QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.widget_9)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.minMetricCols = QLineEdit(self.widget_9)
        self.minMetricCols.setObjectName(u"minMetricCols")

        self.verticalLayout_5.addWidget(self.minMetricCols)

        self.btnMinMetric = QPushButton(self.widget_9)
        self.btnMinMetric.setObjectName(u"btnMinMetric")

        self.verticalLayout_5.addWidget(self.btnMinMetric)


        self.verticalLayout_10.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.scrollAreaWidgetContents)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_6 = QVBoxLayout(self.widget_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.intervalBeginPoint = QLineEdit(self.widget_11)
        self.intervalBeginPoint.setObjectName(u"intervalBeginPoint")

        self.horizontalLayout_10.addWidget(self.intervalBeginPoint)

        self.intervalEndPoint = QLineEdit(self.widget_11)
        self.intervalEndPoint.setObjectName(u"intervalEndPoint")

        self.horizontalLayout_10.addWidget(self.intervalEndPoint)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.intervalCols = QLineEdit(self.widget_10)
        self.intervalCols.setObjectName(u"intervalCols")

        self.verticalLayout_6.addWidget(self.intervalCols)

        self.btnInterval = QPushButton(self.widget_10)
        self.btnInterval.setObjectName(u"btnInterval")

        self.verticalLayout_6.addWidget(self.btnInterval)


        self.verticalLayout_10.addWidget(self.widget_10)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_8 = QVBoxLayout(self.widget_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_12 = QLabel(self.widget_12)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_8.addWidget(self.label_12)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.bestScore = QLineEdit(self.widget_14)
        self.bestScore.setObjectName(u"bestScore")

        self.horizontalLayout_12.addWidget(self.bestScore)


        self.verticalLayout_8.addWidget(self.widget_14)

        self.bestScoreCols = QLineEdit(self.widget_12)
        self.bestScoreCols.setObjectName(u"bestScoreCols")

        self.verticalLayout_8.addWidget(self.bestScoreCols)

        self.btnBS = QPushButton(self.widget_12)
        self.btnBS.setObjectName(u"btnBS")

        self.verticalLayout_8.addWidget(self.btnBS)


        self.verticalLayout_10.addWidget(self.widget_12)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea)

        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.horizontalLayout_13 = QHBoxLayout(self.tab_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_13 = QWidget(self.tab_8)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btnStartNorm = QPushButton(self.widget_13)
        self.btnStartNorm.setObjectName(u"btnStartNorm")
        self.btnStartNorm.setMinimumSize(QSize(0, 100))

        self.horizontalLayout_11.addWidget(self.btnStartNorm)


        self.horizontalLayout_13.addWidget(self.widget_13)

        self.tabWidget_3.addTab(self.tab_8, "")

        self.horizontalLayout_9.addWidget(self.tabWidget_3)

        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_2 = QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget_2 = QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableWidget = QTableWidget(self.tab_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(100, 50, 256, 192))
        self.label_5 = QLabel(self.tab_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 20, 54, 16))
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_8 = QWidget(self.tab_4)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.widget_8)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.btnTopsisWork = QPushButton(self.widget_8)
        self.btnTopsisWork.setObjectName(u"btnTopsisWork")

        self.verticalLayout_4.addWidget(self.btnTopsisWork)

        self.topsisMatrix = QTableWidget(self.widget_8)
        self.topsisMatrix.setObjectName(u"topsisMatrix")

        self.verticalLayout_4.addWidget(self.topsisMatrix)

        self.btnTopsisOutput = QPushButton(self.widget_8)
        self.btnTopsisOutput.setObjectName(u"btnTopsisOutput")

        self.verticalLayout_4.addWidget(self.btnTopsisOutput)


        self.horizontalLayout_8.addWidget(self.widget_8)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_2.addTab(self.tab_5, "")

        self.horizontalLayout_2.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.widget_5)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"FIlename\uff1a", None))
        self.filenamelabel.setText(QCoreApplication.translate("Form", u"\u672a\u5bfc\u5165", None))
        self.label.setText(QCoreApplication.translate("Form", u"size\uff1a", None))
        self.sizelabel.setText("")
        self.btn_getFile.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165", None))
        self.btn_output.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
        self.begin_index.setPlaceholderText(QCoreApplication.translate("Form", u"from", None))
        self.end_index.setPlaceholderText(QCoreApplication.translate("Form", u"to", None))
        self.btn_filter.setText(QCoreApplication.translate("Form", u"\u8fc7\u6ee4", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u5f52\u4e00\u5316", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6781\u5c0f\u578b\u6307\u6807", None))
        self.minMetricCols.setPlaceholderText(QCoreApplication.translate("Form", u"\u5217\u53f7\uff0c\u4ee5\u201c,\u201d\u5206\u9694", None))
        self.btnMinMetric.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u533a\u95f4\u578b\u6307\u6807", None))
        self.intervalBeginPoint.setText("")
        self.intervalBeginPoint.setPlaceholderText(QCoreApplication.translate("Form", u"\u503c\u57df\u5de6\u533a\u95f4\u7aef\u70b9", None))
        self.intervalEndPoint.setText("")
        self.intervalEndPoint.setPlaceholderText(QCoreApplication.translate("Form", u"\u503c\u57df\u53f3\u533a\u95f4\u7aef\u70b9", None))
        self.intervalCols.setPlaceholderText(QCoreApplication.translate("Form", u"\u5217\u53f7\uff0c\u4ee5\u201c,\u201d\u5206\u9694", None))
        self.btnInterval.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u4e2d\u95f4\u578b\u6307\u6807", None))
        self.bestScore.setPlaceholderText(QCoreApplication.translate("Form", u"best", None))
        self.bestScoreCols.setText("")
        self.bestScoreCols.setPlaceholderText(QCoreApplication.translate("Form", u"\u5217\u53f7\uff0c\u4ee5\u201c,\u201d\u5206\u9694", None))
        self.btnBS.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("Form", u"\u6b63\u5411\u5316", None))
        self.btnStartNorm.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("Form", u"\u6807\u51c6\u5316", None))
        self.label_4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u9884\u5904\u7406", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Form", u"AHP", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5728\u4f7f\u7528\u524d\u8bf7\u4fdd\u8bc1\u5df2\u6b63\u5411\u5316\u548c\u6807\u51c6\u5316", None))
        self.btnTopsisWork.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.btnTopsisOutput.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Topsis", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u71b5\u6743", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u8bc4\u4ef7\u6a21\u578b", None))
    # retranslateUi

