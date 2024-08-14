import os
import sys

import pandas as pd
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QTableWidgetItem, QHeaderView
from qt_material import apply_stylesheet

from Functions.EvaluateModels.AHP import checkAHPAvailable, arithmeticMeanMethod, geometricMeanMethod, eigenvalueMethod
from Functions.EvaluateModels.EntropyWeight import entropyWeight
from Functions.EvaluateModels.Topsis import topsis
from Functions.OperationsOptimization.LinearProgramming import linearProgramming
from Functions.Preworks.Normalization import normalization
from Functions.Preworks.PositiveTransformation import *
from Functions.Regression.MultiVarLinearRegression import gradientDescent
from Functions.Regression.SingleVarLinearRegression import singleVarLinearRegressionOLS, singleVarLinearRegressionSKL
from Functions.utils.DrawPlot import Figure
from Functions.utils.OutputXlsx import outputXlsx
from MMH import Ui_Form


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
        self.bounds = None
        self.Aub = None
        self.Bub = None
        self.Aeq = None
        self.Beq = None
        self.C = None
        self.aMat = None
        self.AHPW = None
        self.LPtype = 1
        self.graphicviewWidget.hide()
        self.btnStartAHP.setEnabled(False)
        self.matrix_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.topsisWeightMat.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.topsisMatrix.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ewMat.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.boundsMat.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lpResMat.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ahpMat.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.AHPweightMatTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.MVLRPredictResultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.MVLRtrainmat.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lptype_min.setChecked(True)
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
        self.btnTransAHPTo.clicked.connect(lambda: self.transAHPWMatrixTo())
        self.btnLP.clicked.connect(lambda: self.startLP())
        self.btnLPPreload.clicked.connect(lambda: self.preloadLP())
        self.lptype_min.clicked.connect(lambda: self.changeLPtype(1))
        self.lptype_max.clicked.connect(lambda: self.changeLPtype(0))
        self.btnCheckAHP.clicked.connect(lambda: self.checkAHP())
        self.ahpMat.itemChanged.connect(self.ahpItemChanged)
        self.btnStartAHP.clicked.connect(lambda: self.startAHP())
        self.tabWidget.currentChanged.connect(self.onCurrentTabChanged)
        self.btnStartSVLR.clicked.connect(lambda: self.startSVLR())
        self.btnMVLRTrain.clicked.connect(lambda: self.startMVLRTrain())
        self.btnMVLRPred.clicked.connect(lambda: self.startMVLRPred())

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
        self.btnStartAHP.setEnabled(False)
        self.sizelabel.setText(f"{self.mat.shape[0], self.mat.shape[1] - 1}")
        self.topsisWeightMat.setRowCount(1)
        self.topsisWeightMat.setColumnCount(self.mat.shape[1] - 1)
        self.ahpMat.setRowCount(self.mat.shape[1] - 1)
        self.ahpMat.setColumnCount(self.mat.shape[1] - 1)
        self.topsisMatrix.clear()
        for i in range(self.mat.shape[1] - 1):
            for j in range(self.mat.shape[1] - 1):
                if i == j:
                    self.ahpMat.setItem(i, j, QTableWidgetItem(str(1)))
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
        self.topsisMat = topsis(self.mat, self.W)
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

    def startLP(self):
        res = linearProgramming(self.C, self.Aub, self.Bub, self.Aeq, self.Beq, self.bounds)
        vec = res.x
        sc = res.fun
        if self.LPtype == 0:
            sc = -sc
        self.lpResMat.setColumnCount(len(vec))
        self.lpResMat.setRowCount(1)
        for i in range(len(vec)):
            self.lpResMat.setItem(0, i, QTableWidgetItem(str(vec[i])))
        self.lpvaLabel.setText(str(sc))

    def preloadLP(self):
        self.bounds = [[None for _ in range(2)] for _ in range(self.mat.shape[1] - 3)]
        self.boundsMat.setRowCount(self.mat.shape[1] - 1)
        self.boundsMat.setColumnCount(2)
        for i in range(self.mat.shape[1] - 1):
            for j in range(2):
                self.boundsMat.setItem(i, j, QTableWidgetItem('None'))
        self.C = None
        for i in range(self.mat.shape[0]):
            if self.mat[i][self.mat.shape[1] - 2] == 'c':
                self.C = self.mat[i]
        self.C = self.C[1:-2]
        if self.LPtype == 0:
            self.C *= -1
        self.Aub = np.empty((0, self.mat.shape[1] - 3))
        self.Bub = []
        for i in range(self.mat.shape[0]):
            if self.mat[i][self.mat.shape[1] - 2] == 'le':
                tmp = self.mat[i]
                tmp = tmp[1:-2]
                self.Aub = np.append(self.Aub, [tmp], axis=0)
                self.Bub.append(self.mat[i][self.mat.shape[1] - 1])
            elif self.mat[i][self.mat.shape[1] - 2] == 'ge':
                tmp = self.mat[0]
                tmp = tmp[1:-2]
                tmp = tmp * -1
                self.Aub = np.append(self.Aub, [tmp], axis=0)
                self.Bub.append(self.mat[i][self.mat.shape[1] - 1])

    def changeLPtype(self, param):
        self.LPtype = param

    def checkAHP(self):
        m = [[0 for _ in range(self.mat.shape[1] - 1)] for _ in range(self.mat.shape[1] - 1)]
        for i in range(1, self.mat.shape[1]):
            for j in range(1, self.mat.shape[1]):
                m[i - 1][j - 1] = float(self.ahpMat.item(i - 1, j - 1).text())
        m = np.array(m)
        print(m)
        flag = checkAHPAvailable(m)
        if flag:
            self.btnStartAHP.setEnabled(True)
            self.aMat = m
            self.ahpCheckLabel.setText("一致性检验通过")
        else:
            self.ahpCheckLabel.setText("一致性检验未通过")

    def ahpItemChanged(self, item):
        try:
            self.ahpMat.setItem(item.column(), item.row(), QTableWidgetItem(str(1 / int(item.text()))))
        except:
            print(item.row(), item.column())

    def startAHP(self):
        ahpType = self.ahpCalcWeightCB.currentIndex()
        print(ahpType)
        if ahpType == 0:
            self.AHPW = arithmeticMeanMethod(self.aMat)
        elif ahpType == 1:
            self.AHPW = geometricMeanMethod(self.aMat)
        else:
            self.AHPW = eigenvalueMethod(self.aMat)
        print(self.AHPW)
        self.showAHPWeightMatrix()

    def transAHPWMatrixTo(self):
        selected_text = self.transAHPCB.currentText()
        if selected_text == 'Topsis':
            self.W = self.AHPW
            self.W = np.pad(self.W, (1, 0), mode='constant')
            self.showTopsisWeightTable()

    def showAHPWeightMatrix(self):
        self.AHPweightMatTable.setRowCount(1)
        self.AHPweightMatTable.setColumnCount(len(self.AHPW))
        for i in range(len(self.AHPW)):
            self.AHPweightMatTable.setItem(0, i, QTableWidgetItem(str(self.AHPW[i])))

    def onCurrentTabChanged(self, index):
        if index == 3:
            self.graphicviewWidget.show()
            self.matWidget.setMaximumWidth(300)
            self.graphicviewWidget.setMinimumWidth(500)
            self.tabWidget.setMaximumWidth(400)
        else:
            self.graphicviewWidget.hide()
            self.matWidget.setMaximumWidth(114514)
            self.tabWidget.setMaximumWidth(114514)
        pass

    def startSVLR(self):
        x = self.mat[:, 1]
        y = self.mat[:, 2]
        SVLRtype = self.SVLRcb.currentIndex()
        w = 0
        b = 0
        if SVLRtype == 0:
            w, b = singleVarLinearRegressionOLS(x, y)
        elif SVLRtype == 1:
            w, b = singleVarLinearRegressionSKL(x, y)
            w = w[0]
        else:
            w, b, loss = gradientDescent(x, y)
            fig1 = Figure()
            fig1.draw2DScatterPlot(range(1, len(loss) + 1), loss, 1)
            fig1.save('SVLRLossFunc.html')
            self.webEngineView_2.load(
                QUrl.fromLocalFile(os.path.abspath(f'SVLRLossFunc.html')))
        fig = Figure()
        fig.draw2DScatterPlot(x, y, 0)
        fig.drawLinearFunction(w, b, [np.min(x) - 2, np.max(x) + 2])
        fig.save('SVLRgraph.html')
        self.webEngineView.load(
            QUrl.fromLocalFile(os.path.abspath(f'SVLRgraph.html')))

    def startMVLRTrain(self):
        y = self.mat[:, self.mat.shape[1] - 1]
        print(y)
        x = self.mat[:, ]
        y = self.mat[:, 2]

    def startMVLRPred(self):

        pass


def run():
    app = QApplication([])
    apply_stylesheet(app, theme='light_blue.xml')
    window = Frame()
    window.show()
    sys.exit(app.exec_())
