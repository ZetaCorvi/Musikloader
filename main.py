from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow, QStackedWidget, QApplication
import sys
import DownloadMusic
import PlayMusic
import EditMetadata
import EditMusic


class MainWindow(QWidget):
    '''Класс главного меню'''
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        '''Кнопки для перехода в соответсвующие окна'''
        self.button_1 = QPushButton("Скачать музыку", self)
        self.button_1.resize(200, 50)
        self.button_1.move(200, 50)

        self.button_2 = QPushButton("Слушать музыку", self)
        self.button_2.resize(200, 50)
        self.button_2.move(200, 150)

        self.button_3 = QPushButton("Редактировать музыку", self)
        self.button_3.resize(200, 50)
        self.button_3.move(200, 250)

        self.button_4 = QPushButton("Редактировать метаданные", self)
        self.button_4.resize(200, 50)
        self.button_4.move(200, 350)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stackWidget = QStackedWidget()
        self.setCentralWidget(self.stackWidget)

        self.initUI()

    def OpenDownload(self):
        '''Открывает окно скачивания музыки'''
        self.stackWidget.setCurrentIndex(1)

    def OpenPlay(self):
        '''Открывает окно сохранения музыки'''
        self.stackWidget.setCurrentIndex(2)

    def OpenEditMusic(self):
        '''Открывает окно редактирования музыки'''
        self.stackWidget.setCurrentIndex(3)

    def OpenMeta(self):
        '''Открывает окно редактирования метаданных'''
        self.stackWidget.setCurrentIndex(4)

    def exitWin(self):
        self.stackWidget.setCurrentIndex(0)

    def initUI(self):
        '''Параметры окна'''
        self.resize(600, 600)
        self.setWindowTitle("MusicLoader")

        '''Создание главного окна'''
        self.mainWin = MainWindow()

        '''Присоединение методов перехода к кнопкам'''
        self.mainWin.button_1.clicked.connect(self.OpenDownload)
        self.mainWin.button_2.clicked.connect(self.OpenPlay)
        self.mainWin.button_3.clicked.connect(self.OpenEditMusic)
        self.mainWin.button_4.clicked.connect(self.OpenMeta)

        '''Создание объектов окон'''
        self.downMusic = DownloadMusic.DownloadMusicWin()
        self.playMusic = PlayMusic.PlayMusicWin()
        self.editMusic = EditMusic.EditMusicWin()
        self.editMeta = EditMetadata.MetadataWin()

        '''Кнопки выхода в главное меню'''
        self.downMusic.exitButton.clicked.connect(self.exitWin)
        self.playMusic.exit_button.clicked.connect(self.exitWin)
        self.editMusic.exitButton.clicked.connect(self.exitWin)
        self.editMeta.exitButton.clicked.connect(self.exitWin)

        '''Добавление окон в стек виджетов'''
        self.stackWidget.addWidget(self.mainWin)
        self.stackWidget.addWidget(self.downMusic)
        self.stackWidget.addWidget(self.playMusic)
        self.stackWidget.addWidget(self.editMusic)
        self.stackWidget.addWidget(self.editMeta)

        self.stackWidget.setCurrentIndex(0)

        self.show()


'''Основной цикл программы'''
app = QApplication(sys.argv)

QSS = """
QSlider::groove:horizontal {
    border-radius: 1px;       
    height: 7px;              
    margin: -1px 0;           
}
QSlider::handle:horizontal {
    background-color: rgb(255, 0, 0);
    border: 2px solid #ff0000;
    height: 14px;     
    width: 12px;
    margin: -4px 0;     
    border-radius: 7px  ;
    padding: -4px 0px;  
}
QSlider::add-page:horizontal {
    background: darkgray;
}
QSlider::sub-page:horizontal {
    background: red;
}
"""

app.setStyleSheet(QSS)

win = Window()

sys.exit(app.exec_())
