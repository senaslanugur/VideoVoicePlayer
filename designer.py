# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:12:59 2022

@author: usenaslan

"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
import vlc
import time

class Ui_main_page(object):

    def setupUi(self, main_page):
        main_page.setObjectName("main_page")
        main_page.resize(750, 650)
        main_page.setMinimumSize(QtCore.QSize(750, 650))
        main_page.setMaximumSize(QtCore.QSize(750, 650))
        main_page.setAutoFillBackground(False)
        main_page.setStyleSheet("background-color:#2b2b2b;")
        self.centralwidget = QtWidgets.QWidget(main_page)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 140, 681, 371))
        self.frame.setMinimumSize(QtCore.QSize(681, 371))
        self.frame.setMaximumSize(QtCore.QSize(681, 371))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:white;\n"
"border-radius:50%;")
        self.frame.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(10)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 70, 128, 128))
        self.label.setMinimumSize(QtCore.QSize(128, 128))
        self.label.setMaximumSize(QtCore.QSize(128, 128))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("youtube.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.audio_btn = QtWidgets.QPushButton(self.frame)
        self.audio_btn.setGeometry(QtCore.QRect(400, 140, 201, 46))
        self.audio_btn.setMinimumSize(QtCore.QSize(201, 46))
        self.audio_btn.setMaximumSize(QtCore.QSize(201, 46))
        font = QtGui.QFont()
        font.setFamily("inherit")
        font.setBold(True)
        font.setWeight(62)
        self.audio_btn.setFont(font)
        self.audio_btn.setStyleSheet("QPushButton{\n"
"     outline: 0;\n"
"     border: 0;\n"
"     background: none;\n"
"     border: 2px solid #d9d9d9;\n"
"     padding: 8px 0px;\n"
"     margin-bottom: 5px;\n"
"     color: #515151;\n"
"     text-transform: uppercase;\n"
"     width: 130px;\n"
"     font-family: inherit;\n"
"     margin-right: 5px;\n"
"     transition: all 0.3s ease;\n"
"     font-weight: 500;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"     border: 3px solid #ade8f4;\n"
"     color:     white;\n"
"     cursor: pointer;\n"
"     background-color: #00b4d8;\n"
"}")
        self.audio_btn.setObjectName("audio_btn")
        self.video_btn = QtWidgets.QPushButton(self.frame)
        self.audio_btn.clicked.connect(self.get_audio_file)
        self.video_btn.setGeometry(QtCore.QRect(400, 70, 201, 46))
        self.video_btn.setMinimumSize(QtCore.QSize(201, 46))
        self.video_btn.setMaximumSize(QtCore.QSize(241, 46))
        font = QtGui.QFont()
        font.setFamily("inherit")
        font.setBold(True)
        font.setWeight(62)
        self.video_btn.setFont(font)
        self.video_btn.setStyleSheet("QPushButton{\n"
"     outline: 0;\n"
"     border: 0;\n"
"     background: none;\n"
"     border: 2px solid #d9d9d9;\n"
"     padding: 8px 0px;\n"
"     margin-bottom: 5px;\n"
"     color: #515151;\n"
"     text-transform: uppercase;\n"
"     width: 130px;\n"
"     font-family: inherit;\n"
"     margin-right: 5px;\n"
"     transition: all 0.3s ease;\n"
"     font-weight: 500;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"     border: 3px solid #ade8f4;\n"
"     color:     white;\n"
"     cursor: pointer;\n"
"    background-color: #00b4d8;\n"
"}")
        self.video_btn.setObjectName("video_btn")
        self.video_btn.clicked.connect(self.get_video_file)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 220, 251, 71))
        self.label_2.setMinimumSize(QtCore.QSize(251, 71))
        self.label_2.setMaximumSize(QtCore.QSize(251, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("     color: #515151;\n"
"     font-weight: bold;\n"
"     margin: 0;\n"
"     font-size: 20px;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(340, 20, 1, 331))
        self.line.setStyleSheet("background-color:#2b2b2b;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(360, 250, 289, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dinle_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.dinle_btn.setMinimumSize(QtCore.QSize(140, 46))
        self.dinle_btn.setMaximumSize(QtCore.QSize(140, 46))
        font = QtGui.QFont()
        font.setFamily("inherit")
        font.setBold(True)
        font.setWeight(62)
        self.dinle_btn.setFont(font)
        self.dinle_btn.setStyleSheet("QPushButton{\n"
"     outline: 0;\n"
"     border: 0;\n"
"     background: none;\n"
"     border: 2px solid #d9d9d9;\n"
"     padding: 8px 0px;\n"
"     margin-bottom: 5px;\n"
"     color: #515151;\n"
"     text-transform: uppercase;\n"
"     width: 130px;\n"
"     font-family: inherit;\n"
"     margin-right: 5px;\n"
"     transition: all 0.3s ease;\n"
"     font-weight: 500;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"     border: 3px solid #d8f3dc;\n"
"     color:white ;\n"
"     cursor: pointer;\n"
"     background-color:#52b788;\n"
"    \n"
"}")
        self.dinle_btn.setObjectName("dinle_btn")
        self.horizontalLayout.addWidget(self.dinle_btn)
        self.dinle_btn.clicked.connect(self.get_dinle)
        self.bitir_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.bitir_btn.setMinimumSize(QtCore.QSize(140, 46))
        self.bitir_btn.setMaximumSize(QtCore.QSize(140, 46))
        font = QtGui.QFont()
        font.setFamily("inherit")
        font.setBold(True)
        font.setWeight(62)
        self.bitir_btn.setFont(font)
        self.bitir_btn.setStyleSheet("QPushButton{\n"
"     outline: 0;\n"
"     border: 0;\n"
"     background: none;\n"
"     border: 2px solid #d9d9d9;\n"
"     padding: 8px 0px;\n"
"     margin-bottom: 5px;\n"
"     color: #515151;\n"
"     text-transform: uppercase;\n"
"     width: 130px;\n"
"     font-family: inherit;\n"
"     margin-right: 5px;\n"
"     transition: all 0.3s ease;\n"
"     font-weight: 500;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"     border: 3px solid #ff8fa3;\n"
"     color:     white;\n"
"     cursor: pointer;\n"
"    background-color:#ff4d6d;\n"
"\n"
"}")
        self.bitir_btn.setObjectName("bitir_btn")
        self.horizontalLayout.addWidget(self.bitir_btn)
        self.bitir_btn.clicked.connect(self.get_bitir)
        main_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_page)
        QtCore.QMetaObject.connectSlotsByName(main_page)

    def retranslateUi(self, main_page):
        _translate = QtCore.QCoreApplication.translate
        main_page.setWindowTitle(_translate("main_page", "Video-Audio Combine"))
        self.audio_btn.setText(_translate("main_page", "AUDIO"))
        self.video_btn.setText(_translate("main_page", " VIDEO"))
        self.label_2.setText(_translate("main_page", "VIDEO AUDIO PLAYER"))
        self.dinle_btn.setText(_translate("main_page", "PLAY"))
        self.bitir_btn.setText(_translate("main_page", "STOP and CLOSE"))
        
    video_path = ""
    audio_path = ""
    
    def get_video_file(self):
        
        filename = QFileDialog.getOpenFileName()
        
        Ui_main_page.video_path = filename[0]
        
        print("image file name, ", filename[0])
        
    def get_audio_file(self):
        
        filename = QFileDialog.getOpenFileName()
        
        Ui_main_page.audio_path = filename[0]
        
        print("audio file name, ", filename[0])
        
    
    def get_dinle(self):
    
        
        if len(Ui_main_page.video_path) == 0 or len(Ui_main_page.audio_path) == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Video or Audio Source Selection Missing !")
            x = msg.exec_()
            
        else:
            mpeg = Ui_main_page.video_path.split(".")
            mpeg = mpeg[1]
            
            ses = Ui_main_page.audio_path.split(".")
            ses = ses[1]

        
            if mpeg != "mpeg" and ses !="wav" and ses !="mp3":
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("The Extension of the video/ File you choose should be 'mpeg' and the Extension of the Audio Source should be 'wav/mp3'!")
                x = msg.exec_()
                
            elif mpeg != "mpeg":
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("The Extension of the Video/ File You Choose Must Be 'mpeg' !")
                x = msg.exec_()
                
            elif ses !="wav" and ses !="mp3":
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("The Extension of the Audio Source you have chosen should be 'wav/mp3' !")
                x = msg.exec_()       
                
            else:   
                print("Folder-1, ", Ui_main_page.video_path)
                print("Folder-2, ", Ui_main_page.audio_path)
                
                media_player_video = vlc.MediaPlayer()
                media_player_audio = vlc.MediaPlayer()
        
                
                media_video = vlc.Media(Ui_main_page.video_path)
                media_audio = vlc.Media(Ui_main_page.audio_path)
        
                
                media_player_video.set_media(media_video)
                media_player_audio.set_media(media_audio)
        
        
                
                media_player_video.play()
                media_player_video.audio_set_mute(True)
                media_player_video.set_fullscreen(True)
                time.sleep(1)
                media_player_audio.play()
        
    def get_bitir(self):
        print("Program Closing")
        vlc.MediaPlayer().stop()
        app = QtWidgets.QApplication(sys.argv)
        sys.exit(app.exec_())

        
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_page = QtWidgets.QMainWindow()
    ui = Ui_main_page()
    ui.setupUi(main_page)
    main_page.show()
    sys.exit(app.exec_())

