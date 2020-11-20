import sys
# import csv
from qtpy import QtWidgets
from qtpy.QtWidgets import QFileDialog

from ui_pcdaten.mainwindow import Ui_MainWindow
from ui_pcdaten.mainwindow_2 import Ui_mainwindow_2


class MainWindow_2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_pcdaten = Ui_mainwindow_2()
        self.ui_pcdaten.setupUi(self)
        #self.ui_pcdaten.addPC.clicked(self.)


    #def searchWindow(self):

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui_pcdaten.pushButton.clicked.connect(self.browsefiles)

    def browsefiles(self):
        # Problem: Wie kann der Standard Suchpfad so eingestellt werden, dass er direkt in Downloads landet
        file = QFileDialog.getOpenFileName(self, 'Open file', 'C:\%Username%\Downloads')
        fname = file[0]
        if fname[-3:] != "csv":
            # Fenster mit Warnung, dass inkorrekte Datei-Endung eingefügt wurde - evtl Prüfung ob richtiges Format
            print("Bitte eine korrekte CSV Datei einfügen!")
            return 1
        self.ui_pcdaten.lineSearch.setText(fname)

        csvName = self.ui_pcdaten.lineSearch.text()
        with open(csvName, "r", encoding="utf-8") as csvFile:
            for line in csvFile:
                print(line)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow_2()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()