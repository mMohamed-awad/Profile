from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader
from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QColor, QFont, QFontDatabase, QIcon
from PySide6.QtWidgets import QGraphicsDropShadowEffect
import webbrowser


class GUIfunctions():
    def __init__(self, mainWindow):
        self.main = mainWindow
        self.ui = mainWindow.ui
        # apply font
        self.loadSansFont()

        #init app theme
        self.initializeAppTheme()

        self.connectMenuButtons()
        self.ui.HitHUP.clicked.connect(lambda: webbrowser.open("https://github.com/Mohammed-Awad-ENG"))
        self.ui.GItH.clicked.connect(lambda: webbrowser.open("https://github.com/Mohammed-Awad-ENG"))
        self.ui.gitHup.clicked.connect(lambda: webbrowser.open("https://github.com/Mohammed-Awad-ENG"))
        self.ui.Lin.clicked.connect(lambda: webbrowser.open("https://www.linkedin.com/in/mohammed-awd-18185537a/"))
        self.ui.Lin_2.clicked.connect(lambda: webbrowser.open("https://www.linkedin.com/in/mohammed-awd-18185537a/"))
        self.ui.Tweter.clicked.connect(lambda: webbrowser.open("https://x.com/grok?lang=en"))
        self.ui.Twiter.clicked.connect(lambda: webbrowser.open("https://x.com/grok?lang=en"))
        self.ui.pushButton_3.clicked.connect(lambda: webbrowser.open("https://maps.app.goo.gl/2zKZqf8icK4SBQtd7"))
        self.ui.location.clicked.connect(lambda: webbrowser.open("https://maps.app.goo.gl/2zKZqf8icK4SBQtd7"))
        self.ui.Email.clicked.connect(lambda: webbrowser.open("https://mail.google.com/mail/u/0/#sent?compose=GTvVlcSHwrwxQKnVwfrWMjjPlctXnmLdJnLXcwxZsmKzmXxwHJcrCwkcMqxTxDCdJccTSCbGLqXPB"))
        self.ui.contactMe.clicked.connect(lambda: webbrowser.open("https://mail.google.com/mail/u/0/#sent?compose=GTvVlcSHwrwxQKnVwfrWMjjPlctXnmLdJnLXcwxZsmKzmXxwHJcrCwkcMqxTxDCdJccTSCbGLqXPB"))

        self.ui.searchResaltBtn.clicked.connect(self.showSearchResult)


    def connectMenuButtons(self):
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenu.expandMenu())


        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenu.collapseMenu())

        self.ui.notifaction.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.more.clicked.connect(lambda: self.ui.rightMenu.expandMenu())
        self.ui.profileBtn.clicked.connect(lambda: self.ui.rightMenu.expandMenu())

        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenu.collapseMenu())

        # create search tooltip
    def createSearchTooltip(self):
        self.searchTooltip = QCustomTipOverlay(
        title="Search results.",
        description="Searching...",
        icon=self.main.theme.PATH_RESOURCES+"feather/search.png",
        isClosable=True,
        target=self.ui.SearchFrame,
        parent=self.main,
        deleteOnClose=True,
        duration=-1,
        closeIcon=self.main.theme.PATH_RESOURCES+"feather/x.png",
        tailPosition="top-center",
        toolFlag=True,
        )
        loader = QCustom3CirclesLoader(
            parent=self.searchTooltip,
            color=QColor(self.main.theme.COLOR_ACCENT_1), # color from theme
            penWidth=20,
            animationDuration=400
        )
        loader.show()
        # add loader to searchTooltip
        self.searchTooltip.addWidget(loader)


    def showSearchResult(self):
        # only show if serchlineEdit not empty
        if not self.ui.serchlineEdit.text():
            return

        try:
            self.searchTooltip.show()

        except: # tooltip deleted
            # re-init
            self.createSearchTooltip()
            self.searchTooltip.show()

        self.searchTooltip.setDescription("Showing search result For: \n" + self.ui.serchlineEdit.text())




    #initialize app theme
    def initializeAppTheme(self):
        settings = QSettings()
        current_them = settings.value("THEME")
        # print("current them is : ", current_them)

        # add them to them list
        self.populateThemeList(current_them)

        # Connect theme change signal to change app theme
        self.ui.themeList.currentTextChanged.connect(self.changAppTheme)


    def populateThemeList(self, current_them):
        theme_count = -1
        for theme in self.ui.themes:
            self.ui.themeList.addItem(theme.name, theme.name)
            # check default theme/ current theme
            if theme.defaultTheme or theme.name == current_them:
                self.ui.themeList.setCurrentIndex(theme_count)

    def changAppTheme(self):
        # if self.ui.mainPages_2.currentIndex() == 0:
            # if se
            
        settings = QSettings()
        selected_Theme = self.ui.themeList.currentData()
        current_Theme = settings.value("THEME")

        if current_Theme != selected_Theme:
            settings.setValue("THEME", selected_Theme)
            QAppSettings.updateAppSettings(self.main, reloadJson=True)

    # apply custom font
    def loadSansFont(self):
        font_id = QFontDatabase.addApplicationFont("./fonts/google-sans-cufonfonts/ProductSans-Regular.ttf")
        # if font not loaded
        if font_id == -1:
            print("Failed to load Sans font")
            sans = QFont("Sans Serif")
        else:
            font_families = QFontDatabase.applicationFontFamilies(font_id)
            if font_families:
                sans = QFont(font_families[0])
            else:
                sans = QFont("Sans Serif")

        # apply to main
        self.main.setFont(sans)

    








