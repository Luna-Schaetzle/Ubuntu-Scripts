# To run this script, you need to install PyQt5 and PyQtWebEngine
# QT_QPA_PLATFORM=xcb python3 wttr.py # Run this command to start the script

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  # Importiere QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webbrowser in PyQt")
        self.setGeometry(100, 100, 950, 680)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://wttr.in/"))  # Konvertiere String in QUrl

        self.setCentralWidget(self.browser)

        # Button zum Neuladen der Website
        reload_button = QPushButton("Website neu laden")
        reload_button.clicked.connect(self.reload_website)

        layout = QVBoxLayout()
        layout.addWidget(reload_button)
        layout.addWidget(self.browser)  # Füge den Browser zum Layout hinzu

        # Erstelle ein zentrales Widget und setze das Layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def reload_website(self):
        self.browser.reload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())

