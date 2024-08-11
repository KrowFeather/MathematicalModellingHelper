import os
import sys

from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QTableWidgetItem
from qt_material import apply_stylesheet
from MMH import Ui_Form
import pandas as pd


class Frame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Mathematical Modelling Helper a1.0.0")
        self.setStyleSheet("background-color:white")
        self.showMaximized()
        self.df = pd.DataFrame()
        self.bind()

    def bind(self):
        self.btn_getFile.clicked.connect(lambda: self.open_file_dialog())
        self.btn_filter.clicked.connect(lambda: self.showTable())

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Excel Files (*.xlsx)"
        )
        fileName = os.path.basename(file_name)
        if file_name:
            self.filenamelabel.setText(f"{fileName}")
            self.prework(file_name)

    def prework(self, filename):
        (_, extension) = os.path.splitext(filename)
        if extension == ".xlsx":
            self.df = pd.read_excel(filename)
        else:
            self.df = pd.read_csv(filename)
        self.sizelabel.setText(f"{len(self.df), len(self.df.columns)}")
        self.showTable()

    def showTable(self):
        begin = self.begin_index.text()
        end = self.end_index.text()
        mat = self.df.values.tolist()
        if begin == '':
            begin = 0
        else:
            begin = int(begin)-1
        if end == '':
            end = len(mat)
        else:
            end = int(end)
        self.matrix_table.setRowCount(min(end - begin, 300))
        self.matrix_table.setColumnCount(min(len(mat[0]), 300))
        print(mat)
        # self.matrix_table.clear()
        for i in range(begin, end):
            for j in range(1, len(mat[i])):
                self.matrix_table.setItem(i - begin, j - 1, QTableWidgetItem(str(mat[i][j])))


def run():
    app = QApplication([])
    apply_stylesheet(app, theme='light_blue.xml')
    window = Frame()
    window.show()
    sys.exit(app.exec_())
