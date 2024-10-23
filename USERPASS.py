import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(250, 100) 
        MainWidget = QWidget()
        Layout = QFormLayout()
        MainWidget.setLayout(Layout)
        self.setCentralWidget(MainWidget)

        self.userLineEdit = QLineEdit()
        self.passLineEdit = QLineEdit()
        self.passLineEdit.setEchoMode(QLineEdit.Password)
        self.submitButton = QPushButton("Submit")
        self.cancelButton = QPushButton("Cancel")

        
        self.submitButton.clicked.connect(self.on_submit)
        self.cancelButton.clicked.connect(self.on_cancel)

        Layout.addRow(QLabel("Username:"), self.userLineEdit)
        Layout.addRow(QLabel("Password: "), self.passLineEdit)
        Layout.addRow(self.cancelButton, self.submitButton)

    def on_submit(self):
        username = self.userLineEdit.text()
        password = self.passLineEdit.text()
        QMessageBox.information(self, "Login Info", f"Username: {username}\nPassword: {password}")

    def on_cancel(self):
        self.userLineEdit.clear()
        self.passLineEdit.clear()
        self.userLineEdit.setFocus()  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
