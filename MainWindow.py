# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ImagePainterWidget import ImagePainterWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(676, 530)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew.setShortcutContext(Qt.WindowShortcut)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionEdit_All = QAction(MainWindow)
        self.actionEdit_All.setObjectName(u"actionEdit_All")
        self.actionAdit_One = QAction(MainWindow)
        self.actionAdit_One.setObjectName(u"actionAdit_One")
        self.actionEdit_Scripts = QAction(MainWindow)
        self.actionEdit_Scripts.setObjectName(u"actionEdit_Scripts")
        self.actionEdit_2 = QAction(MainWindow)
        self.actionEdit_2.setObjectName(u"actionEdit_2")
        self.actionEdit_Texts = QAction(MainWindow)
        self.actionEdit_Texts.setObjectName(u"actionEdit_Texts")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_4 = QHBoxLayout(self.page)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.stackedWidget_2 = QStackedWidget(self.widget_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.blocks_page_1 = QWidget()
        self.blocks_page_1.setObjectName(u"blocks_page_1")
        self.verticalLayout_6 = QVBoxLayout(self.blocks_page_1)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.block_button_0 = QPushButton(self.blocks_page_1)
        self.block_button_0.setObjectName(u"block_button_0")
        icon = QIcon()
        icon.addFile(u"textures/00_player.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_0.setIcon(icon)
        self.block_button_0.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.block_button_0)

        self.block_button_1 = QPushButton(self.blocks_page_1)
        self.block_button_1.setObjectName(u"block_button_1")
        icon1 = QIcon()
        icon1.addFile(u"textures/01_endstone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_1.setIcon(icon1)
        self.block_button_1.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.block_button_1)

        self.block_button_2 = QPushButton(self.blocks_page_1)
        self.block_button_2.setObjectName(u"block_button_2")
        icon2 = QIcon()
        icon2.addFile(u"textures/02_water.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_2.setIcon(icon2)
        self.block_button_2.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.block_button_2)

        self.block_button_3 = QPushButton(self.blocks_page_1)
        self.block_button_3.setObjectName(u"block_button_3")
        icon3 = QIcon()
        icon3.addFile(u"textures/03_wall.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_3.setIcon(icon3)
        self.block_button_3.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.block_button_3)

        self.block_button_4 = QPushButton(self.blocks_page_1)
        self.block_button_4.setObjectName(u"block_button_4")
        icon4 = QIcon()
        icon4.addFile(u"textures/04_+bomb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_4.setIcon(icon4)
        self.block_button_4.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.block_button_4)

        self.block_button_5 = QPushButton(self.blocks_page_1)
        self.block_button_5.setObjectName(u"block_button_5")
        icon5 = QIcon()
        icon5.addFile(u"textures/05_+fire.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_5.setIcon(icon5)
        self.block_button_5.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.block_button_5)

        self.block_button_6 = QPushButton(self.blocks_page_1)
        self.block_button_6.setObjectName(u"block_button_6")
        icon6 = QIcon()
        icon6.addFile(u"textures/06_+ghost.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_6.setIcon(icon6)
        self.block_button_6.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.block_button_6)

        self.stackedWidget_2.addWidget(self.blocks_page_1)
        self.blocks_page_2 = QWidget()
        self.blocks_page_2.setObjectName(u"blocks_page_2")
        self.verticalLayout_7 = QVBoxLayout(self.blocks_page_2)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.block_button_7 = QPushButton(self.blocks_page_2)
        self.block_button_7.setObjectName(u"block_button_7")
        icon7 = QIcon()
        icon7.addFile(u"textures/07_+dynamit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_7.setIcon(icon7)
        self.block_button_7.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.block_button_7)

        self.block_button_8 = QPushButton(self.blocks_page_2)
        self.block_button_8.setObjectName(u"block_button_8")
        icon8 = QIcon()
        icon8.addFile(u"textures/08_+time_bomb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_8.setIcon(icon8)
        self.block_button_8.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.block_button_8)

        self.block_button_9 = QPushButton(self.blocks_page_2)
        self.block_button_9.setObjectName(u"block_button_9")
        icon9 = QIcon()
        icon9.addFile(u"textures/09_+heart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_9.setIcon(icon9)
        self.block_button_9.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.block_button_9)

        self.block_button_10 = QPushButton(self.blocks_page_2)
        self.block_button_10.setObjectName(u"block_button_10")
        icon10 = QIcon()
        icon10.addFile(u"textures/10_enemy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_10.setIcon(icon10)
        self.block_button_10.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.block_button_10)

        self.block_button_11 = QPushButton(self.blocks_page_2)
        self.block_button_11.setObjectName(u"block_button_11")
        icon11 = QIcon()
        icon11.addFile(u"textures/11_+sword.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_11.setIcon(icon11)
        self.block_button_11.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.block_button_11)

        self.block_button_12 = QPushButton(self.blocks_page_2)
        self.block_button_12.setObjectName(u"block_button_12")
        icon12 = QIcon()
        icon12.addFile(u"textures/12_+atomic_bomb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_12.setIcon(icon12)
        self.block_button_12.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.block_button_12)

        self.block_button_13 = QPushButton(self.blocks_page_2)
        self.block_button_13.setObjectName(u"block_button_13")
        icon13 = QIcon()
        icon13.addFile(u"textures/13_shield.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_13.setIcon(icon13)
        self.block_button_13.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.block_button_13)

        self.stackedWidget_2.addWidget(self.blocks_page_2)
        self.blocks_page_3 = QWidget()
        self.blocks_page_3.setObjectName(u"blocks_page_3")
        self.verticalLayout_8 = QVBoxLayout(self.blocks_page_3)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.block_button_14 = QPushButton(self.blocks_page_3)
        self.block_button_14.setObjectName(u"block_button_14")
        icon14 = QIcon()
        icon14.addFile(u"icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_14.setIcon(icon14)
        self.block_button_14.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.block_button_14)

        self.block_button_15 = QPushButton(self.blocks_page_3)
        self.block_button_15.setObjectName(u"block_button_15")
        icon15 = QIcon()
        icon15.addFile(u"icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_15.setIcon(icon15)
        self.block_button_15.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.block_button_15)

        self.block_button_16 = QPushButton(self.blocks_page_3)
        self.block_button_16.setObjectName(u"block_button_16")
        icon16 = QIcon()
        icon16.addFile(u"icons/move.png", QSize(), QIcon.Normal, QIcon.Off)
        self.block_button_16.setIcon(icon16)
        self.block_button_16.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.block_button_16)

        self.placeholder2 = QPushButton(self.blocks_page_3)
        self.placeholder2.setObjectName(u"placeholder2")
        self.placeholder2.setEnabled(False)
        self.placeholder2.setMinimumSize(QSize(0, 39))

        self.verticalLayout_8.addWidget(self.placeholder2)

        self.placeholder1 = QPushButton(self.blocks_page_3)
        self.placeholder1.setObjectName(u"placeholder1")
        self.placeholder1.setEnabled(False)
        self.placeholder1.setMinimumSize(QSize(0, 39))

        self.verticalLayout_8.addWidget(self.placeholder1)

        self.placeholder3 = QPushButton(self.blocks_page_3)
        self.placeholder3.setObjectName(u"placeholder3")
        self.placeholder3.setEnabled(False)
        self.placeholder3.setMinimumSize(QSize(0, 39))

        self.verticalLayout_8.addWidget(self.placeholder3)

        self.placeholder4 = QPushButton(self.blocks_page_3)
        self.placeholder4.setObjectName(u"placeholder4")
        self.placeholder4.setEnabled(False)
        self.placeholder4.setMinimumSize(QSize(0, 39))

        self.verticalLayout_8.addWidget(self.placeholder4)

        self.stackedWidget_2.addWidget(self.blocks_page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget_2)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.prev_page_btn = QPushButton(self.widget_3)
        self.prev_page_btn.setObjectName(u"prev_page_btn")
        icon17 = QIcon()
        icon17.addFile(u"icons/arrow_left.png", QSize(), QIcon.Normal, QIcon.Off)
        icon17.addFile(u"icons/arrow_left_disabled.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.prev_page_btn.setIcon(icon17)
        self.prev_page_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.prev_page_btn)

        self.next_page_btn = QPushButton(self.widget_3)
        self.next_page_btn.setObjectName(u"next_page_btn")
        self.next_page_btn.setEnabled(True)
        icon18 = QIcon()
        icon18.addFile(u"icons/arrow_right.png", QSize(), QIcon.Normal, QIcon.Off)
        icon18.addFile(u"icons/arrow_right_disabled.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.next_page_btn.setIcon(icon18)
        self.next_page_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.next_page_btn)


        self.verticalLayout_5.addWidget(self.widget_3)


        self.horizontalLayout_4.addWidget(self.widget_2)

        self.imagePainter = ImagePainterWidget(self.page)
        self.imagePainter.setObjectName(u"imagePainter")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagePainter.sizePolicy().hasHeightForWidth())
        self.imagePainter.setSizePolicy(sizePolicy)
        self.imagePainter.setMinimumSize(QSize(500, 500))

        self.horizontalLayout_4.addWidget(self.imagePainter)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 676, 44))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menuFile.sizePolicy().hasHeightForWidth())
        self.menuFile.setSizePolicy(sizePolicy1)
        self.menuFile.setTearOffEnabled(False)
        self.menuFile.setSeparatorsCollapsible(False)
        self.menuFile.setToolTipsVisible(True)
        self.menuScripts = QMenu(self.menubar)
        self.menuScripts.setObjectName(u"menuScripts")
        self.menuScripts.setTearOffEnabled(False)
        self.menuTexts = QMenu(self.menubar)
        self.menuTexts.setObjectName(u"menuTexts")
        self.menuEnemys = QMenu(self.menubar)
        self.menuEnemys.setObjectName(u"menuEnemys")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuScripts.menuAction())
        self.menubar.addAction(self.menuTexts.menuAction())
        self.menubar.addAction(self.menuEnemys.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuScripts.addAction(self.actionEdit_Scripts)
        self.menuTexts.addAction(self.actionEdit_2)
        self.menuTexts.addAction(self.actionEdit_Texts)
        self.menuEnemys.addAction(self.actionEdit_All)
        self.menuEnemys.addAction(self.actionAdit_One)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
#if QT_CONFIG(tooltip)
        self.actionSave_As.setToolTip(QCoreApplication.translate("MainWindow", u"Save As", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave_As.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionEdit_All.setText(QCoreApplication.translate("MainWindow", u"Edit All", None))
        self.actionAdit_One.setText(QCoreApplication.translate("MainWindow", u"Edit One", None))
        self.actionEdit_Scripts.setText(QCoreApplication.translate("MainWindow", u"Edit Script", None))
#if QT_CONFIG(shortcut)
        self.actionEdit_Scripts.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionEdit_2.setText(QCoreApplication.translate("MainWindow", u"New Text", None))
        self.actionEdit_Texts.setText(QCoreApplication.translate("MainWindow", u"Edit Texts", None))
        self.block_button_0.setText(QCoreApplication.translate("MainWindow", u" Player", None))
        self.block_button_1.setText(QCoreApplication.translate("MainWindow", u" Endstone", None))
        self.block_button_2.setText(QCoreApplication.translate("MainWindow", u" Water", None))
        self.block_button_3.setText(QCoreApplication.translate("MainWindow", u" Wall", None))
        self.block_button_4.setText(QCoreApplication.translate("MainWindow", u"+ Bomb", None))
        self.block_button_5.setText(QCoreApplication.translate("MainWindow", u"+ Fire", None))
        self.block_button_6.setText(QCoreApplication.translate("MainWindow", u"+ Ghost", None))
        self.block_button_7.setText(QCoreApplication.translate("MainWindow", u"+ Dynamite", None))
        self.block_button_8.setText(QCoreApplication.translate("MainWindow", u"+ Time Bomb", None))
        self.block_button_9.setText(QCoreApplication.translate("MainWindow", u"+ Heart", None))
        self.block_button_10.setText(QCoreApplication.translate("MainWindow", u" Enemy", None))
        self.block_button_11.setText(QCoreApplication.translate("MainWindow", u"+ Sword", None))
        self.block_button_12.setText(QCoreApplication.translate("MainWindow", u"+ Nuclear", None))
        self.block_button_13.setText(QCoreApplication.translate("MainWindow", u" Shield", None))
        self.block_button_14.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
#if QT_CONFIG(shortcut)
        
#endif // QT_CONFIG(shortcut)
        self.block_button_15.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.block_button_16.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.placeholder2.setText("")
        self.placeholder1.setText("")
        self.placeholder3.setText("")
        self.placeholder4.setText("")
        self.prev_page_btn.setText("")
        self.next_page_btn.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuScripts.setTitle(QCoreApplication.translate("MainWindow", u"Scripts", None))
        self.menuTexts.setTitle(QCoreApplication.translate("MainWindow", u"Texts", None))
        self.menuEnemys.setTitle(QCoreApplication.translate("MainWindow", u"Enemys", None))
    # retranslateUi

