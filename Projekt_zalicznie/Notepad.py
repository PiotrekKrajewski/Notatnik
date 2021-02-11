import sys

from PyQt5.QtCore import QDir, QDateTime
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QApplication, QFileDialog, QPushButton, QHBoxLayout, \
    QMainWindow, QAction, qApp, QMessageBox


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit(self)
        self.save_btn = QPushButton('Zapisz')
        self.open_btn = QPushButton('Otwórz')
        self.initUI()

    def initUI(self):
        PATHNAME = ''
        layout = QVBoxLayout()
        self.textEdit.setAcceptRichText(False)
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

        QApplication.clipboard().dataChanged.connect(self.wklej)

        # self.show()


    def zapisz(self):
        global PATHNAME
        if PATHNAME == '':
            with open('bez_tytulu.txt', 'w') as f:
                text = self.textEdit.toPlainText()
                f.write(text)
                f.close()
        else:
            filename = PATHNAME
            if filename[0].endswith('.txt'):
                with open(filename[0], 'w') as f:
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
        global PATHNAME
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            filename = dialog.selectedFiles()
            PATHNAME = filename
            print(PATHNAME)
            if filename[0].endswith('.txt'):
                with open(filename[0], 'r') as f:
                    text = f.read()
                    self.textEdit.setPlainText(text)
                    f.close()

    def wyczysc(self):
        global PATHNAME
        self.textEdit.clear()
        PATHNAME = ''

    def cofnij(self):
        self.textEdit.undo()

    def wytnij(self):
        #if self.textEdit.selectionChanged() == True:
        #    self.textEdit.selectionChanged.connect(self.textEdit.cut)
        self.textEdit.cut(self)

    def kopiuj(self):
        self.textEdit.copy()

    def wklej(self):
        text = QApplication.clipboard().text()
        self.textEdit.insertPlainText(text)

    def usun(self):
        #text = self.textEdit.toPlainText()
        new_text = ''
        #cursor = self.textEdit.textCursor()
        #print(cursor.selectionStart(), cursor.selectionEnd())
        #for i in range(0, cursor.selectionStart()):
            # new_text = new_text + new_text.join(text[i])
        #    new_text = ''
        #for i in range(cursor.selectionEnd(), len(text)):
            # new_text = new_text + new_text.join(text[i])
        #    new_text = ''
        self.textEdit.insertPlainText(new_text)

    def zaznacz(self):
        self.textEdit.selectAll()

    def datagodzina(self):
        text = QDateTime.currentDateTime().toString()
        text_from_text_edit = self.textEdit.toPlainText()
        self.textEdit.setText(text_from_text_edit + ' ' + text)


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

        menuedycja = menubar.addMenu('Edycja')

        cofnij = QAction('Cofnij', self)
        cofnij.setShortcut('Ctrl+Z')
        menuedycja.addAction(cofnij)
        cofnij.triggered.connect(self.cofnij)

        menuedycja.addSeparator()

        wytnij = QAction('Wytnij', self)
        wytnij.setShortcut('Ctrl+X')
        menuedycja.addAction(wytnij)
        wytnij.triggered.connect(self.wytnij)

        kopiuj = QAction('Kopiuj', self)
        kopiuj.setShortcut('Ctrl+C')
        menuedycja.addAction(kopiuj)
        kopiuj.triggered.connect(self.kopiuj)

        wklej = QAction('Wklej', self)
        wklej.setShortcut('Ctrl+V')
        menuedycja.addAction(wklej)
        wklej.triggered.connect(self.wklej)

        usun = QAction('Usuń zaznaczony tekst', self)
        usun.setShortcut('del')
        menuedycja.addAction(usun)
        usun.triggered.connect(self.usun)

        menuedycja.addSeparator()

        zaznacz = QAction('Zaznacz wszystko', self)
        zaznacz.setShortcut('Ctrl+A')
        menuedycja.addAction(zaznacz)
        zaznacz.triggered.connect(self.zaznacz)

        data = QAction('Data/godzina', self)
        data.setShortcut('F5')
        menuedycja.addAction(data)
        data.triggered.connect(self.datagodzina)

        menupomoc = menubar.addMenu('Pomoc')

        info = QAction('Notatnik - informacje', self)
        menupomoc.addAction(info)
        info.triggered.connect(self.info)


        self.show()

    def nowy(self):
        self.form_widget.wyczysc()

    def otworz(self):
        self.form_widget.otworz()

    def zapisz(self):
        self.form_widget.zapisz()

    def zapisz_jako(self):
        self.form_widget.zapisz_jako()

    def cofnij(self):
        self.form_widget.cofnij()

    def wytnij(self):
        self.form_widget.wytnij()

    def kopiuj(self):
        self.form_widget.kopiuj()

    def wklej(self):
        self.form_widget.wklej()

    def usun(self):
        self.form_widget.usun()

    def zaznacz(self):
        self.form_widget.zaznacz()

    def datagodzina(self):
        self.form_widget.datagodzina()

    def info(self):
        QMessageBox.about(self, 'Aplikacja', 'Prosty notatnik, na zaliczenie zajęć Programowanie wieloplatformowe QT')


app = QApplication(sys.argv)
exe = Menu()
sys.exit(app.exec_())
