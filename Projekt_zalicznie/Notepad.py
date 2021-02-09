import os
import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QApplication, QFileDialog, QPushButton, QHBoxLayout


#spróbować bez self zadeklarować text edit i przyciski


class Notepad(QWidget):
    def __init__(self):
        super(Notepad, self).__init__()
        self.textEdit = QTextEdit(self)
        self.save_btn = QPushButton('Zapisz')
        self.open_btn = QPushButton('Otwórz')
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Notatnik')
        self.setFixedSize(800, 600)

        layout = QVBoxLayout()

        self.textEdit.resize(750, 500)
        self.textEdit.move(25, 25)
        self.save_btn.resize(75, 25)
        self.save_btn.move(100, 525)
        self.open_btn.resize(75, 25)
        self.open_btn.move(175, 425)

        layout.addWidget(self.textEdit)
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.open_btn)
        layout.addLayout(h_layout)

        self.save_btn.clicked.connect(self.zapisz)
        self.open_btn.clicked.connect(self.otworz)

        self.setLayout(layout)

        self.show()

    def zapisz(self):
        with open('bez_tytulu.txt', 'w') as f:
            text = self.textEdit.toPlainText()
            f.write(text)
            f.close()


    def zapisz_jako(self):
        filename = QFileDialog.getSaveFileName(self, 'Zapisz plik jako', 'C:\\', '*.txt')
        if filename[0].endswith('.txt'):
            with open(filename[0], 'w') as f:
                text = self.textEdit.toPlainText()
                f.write(text)
                f.close()


    def otworz(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            filename = dialog.selectedFiles()

            if filename[0].endswith('.txt'):
                with open(filename[0], 'r') as f:
                    text = f.read()
                    self.textEdit.setPlainText(text)
                    f.close()



app = QApplication(sys.argv)
exe = Notepad()
sys.exit(app.exec_())