from PyQt6.QtWidgets import QApplication
from logic import *



def main():
    '''
    Sets up main Gui and calls to functions/modules.
    '''
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()