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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(875, 685)
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
        self.horizontalLayout_16 = QHBoxLayout(self.frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
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


        self.horizontalLayout_16.addWidget(self.widget_3)

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


        self.horizontalLayout_16.addWidget(self.widget_4)


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
        self.matWidget = QWidget(self.widget_5)
        self.matWidget.setObjectName(u"matWidget")
        self.verticalLayout_3 = QVBoxLayout(self.matWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_7 = QWidget(self.matWidget)
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

        self.matrix_table = QTableWidget(self.matWidget)
        self.matrix_table.setObjectName(u"matrix_table")

        self.verticalLayout_3.addWidget(self.matrix_table)


        self.horizontalLayout_6.addWidget(self.matWidget)

        self.graphicviewWidget = QWidget(self.widget_5)
        self.graphicviewWidget.setObjectName(u"graphicviewWidget")
        self.graphicviewWidget.setMinimumSize(QSize(300, 0))
        self.verticalLayout_17 = QVBoxLayout(self.graphicviewWidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.dockWidget_2 = QDockWidget(self.graphicviewWidget)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.horizontalLayout_25 = QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.webEngineView = QWebEngineView(self.dockWidgetContents_2)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_25.addWidget(self.webEngineView)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)

        self.verticalLayout_17.addWidget(self.dockWidget_2)

        self.dockWidget = QDockWidget(self.graphicviewWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout_26 = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.webEngineView_2 = QWebEngineView(self.dockWidgetContents)
        self.webEngineView_2.setObjectName(u"webEngineView_2")
        self.webEngineView_2.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_26.addWidget(self.webEngineView_2)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.verticalLayout_17.addWidget(self.dockWidget)


        self.horizontalLayout_6.addWidget(self.graphicviewWidget)

        self.tabWidget = QTabWidget(self.widget_5)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tabWidget_3 = QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
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
        self.horizontalLayout_17 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.widget_18 = QWidget(self.tab_3)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_2 = QVBoxLayout(self.widget_18)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_13 = QLabel(self.widget_18)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_5 = QLabel(self.widget_18)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.ahpMat = QTableWidget(self.widget_18)
        self.ahpMat.setObjectName(u"ahpMat")

        self.verticalLayout_2.addWidget(self.ahpMat)

        self.btnCheckAHP = QPushButton(self.widget_18)
        self.btnCheckAHP.setObjectName(u"btnCheckAHP")

        self.verticalLayout_2.addWidget(self.btnCheckAHP)

        self.ahpCheckLabel = QLabel(self.widget_18)
        self.ahpCheckLabel.setObjectName(u"ahpCheckLabel")

        self.verticalLayout_2.addWidget(self.ahpCheckLabel)

        self.ahpCalcWeightCB = QComboBox(self.widget_18)
        self.ahpCalcWeightCB.addItem("")
        self.ahpCalcWeightCB.addItem("")
        self.ahpCalcWeightCB.addItem("")
        self.ahpCalcWeightCB.setObjectName(u"ahpCalcWeightCB")

        self.verticalLayout_2.addWidget(self.ahpCalcWeightCB)

        self.btnStartAHP = QPushButton(self.widget_18)
        self.btnStartAHP.setObjectName(u"btnStartAHP")

        self.verticalLayout_2.addWidget(self.btnStartAHP)

        self.AHPweightMatTable = QTableWidget(self.widget_18)
        self.AHPweightMatTable.setObjectName(u"AHPweightMatTable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AHPweightMatTable.sizePolicy().hasHeightForWidth())
        self.AHPweightMatTable.setSizePolicy(sizePolicy)
        self.AHPweightMatTable.setMinimumSize(QSize(0, 90))
        self.AHPweightMatTable.setMaximumSize(QSize(16777215, 90))

        self.verticalLayout_2.addWidget(self.AHPweightMatTable)


        self.horizontalLayout_17.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.tab_3)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_12 = QVBoxLayout(self.widget_19)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.label_11 = QLabel(self.widget_19)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.transAHPCB = QComboBox(self.widget_19)
        self.transAHPCB.addItem("")
        self.transAHPCB.setObjectName(u"transAHPCB")

        self.verticalLayout_12.addWidget(self.transAHPCB)

        self.btnTransAHPTo = QPushButton(self.widget_19)
        self.btnTransAHPTo.setObjectName(u"btnTransAHPTo")

        self.verticalLayout_12.addWidget(self.btnTransAHPTo)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)


        self.horizontalLayout_17.addWidget(self.widget_19)

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

        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.topsisWeightMat = QTableWidget(self.widget_8)
        self.topsisWeightMat.setObjectName(u"topsisWeightMat")

        self.verticalLayout_4.addWidget(self.topsisWeightMat)

        self.label_10 = QLabel(self.widget_8)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.topsisMatrix = QTableWidget(self.widget_8)
        self.topsisMatrix.setObjectName(u"topsisMatrix")

        self.verticalLayout_4.addWidget(self.topsisMatrix)

        self.btnTopsisWork = QPushButton(self.widget_8)
        self.btnTopsisWork.setObjectName(u"btnTopsisWork")

        self.verticalLayout_4.addWidget(self.btnTopsisWork)

        self.btnTopsisOutput = QPushButton(self.widget_8)
        self.btnTopsisOutput.setObjectName(u"btnTopsisOutput")

        self.verticalLayout_4.addWidget(self.btnTopsisOutput)


        self.horizontalLayout_8.addWidget(self.widget_8)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_15 = QWidget(self.tab_5)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_7 = QVBoxLayout(self.widget_15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ewMat = QTableWidget(self.widget_15)
        self.ewMat.setObjectName(u"ewMat")

        self.verticalLayout_7.addWidget(self.ewMat)

        self.btnEntropyWeight = QPushButton(self.widget_15)
        self.btnEntropyWeight.setObjectName(u"btnEntropyWeight")

        self.verticalLayout_7.addWidget(self.btnEntropyWeight)


        self.horizontalLayout_14.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.tab_5)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(100, 0))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_11 = QVBoxLayout(self.widget_17)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.label_8 = QLabel(self.widget_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_11.addWidget(self.label_8)

        self.ewToCB = QComboBox(self.widget_17)
        self.ewToCB.addItem("")
        self.ewToCB.setObjectName(u"ewToCB")

        self.verticalLayout_11.addWidget(self.ewToCB)

        self.btnTransEWBtn = QPushButton(self.widget_17)
        self.btnTransEWBtn.setObjectName(u"btnTransEWBtn")

        self.verticalLayout_11.addWidget(self.btnTransEWBtn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.horizontalLayout_15.addWidget(self.widget_17)


        self.horizontalLayout_14.addWidget(self.widget_16)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.horizontalLayout_2.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_9)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tabWidget_4 = QTabWidget(self.tab_9)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_13 = QVBoxLayout(self.tab_10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.groupBox = QGroupBox(self.tab_10)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lptype_max = QRadioButton(self.groupBox)
        self.lptype_max.setObjectName(u"lptype_max")

        self.horizontalLayout_19.addWidget(self.lptype_max)

        self.lptype_min = QRadioButton(self.groupBox)
        self.lptype_min.setObjectName(u"lptype_min")

        self.horizontalLayout_19.addWidget(self.lptype_min)


        self.verticalLayout_13.addWidget(self.groupBox)

        self.widget_20 = QWidget(self.tab_10)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.widget_6 = QWidget(self.widget_20)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.btnLPPreload = QPushButton(self.widget_6)
        self.btnLPPreload.setObjectName(u"btnLPPreload")

        self.verticalLayout_14.addWidget(self.btnLPPreload)

        self.label_14 = QLabel(self.widget_6)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_14.addWidget(self.label_14)

        self.boundsMat = QTableWidget(self.widget_6)
        self.boundsMat.setObjectName(u"boundsMat")

        self.verticalLayout_14.addWidget(self.boundsMat)

        self.btnLP = QPushButton(self.widget_6)
        self.btnLP.setObjectName(u"btnLP")

        self.verticalLayout_14.addWidget(self.btnLP)


        self.horizontalLayout_20.addWidget(self.widget_6)

        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_15 = QVBoxLayout(self.widget_21)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_15 = QLabel(self.widget_21)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_15.addWidget(self.label_15)

        self.lpResMat = QTableWidget(self.widget_21)
        self.lpResMat.setObjectName(u"lpResMat")

        self.verticalLayout_15.addWidget(self.lpResMat)

        self.label_17 = QLabel(self.widget_21)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_15.addWidget(self.label_17)

        self.lpvaLabel = QLabel(self.widget_21)
        self.lpvaLabel.setObjectName(u"lpvaLabel")

        self.verticalLayout_15.addWidget(self.lpvaLabel)


        self.horizontalLayout_20.addWidget(self.widget_21)


        self.verticalLayout_13.addWidget(self.widget_20)

        self.tabWidget_4.addTab(self.tab_10, "")

        self.horizontalLayout_18.addWidget(self.tabWidget_4)

        self.tabWidget.addTab(self.tab_9, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_22 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.regressionTabs = QTabWidget(self.tab_6)
        self.regressionTabs.setObjectName(u"regressionTabs")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.horizontalLayout_24 = QHBoxLayout(self.tab_11)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.widget_22 = QWidget(self.tab_11)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_16 = QVBoxLayout(self.widget_22)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_19 = QLabel(self.widget_22)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_16.addWidget(self.label_19)

        self.SVLRcb = QComboBox(self.widget_22)
        self.SVLRcb.addItem("")
        self.SVLRcb.addItem("")
        self.SVLRcb.addItem("")
        self.SVLRcb.setObjectName(u"SVLRcb")

        self.verticalLayout_16.addWidget(self.SVLRcb)

        self.widget_28 = QWidget(self.widget_22)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.SVLRiternum = QLineEdit(self.widget_28)
        self.SVLRiternum.setObjectName(u"SVLRiternum")

        self.horizontalLayout_28.addWidget(self.SVLRiternum)

        self.SVLRalpha = QLineEdit(self.widget_28)
        self.SVLRalpha.setObjectName(u"SVLRalpha")

        self.horizontalLayout_28.addWidget(self.SVLRalpha)


        self.verticalLayout_16.addWidget(self.widget_28)

        self.btnStartSVLR = QPushButton(self.widget_22)
        self.btnStartSVLR.setObjectName(u"btnStartSVLR")

        self.verticalLayout_16.addWidget(self.btnStartSVLR)

        self.SVLRansLabel = QLabel(self.widget_22)
        self.SVLRansLabel.setObjectName(u"SVLRansLabel")

        self.verticalLayout_16.addWidget(self.SVLRansLabel)

        self.label_21 = QLabel(self.widget_22)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_16.addWidget(self.label_21)

        self.SVLRPredTable = QTableWidget(self.widget_22)
        self.SVLRPredTable.setObjectName(u"SVLRPredTable")

        self.verticalLayout_16.addWidget(self.SVLRPredTable)

        self.btnStartSVLRPred = QPushButton(self.widget_22)
        self.btnStartSVLRPred.setObjectName(u"btnStartSVLRPred")

        self.verticalLayout_16.addWidget(self.btnStartSVLRPred)


        self.horizontalLayout_24.addWidget(self.widget_22)

        self.regressionTabs.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.verticalLayout_20 = QVBoxLayout(self.tab_12)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_25 = QWidget(self.tab_12)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_18 = QVBoxLayout(self.widget_25)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.MVLRiternum = QLineEdit(self.widget_27)
        self.MVLRiternum.setObjectName(u"MVLRiternum")

        self.horizontalLayout_27.addWidget(self.MVLRiternum)

        self.MVLRalpha = QLineEdit(self.widget_27)
        self.MVLRalpha.setObjectName(u"MVLRalpha")

        self.horizontalLayout_27.addWidget(self.MVLRalpha)


        self.verticalLayout_18.addWidget(self.widget_27)

        self.widget_23 = QWidget(self.widget_25)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_16 = QLabel(self.widget_23)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_21.addWidget(self.label_16)

        self.btnMVLRTrain = QPushButton(self.widget_23)
        self.btnMVLRTrain.setObjectName(u"btnMVLRTrain")

        self.horizontalLayout_21.addWidget(self.btnMVLRTrain)


        self.verticalLayout_18.addWidget(self.widget_23)

        self.MVLRtrainmat = QTableWidget(self.widget_25)
        self.MVLRtrainmat.setObjectName(u"MVLRtrainmat")

        self.verticalLayout_18.addWidget(self.MVLRtrainmat)


        self.verticalLayout_20.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.tab_12)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_19 = QVBoxLayout(self.widget_26)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_24 = QWidget(self.widget_26)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_18 = QLabel(self.widget_24)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_23.addWidget(self.label_18)

        self.btnMVLRPred = QPushButton(self.widget_24)
        self.btnMVLRPred.setObjectName(u"btnMVLRPred")

        self.horizontalLayout_23.addWidget(self.btnMVLRPred)


        self.verticalLayout_19.addWidget(self.widget_24)

        self.MVLRPredictResultTable = QTableWidget(self.widget_26)
        self.MVLRPredictResultTable.setObjectName(u"MVLRPredictResultTable")

        self.verticalLayout_19.addWidget(self.MVLRPredictResultTable)


        self.verticalLayout_20.addWidget(self.widget_26)

        self.regressionTabs.addTab(self.tab_12, "")

        self.horizontalLayout_22.addWidget(self.regressionTabs)

        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.widget_5)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(0)
        self.regressionTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"FIlename:", None))
        self.filenamelabel.setText(QCoreApplication.translate("Form", u"\u672a\u5bfc\u5165", None))
        self.label.setText(QCoreApplication.translate("Form", u"size:", None))
        self.sizelabel.setText("")
        self.btn_getFile.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165", None))
        self.btn_output.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
        self.begin_index.setPlaceholderText(QCoreApplication.translate("Form", u"from", None))
        self.end_index.setPlaceholderText(QCoreApplication.translate("Form", u"to", None))
        self.btn_filter.setText(QCoreApplication.translate("Form", u"\u8fc7\u6ee4", None))
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
        self.label_13.setText(QCoreApplication.translate("Form", u"\u652f\u6301n\u5c0f\u4e8e\u7b49\u4e8e15", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6743\u91cd\u77e9\u9635", None))
        self.btnCheckAHP.setText(QCoreApplication.translate("Form", u"Check", None))
        self.ahpCheckLabel.setText("")
        self.ahpCalcWeightCB.setItemText(0, QCoreApplication.translate("Form", u"\u7b97\u672f\u5e73\u5747\u6cd5", None))
        self.ahpCalcWeightCB.setItemText(1, QCoreApplication.translate("Form", u"\u51e0\u4f55\u5e73\u5747\u6cd5", None))
        self.ahpCalcWeightCB.setItemText(2, QCoreApplication.translate("Form", u"\u7279\u5f81\u503c\u6cd5", None))

        self.btnStartAHP.setText(QCoreApplication.translate("Form", u"start", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Trans to", None))
        self.transAHPCB.setItemText(0, QCoreApplication.translate("Form", u"Topsis", None))

        self.btnTransAHPTo.setText(QCoreApplication.translate("Form", u"Trans", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("Form", u"AHP", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5728\u4f7f\u7528\u524d\u8bf7\u4fdd\u8bc1\u5df2\u6b63\u5411\u5316\u548c\u6807\u51c6\u5316*", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u6743\u91cd\u5206\u914d", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u5f97\u5206", None))
        self.btnTopsisWork.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.btnTopsisOutput.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Topsis", None))
        self.btnEntropyWeight.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Trans to", None))
        self.ewToCB.setItemText(0, QCoreApplication.translate("Form", u"Topsis", None))

        self.btnTransEWBtn.setText(QCoreApplication.translate("Form", u"Trans", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u71b5\u6743", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u8bc4\u4ef7\u6a21\u578b", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u76ee\u6807", None))
        self.lptype_max.setText(QCoreApplication.translate("Form", u"Max", None))
        self.lptype_min.setText(QCoreApplication.translate("Form", u"Min", None))
        self.btnLPPreload.setText(QCoreApplication.translate("Form", u"preload", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Bounds\uff08\u9ed8\u8ba4[-inf,inf]\uff09", None))
        self.btnLP.setText(QCoreApplication.translate("Form", u"Start", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u89e3\u5411\u91cf", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u503c", None))
        self.lpvaLabel.setText("")
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), QCoreApplication.translate("Form", u"\u7ebf\u6027\u89c4\u5212", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("Form", u"\u8fd0\u7b79\u4f18\u5316", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3", None))
        self.SVLRcb.setItemText(0, QCoreApplication.translate("Form", u"\u6700\u5c0f\u4e8c\u4e58\u6cd5\uff08\u95ed\u5f0f\u89e3\uff09", None))
        self.SVLRcb.setItemText(1, QCoreApplication.translate("Form", u"SKlearn OLS", None))
        self.SVLRcb.setItemText(2, QCoreApplication.translate("Form", u"GD\uff08\u5c40\u90e8\u6700\u4f18\uff09", None))

        self.SVLRiternum.setPlaceholderText(QCoreApplication.translate("Form", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.SVLRalpha.setPlaceholderText(QCoreApplication.translate("Form", u"\u5b66\u4e60\u7387", None))
        self.btnStartSVLR.setText(QCoreApplication.translate("Form", u"start", None))
        self.SVLRansLabel.setText("")
        self.label_21.setText(QCoreApplication.translate("Form", u"\u9884\u6d4b", None))
        self.btnStartSVLRPred.setText(QCoreApplication.translate("Form", u"start", None))
        self.regressionTabs.setTabText(self.regressionTabs.indexOf(self.tab_11), QCoreApplication.translate("Form", u"\u4e00\u5143\u7ebf\u6027\u56de\u5f52", None))
        self.MVLRiternum.setPlaceholderText(QCoreApplication.translate("Form", u"\u8fed\u4ee3\u6b21\u6570", None))
        self.MVLRalpha.setPlaceholderText(QCoreApplication.translate("Form", u"\u5b66\u4e60\u7387", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u8bad\u7ec3", None))
        self.btnMVLRTrain.setText(QCoreApplication.translate("Form", u"Train", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u9884\u6d4b", None))
        self.btnMVLRPred.setText(QCoreApplication.translate("Form", u"Predict", None))
        self.regressionTabs.setTabText(self.regressionTabs.indexOf(self.tab_12), QCoreApplication.translate("Form", u"\u591a\u5143\u7ebf\u6027\u56de\u5f52", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u56de\u5f52\u5206\u6790", None))
    # retranslateUi

