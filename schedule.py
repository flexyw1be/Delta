from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from data.all_models import *
from PyQt5 import uic
import openpyxl
from utitlities import get_without_failing
from data.config import *


class Schedule(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(SCHEDULE_UI, self)
        self.setWindowTitle('Расписание')
        self.setWindowIcon(QIcon(ICON))
        self.set_history()
        self.xlsx_push_button.clicked.connect(self.get_xlsx)

    def set_history(self):
        notes = get_without_failing(History, History.id)
        print(notes)
        for i in notes:
            patient = Patient.get(Patient.id == i.Patient_id)
            doctor = Doctor.get(Doctor.id == i.Doctor_id)
            self.list_widget.addItem(f'{i.datetime}    {patient.current_name}    {doctor.current_name}    {i.amount}    {i.name}    {i.note}')

    def get_xlsx(self):
        wb = openpyxl.Workbook()
        list = wb.active
        list.append(('Дата', 'Время', 'Пациент', 'Врач', 'Причина обращения', 'Цена', 'Примечание'))
        notes = get_without_failing(History, History.id)
        for i in notes:
            patient = Patient.get(Patient.id == i.Patient_id)
            doctor = Doctor.get(Doctor.id == i.Doctor_id)
            list.append((
                        i.datetime.split()[0], i.datetime.split()[1], patient.current_name, doctor.current_name, i.name,
                        i.amount, i.note))
        wb.save('products.xlsx')
