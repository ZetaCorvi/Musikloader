from PyQt5.QtWidgets import QWidget, QPushButton, QSlider, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class EditMusicWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def CutDelete(self):
        '''Вырезает музыку'''
        self.message.setText("Вырезано")

    def Cut(self):
        '''Обрезает музыку'''
        self.message.setText("Обрезано")

    def Save(self):
        '''Сохраняет полученный в результате преобразований аудиофайл'''
        self.message.setText("Сохранено")

    def SpeedUp(self):
        '''Вырезает музыку'''
        self.message.setText("Ускорено")

    def SpeedDown(self):
        '''Вырезает музыку'''
        self.message.setText("Замедленно")

    def initUI(self):
        '''Кнопка вырезания музыки'''
        CutDeleteButton = QPushButton(self)
        CutDeleteButton.resize(100, 50)
        CutDeleteButton.move(150, 250)
        CutDeleteButton.setText("Вырезать")
        CutDeleteButton.clicked.connect(self.CutDelete)

        '''Кнопка обрезания музыки'''
        CutButton = QPushButton(self)
        CutButton.resize(100, 50)
        CutButton.move(250, 250)
        CutButton.setText("Обрезать")
        CutButton.clicked.connect(self.Cut)

        '''Кнопка сохроанения преобразованного аудифайла'''
        SaveButton = QPushButton(self)
        SaveButton.resize(100, 50)
        SaveButton.move(350, 250)
        SaveButton.setText("Сохранить")
        SaveButton.clicked.connect(self.Save)

        '''Кнопка ускорения выделенного момента'''
        SpeedUpButton = QPushButton(self)
        SpeedUpButton.resize(100, 50)
        SpeedUpButton.move(150, 350)
        SpeedUpButton.setText("Ускорить")
        SpeedUpButton.clicked.connect(self.SpeedUp)

        '''Кнопка для замедления выделенного момента'''
        SpeedDownButton = QPushButton(self)
        SpeedDownButton.resize(100, 50)
        SpeedDownButton.move(250, 350)
        SpeedDownButton.setText("Замедлить")
        SpeedDownButton.clicked.connect(self.SpeedDown)

        '''Ползунок выбора начала момента музыки для вырезания или обрезания'''
        begin_time = QSlider(Qt.Horizontal, self)
        begin_time.resize(300, 50)
        begin_time.move(150, 100)

        '''Ползунок выбора конца момента музыки для вырезания или обрезания'''
        end_time = QSlider(Qt.Horizontal, self)
        end_time.resize(300, 50)
        end_time.move(150, 150)

        '''Поле статуса работы с музыкой'''
        self.message = QLabel(self)
        self.message.resize(200, 50)
        self.message.move(200, 450)
        self.message.setAlignment(Qt.AlignHCenter)
        self.message.setFont(QFont("Arial font", 20))

        self.exitButton = QPushButton("Выход", self)
        self.exitButton.resize(100, 50)
        self.exitButton.move(250, 500)
