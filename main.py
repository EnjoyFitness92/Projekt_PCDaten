import sys
# import csv
from qtpy import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from qtpy.QtWidgets import QFileDialog

from ui_pcdaten.mainwindow import Ui_MainWindow
from ui_pcdaten.setdevice import Ui_setDevice
from ui_pcdaten.setuser import Ui_setUser

# app = QtWidgets.QApplication(sys.argv)

class UserSetter(QWidget):
    def __init__(self):
        super().__init__()
        self.setUser = Ui_setUser()
        self.setUser.setupUi(self)


class DeviceSetter(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.setDevice = Ui_setDevice()
        self.setDevice.setupUi(self)

        self.setDevice.searchCsv.clicked.connect(self.browsefiles)

    def browsefiles(self):
        # Problem: Wie kann der Standard Suchpfad so eingestellt werden, dass er direkt in Downloads landet
        file = QFileDialog.getOpenFileName(self, 'Open file', 'C:\%Username%\Downloads')
        fname = file[0]
        if fname[-3:] != "csv":
            # Fenster mit Warnung, dass inkorrekte Datei-Endung eingefügt wurde - evtl Prüfung ob richtiges Format
            print("Bitte eine korrekte CSV Datei einfügen!")
            return 1
        self.setDevice.inputCsv.setText(fname)

        csvName = self.setDevice.inputCsv.text()
        with open(csvName, "r", encoding="utf-8") as csvFile:
            for line in csvFile:
                # Herausfischen der wichtigen Daten und abspeichern in einer temporären Liste
                print(line)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_pcdaten = Ui_MainWindow()
        self.ui_pcdaten.setupUi(self)
        # Wenn man auf Gerät hinzufügen klickt öffnet sich das Fenster openSetter
        self.ui_pcdaten.addDevice.clicked.connect(self.openSetDevice)
        self.ui_pcdaten.addUser.clicked.connect(self.openSetUser)

    def openSetDevice(self, checked):
        self.w = DeviceSetter()
        self.w.show()

    def openSetUser(self, checked):
        self.w = UserSetter()
        self.w.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
