from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
import youtube_dl
import download_ydl
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class DownloadMusicWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def DownloadMusik(self):
        ''' example youtube music video
        https://www.youtube.com/watch?v=sZWOq2mleBY #Et si tu n'existais pas
        https://www.youtube.com/watch?v=dQw4w9WgXcQ #Never Gonna Give You Up
        '''
        url = self.url_field.text()

        with youtube_dl.YoutubeDL(download_ydl.ydl_opts) as ydl:
            ydl.download([url])

        CompleteLabel = QLabel(self)
        CompleteLabel.resize(500, 50)
        CompleteLabel.move(50, 300)
        CompleteLabel.setText("Скачивание завершено")
        CompleteLabel.setAlignment(Qt.AlignHCenter)
        CompleteLabel.setFont(QFont("Arial font", 20))
        CompleteLabel.show()


    def initUI(self):
        '''Поле для ввода ссылки на youtube'''
        self.url_field = QLineEdit(self)
        self.url_field.move(100, 50)
        self.url_field.resize(400, 20)

        '''Кнопка скачивания по ссылке'''
        DownloadButton = QPushButton(self)
        DownloadButton.resize(100, 50)
        DownloadButton.move(250, 100)
        DownloadButton.setText("Скачать")
        DownloadButton.clicked.connect(self.DownloadMusik)

        self.exitButton = QPushButton("Выход", self)
        self.exitButton.resize(100, 50)
        self.exitButton.move(250, 500)
