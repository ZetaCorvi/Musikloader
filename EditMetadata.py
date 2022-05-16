from PyQt5.QtWidgets import QWidget, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class MetadataWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def ShowSaveMetaMP3(self):
        '''Отображает статус смены метаданных'''
        self.CompleteText.setText("Метаданные изменены на MP3")

    def ShowSaveMetaWAV(self):
        '''Отображает статус смены метаданных'''
        self.CompleteText.setText("Метаданные изменены на WAV")

    def ShowSaveMetaAIFF(self):
        '''Отображает статус смены метаданных'''
        self.CompleteText.setText("Метаданные изменены на AIFF")

    def ShowSaveMetaAPE(self):
        '''Отображает статус смены метаданных'''
        self.CompleteText.setText("Метаданные изменены на APE")

    def ShowSaveMetaFLAC(self):
        '''Отображает статус смены метаданных'''
        self.CompleteText.setText("Метаданные изменены на FLAC")

    def initUI(self):
        '''Кнопки для смены формата файлов'''
        mp3_button = QPushButton(self)
        mp3_button.resize(100, 50)
        mp3_button.move(150, 100)
        mp3_button.setText("MP3")
        mp3_button.clicked.connect(self.ShowSaveMetaMP3)

        wav_button = QPushButton(self)
        wav_button.resize(100, 50)
        wav_button.move(250, 100)
        wav_button.setText("WAV")
        wav_button.clicked.connect(self.ShowSaveMetaWAV)

        aiff_button = QPushButton(self)
        aiff_button.resize(100, 50)
        aiff_button.move(350, 100)
        aiff_button.setText("AIFF")
        aiff_button.clicked.connect(self.ShowSaveMetaAIFF)

        ape_button = QPushButton(self)
        ape_button.resize(100, 50)
        ape_button.move(150, 200)
        ape_button.setText("APE")
        ape_button.clicked.connect(self.ShowSaveMetaAPE)

        flac_button = QPushButton(self)
        flac_button.resize(100, 50)
        flac_button.move(250, 200)
        flac_button.setText("FLAC")
        flac_button.clicked.connect(self.ShowSaveMetaFLAC)

        self.CompleteText = QLabel(self)
        self.CompleteText.resize(500, 50)
        self.CompleteText.move(50, 300)
        self.CompleteText.setAlignment(Qt.AlignHCenter)
        self.CompleteText.setFont(QFont("Arial font", 20))
        self.CompleteText.show()

        self.exitButton = QPushButton("Выход", self)
        self.exitButton.resize(100, 50)
        self.exitButton.move(250, 500)
