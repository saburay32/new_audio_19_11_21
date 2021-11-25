import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text('My next gui panel')],
          [sg.Text('Enter this===>'),sg.InputText()],
          [sg.Button('OK'),sg.Button('Cancel')]]

window = sg.Window('WindowTitle',layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    print('You entered ',values[0])

window.close()