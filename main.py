import sys
import pyodbc
import dbcon

from qtpy import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from qtpy.QtWidgets import QFileDialog

from ui_pcdaten.mainwindow import Ui_PCDaten
from ui_pcdaten.setdevice import Ui_setDevice
from ui_pcdaten.setuser import Ui_setUser
from ui_pcdaten.searchdevice import Ui_searchDevice
from ui_pcdaten.searchuser import Ui_searchUser

# app = QtWidgets.QApplication(sys.argv)

# Suchen nach einem Benutzer
class UserSearcher(QWidget):
    def __init__(self):
        super().__init__()
        self.searchUser = Ui_searchUser()
        self.searchUser.setupUi(self)

# Suchen nach einem Gerät - mit verschiedenen Attributen möglich
class DeviceSearcher(QWidget):
    def __init__(self):
        super().__init__()
        self.searchDevice = Ui_searchDevice()
        self.searchDevice.setupUi(self)

# Klasse für das Setzen eines neuen Benutzers
class UserSetter(QWidget):
    def __init__(self):
        super().__init__()
        self.setUser = Ui_setUser()
        self.setUser.setupUi(self)

        try:
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=G:\Projekt Inventardb\Inventar.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()

            # Auswahl der höchsten aktuellen Pers_ID
            cursor.execute('Select max(Pers_ID) FROM Benutzer')

            # Zum Testen welches die höchste Pers_ID ist
            # print(cursor.fetchall()[0][0])
            idUser = str(int(cursor.fetchall()[0][0]) + 1)
            self.setUser.persID.setText(idUser)


        except pyodbc.Error as e:
            print("Error in Connection", e)

        self.setUser.insertData.clicked.connect(self.insertUser)


    def insertUser(self):
        # Problem beim Einfügen da die Datenbank mit einer weiteren ID arbeitet
        # Aufgabe: Abklären was man tun kann damit man Datenbankelemente einbinden kann in QT


        dep = self.setUser.department.text()
        def switchDep(argument):
            switcher = {
                'Finanzen': 5,
                'Studium': 1,
                'Bibliothek': 2,
                'Auslandsamt': 3,
                'Rechenzentrum': 4,
                'ZWW/IAFW': 6,
                'Personal': 7,
                'HL': 8,
                'Sprecherrat': 9,
                'QuO': 10,
                'IAFW': 11,
                'ÖA': 12,
                # Doppelter Eintrag in der AccessDB
                #'Sprecherrat': 13,
                'Zentrale Server u. Dienste': 14,
                'Reserve VW': 15,
                'TB': 16,
                'Benutzerbetrueuung': 17,
                '': 4
            }
            return switcher.get(argument, 4)

        # Ausnahmefälle beachten - z.b. wenn firstName und surname nicht inkludiert sind
        persID = self.setUser.firstName.text()
        firstName = self.setUser.firstName.text()
        surname = self.setUser.surName.text()
        telNum = self.setUser.telNum.text()
        department = switchDep(dep)
        room = self.setUser.room.text()
        ndsId = self.setUser.ndsId.text()
        archiv24User = False

        if self.setUser.archiv24User.isChecked():
            archiv24User = True

        try:
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=G:\Projekt Inventardb\Inventar.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()

            #myuser = (persID, firstName, surname, telNum, room,, ndsId, archiv24User)
            cursor.execute('INSERT INTO Benutzer VALUES(?,?,?,?,?,?,?,?)', int(persID), firstName, surname, telNum, room, department, ndsId, archiv24User)
            conn.commit()
            #print('Data Inserted')
            #name = 'Seitz'

            #cursor.execute('Select "Abteilung"  FROM Benutzer Where Nachname = ?', name)
            #print(cursor.fetchall())
        except pyodbc.Error as e:
            print("Error in Connection", e)

# Klasse für das Einfügen eines neuen Rechners
class DeviceSetter(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    # Wichtige Elemente aus CSV die übernommen werden sollen
    comTyp = []
    room = []
    serialnr = []
    hostName = []
    macAddr = []
    ipAddr = []
    idPC = []
    l = []

    def __init__(self):
        super().__init__()
        self.setDevice = Ui_setDevice()
        self.setDevice.setupUi(self)

        self.setDevice.searchCsv.clicked.connect(self.browsefiles)
        self.setDevice.insertData.clicked.connect(self.insertData)

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
                l = line.split(";")
                comTyp = l[5].replace('"', '')
                room = l[8].replace('"', '')
                serialnr = l[9].replace('"', '')
                hostName = l[14].replace('"', '')
                macAddr = l[15].replace('"', '')
                ipAddr = l[20].replace('"', '')

        self.setDevice.ipAddr.setText(ipAddr)
        self.setDevice.comTyp.setText(comTyp)
        self.setDevice.hostName.setText(hostName)
        self.setDevice.serialNumber.setText(serialnr)
        self.setDevice.roomNum.setText(room)
        self.setDevice.MacAddr.setText(macAddr)

        try:
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=G:\Projekt Inventardb\Inventar.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()

            # Auswahl der höchsten aktuellen ID_Rechner
            cursor.execute('Select max(ID_Rechner) FROM Geräte')

            # Zum Testen welches die höchste ID_Rechner ist
            #print(cursor.fetchall()[0][0])
            idPC = str(int(cursor.fetchall()[0][0])+1)
            self.setDevice.idRechner.setText(idPC)

            cursor.execute('Select Benutzer From Geräte')

        except pyodbc.Error as e:
            print("Error in Connection", e)

    def insertData(self):
        # Fügt die Daten in eine neue Zeile der AccessDB ein und prüft Dupletten ab
        # Verbindung zur Datenbank herstellen
        try:
            con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=G:\Projekt Inventardb\Inventar.accdb;'
            conn = pyodbc.connect(con_string)
            cursor = conn.cursor()

            # Auswahl der höchsten aktuellen ID_Rechner
            cursor.execute('Select max(ID_Rechner) FROM Geräte')

            # Zum Testen welches die höchste ID_Rechner ist
            #print(cursor.fetchall())


        except pyodbc.Error as e:
            print("Error in Connection", e)


# Klasse des Hauptmenüs mit der Struktur über den Aufruf der weiteren Fenster
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_pcdaten = Ui_PCDaten()
        self.ui_pcdaten.setupUi(self)

        # Wenn man auf Gerät hinzufügen klickt öffnet sich das Fenster openSetter und bei den anderen Buttons identischer Vorgang
        self.ui_pcdaten.addDevice.clicked.connect(self.openSetDevice)
        self.ui_pcdaten.addUser.clicked.connect(self.openSetUser)
        self.ui_pcdaten.searchDevice.clicked.connect(self.openSearchDevice)
        self.ui_pcdaten.searchUser.clicked.connect(self.openSearchUser)

    def openSetDevice(self, checked):
        self.w = DeviceSetter()
        self.w.show()

    def openSetUser(self, checked):
        self.w = UserSetter()
        self.w.show()

    def openSearchDevice(self, checked):
        self.w = DeviceSearcher()
        self.w.show()

    def openSearchUser(self, checked):
        self.w = UserSearcher()
        self.w.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
