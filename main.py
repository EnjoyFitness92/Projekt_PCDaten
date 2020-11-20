import sys
# import csv
from qtpy import QtWidgets
from qtpy.QtWidgets import QFileDialog

from ui_pcdaten.mainwindow import Ui_MainWindow


app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_pcdaten = Ui_MainWindow()
        self.ui_pcdaten.setupUi(self)
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
        print(fname)


window = MainWindow()

window.show()

sys.exit(app.exec_())

