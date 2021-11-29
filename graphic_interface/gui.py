from PyQt5 import uic, QtWidgets

Form, _ = uic.loadUiType("First.ui")

class Ui(QtWidgets.QDialog,Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.printButtonPressed)

    def printButtonPressed(selfs):
        print("pressed")

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec()


# import PySimpleGUI as sg
#
# sg.theme('Reddit')
#
# layout = [[sg.Text('My next gui panel')],
#           [sg.Text('Enter ===>'),sg.InputText()],
#           [sg.Button('OK'),sg.Button('Cancel')]]
#
# window = sg.Window('GuiPanel',layout)
#
# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED or event == 'Cancel':
#         break
#     print('You entered ',values[0])
#
# window.close()