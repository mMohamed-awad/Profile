import os
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu
# IMPORT GUI FILE
from src.ui_interface import *
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter
from src.functions import GUIfunctions
from src import icons_rc

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # Proper way to call parent class constructor
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load JSON style
        loadJsonStyle(self, self.ui, jsonFiles={"json-styles/style.json"})

        # Update app settings
        QAppSettings.updateAppSettings(self)

        # Initialize GUI functions
        self.app_func = GUIfunctions(self)
        
        # Set up system tray
        try:
            self.setup_system_tray()
        except Exception as e:
            print(f"Error setting up system tray: {e}")

        # # Show the main window
        self.show()

    def setup_system_tray(self):
        # Create system tray icon
        self.tray = QSystemTrayIcon(QIcon(":/material_design/icons/material_design/mark_email_unread.png"), self)
        self.tray.setToolTip("Profile Tray")
        self.tray.show()

        # Create context menu for the tray
        self.menu = QMenu()
        open_action = self.menu.addAction("Open Window")
        hide_action = self.menu.addAction("Hide Window")
        message_action = self.menu.addAction("Show a message from tray")
        exit_action = self.menu.addAction("Exit")

        # Connect actions
        open_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        message_action.triggered.connect(lambda: self.tray_message())
        exit_action.triggered.connect(QApplication.instance().quit)  # Use QApplication.instance() to quit
        self.ui.sendBtn.clicked.connect(lambda: self.tray_message())

        # Set context menu for the tray
        self.tray.setContextMenu(self.menu)
        
    def tray_message(self):
        notification_title = f"Message from {self.ui.Quickname.text()}"
        notification_message = self.ui.Quickmasseg.toPlainText()
        icon = QIcon(":/material_design/icons/material_design/mark_email_unread.png")
        duration = 3000  # 3 seconds
        self.tray.showMessage(notification_title, notification_message, icon, duration)

    def sassCompilationProgress(self, n):
        self.ui.progressBar.setValue(n)
    


        self.sidebar_buttons = {
            "homeBtn": "Profile",
            "dataBtn": "Statistics",
            "graphsBtn": " Reviews ",
            "reportsBtn": "Reports",
            "settingsBtn": "Settings",
            "infoBtn": "Info",
            "helpBtn": "Help",
        }

        # نخزن النصوص الأصلية
        self.original_texts = self.sidebar_buttons.copy()
        self.ui.menuBtn.clicked.connect(self.toggle_sidebar)

        self.sidebar_expanded = False
        self.update_sidebar()

    def toggle_sidebar(self):
        self.sidebar_expanded = not self.sidebar_expanded
        self.update_sidebar()

    def update_sidebar(self):
        for name, original_text in self.original_texts.items():
            button = getattr(self.ui, name, None)
            if button and isinstance(button, QPushButton):
                if self.sidebar_expanded:
                    button.setText(original_text)
                else:
                    button.setText("")
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    appCustomToolTip = QCustomQToolTipFilter(tailPosition='auto')
    app.installEventFilter(appCustomToolTip)
    window = MainWindow()
    sys.exit(app.exec_())
