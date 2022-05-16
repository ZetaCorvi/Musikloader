import os
from PyQt5.QtWidgets import QWidget, QStyle, QComboBox, QSlider, QPushButton
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class PlayMusicWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.files = os.listdir(os.getcwd() + "/Musik")
        self.list_of_music.addItems(self.files)

    files = []
    def playAudio(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.player.pause()
        else:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
            self.player.play()

    def stopAudio(self):
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.player.stop()

    def setPosition(self, position):
        self.player.setPosition(position)

    def positionChanged(self, position):
        self.slider.setValue(position)

    def durationChanged(self, duration):
        self.slider.setRange(0, duration)

    def volumeChanged(self, volume):
        self.player.setVolume(volume)

    filename = ""
    def getMusicFile(self, name):
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.filename = name
        fullname = os.path.join(os.getcwd() + "/Musik", self.filename)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(fullname)))
        self.play_button.setEnabled(True)

    def initUI(self):
        self.player = QMediaPlayer(self)

        self.list_of_music = QComboBox(self)
        self.list_of_music.resize(400, 20)
        self.list_of_music.move(100, 0)
        self.list_of_music.activated[str].connect(self.getMusicFile)

        '''Ползунок для перемотки музыки'''
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.resize(300, 50)
        self.slider.move(150, 200)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.setPosition)

        '''Начальная громкость'''
        self.current_volume = 30
        self.player.setVolume(self.current_volume)

        '''Ползунок громкости'''
        self.volume_slider = QSlider(Qt.Vertical, self)
        self.volume_slider.resize(30, 100)
        self.volume_slider.move(400, 250)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(self.current_volume)
        self.volume_slider.sliderMoved.connect(self.volumeChanged)

        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)

        '''Кнопка проигрывания и остановки музыки'''
        self.play_button = QPushButton(self)
        self.play_button.resize(100, 50)
        self.play_button.move(250, 300)
        self.play_button.clicked.connect(self.playAudio)
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_button.setEnabled(False)

        '''Кнопка выхода'''
        self.exit_button = QPushButton("Выход", self)
        self.exit_button.resize(100, 50)
        self.exit_button.move(250, 500)
        self.exit_button.clicked.connect(self.stopAudio)
