import os
import sys

from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QTableWidgetItem, QHeaderView
from qt_material import apply_stylesheet

from Functions.EvaluateModels.EntropyWeight import entropyWeight
from Functions.EvaluateModels.Topsis import topsis
from Functions.Preworks.Normalization import normalization
from Functions.utils.OutputXlsx import outputXlsx
from MMH import Ui_Form
import pandas as pd
from Functions.Preworks.PositiveTransformation import *


class Frame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.topsisMat = None
        self.fileName = None
        self.setupUi(self)
        self.setWindowTitle("Mathematical Modelling Helper a1.0.0")
        self.setStyleSheet("background-color:white")
        self.showMaximized()
        self.df = pd.DataFrame()
        self.mat = None
        self.W = None
        self.EW = None

        self.matrix_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.topsisWeightMat.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.topsisMatrix.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ewMat.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.bind()

    def bind(self):
        self.btn_getFile.clicked.connect(lambda: self.open_file_dialog())
        self.btn_filter.clicked.connect(lambda: self.showTable())
        self.btnMinMetric.clicked.connect(lambda: self.calcMin())
        self.btnBS.clicked.connect(lambda: self.calcBS())
        self.btnInterval.clicked.connect(lambda: self.calcInterval())
        self.btn_output.clicked.connect(lambda: self.outputXlsx(self.mat))
        self.btnStartNorm.clicked.connect(lambda: self.startNormalization())
        self.btnTopsisWork.clicked.connect(lambda: self.startTopsis())
        self.btnTopsisOutput.clicked.connect(lambda: self.outputXlsx(self.topsisMat))
        self.btnEntropyWeight.clicked.connect(lambda: self.startEW())
        self.btnTransEWBtn.clicked.connect(lambda: self.transWMatrixTo())

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Excel Files (*.xlsx)"
        )
        self.fileName = os.path.basename(file_name)
        if file_name:
            self.filenamelabel.setText(f"{self.fileName}")
            self.prework(file_name)

    def prework(self, filename):
        (_, extension) = os.path.splitext(filename)
        self.df = pd.read_excel(filename)
        self.mat = self.df.to_numpy()
        self.sizelabel.setText(f"{self.mat.shape[0], self.mat.shape[1] - 1}")
        self.topsisWeightMat.setRowCount(1)
        self.topsisWeightMat.setColumnCount(self.mat.shape[1] - 1)
        self.W = [1 for _ in range(self.mat.shape[1])]
        self.showTable()
        self.showTopsisWeightTable()

    def showTable(self):
        begin = self.begin_index.text()
        end = self.end_index.text()
        if begin == '':
            begin = 0
        else:
            begin = int(begin) - 1
        if end == '':
            end = len(self.mat)
        else:
            end = int(end)
        self.matrix_table.setRowCount(min(end - begin, 300))
        self.matrix_table.setColumnCount(min(len(self.mat[0]) - 1, 300))
        for i in range(begin, end):
            for j in range(1, len(self.mat[i])):
                self.matrix_table.setItem(i - begin, j - 1, QTableWidgetItem(str(self.mat[i][j])))

    def calcMin(self):
        cols = list(map(int, self.minMetricCols.text().split(',')))
        minMetrice(self.mat, cols)
        self.showTable()
        print(cols)

    def calcBS(self):
        cols = list(map(int, self.bestScoreCols.text().split(',')))
        print(cols)
        bs = int(self.bestScore.text())
        print(bs)
        bestScoreMatrices(self.mat, cols, bs)
        self.showTable()

    def calcInterval(self):
        cols = list(map(int, self.intervalCols.text().split(',')))
        print(cols)
        l = int(self.intervalBeginPoint.text())
        r = int(self.intervalEndPoint.text())
        intervalMetrice(self.mat, cols, l, r)
        self.showTable()
        pass

    def outputXlsx(self, mat):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            f"{self.fileName}",
            "Excel Files (*.xlsx)"
        )
        outputXlsx(file_path, mat)

    def startNormalization(self):
        mtype = 0
        flag = True
        for i in range(self.mat.shape[0]):
            for j in range(1, self.mat.shape[1]):
                if self.mat[i][j] < 0:
                    mtype = 1
                    flag = False
                    break
            if not flag:
                break
        normalization(self.mat, mtype)
        self.showTable()

    def startTopsis(self):
        self.topsisMat = topsis(self.mat,self.W)
        self.topsisMatrix.setRowCount(min(len(self.topsisMat), 100))
        self.topsisMatrix.setColumnCount(1)
        for i in range(len(self.topsisMat)):
            self.topsisMatrix.setItem(i, 0, QTableWidgetItem(str(self.topsisMat[i])))

    def startEW(self):
        self.EW = entropyWeight(self.mat)
        self.ewMat.setRowCount(1)
        self.ewMat.setColumnCount(min(len(self.EW) - 1, 100))
        for i in range(len(self.EW)):
            self.ewMat.setItem(0, i - 1, QTableWidgetItem(str(self.EW[i])))

    def transWMatrixTo(self):
        selected_text = self.ewToCB.currentText()
        if selected_text == 'Topsis':
            self.W = self.EW
            self.showTopsisWeightTable()

    def showTopsisWeightTable(self):
        for i in range(1, len(self.W)):
            self.topsisWeightMat.setItem(0, i - 1, QTableWidgetItem(str(self.W[i])))


def run():
    app = QApplication([])
    apply_stylesheet(app, theme='light_blue.xml')
    window = Frame()
    window.show()
    sys.exit(app.exec_())
