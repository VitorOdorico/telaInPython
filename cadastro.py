from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
layout = [
    [sg.Text('User name'),sg.Input(key='user',size=(30,1))],
    [sg.Text('PassWord'),sg.Input(key='password',password_char='*',size=(30,1))],
    [sg.Checkbox('remember to you?')],
    [sg.Button('enter')]
]

window = sg.Window('Login', layout)

while True:
    events, value = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'enter':
        if value['UserName'] == 'vitor' and value['PassWord'] == 'test':
            print('Welcome to my web site')