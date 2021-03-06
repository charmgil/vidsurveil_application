# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtMultimediaWidgets import QVideoWidget
import cv2
import os

class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(999, 749)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.first_mediaplayer = QtWidgets.QFrame(self.centralwidget)
        self.first_mediaplayer.setGeometry(QtCore.QRect(540, 0, 461, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.first_mediaplayer.sizePolicy().hasHeightForWidth())
        self.first_mediaplayer.setSizePolicy(sizePolicy)
        self.first_mediaplayer.setStyleSheet("")
        self.first_mediaplayer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.first_mediaplayer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.first_mediaplayer.setObjectName("first_mediaplayer")

        self.time_slider = QtWidgets.QSlider(self.first_mediaplayer)
        self.time_slider.setGeometry(QtCore.QRect(58, 240, 311, 31))
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")
        self.current_time_label = QtWidgets.QLabel(self.first_mediaplayer)
        self.current_time_label.setGeometry(QtCore.QRect(20, 248, 60, 16))
        self.current_time_label.setObjectName("current_time_label")
        self.time_left_label = QtWidgets.QLabel(self.first_mediaplayer)
        self.time_left_label.setGeometry(QtCore.QRect(380, 248, 60, 16))
        self.time_left_label.setObjectName("time_left_label")
        self.video_player = QVideoWidget(self.first_mediaplayer)
        self.video_player.setEnabled(True)
        self.video_player.setGeometry(QtCore.QRect(20, 7, 419, 236))
        
        self.video_player.setAutoFillBackground(False)
        self.video_player.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.video_player.setObjectName("video_player")
        self.volume_control = QtWidgets.QSlider(self.first_mediaplayer)
        self.volume_control.setGeometry(QtCore.QRect(340, 262, 101, 22))
        self.volume_control.setOrientation(QtCore.Qt.Horizontal)
        self.volume_control.setObjectName("volume_control")
        self.pauseButton = QtWidgets.QPushButton(self.first_mediaplayer)
        self.pauseButton.setGeometry(QtCore.QRect(150, 260, 31, 31))
        self.pauseButton.setAutoFillBackground(False)
        self.pauseButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pauseButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/buttons/media_buttons/pause1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon)
        self.pauseButton.setIconSize(QtCore.QSize(31, 31))
        self.pauseButton.setObjectName("pauseButton")
        self.playButton = QtWidgets.QPushButton(self.first_mediaplayer)
        self.playButton.setGeometry(QtCore.QRect(190, 260, 31, 31))
        self.playButton.setAutoFillBackground(False)
        self.playButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.playButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/buttons/media_buttons/play1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setIconSize(QtCore.QSize(31, 31))
        self.playButton.setObjectName("playButton")
        self.nextButton = QtWidgets.QPushButton(self.first_mediaplayer)
        self.nextButton.setGeometry(QtCore.QRect(229, 260, 31, 31))
        self.nextButton.setAutoFillBackground(False)
        self.nextButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.nextButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/buttons/media_buttons/next_vid1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon2)
        self.nextButton.setIconSize(QtCore.QSize(31, 31))
        self.nextButton.setObjectName("nextButton")
        self.stopButton = QtWidgets.QPushButton(self.first_mediaplayer)
        self.stopButton.setGeometry(QtCore.QRect(110, 260, 31, 31))
        self.stopButton.setAutoFillBackground(False)
        self.stopButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.stopButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/buttons/media_buttons/stop1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setIconSize(QtCore.QSize(31, 31))
        self.stopButton.setObjectName("stopButton")
        self.muteButton = QtWidgets.QPushButton(self.first_mediaplayer)
        self.muteButton.setGeometry(QtCore.QRect(278, 262, 23, 23))
        self.muteButton.setAutoFillBackground(False)
        self.muteButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.muteButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/buttons/media_buttons/mute1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.muteButton.setIcon(icon4)
        self.muteButton.setIconSize(QtCore.QSize(31, 31))
        self.muteButton.setObjectName("muteButton")
        self.volumeButton = QtWidgets.QPushButton(self.first_mediaplayer)
        self.volumeButton.setGeometry(QtCore.QRect(310, 261, 23, 23))
        self.volumeButton.setAutoFillBackground(False)
        self.volumeButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.volumeButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/buttons/media_buttons/volume1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volumeButton.setIcon(icon5)
        self.volumeButton.setIconSize(QtCore.QSize(31, 31))
        self.volumeButton.setObjectName("volumeButton")

        self.mini_viewer = QtWidgets.QFrame(self.centralwidget)
        self.mini_viewer.setGeometry(QtCore.QRect(10, 300, 991, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mini_viewer.sizePolicy().hasHeightForWidth())
        self.mini_viewer.setSizePolicy(sizePolicy)
        self.mini_viewer.setStyleSheet("\n"
"")
        self.mini_viewer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mini_viewer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mini_viewer.setObjectName("mini_viewer")
        self.timeline_1 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.timeline_1.setGeometry(QtCore.QRect(47, 77, 886, 24))
        self.timeline_1.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-color: rgb(250, 240, 242);")
        self.timeline_1.setObjectName("timeline_1")
        self.mini_view_1 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.mini_view_1.setGeometry(QtCore.QRect(47, 107, 886, 86))
        self.mini_view_1.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-color: rgb(146, 130, 229);")
        self.mini_view_1.setObjectName("mini_view_1")
        self.timeline_2 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.timeline_2.setGeometry(QtCore.QRect(47, 217, 886, 24))
        self.timeline_2.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-left-color: rgb(255, 150, 150);\n"
                                        "border-right-color: rgb(255, 255, 255);\n"
                                        "border-top-color: rgb(255, 255, 255);\n"
                                        "border-bottom-color: rgb(255, 255, 255);\n")
        self.timeline_2.setObjectName("timeline_2")
        self.mini_view_2 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.mini_view_2.setGeometry(QtCore.QRect(47, 317, 886, 86))
        self.mini_view_2.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-color: rgb(146, 130, 229);")
        self.mini_view_2.setObjectName("mini_view_2")

        # a button to extract videos
        self.push_extract_1 = QtWidgets.QPushButton(self.mini_viewer)
        self.push_extract_1.setGeometry(QtCore.QRect(40, 20, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_extract_1.sizePolicy().hasHeightForWidth())
        self.push_extract_1.setSizePolicy(sizePolicy)
        self.push_extract_1.setStyleSheet("")
        self.push_extract_1.setObjectName("push_extract_1")

        # a button for displaying anomalous time line
        self.push_extract_2 = QtWidgets.QPushButton(self.mini_viewer)
        self.push_extract_2.setGeometry(QtCore.QRect(200, 20, 141, 31))
        self.push_extract_2.setSizePolicy(sizePolicy)
        self.push_extract_2.setStyleSheet("")
        self.push_extract_2.setObjectName("push_extract_2")

        self.timeline_3 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.timeline_3.setGeometry(QtCore.QRect(47, 252, 886, 24))
        self.timeline_3.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-left-color: rgb(150, 255, 150);\n"
                                        "border-right-color: rgb(255, 255, 255);\n"
                                        "border-top-color: rgb(255, 255, 255);\n"
                                        "border-bottom-color: rgb(255, 255, 255);\n")
        self.timeline_3.setObjectName("timeline_3")
        self.timeline_4 = QtWidgets.QGraphicsView(self.mini_viewer)
        self.timeline_4.setGeometry(QtCore.QRect(47, 287, 886, 24))
        self.timeline_4.setStyleSheet("border-style: solid;\n"
                                        "border-width: 3px;\n"
                                        "border-left-color: rgb(150, 150, 255);\n"
                                        "border-right-color: rgb(255, 255, 255);\n"
                                        "border-top-color: rgb(255, 255, 255);\n"
                                        "border-bottom-color: rgb(255, 255, 255);")
        self.timeline_4.setObjectName("timeline_4")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.mini_viewer)
        self.lcdNumber_1.setGeometry(QtCore.QRect(20, 50, 64, 23))
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.lcdNumber_1.setStyleSheet("border-style: transparent;\n"
                                        "color: rgb(146, 130, 229); ")
        #self.lcdNumber.display('10:00')                                
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.mini_viewer)
        self.lcdNumber_2.setGeometry(QtCore.QRect(242, 50, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.setStyleSheet("border-style: transparent;\n"
                                        "color: rgb(146, 130, 229); ")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.mini_viewer)
        self.lcdNumber_4.setGeometry(QtCore.QRect(465, 50, 64, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_4.setStyleSheet("border-style: transparent;\n"
                                        "color: rgb(146, 130, 229); ")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.mini_viewer)
        self.lcdNumber_5.setGeometry(QtCore.QRect(688, 50, 64, 23))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_5.setStyleSheet("border-style: transparent;\n"
                                        "color: rgb(146, 130, 229); ")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.mini_viewer)
        self.lcdNumber_6.setGeometry(QtCore.QRect(910, 50, 64, 23))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_6.setStyleSheet("border-style: transparent;\n"
                                        "color: rgb(146, 130, 229); ")
        self.textEdit = QtWidgets.QTextEdit(self.mini_viewer)
        self.textEdit.setGeometry(QtCore.QRect(500, 20, 441, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("background-color: transparent;")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 511, 301))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1.sizePolicy().hasHeightForWidth())
        self.tab1.setSizePolicy(sizePolicy)
        self.tab1.setObjectName("tab1")
        self.playlistView = QtWidgets.QListView(self.tab1)
        self.playlistView.setEnabled(True)
        self.playlistView.setGeometry(QtCore.QRect(0, 0, 511, 271))
        self.playlistView.setObjectName("playlistView")
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.treeView2 = QtWidgets.QTreeView(self.tab_2)
        self.treeView2.setGeometry(QtCore.QRect(0, 0, 511, 271))
        self.treeView2.setAcceptDrops(True)
        self.treeView2.setObjectName("treeView2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.treeView2_2 = QtWidgets.QTreeView(self.tab)
        self.treeView2_2.setGeometry(QtCore.QRect(0, 0, 511, 271))
        self.treeView2_2.setAcceptDrops(True)
        self.treeView2_2.setObjectName("treeView2_2")
        
        ## button to run models
        self.run_mil_button = QtWidgets.QPushButton(self.tab)
        self.run_mil_button.setEnabled(True)
        self.run_mil_button.setGeometry(QtCore.QRect(80, 10, 112, 32))
        self.run_mil_button.setObjectName("run_mil_button")

        self.run_ffpa_button = QtWidgets.QPushButton(self.tab)
        self.run_ffpa_button.setEnabled(True)
        self.run_ffpa_button.setGeometry(QtCore.QRect(200, 10, 112, 32))
        self.run_ffpa_button.setObjectName("run_ffpa_button")

        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 999, 22))
        self.menuBar.setToolTipDuration(0)
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuFiles = QtWidgets.QMenu(self.menuBar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuVidsurveil = QtWidgets.QMenu(self.menuBar)
        self.menuVidsurveil.setObjectName("menuVidsurveil")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionAdd_Files = QtWidgets.QAction(MainWindow)
        self.actionAdd_Files.setCheckable(True)
        self.actionAdd_Files.setChecked(False)
        self.actionAdd_Files.setObjectName("actionAdd_Files")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionLicense)
        self.menuFiles.addAction(self.actionAdd_Files)
        self.menuVidsurveil.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuVidsurveil.menuAction())
        self.menuBar.addAction(self.menuFiles.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#faf0f2;\">⬤</span><span style=\" color:#ee5262;\"> </span><span style=\" font-size:20pt; font-weight:600; color:#000000; vertical-align:sub;\">Combined     </span><span style=\" color:#ff9696;\">⬤</span><span style=\" color:#96ff96;\"> </span><span style=\" font-size:20pt; font-weight:600; color:#000000; vertical-align:sub;\">MIL+C3D</span><span style=\" font-size:20pt; color:#000000; vertical-align:sub;\">      </span><span style=\" color:#96ff96;\">⬤</span><span style=\" font-size:20pt; color:#ee5262; vertical-align:sub;\"> </span><span style=\" font-size:20pt; font-weight:600; color:#000000; vertical-align:sub;\">Future Frame     </span><span style=\" color:#9696ff;\">⬤</span><span style=\" color:#ee5262;\"> </span><span style=\" font-size:20pt; font-weight:600; color:#000000; vertical-align:sub;\">MNAD</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; color:#000000; vertical-align:sub;\"><br /></p></body></html>"))
        self.current_time_label.setText(_translate("MainWindow", "0:00"))
        self.time_left_label.setText(_translate("MainWindow", "0:00"))
        self.push_extract_1.setText(_translate("MainWindow", "Extract Videos"))
        self.push_extract_2.setText(_translate("MainWindow", "Show Anomalous Time"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Original Videos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Extracted Videos"))
        self.run_mil_button.setText(_translate("MainWindow", "Run MIL"))
        self.run_ffpa_button.setText(_translate("MainWindow", "Run FFPA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Model"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuVidsurveil.setTitle(_translate("MainWindow", "Vidsurveil"))
        self.actionLicense.setText(_translate("MainWindow", "License"))
        self.actionAdd_Files.setText(_translate("MainWindow", "Add Files"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
   
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
