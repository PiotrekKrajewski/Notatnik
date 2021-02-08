import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMenu, QMessageBox


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.textEditBox = QTextEdit()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Notatnik')
        self.setFixedSize(800, 600)

        menuBar = self.menuBar()
        plikMenu = menuBar.addMenu('Plik')
        editMenu = menuBar.addMenu('Edytuj')
        formatMenu = menuBar.addMenu('')
        pomocMenu = menuBar.addMenu('Pomoc')

        # plik
        nowy = QAction('Nowy', self)
        nowy.setShortcut('Ctrl+N')
        plikMenu.addAction(nowy)

        otworz = QAction('Otwórz...', self)
        otworz.setShortcut('Ctrl+O')
        plikMenu.addAction(otworz)

        zapisz = QAction('Zapisz', self)
        zapisz.setShortcut('Ctrl+S')
        plikMenu.addAction(zapisz)

        zapiszJako = QAction('Zapisz jako...', self)
        zapiszJako.setShortcut('Ctrl+Shift+S')
        plikMenu.addAction(zapiszJako)


        exitApp = QAction('Wyjście', self)
        exitApp.setShortcut('Ctrl+Q')
        exitApp.triggered.connect(qApp.quit)
        plikMenu.addAction(exitApp)

        #edycja
        cofnij = QAction('Cofnij', self)
        cofnij.setShortcut('Ctrl+Z')
        editMenu.addAction(cofnij)

        wytnij = QAction('Wytnij', self)
        wytnij.setShortcut('Ctrl+X')
        editMenu.addAction(wytnij)

        kopiuj = QAction('Kopiuj', self)
        kopiuj.setShortcut('Ctrl+C')
        editMenu.addAction(kopiuj)

        wklej = QAction('Wklej', self)
        wklej.setShortcut('Ctrl+V')
        editMenu.addAction(wklej)

        znajdz = QAction('Znajdź', self)
        znajdz.setShortcut('Ctrl+F')
        editMenu.addAction(znajdz)

        zaznaczWszystko = QAction('Zaznacz wszystko', self)
        zaznaczWszystko.setShortcut('Ctrl+A')
        editMenu.addAction(zaznaczWszystko)

        godzinaData = QAction('Godzina/data', self)
        godzinaData.setShortcut('F5')
        editMenu.addAction(godzinaData)

        # pomoc
        infoQt = QAction('Qt', self)
        infoQt.setShortcut('Ctrl+T')
        infoQt.triggered.connect(qApp.aboutQt)

        infoApp = QAction('App', self)
        infoApp.setShortcut('Ctrl+A')
        infoApp.triggered.connect(self.notatnikInfo)

        # pomoc/ info
        infoMenu = QMenu('Informacje', self)
        infoMenu.addAction(infoQt)
        infoMenu.addAction(infoApp)
        pomocMenu.addMenu(infoMenu)

        self.show()

    def notatnikInfo(self):
        QMessageBox.about(self, 'Aplikacja', 'Notatnik wzorowany na tym z systemu Windows 10')

app = QApplication(sys.argv)
exe = Notepad()
sys.exit(app.exec_())