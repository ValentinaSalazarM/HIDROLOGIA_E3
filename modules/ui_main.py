# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainVFexoj.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import modules.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1298, 813)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setEnabled(True)
        self.topLogo.setGeometry(QRect(10, 0, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"border-image: url(:/images/images/images/wave.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setStyleSheet(u"font: 8pt \"Allerta\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setFont(font)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy3)
        self.stackedWidget.setMaximumSize(QSize(1350, 610))
        self.stackedWidget.setBaseSize(QSize(50, 50))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setLineWidth(-2)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/LogoHome.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.MenuPrincipal = QWidget()
        self.MenuPrincipal.setObjectName(u"MenuPrincipal")
        self.txtCantarrana = QPlainTextEdit(self.MenuPrincipal)
        self.txtCantarrana.setObjectName(u"txtCantarrana")
        self.txtCantarrana.setGeometry(QRect(260, 110, 200, 200))
        self.txtCantarrana.setMinimumSize(QSize(200, 200))
        font3 = QFont()
        font3.setFamilies([u"Allerta"])
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setKerning(True)
        self.txtCantarrana.setFont(font3)
        self.txtCantarrana.setLayoutDirection(Qt.LeftToRight)
        self.txtCantarrana.setAutoFillBackground(False)
        self.txtCantarrana.setStyleSheet(u"font: 500 18pt \"Allerta\";\n"
"background-color: rgb(57, 163, 136);\n"
"")
        self.txtCantarrana.setReadOnly(False)
        self.txtCantarrana.setTabStopDistance(96.000000000000000)
        self.botonMenuCantarrana = QPushButton(self.MenuPrincipal)
        self.botonMenuCantarrana.setObjectName(u"botonMenuCantarrana")
        self.botonMenuCantarrana.setGeometry(QRect(260, 110, 201, 201))
        self.botonMenuCantarrana.setStyleSheet(u"font: 650 20pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: transparent;")
        self.txtBosa = QPlainTextEdit(self.MenuPrincipal)
        self.txtBosa.setObjectName(u"txtBosa")
        self.txtBosa.setGeometry(QRect(730, 110, 200, 200))
        self.txtBosa.setMinimumSize(QSize(200, 200))
        self.txtBosa.setFont(font3)
        self.txtBosa.setLayoutDirection(Qt.LeftToRight)
        self.txtBosa.setAutoFillBackground(False)
        self.txtBosa.setStyleSheet(u"font: 500 18pt \"Allerta\";\n"
"background-color: rgb(145, 145, 217);\n"
"")
        self.txtBosa.setReadOnly(False)
        self.txtBosa.setTabStopDistance(96.000000000000000)
        self.botonMenuBosa = QPushButton(self.MenuPrincipal)
        self.botonMenuBosa.setObjectName(u"botonMenuBosa")
        self.botonMenuBosa.setGeometry(QRect(730, 110, 201, 201))
        self.botonMenuBosa.setStyleSheet(u"font: 650 20pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: transparent;")
        self.CantarranaBtnLbl_3 = QLabel(self.MenuPrincipal)
        self.CantarranaBtnLbl_3.setObjectName(u"CantarranaBtnLbl_3")
        self.CantarranaBtnLbl_3.setGeometry(QRect(260, 340, 201, 210))
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.CantarranaBtnLbl_3.sizePolicy().hasHeightForWidth())
        self.CantarranaBtnLbl_3.setSizePolicy(sizePolicy4)
        self.CantarranaBtnLbl_3.setStyleSheet(u"font: 400 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: transparent;")
        self.CantarranaBtnLbl_3.setLineWidth(1)
        self.CantarranaBtnLbl_3.setAlignment(Qt.AlignCenter)
        self.CantarranaBtnLbl_4 = QLabel(self.MenuPrincipal)
        self.CantarranaBtnLbl_4.setObjectName(u"CantarranaBtnLbl_4")
        self.CantarranaBtnLbl_4.setGeometry(QRect(730, 340, 201, 210))
        sizePolicy4.setHeightForWidth(self.CantarranaBtnLbl_4.sizePolicy().hasHeightForWidth())
        self.CantarranaBtnLbl_4.setSizePolicy(sizePolicy4)
        self.CantarranaBtnLbl_4.setStyleSheet(u"font: 400 16pt \"Allerta\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: transparent;")
        self.CantarranaBtnLbl_4.setLineWidth(1)
        self.CantarranaBtnLbl_4.setAlignment(Qt.AlignCenter)
        self.EstacionLbl_13 = QLineEdit(self.MenuPrincipal)
        self.EstacionLbl_13.setObjectName(u"EstacionLbl_13")
        self.EstacionLbl_13.setGeometry(QRect(240, 340, 4, 220))
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.EstacionLbl_13.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_13.setSizePolicy(sizePolicy5)
        self.EstacionLbl_13.setMinimumSize(QSize(4, 220))
        self.EstacionLbl_13.setMaximumSize(QSize(2, 220))
        self.EstacionLbl_13.setStyleSheet(u"border-color: rgb(89, 255, 211);\n"
"font: 550 11pt \"Allerta\";")
        self.EstacionLbl_14 = QLineEdit(self.MenuPrincipal)
        self.EstacionLbl_14.setObjectName(u"EstacionLbl_14")
        self.EstacionLbl_14.setGeometry(QRect(710, 330, 4, 220))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_14.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_14.setSizePolicy(sizePolicy5)
        self.EstacionLbl_14.setMinimumSize(QSize(4, 220))
        self.EstacionLbl_14.setMaximumSize(QSize(2, 220))
        self.EstacionLbl_14.setStyleSheet(u"border-color: rgb(169, 161, 255);\n"
"font: 550 11pt \"Allerta\";")
        self.CantarranaBtnLbl_7 = QLabel(self.MenuPrincipal)
        self.CantarranaBtnLbl_7.setObjectName(u"CantarranaBtnLbl_7")
        self.CantarranaBtnLbl_7.setGeometry(QRect(-10, 0, 1201, 81))
        sizePolicy4.setHeightForWidth(self.CantarranaBtnLbl_7.sizePolicy().hasHeightForWidth())
        self.CantarranaBtnLbl_7.setSizePolicy(sizePolicy4)
        self.CantarranaBtnLbl_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: transparent;\n"
"font: 900 60pt\"Market Deco\";")
        self.CantarranaBtnLbl_7.setLineWidth(1)
        self.CantarranaBtnLbl_7.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.MenuPrincipal)
        self.pagina_Cantarrana = QWidget()
        self.pagina_Cantarrana.setObjectName(u"pagina_Cantarrana")
        self.tabCantarrana = QTabWidget(self.pagina_Cantarrana)
        self.tabCantarrana.setObjectName(u"tabCantarrana")
        self.tabCantarrana.setGeometry(QRect(0, 0, 1131, 621))
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tabCantarrana.sizePolicy().hasHeightForWidth())
        self.tabCantarrana.setSizePolicy(sizePolicy6)
        self.tabCantarrana.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabCantarrana.setTabPosition(QTabWidget.West)
        self.tabCantarrana.setTabsClosable(False)
        self.CantarranaEntrada = QWidget()
        self.CantarranaEntrada.setObjectName(u"CantarranaEntrada")
        self.CantarranaEntrada.setStyleSheet(u"")
        self.EstacionLbl = QLineEdit(self.CantarranaEntrada)
        self.EstacionLbl.setObjectName(u"EstacionLbl")
        self.EstacionLbl.setGeometry(QRect(130, 100, 830, 2))
        sizePolicy5.setHeightForWidth(self.EstacionLbl.sizePolicy().hasHeightForWidth())
        self.EstacionLbl.setSizePolicy(sizePolicy5)
        self.EstacionLbl.setMinimumSize(QSize(830, 2))
        self.EstacionLbl.setMaximumSize(QSize(830, 2))
        self.EstacionLbl.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.EstacionLbl_5 = QLabel(self.CantarranaEntrada)
        self.EstacionLbl_5.setObjectName(u"EstacionLbl_5")
        self.EstacionLbl_5.setGeometry(QRect(10, 50, 1061, 35))
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.EstacionLbl_5.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_5.setSizePolicy(sizePolicy7)
        self.EstacionLbl_5.setStyleSheet(u"font: 650 25pt \"Allerta\";\n"
"")
        self.EstacionLbl_5.setLineWidth(1)
        self.EstacionLbl_5.setAlignment(Qt.AlignCenter)
        self.EstacionLbl_2 = QLineEdit(self.CantarranaEntrada)
        self.EstacionLbl_2.setObjectName(u"EstacionLbl_2")
        self.EstacionLbl_2.setGeometry(QRect(130, 40, 830, 2))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_2.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_2.setSizePolicy(sizePolicy5)
        self.EstacionLbl_2.setMinimumSize(QSize(830, 2))
        self.EstacionLbl_2.setMaximumSize(QSize(830, 2))
        self.EstacionLbl_2.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.groupBox_Propiedades_45 = QGroupBox(self.CantarranaEntrada)
        self.groupBox_Propiedades_45.setObjectName(u"groupBox_Propiedades_45")
        self.groupBox_Propiedades_45.setGeometry(QRect(50, 130, 770, 161))
        sizePolicy6.setHeightForWidth(self.groupBox_Propiedades_45.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_45.setSizePolicy(sizePolicy6)
        self.groupBox_Propiedades_45.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_45.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_45.setStyleSheet(u"QGroupBox {\n"
"color: rgb(118, 199, 158);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(118, 199, 158);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_45.setAlignment(Qt.AlignCenter)
        self.verticalLayout_44 = QVBoxLayout(self.groupBox_Propiedades_45)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.row_73 = QFrame(self.groupBox_Propiedades_45)
        self.row_73.setObjectName(u"row_73")
        self.row_73.setStyleSheet(u"")
        self.row_73.setFrameShape(QFrame.StyledPanel)
        self.row_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.row_73)
        self.verticalLayout_93.setSpacing(0)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_143 = QGridLayout()
        self.gridLayout_143.setSpacing(20)
        self.gridLayout_143.setObjectName(u"gridLayout_143")
        self.gridLayout_143.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_143.setContentsMargins(20, 5, 20, 5)
        self.CantarranaBtnLbl_2 = QLabel(self.row_73)
        self.CantarranaBtnLbl_2.setObjectName(u"CantarranaBtnLbl_2")
        sizePolicy4.setHeightForWidth(self.CantarranaBtnLbl_2.sizePolicy().hasHeightForWidth())
        self.CantarranaBtnLbl_2.setSizePolicy(sizePolicy4)
        self.CantarranaBtnLbl_2.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaBtnLbl_2.setLineWidth(1)
        self.CantarranaBtnLbl_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_143.addWidget(self.CantarranaBtnLbl_2, 1, 0, 1, 1)

        self.CantarranaBtnLbl = QLabel(self.row_73)
        self.CantarranaBtnLbl.setObjectName(u"CantarranaBtnLbl")
        sizePolicy4.setHeightForWidth(self.CantarranaBtnLbl.sizePolicy().hasHeightForWidth())
        self.CantarranaBtnLbl.setSizePolicy(sizePolicy4)
        self.CantarranaBtnLbl.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaBtnLbl.setLineWidth(1)
        self.CantarranaBtnLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_143.addWidget(self.CantarranaBtnLbl, 0, 0, 1, 1)

        self.CantarranaComboBoxIntervalo = QLineEdit(self.row_73)
        self.CantarranaComboBoxIntervalo.setObjectName(u"CantarranaComboBoxIntervalo")
        sizePolicy7.setHeightForWidth(self.CantarranaComboBoxIntervalo.sizePolicy().hasHeightForWidth())
        self.CantarranaComboBoxIntervalo.setSizePolicy(sizePolicy7)
        self.CantarranaComboBoxIntervalo.setMinimumSize(QSize(110, 35))
        self.CantarranaComboBoxIntervalo.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.CantarranaComboBoxIntervalo.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.CantarranaComboBoxIntervalo.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.CantarranaComboBoxIntervalo.setAlignment(Qt.AlignCenter)

        self.gridLayout_143.addWidget(self.CantarranaComboBoxIntervalo, 1, 1, 1, 1)

        self.CantarranaComboBoxNivel = QComboBox(self.row_73)
        self.CantarranaComboBoxNivel.addItem("")
        self.CantarranaComboBoxNivel.addItem("")
        self.CantarranaComboBoxNivel.addItem("")
        self.CantarranaComboBoxNivel.addItem("")
        self.CantarranaComboBoxNivel.addItem("")
        self.CantarranaComboBoxNivel.setObjectName(u"CantarranaComboBoxNivel")
        self.CantarranaComboBoxNivel.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.CantarranaComboBoxNivel.sizePolicy().hasHeightForWidth())
        self.CantarranaComboBoxNivel.setSizePolicy(sizePolicy6)
        self.CantarranaComboBoxNivel.setMinimumSize(QSize(200, 35))
        self.CantarranaComboBoxNivel.setMaximumSize(QSize(150, 30))
        self.CantarranaComboBoxNivel.setLayoutDirection(Qt.LeftToRight)
        self.CantarranaComboBoxNivel.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.CantarranaComboBoxNivel.setEditable(False)
        self.CantarranaComboBoxNivel.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.CantarranaComboBoxNivel.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_143.addWidget(self.CantarranaComboBoxNivel, 0, 1, 1, 1)


        self.verticalLayout_93.addLayout(self.gridLayout_143)


        self.verticalLayout_44.addWidget(self.row_73)

        self.verticalLayoutWidget_6 = QWidget(self.CantarranaEntrada)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(890, 140, 141, 141))
        self.verticalLayout_49 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_49.setSpacing(20)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(20)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.CantarranaBtnCalcular = QPushButton(self.verticalLayoutWidget_6)
        self.CantarranaBtnCalcular.setObjectName(u"CantarranaBtnCalcular")
        self.CantarranaBtnCalcular.setMinimumSize(QSize(50, 50))
        self.CantarranaBtnCalcular.setMaximumSize(QSize(40, 40))
        self.CantarranaBtnCalcular.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-color: rgb(57, 163, 136);\n"
"	border-width: 2px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(57, 163, 136);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  	border: 3px solid rgb(28, 80, 66);\n"
"	background-color: rgb(28, 80, 66);\n"
"}")

        self.horizontalLayout_30.addWidget(self.CantarranaBtnCalcular)


        self.verticalLayout_50.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.CantarranaLblCalcular = QLabel(self.verticalLayoutWidget_6)
        self.CantarranaLblCalcular.setObjectName(u"CantarranaLblCalcular")
        sizePolicy5.setHeightForWidth(self.CantarranaLblCalcular.sizePolicy().hasHeightForWidth())
        self.CantarranaLblCalcular.setSizePolicy(sizePolicy5)
        self.CantarranaLblCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"")
        self.CantarranaLblCalcular.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_120.addWidget(self.CantarranaLblCalcular)


        self.verticalLayout_50.addLayout(self.horizontalLayout_120)


        self.verticalLayout_49.addLayout(self.verticalLayout_50)

        self.layoutWidget_10 = QWidget(self.CantarranaEntrada)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(360, 280, 502, 302))
        self.horizontalLayout_156 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.horizontalLayout_156.setContentsMargins(0, 0, 0, 0)
        self.CantarranaGrafica = QPushButton(self.layoutWidget_10)
        self.CantarranaGrafica.setObjectName(u"CantarranaGrafica")
        self.CantarranaGrafica.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.CantarranaGrafica.sizePolicy().hasHeightForWidth())
        self.CantarranaGrafica.setSizePolicy(sizePolicy5)
        self.CantarranaGrafica.setMinimumSize(QSize(500, 300))
        self.CantarranaGrafica.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-image: url(:/curvasDuracion/images/curvasDuracion/Cantarrana_diario.jpg);")
        self.CantarranaGrafica.setFlat(True)

        self.horizontalLayout_156.addWidget(self.CantarranaGrafica)

        self.EstacionLbl_3 = QLineEdit(self.CantarranaEntrada)
        self.EstacionLbl_3.setObjectName(u"EstacionLbl_3")
        self.EstacionLbl_3.setGeometry(QRect(60, 570, 265, 2))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_3.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_3.setSizePolicy(sizePolicy5)
        self.EstacionLbl_3.setMinimumSize(QSize(265, 2))
        self.EstacionLbl_3.setMaximumSize(QSize(250, 2))
        self.EstacionLbl_3.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.EstacionLbl_6 = QLabel(self.CantarranaEntrada)
        self.EstacionLbl_6.setObjectName(u"EstacionLbl_6")
        self.EstacionLbl_6.setGeometry(QRect(60, 330, 265, 21))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_6.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_6.setSizePolicy(sizePolicy5)
        self.EstacionLbl_6.setMinimumSize(QSize(265, 0))
        self.EstacionLbl_6.setMaximumSize(QSize(265, 16777215))
        self.EstacionLbl_6.setStyleSheet(u"font: 600 12pt \"Allerta\";\n"
"background-color: rgb(118, 199, 158);\n"
"color: rgb(255, 255, 255);")
        self.EstacionLbl_6.setTextFormat(Qt.AutoText)
        self.EstacionLbl_6.setAlignment(Qt.AlignCenter)
        self.EstacionLbl_4 = QLineEdit(self.CantarranaEntrada)
        self.EstacionLbl_4.setObjectName(u"EstacionLbl_4")
        self.EstacionLbl_4.setGeometry(QRect(60, 320, 265, 2))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_4.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_4.setSizePolicy(sizePolicy5)
        self.EstacionLbl_4.setMinimumSize(QSize(265, 2))
        self.EstacionLbl_4.setMaximumSize(QSize(250, 2))
        self.EstacionLbl_4.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.layoutWidget = QWidget(self.CantarranaEntrada)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(210, 360, 111, 201))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.CantarranaFieldMinimo = QLabel(self.layoutWidget)
        self.CantarranaFieldMinimo.setObjectName(u"CantarranaFieldMinimo")
        sizePolicy4.setHeightForWidth(self.CantarranaFieldMinimo.sizePolicy().hasHeightForWidth())
        self.CantarranaFieldMinimo.setSizePolicy(sizePolicy4)
        self.CantarranaFieldMinimo.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaFieldMinimo.setLineWidth(1)
        self.CantarranaFieldMinimo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.CantarranaFieldMinimo)

        self.CantarranaFieldMaximo = QLabel(self.layoutWidget)
        self.CantarranaFieldMaximo.setObjectName(u"CantarranaFieldMaximo")
        sizePolicy4.setHeightForWidth(self.CantarranaFieldMaximo.sizePolicy().hasHeightForWidth())
        self.CantarranaFieldMaximo.setSizePolicy(sizePolicy4)
        self.CantarranaFieldMaximo.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaFieldMaximo.setLineWidth(1)
        self.CantarranaFieldMaximo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.CantarranaFieldMaximo)

        self.CantarranaFieldRango = QLabel(self.layoutWidget)
        self.CantarranaFieldRango.setObjectName(u"CantarranaFieldRango")
        sizePolicy4.setHeightForWidth(self.CantarranaFieldRango.sizePolicy().hasHeightForWidth())
        self.CantarranaFieldRango.setSizePolicy(sizePolicy4)
        self.CantarranaFieldRango.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaFieldRango.setLineWidth(1)
        self.CantarranaFieldRango.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.CantarranaFieldRango)

        self.CantarranaFieldAmplitud = QLabel(self.layoutWidget)
        self.CantarranaFieldAmplitud.setObjectName(u"CantarranaFieldAmplitud")
        sizePolicy4.setHeightForWidth(self.CantarranaFieldAmplitud.sizePolicy().hasHeightForWidth())
        self.CantarranaFieldAmplitud.setSizePolicy(sizePolicy4)
        self.CantarranaFieldAmplitud.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaFieldAmplitud.setLineWidth(1)
        self.CantarranaFieldAmplitud.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.CantarranaFieldAmplitud)

        self.CantarranaFieldDatos = QLabel(self.layoutWidget)
        self.CantarranaFieldDatos.setObjectName(u"CantarranaFieldDatos")
        sizePolicy4.setHeightForWidth(self.CantarranaFieldDatos.sizePolicy().hasHeightForWidth())
        self.CantarranaFieldDatos.setSizePolicy(sizePolicy4)
        self.CantarranaFieldDatos.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaFieldDatos.setLineWidth(1)
        self.CantarranaFieldDatos.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.CantarranaFieldDatos)

        self.layoutWidget1 = QWidget(self.CantarranaEntrada)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(60, 360, 138, 201))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.CantarranaLblMinimo = QLabel(self.layoutWidget1)
        self.CantarranaLblMinimo.setObjectName(u"CantarranaLblMinimo")
        sizePolicy4.setHeightForWidth(self.CantarranaLblMinimo.sizePolicy().hasHeightForWidth())
        self.CantarranaLblMinimo.setSizePolicy(sizePolicy4)
        self.CantarranaLblMinimo.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblMinimo.setLineWidth(1)
        self.CantarranaLblMinimo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.CantarranaLblMinimo)

        self.CantarranaLblMaximo = QLabel(self.layoutWidget1)
        self.CantarranaLblMaximo.setObjectName(u"CantarranaLblMaximo")
        sizePolicy4.setHeightForWidth(self.CantarranaLblMaximo.sizePolicy().hasHeightForWidth())
        self.CantarranaLblMaximo.setSizePolicy(sizePolicy4)
        self.CantarranaLblMaximo.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblMaximo.setLineWidth(1)
        self.CantarranaLblMaximo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.CantarranaLblMaximo)

        self.CantarranaLblRango = QLabel(self.layoutWidget1)
        self.CantarranaLblRango.setObjectName(u"CantarranaLblRango")
        sizePolicy4.setHeightForWidth(self.CantarranaLblRango.sizePolicy().hasHeightForWidth())
        self.CantarranaLblRango.setSizePolicy(sizePolicy4)
        self.CantarranaLblRango.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblRango.setLineWidth(1)
        self.CantarranaLblRango.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.CantarranaLblRango)

        self.CantarranaLblAmplitud = QLabel(self.layoutWidget1)
        self.CantarranaLblAmplitud.setObjectName(u"CantarranaLblAmplitud")
        sizePolicy4.setHeightForWidth(self.CantarranaLblAmplitud.sizePolicy().hasHeightForWidth())
        self.CantarranaLblAmplitud.setSizePolicy(sizePolicy4)
        self.CantarranaLblAmplitud.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblAmplitud.setLineWidth(1)
        self.CantarranaLblAmplitud.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.CantarranaLblAmplitud)

        self.CantarranaLblDatos = QLabel(self.layoutWidget1)
        self.CantarranaLblDatos.setObjectName(u"CantarranaLblDatos")
        sizePolicy4.setHeightForWidth(self.CantarranaLblDatos.sizePolicy().hasHeightForWidth())
        self.CantarranaLblDatos.setSizePolicy(sizePolicy4)
        self.CantarranaLblDatos.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblDatos.setLineWidth(1)
        self.CantarranaLblDatos.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.CantarranaLblDatos)

        self.tabCantarrana.addTab(self.CantarranaEntrada, "")
        self.CantarranaResultados = QWidget()
        self.CantarranaResultados.setObjectName(u"CantarranaResultados")
        self.CantarranaTabla = QTableWidget(self.CantarranaResultados)
        self.CantarranaTabla.setObjectName(u"CantarranaTabla")
        self.CantarranaTabla.setGeometry(QRect(30, 20, 780, 551))
        self.CantarranaTabla.setLayoutDirection(Qt.LeftToRight)
        self.CantarranaTabla.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"StepsViewer::StepsViewer(QWidget *parent) : QTableWidget(parent)\n"
"{\n"
"setColumnCount(2);\n"
"setColumnWidth(0, 300);\n"
"setColumnWidth(1, 400);\n"
"}")
        self.CantarranaTabla.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.CantarranaTabla.setAlternatingRowColors(False)
        self.CantarranaTabla.setTextElideMode(Qt.ElideMiddle)
        self.CantarranaBtnDescargarGrafica = QPushButton(self.CantarranaResultados)
        self.CantarranaBtnDescargarGrafica.setObjectName(u"CantarranaBtnDescargarGrafica")
        self.CantarranaBtnDescargarGrafica.setEnabled(True)
        self.CantarranaBtnDescargarGrafica.setGeometry(QRect(880, 30, 180, 50))
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.CantarranaBtnDescargarGrafica.sizePolicy().hasHeightForWidth())
        self.CantarranaBtnDescargarGrafica.setSizePolicy(sizePolicy8)
        self.CantarranaBtnDescargarGrafica.setMinimumSize(QSize(180, 50))
        self.CantarranaBtnDescargarGrafica.setMaximumSize(QSize(160, 40))
        self.CantarranaBtnDescargarGrafica.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.CantarranaBtnDescargarGrafica.setCheckable(False)
        self.CantarranaBtnDescargarGrafica.setChecked(False)
        self.CantarranaBtnDescargarGrafica.setAutoDefault(False)
        self.tabCantarrana.addTab(self.CantarranaResultados, "")
        self.stackedWidget.addWidget(self.pagina_Cantarrana)
        self.pagina_Bosa = QWidget()
        self.pagina_Bosa.setObjectName(u"pagina_Bosa")
        self.tabBosa = QTabWidget(self.pagina_Bosa)
        self.tabBosa.setObjectName(u"tabBosa")
        self.tabBosa.setGeometry(QRect(0, 0, 1131, 621))
        sizePolicy6.setHeightForWidth(self.tabBosa.sizePolicy().hasHeightForWidth())
        self.tabBosa.setSizePolicy(sizePolicy6)
        self.tabBosa.setStyleSheet(u"font: 500 10pt \"Allerta\";\n"
"color: rgb(79, 79, 79);")
        self.tabBosa.setTabPosition(QTabWidget.West)
        self.tabBosa.setTabsClosable(False)
        self.BosaEntrada = QWidget()
        self.BosaEntrada.setObjectName(u"BosaEntrada")
        self.BosaEntrada.setStyleSheet(u"")
        self.EstacionLbl_7 = QLineEdit(self.BosaEntrada)
        self.EstacionLbl_7.setObjectName(u"EstacionLbl_7")
        self.EstacionLbl_7.setGeometry(QRect(130, 100, 830, 2))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_7.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_7.setSizePolicy(sizePolicy5)
        self.EstacionLbl_7.setMinimumSize(QSize(830, 2))
        self.EstacionLbl_7.setMaximumSize(QSize(830, 2))
        self.EstacionLbl_7.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.EstacionLbl_8 = QLabel(self.BosaEntrada)
        self.EstacionLbl_8.setObjectName(u"EstacionLbl_8")
        self.EstacionLbl_8.setGeometry(QRect(10, 50, 1061, 35))
        sizePolicy7.setHeightForWidth(self.EstacionLbl_8.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_8.setSizePolicy(sizePolicy7)
        self.EstacionLbl_8.setStyleSheet(u"font: 650 25pt \"Allerta\";\n"
"")
        self.EstacionLbl_8.setLineWidth(1)
        self.EstacionLbl_8.setAlignment(Qt.AlignCenter)
        self.EstacionLbl_9 = QLineEdit(self.BosaEntrada)
        self.EstacionLbl_9.setObjectName(u"EstacionLbl_9")
        self.EstacionLbl_9.setGeometry(QRect(130, 40, 830, 2))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_9.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_9.setSizePolicy(sizePolicy5)
        self.EstacionLbl_9.setMinimumSize(QSize(830, 2))
        self.EstacionLbl_9.setMaximumSize(QSize(830, 2))
        self.EstacionLbl_9.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.groupBox_Propiedades_46 = QGroupBox(self.BosaEntrada)
        self.groupBox_Propiedades_46.setObjectName(u"groupBox_Propiedades_46")
        self.groupBox_Propiedades_46.setGeometry(QRect(50, 130, 770, 161))
        sizePolicy6.setHeightForWidth(self.groupBox_Propiedades_46.sizePolicy().hasHeightForWidth())
        self.groupBox_Propiedades_46.setSizePolicy(sizePolicy6)
        self.groupBox_Propiedades_46.setMinimumSize(QSize(770, 0))
        self.groupBox_Propiedades_46.setMaximumSize(QSize(700, 16777215))
        self.groupBox_Propiedades_46.setStyleSheet(u"QGroupBox {\n"
"color: rgb(145, 145, 217);\n"
"font: bold; \n"
"border: 2px solid;\n"
"font: 700 11pt \"Allerta\";\n"
"border-color: rgb(145, 145, 217);\n"
"border-radius: 6px;\n"
"margin: 10px;\n"
"\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"   	subcontrol-position: top left;\n"
"    padding: 0px 15px 0px 15px;\n"
"}\n"
"")
        self.groupBox_Propiedades_46.setAlignment(Qt.AlignCenter)
        self.verticalLayout_46 = QVBoxLayout(self.groupBox_Propiedades_46)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.row_75 = QFrame(self.groupBox_Propiedades_46)
        self.row_75.setObjectName(u"row_75")
        self.row_75.setStyleSheet(u"")
        self.row_75.setFrameShape(QFrame.StyledPanel)
        self.row_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.row_75)
        self.verticalLayout_95.setSpacing(0)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_145 = QGridLayout()
        self.gridLayout_145.setSpacing(20)
        self.gridLayout_145.setObjectName(u"gridLayout_145")
        self.gridLayout_145.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_145.setContentsMargins(20, 5, 20, 5)
        self.CantarranaBtnLbl_5 = QLabel(self.row_75)
        self.CantarranaBtnLbl_5.setObjectName(u"CantarranaBtnLbl_5")
        sizePolicy4.setHeightForWidth(self.CantarranaBtnLbl_5.sizePolicy().hasHeightForWidth())
        self.CantarranaBtnLbl_5.setSizePolicy(sizePolicy4)
        self.CantarranaBtnLbl_5.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaBtnLbl_5.setLineWidth(1)
        self.CantarranaBtnLbl_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_145.addWidget(self.CantarranaBtnLbl_5, 1, 0, 1, 1)

        self.CantarranaBtnLbl_6 = QLabel(self.row_75)
        self.CantarranaBtnLbl_6.setObjectName(u"CantarranaBtnLbl_6")
        sizePolicy4.setHeightForWidth(self.CantarranaBtnLbl_6.sizePolicy().hasHeightForWidth())
        self.CantarranaBtnLbl_6.setSizePolicy(sizePolicy4)
        self.CantarranaBtnLbl_6.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaBtnLbl_6.setLineWidth(1)
        self.CantarranaBtnLbl_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_145.addWidget(self.CantarranaBtnLbl_6, 0, 0, 1, 1)

        self.BosaComboBoxIntervalo = QLineEdit(self.row_75)
        self.BosaComboBoxIntervalo.setObjectName(u"BosaComboBoxIntervalo")
        sizePolicy7.setHeightForWidth(self.BosaComboBoxIntervalo.sizePolicy().hasHeightForWidth())
        self.BosaComboBoxIntervalo.setSizePolicy(sizePolicy7)
        self.BosaComboBoxIntervalo.setMinimumSize(QSize(110, 35))
        self.BosaComboBoxIntervalo.setMaximumSize(QSize(200, 35))
#if QT_CONFIG(tooltip)
        self.BosaComboBoxIntervalo.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.BosaComboBoxIntervalo.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 650 11pt \"Allerta\";\n"
"")
        self.BosaComboBoxIntervalo.setAlignment(Qt.AlignCenter)

        self.gridLayout_145.addWidget(self.BosaComboBoxIntervalo, 1, 1, 1, 1)

        self.BosaComboBoxNivel = QComboBox(self.row_75)
        self.BosaComboBoxNivel.addItem("")
        self.BosaComboBoxNivel.addItem("")
        self.BosaComboBoxNivel.addItem("")
        self.BosaComboBoxNivel.addItem("")
        self.BosaComboBoxNivel.addItem("")
        self.BosaComboBoxNivel.setObjectName(u"BosaComboBoxNivel")
        self.BosaComboBoxNivel.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.BosaComboBoxNivel.sizePolicy().hasHeightForWidth())
        self.BosaComboBoxNivel.setSizePolicy(sizePolicy6)
        self.BosaComboBoxNivel.setMinimumSize(QSize(200, 35))
        self.BosaComboBoxNivel.setMaximumSize(QSize(150, 30))
        self.BosaComboBoxNivel.setLayoutDirection(Qt.LeftToRight)
        self.BosaComboBoxNivel.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"background-color: rgb(255, 255, 255);")
        self.BosaComboBoxNivel.setEditable(False)
        self.BosaComboBoxNivel.setInsertPolicy(QComboBox.InsertAtCurrent)
        self.BosaComboBoxNivel.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.gridLayout_145.addWidget(self.BosaComboBoxNivel, 0, 1, 1, 1)


        self.verticalLayout_95.addLayout(self.gridLayout_145)


        self.verticalLayout_46.addWidget(self.row_75)

        self.verticalLayoutWidget_7 = QWidget(self.BosaEntrada)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(890, 140, 141, 141))
        self.verticalLayout_53 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_53.setSpacing(20)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setSpacing(20)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.BosaBtnCalcular = QPushButton(self.verticalLayoutWidget_7)
        self.BosaBtnCalcular.setObjectName(u"BosaBtnCalcular")
        self.BosaBtnCalcular.setMinimumSize(QSize(50, 50))
        self.BosaBtnCalcular.setMaximumSize(QSize(40, 40))
        self.BosaBtnCalcular.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-color: rgb(145, 145, 217);\n"
"	border-width: 2px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(145, 145, 217);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  	border: 3px solid rgb(94, 94, 141);\n"
"	background-color: rgb(94, 94, 141);\n"
"}")

        self.horizontalLayout_32.addWidget(self.BosaBtnCalcular)


        self.verticalLayout_54.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.BosaLblCalcular = QLabel(self.verticalLayoutWidget_7)
        self.BosaLblCalcular.setObjectName(u"BosaLblCalcular")
        sizePolicy5.setHeightForWidth(self.BosaLblCalcular.sizePolicy().hasHeightForWidth())
        self.BosaLblCalcular.setSizePolicy(sizePolicy5)
        self.BosaLblCalcular.setStyleSheet(u"font: 500 12pt \"Allerta\";\n"
"")
        self.BosaLblCalcular.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_122.addWidget(self.BosaLblCalcular)


        self.verticalLayout_54.addLayout(self.horizontalLayout_122)


        self.verticalLayout_53.addLayout(self.verticalLayout_54)

        self.EstacionLbl_10 = QLineEdit(self.BosaEntrada)
        self.EstacionLbl_10.setObjectName(u"EstacionLbl_10")
        self.EstacionLbl_10.setGeometry(QRect(60, 570, 265, 2))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_10.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_10.setSizePolicy(sizePolicy5)
        self.EstacionLbl_10.setMinimumSize(QSize(265, 2))
        self.EstacionLbl_10.setMaximumSize(QSize(250, 2))
        self.EstacionLbl_10.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.EstacionLbl_11 = QLabel(self.BosaEntrada)
        self.EstacionLbl_11.setObjectName(u"EstacionLbl_11")
        self.EstacionLbl_11.setGeometry(QRect(60, 330, 265, 21))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_11.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_11.setSizePolicy(sizePolicy5)
        self.EstacionLbl_11.setMinimumSize(QSize(265, 0))
        self.EstacionLbl_11.setMaximumSize(QSize(265, 16777215))
        self.EstacionLbl_11.setStyleSheet(u"font: 600 12pt \"Allerta\";\n"
"background-color: rgb(145, 145, 217);\n"
"color: rgb(255, 255, 255);")
        self.EstacionLbl_11.setTextFormat(Qt.AutoText)
        self.EstacionLbl_11.setAlignment(Qt.AlignCenter)
        self.EstacionLbl_12 = QLineEdit(self.BosaEntrada)
        self.EstacionLbl_12.setObjectName(u"EstacionLbl_12")
        self.EstacionLbl_12.setGeometry(QRect(60, 320, 265, 2))
        sizePolicy5.setHeightForWidth(self.EstacionLbl_12.sizePolicy().hasHeightForWidth())
        self.EstacionLbl_12.setSizePolicy(sizePolicy5)
        self.EstacionLbl_12.setMinimumSize(QSize(265, 2))
        self.EstacionLbl_12.setMaximumSize(QSize(250, 2))
        self.EstacionLbl_12.setStyleSheet(u"border-color: rgb(211, 212, 216);\n"
"font: 550 11pt \"Allerta\";")
        self.layoutWidget_2 = QWidget(self.BosaEntrada)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(210, 360, 111, 201))
        self.verticalLayout_19 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.BosaFieldMinimo = QLabel(self.layoutWidget_2)
        self.BosaFieldMinimo.setObjectName(u"BosaFieldMinimo")
        sizePolicy4.setHeightForWidth(self.BosaFieldMinimo.sizePolicy().hasHeightForWidth())
        self.BosaFieldMinimo.setSizePolicy(sizePolicy4)
        self.BosaFieldMinimo.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.BosaFieldMinimo.setLineWidth(1)
        self.BosaFieldMinimo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.BosaFieldMinimo)

        self.BosaFieldMaximo = QLabel(self.layoutWidget_2)
        self.BosaFieldMaximo.setObjectName(u"BosaFieldMaximo")
        sizePolicy4.setHeightForWidth(self.BosaFieldMaximo.sizePolicy().hasHeightForWidth())
        self.BosaFieldMaximo.setSizePolicy(sizePolicy4)
        self.BosaFieldMaximo.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.BosaFieldMaximo.setLineWidth(1)
        self.BosaFieldMaximo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.BosaFieldMaximo)

        self.BosaFieldRango = QLabel(self.layoutWidget_2)
        self.BosaFieldRango.setObjectName(u"BosaFieldRango")
        sizePolicy4.setHeightForWidth(self.BosaFieldRango.sizePolicy().hasHeightForWidth())
        self.BosaFieldRango.setSizePolicy(sizePolicy4)
        self.BosaFieldRango.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.BosaFieldRango.setLineWidth(1)
        self.BosaFieldRango.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.BosaFieldRango)

        self.BosaFieldAmplitud = QLabel(self.layoutWidget_2)
        self.BosaFieldAmplitud.setObjectName(u"BosaFieldAmplitud")
        sizePolicy4.setHeightForWidth(self.BosaFieldAmplitud.sizePolicy().hasHeightForWidth())
        self.BosaFieldAmplitud.setSizePolicy(sizePolicy4)
        self.BosaFieldAmplitud.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.BosaFieldAmplitud.setLineWidth(1)
        self.BosaFieldAmplitud.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.BosaFieldAmplitud)

        self.BosaFieldDatos = QLabel(self.layoutWidget_2)
        self.BosaFieldDatos.setObjectName(u"BosaFieldDatos")
        sizePolicy4.setHeightForWidth(self.BosaFieldDatos.sizePolicy().hasHeightForWidth())
        self.BosaFieldDatos.setSizePolicy(sizePolicy4)
        self.BosaFieldDatos.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.BosaFieldDatos.setLineWidth(1)
        self.BosaFieldDatos.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.BosaFieldDatos)

        self.layoutWidget_3 = QWidget(self.BosaEntrada)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(60, 360, 138, 201))
        self.verticalLayout_20 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.CantarranaLblMinimo_3 = QLabel(self.layoutWidget_3)
        self.CantarranaLblMinimo_3.setObjectName(u"CantarranaLblMinimo_3")
        sizePolicy4.setHeightForWidth(self.CantarranaLblMinimo_3.sizePolicy().hasHeightForWidth())
        self.CantarranaLblMinimo_3.setSizePolicy(sizePolicy4)
        self.CantarranaLblMinimo_3.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblMinimo_3.setLineWidth(1)
        self.CantarranaLblMinimo_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.CantarranaLblMinimo_3)

        self.CantarranaLblMaximo_3 = QLabel(self.layoutWidget_3)
        self.CantarranaLblMaximo_3.setObjectName(u"CantarranaLblMaximo_3")
        sizePolicy4.setHeightForWidth(self.CantarranaLblMaximo_3.sizePolicy().hasHeightForWidth())
        self.CantarranaLblMaximo_3.setSizePolicy(sizePolicy4)
        self.CantarranaLblMaximo_3.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblMaximo_3.setLineWidth(1)
        self.CantarranaLblMaximo_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.CantarranaLblMaximo_3)

        self.CantarranaLblRango_3 = QLabel(self.layoutWidget_3)
        self.CantarranaLblRango_3.setObjectName(u"CantarranaLblRango_3")
        sizePolicy4.setHeightForWidth(self.CantarranaLblRango_3.sizePolicy().hasHeightForWidth())
        self.CantarranaLblRango_3.setSizePolicy(sizePolicy4)
        self.CantarranaLblRango_3.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblRango_3.setLineWidth(1)
        self.CantarranaLblRango_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.CantarranaLblRango_3)

        self.CantarranaLblAmplitud_3 = QLabel(self.layoutWidget_3)
        self.CantarranaLblAmplitud_3.setObjectName(u"CantarranaLblAmplitud_3")
        sizePolicy4.setHeightForWidth(self.CantarranaLblAmplitud_3.sizePolicy().hasHeightForWidth())
        self.CantarranaLblAmplitud_3.setSizePolicy(sizePolicy4)
        self.CantarranaLblAmplitud_3.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblAmplitud_3.setLineWidth(1)
        self.CantarranaLblAmplitud_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.CantarranaLblAmplitud_3)

        self.CantarranaLblDatos_3 = QLabel(self.layoutWidget_3)
        self.CantarranaLblDatos_3.setObjectName(u"CantarranaLblDatos_3")
        sizePolicy4.setHeightForWidth(self.CantarranaLblDatos_3.sizePolicy().hasHeightForWidth())
        self.CantarranaLblDatos_3.setSizePolicy(sizePolicy4)
        self.CantarranaLblDatos_3.setStyleSheet(u"font: 650 12pt \"Allerta\";")
        self.CantarranaLblDatos_3.setLineWidth(1)
        self.CantarranaLblDatos_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_20.addWidget(self.CantarranaLblDatos_3)

        self.layoutWidget_12 = QWidget(self.BosaEntrada)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(360, 280, 502, 302))
        self.horizontalLayout_157 = QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalLayout_157.setContentsMargins(0, 0, 0, 0)
        self.BosaGrafica = QPushButton(self.layoutWidget_12)
        self.BosaGrafica.setObjectName(u"BosaGrafica")
        self.BosaGrafica.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.BosaGrafica.sizePolicy().hasHeightForWidth())
        self.BosaGrafica.setSizePolicy(sizePolicy5)
        self.BosaGrafica.setMinimumSize(QSize(500, 300))
        self.BosaGrafica.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-image: url(:/curvasDuracion/images/curvasDuracion/Bosa_diario.jpg);\n"
"")
        self.BosaGrafica.setFlat(True)

        self.horizontalLayout_157.addWidget(self.BosaGrafica)

        self.tabBosa.addTab(self.BosaEntrada, "")
        self.BosaResultados = QWidget()
        self.BosaResultados.setObjectName(u"BosaResultados")
        self.BosaTabla = QTableWidget(self.BosaResultados)
        self.BosaTabla.setObjectName(u"BosaTabla")
        self.BosaTabla.setGeometry(QRect(30, 20, 780, 551))
        self.BosaTabla.setMinimumSize(QSize(780, 0))
        self.BosaTabla.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"StepsViewer::StepsViewer(QWidget *parent) : QTableWidget(parent)\n"
"{\n"
"setColumnCount(2);\n"
"setColumnWidth(0, 300);\n"
"setColumnWidth(1, 400);\n"
"}")
        self.BosaBtnDescargarGrafica = QPushButton(self.BosaResultados)
        self.BosaBtnDescargarGrafica.setObjectName(u"BosaBtnDescargarGrafica")
        self.BosaBtnDescargarGrafica.setEnabled(True)
        self.BosaBtnDescargarGrafica.setGeometry(QRect(880, 30, 180, 50))
        sizePolicy8.setHeightForWidth(self.BosaBtnDescargarGrafica.sizePolicy().hasHeightForWidth())
        self.BosaBtnDescargarGrafica.setSizePolicy(sizePolicy8)
        self.BosaBtnDescargarGrafica.setMinimumSize(QSize(180, 50))
        self.BosaBtnDescargarGrafica.setMaximumSize(QSize(160, 40))
        self.BosaBtnDescargarGrafica.setStyleSheet(u"background-color: rgb(163, 160, 159);\n"
"border-width: 5px;\n"
"border-color: rgb(163, 160, 159);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Allerta\";\n"
"\n"
"")
        self.BosaBtnDescargarGrafica.setCheckable(False)
        self.BosaBtnDescargarGrafica.setChecked(False)
        self.BosaBtnDescargarGrafica.setAutoDefault(False)
        self.tabBosa.addTab(self.BosaResultados, "")
        self.stackedWidget.addWidget(self.pagina_Bosa)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_6.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabCantarrana.setCurrentIndex(0)
        self.tabBosa.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.topLogo.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"HidrApp Uniandes", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Hidr\u00e1ulica de canales abiertos", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Estudio hidrol\u00f3gico de la cuenca del R\u00edo Tunjuelo</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.txtCantarrana.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.txtCantarrana.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.txtCantarrana.setPlainText("")
        self.botonMenuCantarrana.setText(QCoreApplication.translate("MainWindow", u"Estaci\u00f3n \n"
" Cantarrana", None))
#if QT_CONFIG(tooltip)
        self.txtBosa.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:18pt; font-weight:500; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:30px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.txtBosa.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.txtBosa.setPlainText("")
        self.botonMenuBosa.setText(QCoreApplication.translate("MainWindow", u"Estaci\u00f3n \n"
" Puente Bosa", None))
        self.CantarranaBtnLbl_3.setText(QCoreApplication.translate("MainWindow", u"Latitud: 4\u00b029' \n"
"\n"
"Longitud: 74\u00b007' \n"
" \n"
"Entidad: EAAB \n"
"\n"
"Per\u00edodo: 1958", None))
        self.CantarranaBtnLbl_4.setText(QCoreApplication.translate("MainWindow", u"Latitud: 4\u00b037' \n"
"\n"
"Longitud: 74\u00b016' \n"
" \n"
"Entidad: EAAB \n"
"\n"
"Per\u00edodo: 1970", None))
#if QT_CONFIG(tooltip)
        self.EstacionLbl_13.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl_13.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl_13.setText("")
        self.EstacionLbl_13.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.EstacionLbl_14.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl_14.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl_14.setText("")
        self.EstacionLbl_14.setPlaceholderText("")
        self.CantarranaBtnLbl_7.setText(QCoreApplication.translate("MainWindow", u"MENU PRINCIPAL", None))
#if QT_CONFIG(tooltip)
        self.EstacionLbl.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl.setText("")
        self.EstacionLbl.setPlaceholderText("")
        self.EstacionLbl_5.setText(QCoreApplication.translate("MainWindow", u"ESTACI\u00d3N CANTARRANA", None))
#if QT_CONFIG(tooltip)
        self.EstacionLbl_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl_2.setText("")
        self.EstacionLbl_2.setPlaceholderText("")
        self.groupBox_Propiedades_45.setTitle(QCoreApplication.translate("MainWindow", u"Criterios", None))
        self.CantarranaBtnLbl_2.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de intervalos de frecuencia", None))
        self.CantarranaBtnLbl.setText(QCoreApplication.translate("MainWindow", u"Nivel de agregaci\u00f3n", None))
#if QT_CONFIG(whatsthis)
        self.CantarranaComboBoxIntervalo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.CantarranaComboBoxIntervalo.setText("")
        self.CantarranaComboBoxIntervalo.setPlaceholderText("")
        self.CantarranaComboBoxNivel.setItemText(0, QCoreApplication.translate("MainWindow", u"Diario", None))
        self.CantarranaComboBoxNivel.setItemText(1, QCoreApplication.translate("MainWindow", u"Semanal", None))
        self.CantarranaComboBoxNivel.setItemText(2, QCoreApplication.translate("MainWindow", u"Decadal", None))
        self.CantarranaComboBoxNivel.setItemText(3, QCoreApplication.translate("MainWindow", u"Quincenal", None))
        self.CantarranaComboBoxNivel.setItemText(4, QCoreApplication.translate("MainWindow", u"Mensual", None))

        self.CantarranaComboBoxNivel.setCurrentText(QCoreApplication.translate("MainWindow", u"Diario", None))
        self.CantarranaBtnCalcular.setText("")
        self.CantarranaLblCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
        self.CantarranaGrafica.setText("")
#if QT_CONFIG(tooltip)
        self.EstacionLbl_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl_3.setText("")
        self.EstacionLbl_3.setPlaceholderText("")
        self.EstacionLbl_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Estad\u00edsticas</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.EstacionLbl_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl_4.setText("")
        self.EstacionLbl_4.setPlaceholderText("")
        self.CantarranaFieldMinimo.setText("")
        self.CantarranaFieldMaximo.setText("")
        self.CantarranaFieldRango.setText("")
        self.CantarranaFieldAmplitud.setText("")
        self.CantarranaFieldDatos.setText("")
        self.CantarranaLblMinimo.setText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
        self.CantarranaLblMaximo.setText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
        self.CantarranaLblRango.setText(QCoreApplication.translate("MainWindow", u"Rango", None))
        self.CantarranaLblAmplitud.setText(QCoreApplication.translate("MainWindow", u"Amplitud", None))
        self.CantarranaLblDatos.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de datos", None))
        self.tabCantarrana.setTabText(self.tabCantarrana.indexOf(self.CantarranaEntrada), QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.CantarranaBtnDescargarGrafica.setText(QCoreApplication.translate("MainWindow", u"Descargar \n"
" tabla", None))
        self.tabCantarrana.setTabText(self.tabCantarrana.indexOf(self.CantarranaResultados), QCoreApplication.translate("MainWindow", u"Resultados", None))
#if QT_CONFIG(tooltip)
        self.EstacionLbl_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl_7.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl_7.setText("")
        self.EstacionLbl_7.setPlaceholderText("")
        self.EstacionLbl_8.setText(QCoreApplication.translate("MainWindow", u"ESTACI\u00d3N PUENTE BOSA", None))
#if QT_CONFIG(tooltip)
        self.EstacionLbl_9.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl_9.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl_9.setText("")
        self.EstacionLbl_9.setPlaceholderText("")
        self.groupBox_Propiedades_46.setTitle(QCoreApplication.translate("MainWindow", u"Criterios", None))
        self.CantarranaBtnLbl_5.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de intervalos de frecuencia", None))
        self.CantarranaBtnLbl_6.setText(QCoreApplication.translate("MainWindow", u"Nivel de agregaci\u00f3n", None))
#if QT_CONFIG(whatsthis)
        self.BosaComboBoxIntervalo.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.BosaComboBoxIntervalo.setText("")
        self.BosaComboBoxIntervalo.setPlaceholderText("")
        self.BosaComboBoxNivel.setItemText(0, QCoreApplication.translate("MainWindow", u"Diario", None))
        self.BosaComboBoxNivel.setItemText(1, QCoreApplication.translate("MainWindow", u"Semanal", None))
        self.BosaComboBoxNivel.setItemText(2, QCoreApplication.translate("MainWindow", u"Decadal", None))
        self.BosaComboBoxNivel.setItemText(3, QCoreApplication.translate("MainWindow", u"Quincenal", None))
        self.BosaComboBoxNivel.setItemText(4, QCoreApplication.translate("MainWindow", u"Mensual", None))

        self.BosaComboBoxNivel.setCurrentText(QCoreApplication.translate("MainWindow", u"Diario", None))
        self.BosaBtnCalcular.setText("")
        self.BosaLblCalcular.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Calcular</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.EstacionLbl_10.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl_10.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl_10.setText("")
        self.EstacionLbl_10.setPlaceholderText("")
        self.EstacionLbl_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Estad\u00edsticas</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.EstacionLbl_12.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.EstacionLbl_12.setWhatsThis(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Allerta'; font-size:12pt; font-weight:650; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EstacionLbl_12.setText("")
        self.EstacionLbl_12.setPlaceholderText("")
        self.BosaFieldMinimo.setText("")
        self.BosaFieldMaximo.setText("")
        self.BosaFieldRango.setText("")
        self.BosaFieldAmplitud.setText("")
        self.BosaFieldDatos.setText("")
        self.CantarranaLblMinimo_3.setText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
        self.CantarranaLblMaximo_3.setText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
        self.CantarranaLblRango_3.setText(QCoreApplication.translate("MainWindow", u"Rango", None))
        self.CantarranaLblAmplitud_3.setText(QCoreApplication.translate("MainWindow", u"Amplitud", None))
        self.CantarranaLblDatos_3.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de datos", None))
        self.BosaGrafica.setText("")
        self.tabBosa.setTabText(self.tabBosa.indexOf(self.BosaEntrada), QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.BosaBtnDescargarGrafica.setText(QCoreApplication.translate("MainWindow", u"Descargar \n"
" gr\u00e1fica", None))
        self.tabBosa.setTabText(self.tabBosa.indexOf(self.BosaResultados), QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Universidad de los Andes - 2022", None))
    # retranslateUi

