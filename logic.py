from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget
from gui import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        '''
        This sets up the main window and initializes variables.
        '''
        super().__init__()
        self.setupUi(self)
        self.button_save.clicked.connect(self.validate_all)
        self.button_clear.clicked.connect(self.clear)

    def num_students(self) -> bool:
        '''
        This function checks how many students and that entry is validated
        '''
        stud = self.entry_num_students.text().strip()
        if stud == '':
            self.error_students.setText('Please enter a number ex: \'3\'')
            self.num_studs = 0
            return False
        else:
            for char in stud:
                if not char.isdigit():
                    self.error_students.setText('Enter only digits, no letters or symbols')
                    self.num_studs = 0
                    return False
            try:
                self.num_studs = int(stud)
                self.error_students.setText('')
                return True

            except ValueError:
                self.error_students.setText('Enter only whole numbers')
                self.num_studs = 0
                return False

    def scores(self) -> bool:
        '''
        Checks if there is a score for each student and correct characters are entered
        '''
        self.scores_list = self.entry_scores.toPlainText().strip().split()
        if len(self.scores_list) != self.num_studs:
            self.error_scores.setText('Enter a grade for each student')
            return False
        else:
            for num in self.scores_list:
                if not num.strip().isdigit():
                    self.error_scores.setText('Only positive numbers, no letters or negatives')
                    return False
                else:
                    if not 0 <= int(num) <= 100:
                        self.error_scores.setText('Enter 0 to 100')
                        return False
            self.error_scores.setText('')
            return True

    def grades(self) -> bool:
        '''
        Gets listed scores from entry and assigns them grades
        '''
        self.grades_list = []
        for score in self.scores_list:
            score = int(score)
            if score == 100:
                self.grades_list.append('A+')
            elif score >= 90:
                self.grades_list.append('A')
            elif score >= 80:
                self.grades_list.append('B')
            elif score >= 70:
                self.grades_list.append('C')
            elif score >= 60:
                self.grades_list.append('D')
            else:
                self.grades_list.append('F')
        return True

    def validate_all(self) -> None:
        '''
        Checks if each previous function is valid and then calls save()
        '''
        if self.num_students() and self.scores() and self.grades():
            self.entry_num_students.clear()
            self.entry_scores.clear()
            self.error_students.setText('')
            self.error_scores.setText('')
            self.save()

    def save(self) -> None:
        '''
        This function saves all values entered into a table and assigns grades
        to table as well
        '''
        #used chatgpt to troubleshoot an index error. it suggested a list
        #over a dict for ease of use and convenience
        for i in range(len(self.scores_list)):
            row = self.table_grades.rowCount()
            self.table_grades.insertRow(row)

            self.table_grades.setItem(row, 0, QTableWidgetItem(str(f'Student{row + 1}')))
            self.table_grades.setItem(row, 1,QTableWidgetItem(str(self.scores_list[i])))
            self.table_grades.setItem(row, 2,QTableWidgetItem(str(self.grades_list[i])))

    def clear(self) -> None:
        '''
        This function clears all table values so one may restart value entry
        '''
        self.table_grades.setRowCount(0)