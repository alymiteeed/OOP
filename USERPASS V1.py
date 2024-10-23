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

        
        self.correct_username = "ALYiens"
        self.correct_password = "password123"

    def on_submit(self):
        username = self.userLineEdit.text()
        password = self.passLineEdit.text()

        if username == self.correct_username and password == self.correct_password:
            QMessageBox.information(self, "Login Success", "You have logged in successfully!")
        elif username == self.correct_username:
            QMessageBox.warning(self, "Invalid Password", "The password is incorrect.")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username.")

    def on_cancel(self):
        self.userLineEdit.clear()
        self.passLineEdit.clear()
        self.userLineEdit.setFocus()  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
