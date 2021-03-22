"""Calculadora simples feita usando PySimpleGUI"""

import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("Digite o primeiro número")],
          [sg.InputText(key='entrada1')],
          [sg.Text("Digite o segundo número")],
          [sg.Input(key='entrada2')],
          [sg.Text("Digite o tipo de operação (+,-,/,*,%)")],
          [sg.Input(key='entrada3')],
          [sg.Text(size=(40,1), key='saida')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Calculadora do Yurão', layout)

# Display and interact with the Window using an Event Loop
while True:
    try:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        # Output a message to the window
        lista1 = float(values['entrada1'])
        lista2 = float(values['entrada2'])
        lista3 = (values['entrada3'])
        if "+" in lista3:
            window['saida'].update(f'O resultado da conta é: {lista1+lista2}')
        elif "-" in lista3:
            window['saida'].update(f'O resultado da conta é: {lista1-lista2}')
        elif "/" in lista3:
            window['saida'].update(f'O resultado da conta é: {lista1/lista2}')
        elif "*" in lista3:
            window['saida'].update(f'O resultado da conta é: {lista1*lista2}')
        elif "%" in lista3:
            window['saida'].update(f'O resultado da conta é: {(lista1/lista2)*100}%')
        elif "+" or "-" or "/" or "*" or "%" not in lista3:
            window['saida'].update('você deve digitar o tipo de operação que deseja!')
            continue

    except ValueError:
        window['saida'].update('você deve digitar apenas números')
        continue

# Finish up by removing from the screen
window.close()