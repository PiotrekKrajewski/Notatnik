import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QApplication, QFileDialog, QPushButton, QHBoxLayout, \
    QMainWindow, QAction, qApp


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit(self)
        self.save_btn = QPushButton('Zapisz')
        self.open_btn = QPushButton('Otwórz')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.textEdit.resize(750, 500)
        self.textEdit.move(25, 25)
        self.save_btn.resize(75, 25)
        self.open_btn.resize(75, 25)

        layout.addWidget(self.textEdit)
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.open_btn)
        layout.addLayout(h_layout)

        self.save_btn.clicked.connect(self.zapisz)
        self.open_btn.clicked.connect(self.otworz)

        self.setLayout(layout)

        # self.show()

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

    def wyczysc(self):
        self.textEdit.clear()


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Notatnik')
        self.setFixedSize(800, 600)

        menubar = self.menuBar()
        menuplik = menubar.addMenu('Plik')

        nowy = QAction('Nowy', self)
        nowy.setShortcut('Ctrl+N')
        menuplik.addAction(nowy)
        nowy.triggered.connect(self.nowy)

        menuplik.addSeparator()

        otworz = QAction('Otwórz...', self)
        otworz.setShortcut('Ctrl+O')
        menuplik.addAction(otworz)
        otworz.triggered.connect(self.otworz)

        zapisz = QAction('Zapisz', self)
        zapisz.setShortcut('Ctrl+S')
        menuplik.addAction(zapisz)
        zapisz.triggered.connect(self.zapisz)

        zapisz_jako = QAction('Zapisz jako...', self)
        zapisz_jako.setShortcut('Ctrl+Shift+S')
        menuplik.addAction(zapisz_jako)
        zapisz_jako.triggered.connect(self.zapisz_jako)

        menuplik.addSeparator()

        zakoncz = QAction('Zakończ', self)
        zakoncz.setShortcut('Ctrl+Q')
        menuplik.addAction(zakoncz)
        zakoncz.triggered.connect(qApp.quit)

        self.show()

    def nowy(self):
        self.form_widget.wyczysc()

    def otworz(self):
        self.form_widget.otworz()

    def zapisz(self):
        self.form_widget.zapisz()

    def zapisz_jako(self):
        self.form_widget.zapisz_jako()


app = QApplication(sys.argv)
exe = Menu()
sys.exit(app.exec_())
