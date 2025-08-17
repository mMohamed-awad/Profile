# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1138, 590)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1036, 590))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.main_menu = QCustomSlideMenu(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.main_menu)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.main_menu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(46, 42))
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.menuBtn = QPushButton(self.widget_5)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(148, 140))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 3, -1)
        self.homeBtn = QPushButton(self.widget_3)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.dataBtn = QPushButton(self.widget_3)
        self.dataBtn.setObjectName(u"dataBtn")
        self.dataBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/pie-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dataBtn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.dataBtn)

        self.graphsBtn = QPushButton(self.widget_3)
        self.graphsBtn.setObjectName(u"graphsBtn")
        self.graphsBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/feather/icons/feather/star.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.graphsBtn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.graphsBtn)

        self.reportsBtn = QPushButton(self.widget_3)
        self.reportsBtn.setObjectName(u"reportsBtn")
        self.reportsBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/printer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reportsBtn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.reportsBtn)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(114, 108))
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settingsBtn = QPushButton(self.widget_4)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.widget_4)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.infoBtn.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.widget_4)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/feather/icons/feather/help-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addWidget(self.main_menu)

        self.centerMenu = QCustomSlideMenu(self.centralwidget)
        self.centerMenu.setObjectName(u"centerMenu")
        self.centerMenu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centerMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.widget_2)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        self.closeCenterMenuBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/feather/icons/feather/x-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeCenterMenuBtn.setIcon(icon8)

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.centerMenuPages = QCustomQStackedWidget(self.centerMenu)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_6 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.widget_6 = QWidget(self.settingsPage)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.frame = QFrame(self.widget_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 9, 3, 9)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.themeList = QComboBox(self.frame)
        self.themeList.setObjectName(u"themeList")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeList.sizePolicy().hasHeightForWidth())
        self.themeList.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.themeList)


        self.verticalLayout_7.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addWidget(self.widget_6)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.verticalLayout_8 = QVBoxLayout(self.infoPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.infoPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignVCenter)

        self.centerMenuPages.addWidget(self.infoPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_9 = QVBoxLayout(self.helpPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.helpPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignVCenter)

        self.centerMenuPages.addWidget(self.helpPage)

        self.verticalLayout_5.addWidget(self.centerMenuPages)


        self.horizontalLayout.addWidget(self.centerMenu)

        self.MainBody = QWidget(self.centralwidget)
        self.MainBody.setObjectName(u"MainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainBody.sizePolicy().hasHeightForWidth())
        self.MainBody.setSizePolicy(sizePolicy1)
        self.verticalLayout_10 = QVBoxLayout(self.MainBody)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.MainBody)
        self.header.setObjectName(u"header")
        self.horizontalLayout_7 = QHBoxLayout(self.header)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.TitelText = QLabel(self.header)
        self.TitelText.setObjectName(u"TitelText")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.TitelText.setFont(font1)

        self.horizontalLayout_7.addWidget(self.TitelText, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, -1, 5)
        self.notifaction = QPushButton(self.frame_2)
        self.notifaction.setObjectName(u"notifaction")
        self.notifaction.setMaximumSize(QSize(40, 40))
        self.notifaction.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/bell.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notifaction.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.notifaction)

        self.more = QPushButton(self.frame_2)
        self.more.setObjectName(u"more")
        self.more.setMaximumSize(QSize(40, 40))
        self.more.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/more-horizontal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.more.setIcon(icon10)

        self.horizontalLayout_6.addWidget(self.more)

        self.profileBtn = QPushButton(self.frame_2)
        self.profileBtn.setObjectName(u"profileBtn")
        self.profileBtn.setMaximumSize(QSize(40, 40))
        self.profileBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/feather/icons/feather/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn.setIcon(icon11)

        self.horizontalLayout_6.addWidget(self.profileBtn)


        self.horizontalLayout_7.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.SearchFrame = QFrame(self.header)
        self.SearchFrame.setObjectName(u"SearchFrame")
        sizePolicy1.setHeightForWidth(self.SearchFrame.sizePolicy().hasHeightForWidth())
        self.SearchFrame.setSizePolicy(sizePolicy1)
        self.SearchFrame.setMinimumSize(QSize(200, 0))
        self.SearchFrame.setMaximumSize(QSize(400, 300))
        self.SearchFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SearchFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.SearchFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.SearchFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(16, 16))
        self.label_8.setMaximumSize(QSize(22, 22))
        self.label_8.setBaseSize(QSize(0, 0))
        self.label_8.setPixmap(QPixmap(u":/material_design/icons/material_design/search.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.serchlineEdit = QLineEdit(self.SearchFrame)
        self.serchlineEdit.setObjectName(u"serchlineEdit")
        self.serchlineEdit.setMinimumSize(QSize(200, 0))
        self.serchlineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.serchlineEdit)

        self.searchResaltBtn = QPushButton(self.SearchFrame)
        self.searchResaltBtn.setObjectName(u"searchResaltBtn")
        self.searchResaltBtn.setMaximumSize(QSize(16777215, 16777215))
        self.searchResaltBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/font_awesome_brands/icons/font_awesome/brands/wpexplorer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchResaltBtn.setIcon(icon12)
        self.searchResaltBtn.setIconSize(QSize(19, 19))

        self.horizontalLayout_8.addWidget(self.searchResaltBtn)


        self.horizontalLayout_7.addWidget(self.SearchFrame, 0, Qt.AlignmentFlag.AlignBottom)

        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(150, 400))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.MinmizeBtn = QPushButton(self.frame_4)
        self.MinmizeBtn.setObjectName(u"MinmizeBtn")
        self.MinmizeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MinmizeBtn.setIcon(icon13)

        self.horizontalLayout_9.addWidget(self.MinmizeBtn)

        self.MaxmizeBtn = QPushButton(self.frame_4)
        self.MaxmizeBtn.setObjectName(u"MaxmizeBtn")
        self.MaxmizeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/feather/icons/feather/square.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MaxmizeBtn.setIcon(icon14)

        self.horizontalLayout_9.addWidget(self.MaxmizeBtn)

        self.closeBtn = QPushButton(self.frame_4)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/feather/icons/feather/x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeBtn.setIcon(icon15)

        self.horizontalLayout_9.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_10.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.mainContant = QWidget(self.MainBody)
        self.mainContant.setObjectName(u"mainContant")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainContant.sizePolicy().hasHeightForWidth())
        self.mainContant.setSizePolicy(sizePolicy3)
        self.horizontalLayout_10 = QHBoxLayout(self.mainContant)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QWidget(self.mainContant)
        self.mainPages.setObjectName(u"mainPages")
        self.verticalLayout_11 = QVBoxLayout(self.mainPages)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.mainPages_2 = QCustomQStackedWidget(self.mainPages)
        self.mainPages_2.setObjectName(u"mainPages_2")
        self.Home_page = QWidget()
        self.Home_page.setObjectName(u"Home_page")
        self.verticalLayout_38 = QVBoxLayout(self.Home_page)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.scrollArea = QScrollArea(self.Home_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -49, 1073, 3125))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.firstPageFrame = QWidget(self.scrollAreaWidgetContents)
        self.firstPageFrame.setObjectName(u"firstPageFrame")
        self.firstPageFrame.setMinimumSize(QSize(0, 700))
        self.firstPageFrame.setStyleSheet(u"QWidget#firstPageFrame {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0.2     #1a2c5e,   /* Deep navy (top) */\n"
"        stop: 0.5   #1f2c5f,   /* Mid transition blue */\n"
"        stop: 1    #402281    /* Rich deep royal purple (bottom) */\n"
"    );\n"
"    border: none;\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.firstPageFrame)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 9, -1, -1)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_7)

        self.label_6 = QLabel(self.firstPageFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(200, 200))
        self.label_6.setStyleSheet(u"border: 1px solid ;\n"
"    border-radius: 100px;\n"
"background-color: rgb(0, 0, 0);")
        self.label_6.setPixmap(QPixmap(u"../Qss/icons/me.png"))
        self.label_6.setScaledContents(True)

        self.verticalLayout_20.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_20.addItem(self.verticalSpacer_5)

        self.label_7 = QLabel(self.firstPageFrame)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setPointSize(24)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.label_18 = QLabel(self.firstPageFrame)
        self.label_18.setObjectName(u"label_18")
        font3 = QFont()
        font3.setPointSize(9)
        self.label_18.setFont(font3)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_18, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.label_19 = QLabel(self.firstPageFrame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(836, 56))
        self.label_19.setMaximumSize(QSize(836, 56))
        font4 = QFont()
        font4.setPointSize(16)
        self.label_19.setFont(font4)
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_19.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_19, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_10 = QWidget(self.firstPageFrame)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.pushButton_3 = QPushButton(self.widget_10)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(155, 20))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setStrikeOut(False)
        self.pushButton_3.setFont(font5)
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"\n"
"    color: palette(window-text);\n"
"    font: normal;\n"
"    text-align: left;\n"
"min-width:155;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/font_awesome_solid/icons/font_awesome/solid/location-dot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon16)

        self.horizontalLayout_15.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget_10)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(136, 20))
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"\n"
"    color: palette(window-text);\n"
"    font: normal;\n"
"    text-align: left;\n"
"	min-width:136;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/feather/icons/feather/calendar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon17)

        self.horizontalLayout_15.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(87, 20))
        self.pushButton.setFont(font5)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"\n"
"    color: palette(window-text);\n"
"    font: normal;\n"
"    text-align: left;\n"
"	min-width:87;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/feather/icons/feather/coffee.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon18)

        self.horizontalLayout_15.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)


        self.verticalLayout_20.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.firstPageFrame)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)

        self.HitHUP = QPushButton(self.widget_11)
        self.HitHUP.setObjectName(u"HitHUP")
        self.HitHUP.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color:#1c1531 ;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"    padding: 12px 24px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    margin: 5px;\n"
"    min-width: 160px;\n"
"    max-width: 200px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"")
        icon19 = QIcon()
        icon19.addFile(u":/font_awesome_brands/icons/font_awesome/brands/github.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HitHUP.setIcon(icon19)

        self.horizontalLayout_17.addWidget(self.HitHUP)

        self.pushButton_6 = QPushButton(self.widget_11)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #5b69ff, stop:1 #8a2be2);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 12px 24px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    margin: 5px;\n"
"    min-width: 160px;\n"
"    max-width: 200px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #6d7dfc, stop:1 #a333f5);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #4a58d8, stop:1 #701dd0);\n"
"    color: white;\n"
"}\n"
"")
        icon20 = QIcon()
        icon20.addFile(u":/feather/icons/feather/download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon20)

        self.horizontalLayout_17.addWidget(self.pushButton_6)

        self.contactMe = QPushButton(self.widget_11)
        self.contactMe.setObjectName(u"contactMe")
        self.contactMe.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #1a1a1a;\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"    padding: 12px 24px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    margin: 5px;\n"
"    min-width: 160px;\n"
"    max-width: 200px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"")
        icon21 = QIcon()
        icon21.addFile(u":/material_design/icons/material_design/email.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contactMe.setIcon(icon21)

        self.horizontalLayout_17.addWidget(self.contactMe)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)


        self.verticalLayout_20.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.firstPageFrame)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_5)

        self.GItH = QPushButton(self.widget_12)
        self.GItH.setObjectName(u"GItH")
        self.GItH.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        self.GItH.setIcon(icon19)
        self.GItH.setIconSize(QSize(18, 18))

        self.horizontalLayout_18.addWidget(self.GItH)

        self.Lin_2 = QPushButton(self.widget_12)
        self.Lin_2.setObjectName(u"Lin_2")
        self.Lin_2.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        icon22 = QIcon()
        icon22.addFile(u":/font_awesome_brands/icons/font_awesome/brands/linkedin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Lin_2.setIcon(icon22)
        self.Lin_2.setIconSize(QSize(18, 18))

        self.horizontalLayout_18.addWidget(self.Lin_2)

        self.Tweter = QPushButton(self.widget_12)
        self.Tweter.setObjectName(u"Tweter")
        self.Tweter.setStyleSheet(u"border: none;\n"
"background: transparent;\n"
"")
        icon23 = QIcon()
        icon23.addFile(u":/font_awesome_brands/icons/font_awesome/brands/x-twitter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Tweter.setIcon(icon23)
        self.Tweter.setIconSize(QSize(18, 18))

        self.horizontalLayout_18.addWidget(self.Tweter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)


        self.verticalLayout_20.addWidget(self.widget_12)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_8)


        self.verticalLayout_12.addWidget(self.firstPageFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.SecondPageFrame = QWidget(self.scrollAreaWidgetContents)
        self.SecondPageFrame.setObjectName(u"SecondPageFrame")
        self.SecondPageFrame.setMinimumSize(QSize(600, 600))
        self.SecondPageFrame.setStyleSheet(u"background-color: rgb(20, 22, 26);")
        self.gridLayout = QGridLayout(self.SecondPageFrame)
        self.gridLayout.setSpacing(25)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(50, 12, 50, 40)
        self.frame_1_1 = QFrame(self.SecondPageFrame)
        self.frame_1_1.setObjectName(u"frame_1_1")
        self.frame_1_1.setStyleSheet(u"QFrame#frame_1_1{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0     #24272e,  \n"
"        stop: 0.9     #1a1c21   \n"
"    );\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(70, 90, 160, 0.3); \n"
"    border-radius: 12px;\n"
"    padding: 3px;\n"
"    margin: 3px;\n"
"    color: white;\n"
"}\n"
"")
        self.frame_1_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_1_1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_13 = QWidget(self.frame_1_1)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(50, 50))
        self.widget_13.setStyleSheet(u"    border-radius: 12px;\n"
"background-color: rgb(50, 52, 85);\n"
"")
        self.gridLayout_8 = QGridLayout(self.widget_13)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_20 = QLabel(self.widget_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"background-color: rgb(50, 52, 85);\n"
"    border-radius: 12px;\n"
"\n"
"")
        self.label_20.setPixmap(QPixmap(u":/material_design/icons/material_design/fingerprint.png"))
        self.label_20.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_13, 0, 0, 1, 1)

        self.label_21 = QLabel(self.frame_1_1)
        self.label_21.setObjectName(u"label_21")
        font6 = QFont()
        font6.setPointSize(15)
        self.label_21.setFont(font6)
        self.label_21.setStyleSheet(u"background-color: transparent;")

        self.gridLayout_9.addWidget(self.label_21, 0, 1, 1, 1)

        self.label_22 = QLabel(self.frame_1_1)
        self.label_22.setObjectName(u"label_22")
        font7 = QFont()
        font7.setPointSize(11)
        self.label_22.setFont(font7)
        self.label_22.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(172, 176, 185);")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_22.setWordWrap(True)

        self.gridLayout_9.addWidget(self.label_22, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.frame_1_1, 2, 1, 1, 1)

        self.frame_0_1 = QFrame(self.SecondPageFrame)
        self.frame_0_1.setObjectName(u"frame_0_1")
        self.frame_0_1.setStyleSheet(u"QFrame#frame_0_1{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0     #24272e,  \n"
"        stop: 0.9     #1a1c21   \n"
"    );\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(70, 90, 160, 0.3); \n"
"    border-radius: 12px;\n"
"    padding: 3px;\n"
"    margin: 3px;\n"
"    color: white;\n"
"}\n"
"")
        self.frame_0_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_0_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_0_1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_14 = QWidget(self.frame_0_1)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(50, 50))
        self.widget_14.setStyleSheet(u"background-color: #494125;\n"
"    border-radius: 12px;\n"
"")
        self.gridLayout_4 = QGridLayout(self.widget_14)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_23 = QLabel(self.widget_14)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"background-color: #494125;\n"
"    border-radius: 12px;\n"
"\n"
"")
        self.label_23.setPixmap(QPixmap(u":/feather/icons/feather/target.png"))
        self.label_23.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_23, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_14, 0, 0, 1, 1)

        self.label_24 = QLabel(self.frame_0_1)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"background-color: transparent;")

        self.gridLayout_5.addWidget(self.label_24, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_25 = QLabel(self.frame_0_1)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font7)
        self.label_25.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(172, 176, 185);")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_25.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.frame_0_1, 1, 1, 1, 1)

        self.frame_0_0 = QFrame(self.SecondPageFrame)
        self.frame_0_0.setObjectName(u"frame_0_0")
        self.frame_0_0.setStyleSheet(u"QFrame#frame_0_0{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0     #24272e,  \n"
"        stop: 0.9     #1a1c21   \n"
"    );\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(70, 90, 160, 0.3); \n"
"    border-radius: 12px;\n"
"    padding: 3px;\n"
"    margin: 3px;\n"
"    color: white;\n"
"}\n"
"")
        self.frame_0_0.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_0_0.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_0_0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_15 = QWidget(self.frame_0_0)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMaximumSize(QSize(50, 50))
        self.widget_15.setStyleSheet(u"background-color: rgb(39, 56, 84);\n"
"    border-radius: 12px;\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget_15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_26 = QLabel(self.widget_15)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"background-color: rgb(39, 56, 84);\n"
"    border-radius: 12px;\n"
"\n"
"")
        self.label_26.setPixmap(QPixmap(u":/feather/icons/feather/user.png"))
        self.label_26.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_26, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_15, 0, 0, 1, 1)

        self.label_27 = QLabel(self.frame_0_0)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font6)
        self.label_27.setStyleSheet(u"background-color: transparent;")

        self.gridLayout_3.addWidget(self.label_27, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_28 = QLabel(self.frame_0_0)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font7)
        self.label_28.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(172, 176, 185);")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_28.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.frame_0_0, 1, 0, 1, 1)

        self.widget_16 = QWidget(self.SecondPageFrame)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_21 = QVBoxLayout(self.widget_16)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_29 = QLabel(self.widget_16)
        self.label_29.setObjectName(u"label_29")
        font8 = QFont()
        font8.setPointSize(19)
        self.label_29.setFont(font8)
        self.label_29.setStyleSheet(u"color: #4A6FEC;")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_29)

        self.label_30 = QLabel(self.widget_16)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font7)
        self.label_30.setStyleSheet(u"color: rgb(172, 176, 185);")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_30)


        self.gridLayout.addWidget(self.widget_16, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.frame_1_0 = QFrame(self.SecondPageFrame)
        self.frame_1_0.setObjectName(u"frame_1_0")
        self.frame_1_0.setStyleSheet(u"QFrame#frame_1_0{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0     #24272e,  \n"
"        stop: 0.9     #1a1c21   \n"
"    );\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(70, 90, 160, 0.3); \n"
"    border-radius: 12px;\n"
"    padding: 3px;\n"
"    margin: 3px;\n"
"    color: white;\n"
"}\n"
"")
        self.frame_1_0.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1_0.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_1_0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_17 = QWidget(self.frame_1_0)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMaximumSize(QSize(50, 50))
        self.widget_17.setStyleSheet(u"    border-radius: 12px;\n"
"background-color: rgb(29, 63, 41);\n"
"")
        self.gridLayout_6 = QGridLayout(self.widget_17)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_31 = QLabel(self.widget_17)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"background-color: rgb(29, 63, 41);\n"
"    border-radius: 12px;\n"
"\n"
"")
        self.label_31.setPixmap(QPixmap(u":/font_awesome_brands/icons/font_awesome/brands/canadian-maple-leaf.png"))
        self.label_31.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_31, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget_17, 0, 0, 1, 1)

        self.label_32 = QLabel(self.frame_1_0)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font6)
        self.label_32.setStyleSheet(u"background-color: transparent;")

        self.gridLayout_7.addWidget(self.label_32, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_33 = QLabel(self.frame_1_0)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font7)
        self.label_33.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(172, 176, 185);")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_33.setWordWrap(True)

        self.gridLayout_7.addWidget(self.label_33, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.frame_1_0, 2, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.SecondPageFrame)

        self.therdPageFrame = QWidget(self.scrollAreaWidgetContents)
        self.therdPageFrame.setObjectName(u"therdPageFrame")
        self.therdPageFrame.setMinimumSize(QSize(0, 400))
        self.therdPageFrame.setStyleSheet(u"background-color: rgb(29, 32, 37);")
        self.gridLayout_14 = QGridLayout(self.therdPageFrame)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(25)
        self.gridLayout_14.setContentsMargins(-1, -1, -1, 35)
        self.frame_0_3 = QFrame(self.therdPageFrame)
        self.frame_0_3.setObjectName(u"frame_0_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_0_3.sizePolicy().hasHeightForWidth())
        self.frame_0_3.setSizePolicy(sizePolicy4)
        self.frame_0_3.setMinimumSize(QSize(490, 0))
        self.frame_0_3.setMaximumSize(QSize(900, 200))
        self.frame_0_3.setStyleSheet(u"QFrame#frame_0_3{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0     #24272e,  \n"
"        stop: 0.9     #1a1c21   \n"
"    );\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(70, 90, 160, 0.3); \n"
"    border-radius: 12px;\n"
"    padding: 3px;\n"
"    margin: 3px;\n"
"    color: white;\n"
"}\n"
"")
        self.frame_0_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_0_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_0_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_19 = QPushButton(self.frame_0_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        font9 = QFont()
        font9.setPointSize(13)
        font9.setBold(True)
        self.pushButton_19.setFont(font9)
        self.pushButton_19.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_19.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(191, 146, 14);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")
        self.pushButton_19.setIconSize(QSize(30, 30))

        self.gridLayout_12.addWidget(self.pushButton_19, 2, 0, 1, 2)

        self.pushButton_18 = QPushButton(self.frame_0_3)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font9)
        self.pushButton_18.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_18.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(191, 146, 14);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")
        self.pushButton_18.setIconSize(QSize(30, 30))

        self.gridLayout_12.addWidget(self.pushButton_18, 2, 2, 1, 1)

        self.label_36 = QLabel(self.frame_0_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font7)
        self.label_36.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(172, 176, 185);")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_36.setWordWrap(True)

        self.gridLayout_12.addWidget(self.label_36, 1, 0, 1, 8, Qt.AlignmentFlag.AlignTop)

        self.pushButton_21 = QPushButton(self.frame_0_3)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setFont(font9)
        self.pushButton_21.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_21.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(191, 146, 14);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")
        self.pushButton_21.setIconSize(QSize(30, 30))

        self.gridLayout_12.addWidget(self.pushButton_21, 2, 5, 1, 3)

        self.widget_20 = QWidget(self.frame_0_3)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setStyleSheet(u"background-color: transparent;\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMaximumSize(QSize(50, 50))
        self.widget_21.setStyleSheet(u"background-color: #494125;\n"
"    border-radius: 12px;\n"
"")
        self.gridLayout_13 = QGridLayout(self.widget_21)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_37 = QLabel(self.widget_21)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"background-color: #494125;\n"
"    border-radius: 12px;\n"
"\n"
"")
        self.label_37.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/book-open.png"))
        self.label_37.setScaledContents(True)

        self.gridLayout_13.addWidget(self.label_37, 0, 0, 1, 1)


        self.horizontalLayout_19.addWidget(self.widget_21)

        self.label_38 = QLabel(self.widget_20)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font6)
        self.label_38.setStyleSheet(u"background-color: transparent;\n"
"margin-top: 9;")

        self.horizontalLayout_19.addWidget(self.label_38)


        self.gridLayout_12.addWidget(self.widget_20, 0, 0, 1, 4)

        self.pushButton_20 = QPushButton(self.frame_0_3)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font9)
        self.pushButton_20.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.pushButton_20.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(191, 146, 14);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")
        self.pushButton_20.setIconSize(QSize(30, 30))

        self.gridLayout_12.addWidget(self.pushButton_20, 2, 3, 1, 2)

        self.widget_19 = QWidget(self.frame_0_3)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 0))

        self.gridLayout_12.addWidget(self.widget_19, 3, 2, 1, 1)


        self.gridLayout_14.addWidget(self.frame_0_3, 1, 2, 1, 1)

        self.frame_0_2 = QFrame(self.therdPageFrame)
        self.frame_0_2.setObjectName(u"frame_0_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_0_2.sizePolicy().hasHeightForWidth())
        self.frame_0_2.setSizePolicy(sizePolicy5)
        self.frame_0_2.setMinimumSize(QSize(490, 0))
        self.frame_0_2.setMaximumSize(QSize(900, 200))
        self.frame_0_2.setStyleSheet(u"QFrame#frame_0_2{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0     #24272e,  \n"
"        stop: 0.9     #1a1c21   \n"
"    );\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(70, 90, 160, 0.3); \n"
"    border-radius: 12px;\n"
"    padding: 3px;\n"
"    margin: 3px;\n"
"    color: white;\n"
"}\n"
"")
        self.frame_0_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_0_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_0_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_10.setHorizontalSpacing(0)
        self.gridLayout_10.setVerticalSpacing(6)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_9, 4, 0, 1, 1)

        self.widget_22 = QWidget(self.frame_0_2)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(50, 50))
        self.widget_22.setStyleSheet(u"background-color: rgb(39, 56, 84);\n"
"    border-radius: 12px;\n"
"")
        self.gridLayout_11 = QGridLayout(self.widget_22)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_39 = QLabel(self.widget_22)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"background-color: rgb(39, 56, 84);\n"
"    border-radius: 12px;\n"
"\n"
"")
        self.label_39.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/code.png"))
        self.label_39.setScaledContents(True)

        self.gridLayout_11.addWidget(self.label_39, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.widget_22, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.frame_0_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font9)
        self.pushButton_13.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(28, 154, 74);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_13, 3, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_0_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font9)
        self.pushButton_11.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(28, 154, 74);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.label_40 = QLabel(self.frame_0_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font6)
        self.label_40.setStyleSheet(u"background-color: transparent;\n"
"margin-top: 9;")

        self.gridLayout_10.addWidget(self.label_40, 0, 1, 1, 3)

        self.pushButton_26 = QPushButton(self.frame_0_2)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setFont(font9)
        self.pushButton_26.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(28, 154, 74);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_26, 2, 3, 1, 1)

        self.label_41 = QLabel(self.frame_0_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font7)
        self.label_41.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(172, 176, 185);")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_41.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_41, 1, 0, 1, 5, Qt.AlignmentFlag.AlignTop)

        self.pushButton_10 = QPushButton(self.frame_0_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font9)
        self.pushButton_10.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(28, 154, 74);\n"
"    color: white;\n"
"	margin:5px;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	max-height:25;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_10, 2, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_0_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font9)
        self.pushButton_12.setStyleSheet(u"\n"
"QPushButton{\n"
"    background-color: rgb(28, 154, 74);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_12, 3, 0, 1, 1)

        self.pushButton_27 = QPushButton(self.frame_0_2)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setFont(font9)
        self.pushButton_27.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(28, 154, 74);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_27, 2, 4, 1, 1)

        self.pushButton_28 = QPushButton(self.frame_0_2)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setFont(font9)
        self.pushButton_28.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(28, 154, 74);\n"
"    color: white;\n"
"    border: 1px solid #333;\n"
"    border-radius: 10px;\n"
"	margin:5px;\n"
"\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2a2a2a;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_10.addWidget(self.pushButton_28, 2, 1, 1, 1)


        self.gridLayout_14.addWidget(self.frame_0_2, 1, 1, 1, 1)

        self.widget_18 = QWidget(self.therdPageFrame)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_22 = QVBoxLayout(self.widget_18)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_34 = QLabel(self.widget_18)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font8)
        self.label_34.setStyleSheet(u"color: #4A6FEC;")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_34, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.label_35 = QLabel(self.widget_18)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font7)
        self.label_35.setStyleSheet(u"color: rgb(172, 176, 185);")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_35, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_14.addWidget(self.widget_18, 0, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_10, 1, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_11, 1, 3, 1, 1)


        self.verticalLayout_12.addWidget(self.therdPageFrame)

        self.ForthPageFrame = QWidget(self.scrollAreaWidgetContents)
        self.ForthPageFrame.setObjectName(u"ForthPageFrame")
        self.ForthPageFrame.setStyleSheet(u"background-color: rgb(20, 22, 26);")
        self.verticalLayout_23 = QVBoxLayout(self.ForthPageFrame)
        self.verticalLayout_23.setSpacing(30)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(100, 16, 100, 16)
        self.widget_23 = QWidget(self.ForthPageFrame)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_24 = QVBoxLayout(self.widget_23)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_42 = QLabel(self.widget_23)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font8)
        self.label_42.setStyleSheet(u"color: #4A6FEC;")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_42)

        self.label_43 = QLabel(self.widget_23)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font7)
        self.label_43.setStyleSheet(u"color: rgb(172, 176, 185);")
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_43)

        self.label_44 = QLabel(self.widget_23)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font7)
        self.label_44.setStyleSheet(u"color: rgb(172, 176, 185);")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_44, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_23.addWidget(self.widget_23, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_24 = QWidget(self.ForthPageFrame)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setStyleSheet(u"QWidget#widget_24{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0.2     #24272e,  \n"
"        stop: 0.9     #1a1c21   \n"
"    );\n"
"    border: 1px solid rgba(70, 90, 160, 0.3); \n"
"    border-radius: 12px;\n"
"\n"
"    color: white;\n"
"}\n"
"")
        self.gridLayout_15 = QGridLayout(self.widget_24)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.pushButton_29 = QPushButton(self.widget_24)
        self.pushButton_29.setObjectName(u"pushButton_29")
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        self.pushButton_29.setFont(font10)
        self.pushButton_29.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_15.addWidget(self.pushButton_29, 2, 1, 1, 1)

        self.widget_25 = QWidget(self.widget_24)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_25 = QVBoxLayout(self.widget_25)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.pushButton_30 = QPushButton(self.widget_25)
        self.pushButton_30.setObjectName(u"pushButton_30")
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(True)
        font11.setItalic(False)
        font11.setUnderline(False)
        font11.setStrikeOut(False)
        font11.setKerning(False)
        self.pushButton_30.setFont(font11)
        self.pushButton_30.setStyleSheet(u"\n"
"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"	color: rgb(255, 255, 255);\n"
"   \n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"	 color: #4A6FEC;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")

        self.verticalLayout_25.addWidget(self.pushButton_30)

        self.label_45 = QLabel(self.widget_25)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_25.addWidget(self.label_45)


        self.gridLayout_15.addWidget(self.widget_25, 0, 0, 1, 5)

        self.label_46 = QLabel(self.widget_24)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font7)
        self.label_46.setStyleSheet(u"background-color: transparent;\n"
"    margin-left: 5px;\n"
"    margin-bottom: 5px;\n"
"\n"
"\n"
"")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_46.setWordWrap(True)

        self.gridLayout_15.addWidget(self.label_46, 1, 0, 1, 7)

        self.pushButton_31 = QPushButton(self.widget_24)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setFont(font10)
        self.pushButton_31.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_15.addWidget(self.pushButton_31, 2, 2, 1, 1)

        self.pushButton_32 = QPushButton(self.widget_24)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setFont(font9)
        self.pushButton_32.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_15.addWidget(self.pushButton_32, 2, 0, 1, 1)

        self.pushButton_33 = QPushButton(self.widget_24)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setFont(font10)
        self.pushButton_33.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_15.addWidget(self.pushButton_33, 2, 4, 1, 1)

        self.pushButton_34 = QPushButton(self.widget_24)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setFont(font10)
        self.pushButton_34.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_15.addWidget(self.pushButton_34, 2, 3, 1, 1)

        self.widget_26 = QWidget(self.widget_24)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_26 = QVBoxLayout(self.widget_26)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.pushButton_35 = QPushButton(self.widget_26)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setFont(font5)
        self.pushButton_35.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"	color: rgb(172, 176, 185);\n"
"    margin: 0;\n"
"\n"
"    font: normal;\n"
"    text-align: right;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pushButton_35.setIcon(icon17)

        self.verticalLayout_26.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.widget_26)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setFont(font5)
        self.pushButton_36.setMouseTracking(True)
        self.pushButton_36.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.pushButton_36.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"	color: rgb(172, 176, 185);\n"
"    margin: 0;\n"
"\n"
"    font: normal;\n"
"    text-align: right;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pushButton_36.setIcon(icon16)

        self.verticalLayout_26.addWidget(self.pushButton_36)


        self.gridLayout_15.addWidget(self.widget_26, 0, 6, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_7, 2, 6, 1, 1)


        self.verticalLayout_23.addWidget(self.widget_24)

        self.widget_27 = QWidget(self.ForthPageFrame)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setStyleSheet(u"QWidget#widget_27{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0.2     #24272e,  \n"
"        stop: 0.9     #1a1c21   \n"
"    );\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(70, 90, 160, 0.3); \n"
"    border-radius: 12px;\n"
"\n"
"    color: white;\n"
"}\n"
"")
        self.gridLayout_16 = QGridLayout(self.widget_27)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pushButton_37 = QPushButton(self.widget_27)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setFont(font10)
        self.pushButton_37.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_16.addWidget(self.pushButton_37, 2, 2, 1, 1)

        self.pushButton_38 = QPushButton(self.widget_27)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setFont(font9)
        self.pushButton_38.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_16.addWidget(self.pushButton_38, 2, 0, 1, 1)

        self.pushButton_39 = QPushButton(self.widget_27)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setFont(font10)
        self.pushButton_39.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_16.addWidget(self.pushButton_39, 2, 1, 1, 1)

        self.pushButton_40 = QPushButton(self.widget_27)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setFont(font10)
        self.pushButton_40.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_16.addWidget(self.pushButton_40, 2, 4, 1, 1)

        self.pushButton_41 = QPushButton(self.widget_27)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setFont(font10)
        self.pushButton_41.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_16.addWidget(self.pushButton_41, 2, 3, 1, 1)

        self.widget_28 = QWidget(self.widget_27)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_27 = QVBoxLayout(self.widget_28)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.pushButton_42 = QPushButton(self.widget_28)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setFont(font5)
        self.pushButton_42.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"	color: rgb(172, 176, 185);\n"
"    margin: 0;\n"
"\n"
"    font: normal;\n"
"    text-align: right;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pushButton_42.setIcon(icon17)

        self.verticalLayout_27.addWidget(self.pushButton_42)

        self.pushButton_43 = QPushButton(self.widget_28)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setFont(font5)
        self.pushButton_43.setMouseTracking(True)
        self.pushButton_43.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.pushButton_43.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"	color: rgb(172, 176, 185);\n"
"    margin: 0;\n"
"\n"
"    font: normal;\n"
"    text-align: right;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pushButton_43.setIcon(icon16)

        self.verticalLayout_27.addWidget(self.pushButton_43)


        self.gridLayout_16.addWidget(self.widget_28, 0, 5, 1, 1)

        self.widget_29 = QWidget(self.widget_27)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_28 = QVBoxLayout(self.widget_29)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.pushButton_44 = QPushButton(self.widget_29)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setFont(font11)
        self.pushButton_44.setStyleSheet(u"\n"
"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"	color: rgb(255, 255, 255);\n"
"   \n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"	 color: #4A6FEC;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")

        self.verticalLayout_28.addWidget(self.pushButton_44)

        self.label_47 = QLabel(self.widget_29)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_28.addWidget(self.label_47)


        self.gridLayout_16.addWidget(self.widget_29, 0, 0, 1, 5)

        self.label_48 = QLabel(self.widget_27)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font7)
        self.label_48.setStyleSheet(u"background-color: transparent;\n"
"    margin-left: 5px;\n"
"    margin-bottom: 5px;\n"
"\n"
"\n"
"")
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_48.setWordWrap(True)

        self.gridLayout_16.addWidget(self.label_48, 1, 0, 1, 6)

        self.horizontalSpacer_8 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_8, 2, 5, 1, 1)


        self.verticalLayout_23.addWidget(self.widget_27)

        self.widget_30 = QWidget(self.ForthPageFrame)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setStyleSheet(u"QWidget#widget_30{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0,\n"
"        x2: 0, y2: 1,\n"
"        stop: 0.2     #24272e,  \n"
"        stop: 0.9     #1a1c21   \n"
"    );\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(70, 90, 160, 0.3); \n"
"    border-radius: 12px;\n"
"\n"
"    color: white;\n"
"}\n"
"")
        self.gridLayout_17 = QGridLayout(self.widget_30)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.widget_31)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.pushButton_45 = QPushButton(self.widget_31)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setFont(font11)
        self.pushButton_45.setStyleSheet(u"\n"
"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"	color: rgb(255, 255, 255);\n"
"   \n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"	 color: #4A6FEC;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")

        self.verticalLayout_29.addWidget(self.pushButton_45)

        self.label_49 = QLabel(self.widget_31)
        self.label_49.setObjectName(u"label_49")

        self.verticalLayout_29.addWidget(self.label_49)


        self.gridLayout_17.addWidget(self.widget_31, 0, 0, 1, 5)

        self.widget_32 = QWidget(self.widget_30)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_30 = QVBoxLayout(self.widget_32)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.pushButton_46 = QPushButton(self.widget_32)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setFont(font5)
        self.pushButton_46.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"	color: rgb(172, 176, 185);\n"
"    margin: 0;\n"
"\n"
"    font: normal;\n"
"    text-align: right;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pushButton_46.setIcon(icon17)

        self.verticalLayout_30.addWidget(self.pushButton_46)

        self.pushButton_47 = QPushButton(self.widget_32)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setFont(font5)
        self.pushButton_47.setMouseTracking(True)
        self.pushButton_47.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.pushButton_47.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"	color: rgb(172, 176, 185);\n"
"    margin: 0;\n"
"\n"
"    font: normal;\n"
"    text-align: right;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.pushButton_47.setIcon(icon16)

        self.verticalLayout_30.addWidget(self.pushButton_47)


        self.gridLayout_17.addWidget(self.widget_32, 0, 5, 1, 1)

        self.label_50 = QLabel(self.widget_30)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font7)
        self.label_50.setStyleSheet(u"background-color: transparent;\n"
"    margin-left: 5px;\n"
"    margin-bottom: 5px;\n"
"\n"
"\n"
"")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_50.setWordWrap(True)

        self.gridLayout_17.addWidget(self.label_50, 1, 0, 1, 6)

        self.pushButton_48 = QPushButton(self.widget_30)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setFont(font9)
        self.pushButton_48.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_17.addWidget(self.pushButton_48, 2, 0, 1, 1)

        self.pushButton_49 = QPushButton(self.widget_30)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setFont(font10)
        self.pushButton_49.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_17.addWidget(self.pushButton_49, 2, 1, 1, 1)

        self.pushButton_50 = QPushButton(self.widget_30)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setFont(font10)
        self.pushButton_50.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_17.addWidget(self.pushButton_50, 2, 2, 1, 1)

        self.pushButton_51 = QPushButton(self.widget_30)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setFont(font10)
        self.pushButton_51.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_17.addWidget(self.pushButton_51, 2, 3, 1, 1)

        self.pushButton_52 = QPushButton(self.widget_30)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setFont(font10)
        self.pushButton_52.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(32, 39, 61);\n"
"    color: white;\n"
"    border: 1px solid rgb(32, 37, 147);\n"
"    border-radius: 12px;\n"
"\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(57, 83, 255);\n"
"    border-color: #444;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222;\n"
"    border-color: #444;\n"
"    color: white;\n"
"}")

        self.gridLayout_17.addWidget(self.pushButton_52, 2, 4, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(200, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_9, 2, 5, 1, 1)


        self.verticalLayout_23.addWidget(self.widget_30)


        self.verticalLayout_12.addWidget(self.ForthPageFrame)

        self.fnalPageFrame = QWidget(self.scrollAreaWidgetContents)
        self.fnalPageFrame.setObjectName(u"fnalPageFrame")
        self.fnalPageFrame.setStyleSheet(u"background-color: rgb(29, 32, 37);")
        self.gridLayout_18 = QGridLayout(self.fnalPageFrame)
        self.gridLayout_18.setSpacing(20)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(20, 20, 20, 20)
        self.frame_6 = QFrame(self.fnalPageFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(397, 500))
        self.frame_6.setStyleSheet(u"QFrame#frame_6{\n"
"background-color: rgb(20, 22, 26);\n"
" border: 1px solid #1f204b;\n"
"    border-radius: 12px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(20, 20, 20, 20)
        self.label_51 = QLabel(self.frame_6)
        self.label_51.setObjectName(u"label_51")
        font12 = QFont()
        font12.setPointSize(12)
        self.label_51.setFont(font12)
        self.label_51.setStyleSheet(u"background-color: transparent;\n"
"")

        self.gridLayout_19.addWidget(self.label_51, 0, 0, 1, 1)

        self.widget_33 = QWidget(self.frame_6)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_31 = QVBoxLayout(self.widget_33)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_52 = QLabel(self.widget_33)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font1)

        self.verticalLayout_31.addWidget(self.label_52)

        self.Quickname = QLineEdit(self.widget_33)
        self.Quickname.setObjectName(u"Quickname")
        self.Quickname.setMinimumSize(QSize(40, 62))
        self.Quickname.setStyleSheet(u"QLineEdit {\n"
"	\n"
"	background-color: rgb(35, 39, 46);\n"
"    color: white;\n"
"    border: 1px solid rgb(226, 226, 240);              /* Thin dark border */\n"
"    border-radius: 8px;\n"
"    padding: 10px 14px;\n"
"    font-size: 14px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #4A6FEC;               /* Blue on hover */\n"
"    box-shadow: 0 0 8px rgba(74, 111, 236, 0.2);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4A6FEC;\n"
"    outline: none;\n"
"    box-shadow: 0 0 12px rgba(74, 111, 236, 0.3);\n"
"}")
        self.Quickname.setClearButtonEnabled(True)

        self.verticalLayout_31.addWidget(self.Quickname)


        self.gridLayout_19.addWidget(self.widget_33, 1, 0, 1, 1)

        self.widget_34 = QWidget(self.frame_6)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_32 = QVBoxLayout(self.widget_34)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(-1, 0, -1, 0)
        self.label_53 = QLabel(self.widget_34)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font1)

        self.verticalLayout_32.addWidget(self.label_53)

        self.Quickemail = QLineEdit(self.widget_34)
        self.Quickemail.setObjectName(u"Quickemail")
        self.Quickemail.setMinimumSize(QSize(0, 62))
        self.Quickemail.setStyleSheet(u"QLineEdit {\n"
"	\n"
"	background-color: rgb(35, 39, 46);\n"
"    color: white;\n"
"    border: 1px solid rgb(226, 226, 240);              /* Thin dark border */\n"
"    border-radius: 8px;\n"
"    padding: 10px 14px;\n"
"    font-size: 14px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: #4A6FEC;               /* Blue on hover */\n"
"    box-shadow: 0 0 8px rgba(74, 111, 236, 0.2);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4A6FEC;\n"
"    outline: none;\n"
"    box-shadow: 0 0 12px rgba(74, 111, 236, 0.3);\n"
"}")

        self.verticalLayout_32.addWidget(self.Quickemail)


        self.gridLayout_19.addWidget(self.widget_34, 2, 0, 1, 1)

        self.widget_35 = QWidget(self.frame_6)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_33 = QVBoxLayout(self.widget_35)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_54 = QLabel(self.widget_35)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font1)

        self.verticalLayout_33.addWidget(self.label_54)

        self.Quickmasseg = QPlainTextEdit(self.widget_35)
        self.Quickmasseg.setObjectName(u"Quickmasseg")
        self.Quickmasseg.setStyleSheet(u"QPlainTextEdit {\n"
"	\n"
"	background-color: rgb(35, 39, 46);\n"
"    color: white;\n"
"    border: 1px solid rgb(226, 226, 240);              /* Thin dark border */\n"
"    border-radius: 8px;\n"
"    padding: 10px 14px;\n"
"    font-size: 14px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    border-color: #4A6FEC;               /* Blue on hover */\n"
"    box-shadow: 0 0 8px rgba(74, 111, 236, 0.2);\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4A6FEC;\n"
"    outline: none;\n"
"    box-shadow: 0 0 12px rgba(74, 111, 236, 0.3);\n"
"}")

        self.verticalLayout_33.addWidget(self.Quickmasseg)

        self.sendBtn = QPushButton(self.widget_35)
        self.sendBtn.setObjectName(u"sendBtn")
        self.sendBtn.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #5b69ff, stop:1 #8a2be2);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 12px 24px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    margin: 5px;\n"
"    margin-left: 50px;\n"
"    margin-top: 20px;\n"
"\n"
"    min-width: 160px;\n"
"    max-width: 200px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #6d7dfc, stop:1 #a333f5);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #4a58d8, stop:1 #701dd0);\n"
"    color: white;\n"
"}\n"
"")
        icon24 = QIcon()
        icon24.addFile(u":/feather/icons/feather/send.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sendBtn.setIcon(icon24)

        self.verticalLayout_33.addWidget(self.sendBtn)


        self.gridLayout_19.addWidget(self.widget_35, 3, 0, 1, 1)


        self.gridLayout_18.addWidget(self.frame_6, 1, 1, 1, 1)

        self.widget_36 = QWidget(self.fnalPageFrame)
        self.widget_36.setObjectName(u"widget_36")
        self.verticalLayout_34 = QVBoxLayout(self.widget_36)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_55 = QLabel(self.widget_36)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font8)
        self.label_55.setStyleSheet(u"color: #4A6FEC;")
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_55, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_56 = QLabel(self.widget_36)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font7)
        self.label_56.setStyleSheet(u"color: rgb(172, 176, 185);")
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_56, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_18.addWidget(self.widget_36, 0, 0, 1, 2, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.frame_7 = QFrame(self.fnalPageFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 500))
        self.frame_7.setMaximumSize(QSize(399, 500))
        self.frame_7.setStyleSheet(u"QFrame#frame_7{\n"
"background-color: rgb(20, 22, 26);\n"
" border: 1px solid #1f204b;\n"
"    border-radius: 12px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_7)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.widget_37 = QWidget(self.frame_7)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_36 = QVBoxLayout(self.widget_37)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_57 = QLabel(self.widget_37)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font12)
        self.label_57.setStyleSheet(u"background-color: transparent;\n"
"    margin-left: 10px;\n"
"    margin-top: 10px;\n"
"")

        self.verticalLayout_36.addWidget(self.label_57)

        self.widget_38 = QWidget(self.widget_37)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setStyleSheet(u"background-color: transparent;\n"
"")
        self.verticalLayout_37 = QVBoxLayout(self.widget_38)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.Email = QPushButton(self.widget_38)
        self.Email.setObjectName(u"Email")
        font13 = QFont()
        font13.setPointSize(10)
        font13.setBold(False)
        font13.setItalic(False)
        font13.setUnderline(False)
        font13.setStrikeOut(False)
        self.Email.setFont(font13)
        self.Email.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"	color: rgb(192, 197, 207);\n"
"\n"
"    font: normal;\n"
"    text-align: left;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    color: #4A6FEC;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"	color: #4A6FEC;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.Email.setIcon(icon21)
        self.Email.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.Email)

        self.Phone = QPushButton(self.widget_38)
        self.Phone.setObjectName(u"Phone")
        self.Phone.setFont(font13)
        self.Phone.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"\n"
"    	color: rgb(192, 197, 207);\n"
"\n"
"    font: normal;\n"
"    text-align: left;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    color: #4A6FEC;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"	color: #4A6FEC;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/font_awesome_solid/icons/font_awesome/solid/phone.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Phone.setIcon(icon25)
        self.Phone.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.Phone)

        self.location = QPushButton(self.widget_38)
        self.location.setObjectName(u"location")
        self.location.setFont(font13)
        self.location.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"color: rgb(192, 197, 207);\n"
"    font: normal;\n"
"    text-align: left;\n"
"    text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    color: #4A6FEC;\n"
"}\n"
"QPushButton:pressed {\n"
"    background: transparent;\n"
"	color: #4A6FEC;\n"
"    border: none;\n"
"    padding: 0;\n"
"}\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"}")
        self.location.setIcon(icon16)
        self.location.setIconSize(QSize(20, 20))

        self.verticalLayout_37.addWidget(self.location)


        self.verticalLayout_36.addWidget(self.widget_38)

        self.widget_39 = QWidget(self.widget_37)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setStyleSheet(u"background-color: transparent;\n"
"")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.gitHup = QPushButton(self.widget_39)
        self.gitHup.setObjectName(u"gitHup")
        self.gitHup.setStyleSheet(u"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #6d7dfc, stop:1 #a333f5);\n"
"border:none;\n"
"border-radius:9px\n"
"}")
        self.gitHup.setIcon(icon19)
        self.gitHup.setIconSize(QSize(26, 26))

        self.horizontalLayout_20.addWidget(self.gitHup)

        self.Lin = QPushButton(self.widget_39)
        self.Lin.setObjectName(u"Lin")
        self.Lin.setStyleSheet(u"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #6d7dfc, stop:1 #a333f5);\n"
"border:none;\n"
"border-radius:9px\n"
"}")
        self.Lin.setIcon(icon22)
        self.Lin.setIconSize(QSize(26, 26))

        self.horizontalLayout_20.addWidget(self.Lin)

        self.Twiter = QPushButton(self.widget_39)
        self.Twiter.setObjectName(u"Twiter")
        self.Twiter.setStyleSheet(u"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
"                                stop:0 #6d7dfc, stop:1 #a333f5);\n"
"border:none;\n"
"border-radius:9px\n"
"}")
        self.Twiter.setIcon(icon23)
        self.Twiter.setIconSize(QSize(26, 26))

        self.horizontalLayout_20.addWidget(self.Twiter)


        self.verticalLayout_36.addWidget(self.widget_39, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_35.addWidget(self.widget_37)

        self.verticalSpacer_6 = QSpacerItem(5, 220, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_35.addItem(self.verticalSpacer_6)


        self.gridLayout_18.addWidget(self.frame_7, 1, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.fnalPageFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_38.addWidget(self.scrollArea)

        self.mainPages_2.addWidget(self.Home_page)
        self.StatisPage = QWidget()
        self.StatisPage.setObjectName(u"StatisPage")
        self.verticalLayout_13 = QVBoxLayout(self.StatisPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_9 = QLabel(self.StatisPage)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_13.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.mainPages_2.addWidget(self.StatisPage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.horizontalLayout_11 = QHBoxLayout(self.reportsPage)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.reportsPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10.setWordWrap(True)

        self.horizontalLayout_11.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.mainPages_2.addWidget(self.reportsPage)
        self.revewBage = QWidget()
        self.revewBage.setObjectName(u"revewBage")
        self.verticalLayout_14 = QVBoxLayout(self.revewBage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_11 = QLabel(self.revewBage)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_14.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.mainPages_2.addWidget(self.revewBage)

        self.verticalLayout_11.addWidget(self.mainPages_2)


        self.horizontalLayout_10.addWidget(self.mainPages)

        self.rightMenu = QCustomSlideMenu(self.mainContant)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_15 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.widget_7 = QWidget(self.rightMenu)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.closeRightMenuBtn = QPushButton(self.widget_7)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeRightMenuBtn.setIcon(icon8)

        self.horizontalLayout_12.addWidget(self.closeRightMenuBtn)


        self.verticalLayout_15.addWidget(self.widget_7)

        self.rightMenuPages = QCustomQStackedWidget(self.rightMenu)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.rightMenuPages.setMaximumSize(QSize(200, 16777215))
        font14 = QFont()
        font14.setPointSize(10)
        font14.setBold(False)
        self.rightMenuPages.setFont(font14)
        self.notifationPage = QWidget()
        self.notifationPage.setObjectName(u"notifationPage")
        self.verticalLayout_16 = QVBoxLayout(self.notifationPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_13 = QLabel(self.notifationPage)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_16.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.rightMenuPages.addWidget(self.notifationPage)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"ProfilePage")
        self.verticalLayout_19 = QVBoxLayout(self.ProfilePage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_16 = QLabel(self.ProfilePage)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setMinimumSize(QSize(151, 151))
        self.label_16.setMaximumSize(QSize(151, 151))
        self.label_16.setStyleSheet(u"border: 3px solid ;\n"
"    border-radius: 74px;\n"
"    background: transparent;\n"
"")
        self.label_16.setPixmap(QPixmap(u"../Qss/icons/me.png"))
        self.label_16.setScaledContents(True)

        self.verticalLayout_19.addWidget(self.label_16)

        self.label_58 = QLabel(self.ProfilePage)
        self.label_58.setObjectName(u"label_58")
        font15 = QFont()
        font15.setPointSize(17)
        font15.setBold(False)
        font15.setUnderline(False)
        self.label_58.setFont(font15)
        self.label_58.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_58, 0, Qt.AlignmentFlag.AlignTop)

        self.rightMenuPages.addWidget(self.ProfilePage)
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.verticalLayout_18 = QVBoxLayout(self.morePage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_14 = QLabel(self.morePage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(200, 16777215))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.rightMenuPages.addWidget(self.morePage)

        self.verticalLayout_15.addWidget(self.rightMenuPages, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_10.addWidget(self.rightMenu)


        self.verticalLayout_10.addWidget(self.mainContant)

        self.fotter = QWidget(self.MainBody)
        self.fotter.setObjectName(u"fotter")
        self.fotter.setMinimumSize(QSize(767, 0))
        self.horizontalLayout_5 = QHBoxLayout(self.fotter)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 0, 5)
        self.EmailBtn = QPushButton(self.fotter)
        self.EmailBtn.setObjectName(u"EmailBtn")
        sizePolicy2.setHeightForWidth(self.EmailBtn.sizePolicy().hasHeightForWidth())
        self.EmailBtn.setSizePolicy(sizePolicy2)
        self.EmailBtn.setMaximumSize(QSize(180, 16777215))
        self.EmailBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.EmailBtn.setIcon(icon21)

        self.horizontalLayout_5.addWidget(self.EmailBtn, 0, Qt.AlignmentFlag.AlignBottom)

        self.frame_3 = QFrame(self.fotter)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_16.addWidget(self.label_17)

        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_16.addWidget(self.progressBar)


        self.horizontalLayout_5.addWidget(self.frame_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.sizeGrip = QFrame(self.fotter)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(15, 15))
        self.sizeGrip.setMaximumSize(QSize(15, 15))
        self.sizeGrip.setCursor(QCursor(Qt.CursorShape.SizeFDiagCursor))
        self.sizeGrip.setFrameShape(QFrame.Shape.NoFrame)
        self.sizeGrip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.sizeGrip, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_10.addWidget(self.fotter, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.MainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(2)
        self.mainPages_2.setCurrentIndex(0)
        self.rightMenuPages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
#if QT_CONFIG(tooltip)
        self.dataBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Statistics", None))
#endif // QT_CONFIG(tooltip)
        self.dataBtn.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
#if QT_CONFIG(tooltip)
        self.graphsBtn.setToolTip(QCoreApplication.translate("MainWindow", u" Reviews ", None))
#endif // QT_CONFIG(tooltip)
        self.graphsBtn.setText(QCoreApplication.translate("MainWindow", u" Reviews ", None))
#if QT_CONFIG(tooltip)
        self.reportsBtn.setToolTip(QCoreApplication.translate("MainWindow", u" Reports", None))
#endif // QT_CONFIG(tooltip)
        self.reportsBtn.setText(QCoreApplication.translate("MainWindow", u" Reports", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u" Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u" Information", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u" Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u" Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u" Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center Menu", None))
        self.closeCenterMenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"This app was made by Mohammed Awad  using QT desinger & PySide6 & Python", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Help Your Self ", None))
        self.TitelText.setText(QCoreApplication.translate("MainWindow", u"My Personal Profile", None))
#if QT_CONFIG(tooltip)
        self.notifaction.setToolTip(QCoreApplication.translate("MainWindow", u"Notifictaion", None))
#endif // QT_CONFIG(tooltip)
        self.notifaction.setText("")
#if QT_CONFIG(tooltip)
        self.more.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.more.setText("")
#if QT_CONFIG(tooltip)
        self.profileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"It's me mario", None))
#endif // QT_CONFIG(tooltip)
        self.profileBtn.setText("")
        self.label_8.setText("")
        self.serchlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
#if QT_CONFIG(tooltip)
        self.searchResaltBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Search", None))
#endif // QT_CONFIG(tooltip)
        self.searchResaltBtn.setText("")
#if QT_CONFIG(tooltip)
        self.MinmizeBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.MinmizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.MaxmizeBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.MaxmizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<strong>Mohammed Awad</strong>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:700;\">Software Engineer</span></h1></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Passionate developer with <span style=\" font-weight:700; color:#20764b;\">1+ year</span> of experience building desktop applications, now expanding into <span style=\" color:#d9a60c;\">modern web development</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Kafr El Sheikh, Egypt", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Available for hire ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Tea addict", None))
        self.HitHUP.setText(QCoreApplication.translate("MainWindow", u"View Projects", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Download Resume", None))
        self.contactMe.setText(QCoreApplication.translate("MainWindow", u"Contact me", None))
        self.GItH.setText("")
        self.Lin_2.setText("")
        self.Tweter.setText("")
        self.label_20.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:large; font-weight:700;\">My Philosophy</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"I believe in Learn something about everything and everything about one thing. from front-end design to backend systems, from databases to DevOps to understand how the full stack comes together, But I also dive deep into my specialist skills.", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Goals</span></h3></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Currently focused on mastering modern web technologies to become a full-stack developer. My goal is to bridge the gap between desktop and web applications, creating seamless cross-platform experiences using technologies like Electron.", None))
        self.label_26.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">My Story</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Started my programming journey 1 year ago with a passion for solving real world problems. I've learned C++ Python, My SQL, SQLite, and more,and now I'm expand into web development to create more accessible and interactive user experiences.", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<strong>About Me</strong>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"My journey, Goals, and what drives me as a developer", None))
        self.label_31.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Learning plan</span></h3></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Technology never stands still \u2014 and neither do I. I love diving into new frameworks, exploring emerging tools, and staying ahead of the curve. Every project is a chance to learn, grow, and become a better programmer.", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"JavaScript", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"CSS", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Web technologies I'm actively learning to expand my skill set", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Electron", None))
        self.label_37.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:large; font-weight:700;\">Learning Journey</span></p></body></html>", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"React", None))
        self.label_39.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"My SQL", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"SQLite", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Current Mastery</span></h3></body></html>", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"PyQt5", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Technologies I'm proficient in and use for professional development", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"C++", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"CSS", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PySide6", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Technical Experience</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"What I have learned so far and what I intend to learn", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Professional Experienc</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"My career progression and key achievements in software development", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" vertical-align:sub;\">~This section is from a future perspective~</span></p></body></html>", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"My SQL", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Senior Software Developer", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">TechCorp Solutions</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Led development of enterprise desktop applications using C++ and Python. Designed and implemented database architectures with MySQL and SQLite. Mentored junior developers and established best practices for code quality.", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"C++", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"GIT", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"PyQt5", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"2025-2027", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"San Francisco", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"My SQL", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"PySide6", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Docker", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"SQLite", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"2027-2030", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"Remote", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"Software Engineer", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">DataFlow Systems</span></p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Developed data processing applications and GUI interfaces using Python and PyQt5. Optimized database queries and improved application performance by 40%. Collaborated with cross-functional teams on feature development.", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"Software Engineer", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">TechCorp Solutions</span></p></body></html>", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"2030-Present", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"San Andreas ", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Built end-to-end desktop applications with Python and PySide6, from responsive GUIs to efficient data handling logic. Enhanced system performance through query optimization and caching strategies, achieving a 40% speed improvement. Delivered features through agile collaboration with product and QA teams.", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"C++", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"SQLite", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"PySide6", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"Linux", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Quick Message</span></h3></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.Quickname.setText("")
        self.Quickname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Name", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Quickemail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"YourEmail@example.org", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.Quickmasseg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tell me about your project...", None))
        self.sendBtn.setText(QCoreApplication.translate("MainWindow", u"Send Message", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h2 style=\" margin-top:16px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:700;\">Let's Work Together</span></h2></body></html>", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"I'm always interested in new opportunities and exciting projects.\n"
" Let's connect and discuss how we can collaborate!", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">Get in Touch</span></h3></body></html>", None))
        self.Email.setText(QCoreApplication.translate("MainWindow", u"Email\n"
"Potkiller9000@gmail.com", None))
        self.Phone.setText(QCoreApplication.translate("MainWindow", u"Phone\n"
"+01018206086", None))
        self.location.setText(QCoreApplication.translate("MainWindow", u"Location\n"
"Kafr El Sheikh, Egypt", None))
        self.gitHup.setText("")
        self.Lin.setText("")
        self.Twiter.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Statis Page", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"To be honest with you, I also don't know why I added this page or this button, but I think the reason whay  I add't  was just for aesthetics.", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Reviews Page", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.closeRightMenuBtn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notifictaion", None))
        self.label_16.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:700;\">I'm </span><span style=\" font-size:10pt; font-weight:700;\">Mohammed Awad</span><span style=\" font-size:9pt; font-weight:700;\">, a coding enthusiast with a love for all things tech. Whether it's unraveling complex computer challenges or crafting elegant solutions through programming, I'm always eager to push the boundaries of what's possible in th"
                        "e digital world.</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>More</p></body></html>", None))
        self.EmailBtn.setText(QCoreApplication.translate("MainWindow", u"procoder.main@gmail.com", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Theme progress:", None))
    # retranslateUi

