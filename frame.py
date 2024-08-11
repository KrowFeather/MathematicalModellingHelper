import os
import sys

from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QTableWidgetItem
from qt_material import apply_stylesheet

from Functions.utils.OutputXlsx import outputXlsx
from MMH import Ui_Form
import pandas as pd
from Functions.Preworks.PositiveTransformation import *


class Frame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.fileName = None
        self.setupUi(self)
        self.setWindowTitle("Mathematical Modelling Helper a1.0.0")
        self.setStyleSheet("background-color:white")
        self.showMaximized()
        self.df = pd.DataFrame()
        self.mat = None
        self.bind()

    def bind(self):
        self.btn_getFile.clicked.connect(lambda: self.open_file_dialog())
        self.btn_filter.clicked.connect(lambda: self.showTable())
        self.btnMinMetric.clicked.connect(lambda: self.calcMin())
        self.btnBS.clicked.connect(lambda: self.calcBS())
        self.btnInterval.clicked.connect(lambda: self.calcInterval())
        self.btn_output.clicked.connect(lambda: self.outputXlsx())

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
        if extension == ".xlsx":
            self.df = pd.read_excel(filename)
        else:
            self.df = pd.read_csv(filename)
        self.mat = self.df.to_numpy()
        self.sizelabel.setText(f"{self.mat.shape}")
        self.showTable()

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

    def outputXlsx(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            f"{self.fileName}",
            "Excel Files (*.xlsx)"
        )
        outputXlsx(file_path, self.mat)


def run():
    app = QApplication([])
    apply_stylesheet(app, theme='light_blue.xml')
    window = Frame()
    window.show()
    sys.exit(app.exec_())
