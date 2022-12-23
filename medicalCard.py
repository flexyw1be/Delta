from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
from utitlities import *
from config import *


class MedicalCard(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(MEDICAL_CARD_UI, self)
        self.setWindowTitle('Медицинская Карта')
        self.setWindowIcon(QIcon(ICON))
