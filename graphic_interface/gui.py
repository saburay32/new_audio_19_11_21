import PySimpleGUI as sg

sg.theme('Reddit')

layout = [[sg.Text('My next gui panel')],
          [sg.Text('Enter ===>'),sg.InputText()],
          [sg.Button('OK'),sg.Button('Cancel')]]

window = sg.Window('GuiPanel',layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    print('You entered ',values[0])

window.close()