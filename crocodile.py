'''Simply python game 'Crocodile' for guess words. Images in the project - "Crocodile Cartoon Mascot Character" by Chud Tsankov (https://www.behance.net/gallery/23033339/Crocodile-Cartoon-Mascot-Character)'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import random

words = ['Hiccup', 'Rainbow', 'Slippery', 'Coffee', 'Helicopter', 'Giraffe', 'Garden', 'Measure', 'Sunshine', 'Hurt',
         'Stubbed toe', 'Limbo', 'Light bulb', 'Ladder', 'Shopping', 'Shoelaces', 'Shuffle', 'Banana peel', 'Hungry',
         'Surprise', 'Singer', 'River danceSick', 'Mash', 'Yo-yo', 'Spider', 'Monster', 'Mirror', 'Window', 'Fishing',
         'Heavy', 'Dinosaur', 'The Lion King', 'Clown', 'River dance', 'Slice', 'Nosey', 'ating', 'Hot dog', 'Smear',
         'Hurricane', 'Swing', 'Cheers', 'Trampoline', 'Balloon', 'Drool', 'Waterfall', 'Skateboard', 'Pirate',
         'President', 'Magic', 'Wizard of Oz', 'Strong', 'Fart', 'Macarena', 'Tap dance', 'Kite', 'Bright', 'Haircut',
         'Blanket', 'Deer', 'Karate', 'Nightmare', 'Halo', 'Fight Club', 'Book', 'Ice skating', 'Excitement',
         'Flashlight', 'Overwhelmed', 'Soccer', 'Sword', 'Makeup', 'Wheelbarrow', 'Firefighter', 'Cradle', 'Gallop',
         'Electric Slide', 'Paint', 'Read', 'Button', 'Balance beam', 'Christmas', 'Light', 'Braces', 'Car',
         'Motorcycle', 'Marriage', 'Shadow', 'Disco', 'Bump', 'Ballet', 'Pancakes', 'Dizzy'] #here you can add another words


class Ui_MainWindow(object): #start window
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QLabel{\n"
                                 "background-color: None\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLabel{\n"
                                         "background-color: None\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 581))
        font = QtGui.QFont()
        font.setFamily("FabfeltScript Bold")
        font.setPointSize(36)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: white;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(340, 30, 501, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/main.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 401, 171))
        font = QtGui.QFont()
        font.setFamily("FabfeltScript Bold")
        font.setPointSize(80)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
                                   "background-color: None;\n"
                                   "color: rgb(65, 131, 0);\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(320, 160, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
                                   "background-color: None;\n"
                                   "color: rgb(175, 1, 152);\n"
                                   "}")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 420, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Cyrillic")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(68, 136, 0);\n"
                                      "color: white;\n"
                                      "border-radius: 10px;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def start(self):
        self.RulesWindow = QtWidgets.QMainWindow()
        self.rules_ui = Rules()
        self.rules_ui.setupUi(self.RulesWindow)
        self.RulesWindow.show()
        MainWindow.close()
        print('start')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Crocodile"))
        self.label_3.setText(_translate("MainWindow", "game"))
        self.pushButton.setText(_translate("MainWindow", "Push to start!"))


class Rules(object): #next window (rules)
    def setupUi(self, MainWindow):
        self.ruleswindow = MainWindow
        self.ruleswindow.setObjectName("MainWindow")
        self.ruleswindow.resize(800, 597)
        self.ruleswindow.setStyleSheet("QLabel{\n"
                                       "background-color: None\n"
                                       "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLabel{\n"
                                         "background-color: None\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 581))
        font = QtGui.QFont()
        font.setFamily("FabfeltScript Bold")
        font.setPointSize(36)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: white;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(340, 0, 101, 101))
        font = QtGui.QFont()
        font.setFamily("FabfeltScript Bold")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(68, 136, 0);")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 47, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/paw.svg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 47, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/paw.svg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 270, 47, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/paw.svg"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 350, 47, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("img/paw.svg"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(100, 110, 671, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(100, 190, 671, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(100, 280, 671, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(100, 360, 671, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(250, 450, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Cyrillic")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(68, 136, 0);\n"
                                      "color: white;\n"
                                      "border-radius: 10px;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.BackButton = QtWidgets.QPushButton(self.frame)
        self.BackButton.setGeometry(QtCore.QRect(10, 0, 81, 81))
        self.BackButton.setStyleSheet("background-color: white; border-radius: 10px;")
        self.BackButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon)
        self.BackButton.setIconSize(QtCore.QSize(50, 50))
        self.BackButton.setAutoRepeat(False)
        self.BackButton.setObjectName("BackButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.BackButton.clicked.connect(self.go_back)
        self.pushButton.clicked.connect(self.start_game)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def go_back(self):
        self.StartWindow = QtWidgets.QMainWindow()
        self.start_ui = Ui_MainWindow()
        self.start_ui.setupUi(self.StartWindow)
        self.StartWindow.show()
        self.ruleswindow.close()
        print('back')

    def start_game(self):
        self.GameWindow = QtWidgets.QMainWindow()
        self.game_ui = Game()
        self.game_ui.setupUi(self.GameWindow)
        self.GameWindow.show()
        self.ruleswindow.close()
        print('start game')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Rules:"))
        self.label_6.setText(_translate("MainWindow", "You\'ll see the word what you have to show to other members"))
        self.label_7.setText(_translate("MainWindow", "You\'ll have 3 minutes"))
        self.label_8.setText(_translate("MainWindow", "No sounds! Only facial expressions and gestures :)"))
        self.label_9.setText(_translate("MainWindow", "Who has guessed - shows the next one"))
        self.pushButton.setText(_translate("MainWindow", "Let\'s start!"))


class Game(object): #game's window
    def setupUi(self, MainWindow):
        self.gamewindow = MainWindow
        self.gamewindow.setObjectName("MainWindow")
        self.gamewindow.resize(800, 595)
        self.gamewindow.setStyleSheet("QLabel{\n"
                                      "background-color: None\n"
                                      "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLabel{\n"
                                         "background-color: None\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 581))
        font = QtGui.QFont()
        font.setFamily("FabfeltScript Bold")
        font.setPointSize(36)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: rgb(221, 244, 202);\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.timer = QTimer()
        self.GoButton = QtWidgets.QPushButton(self.frame)
        self.GoButton.setGeometry(QtCore.QRect(360, 460, 95, 95))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Cyrillic")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.GoButton.setFont(font)
        self.GoButton.setStyleSheet("QPushButton{\n"
                                    "background-color: rgb(68, 136, 0);\n"
                                    "color: white;\n"
                                    "border-radius: 45;\n"
                                    "}")
        self.GoButton.setObjectName("GoButton")
        self.GuessText = QtWidgets.QLabel(self.frame)
        self.GuessText.setGeometry(QtCore.QRect(170, 190, 441, 191))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Cyrillic")
        font.setPointSize(60)
        self.GuessText.setFont(font)
        self.GuessText.setStyleSheet("color: rgb(68, 136, 0);")
        self.GuessText.setAlignment(QtCore.Qt.AlignCenter)
        self.GuessText.setObjectName("GuessText")
        self.Chrono = QtWidgets.QLabel(self.frame)
        self.Chrono.setGeometry(QtCore.QRect(330, 20, 131, 161))
        self.Chrono.setText("")
        self.Chrono.setPixmap(QtGui.QPixmap("img/clock.png"))
        self.Chrono.setScaledContents(True)
        self.Chrono.setObjectName("Chrono")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 370, 141, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/croco_game.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(350, 90, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(68, 136, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.ExitButton = QtWidgets.QPushButton(self.frame)
        self.ExitButton.setGeometry(QtCore.QRect(740, 10, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Cyrillic")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgb(255, 3, 49);\n"
                                      "color: white;\n"
                                      "border-radius: 25%;\n"
                                      "}")
        self.ExitButton.setObjectName("ExitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.counter = 181
        self.seconds = '181'
        # timer

        self.retranslateUi(MainWindow)
        self.GoButton.clicked.connect(self.game)
        self.GoButton.clicked.connect(self.startTimer)
        self.ExitButton.clicked.connect(self.exit_game)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showTime(self):
        self.counter -= 1
        self.label_2.setText(str(self.counter))
        if self.counter == 0:
            self.timer.stop()
            self.Chrono.setPixmap(QtGui.QPixmap("img/clock_red.png"))
            self.label_2.setStyleSheet("color: #FF0F0F")

    def startTimer(self):
        self.timer.start(1000)
        if self.GoButton.clicked:
            self.counter = 181
            self.Chrono.setPixmap(QtGui.QPixmap("img/clock.png"))
            self.label_2.setStyleSheet("color: rgb(68, 136, 0);")

    def game(self):
        self.GuessText.setText(random.choice(words))
        self.GoButton.setText('Next')
        self.GuessText.setStyleSheet("color: rgb(255, 85, 0);")

    def exit_game(self):
        self.ToMainWindow = QtWidgets.QMainWindow()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self.ToMainWindow)
        self.ToMainWindow.show()
        self.gamewindow.close()
        print('start')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.GoButton.setText(_translate("MainWindow", "Go!"))
        self.GuessText.setText(_translate("MainWindow", "Are you ready?"))
        self.label_2.setText(_translate("MainWindow", "180"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
