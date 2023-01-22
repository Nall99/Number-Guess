import PySimpleGUI as sg
import random

# global variables
historic = []
lives = 3

layout = [
    [sg.Text("Number between 0 and 10: "),sg.Input(key='num', size=(5,1)),sg.Text(f'Lives: {lives}',key='lives')],
    [sg.Text("",key='historic',size=(35,3), background_color='white',text_color='black')],
    [sg.Submit(),sg.Button("Reset")]
]

# Window
window = sg.Window('Number Guess', layout)

# Drawn a number between 0 and 10
drawn = random.randint(0,10)

# functions
def Reset(): # Reset historic, lives and drawn new number
    window['historic'].update('')
    window['lives'].update(f'Lives: 3')
    return random.randint(0,10), [], 3

def Historic(hist): # Update historic display and list
    hist.append(f"{tip} than {values['num']}\n")
    hist = ''.join(hist)
    window['historic'].update(hist)

# Loop Game
while True:

    event, values =  window.read()
    # close window
    if event == sg.WIN_CLOSED:
        break

    # Submit button
    elif event == 'Submit':
        window['num'].update('')

        # Notify case number greater than maximum
        if int(values['num']) > 10:
            sg.popup('[ERRO] Number greater than 10')
        
        # Notify case number less than minimum
        elif int(values['num']) < 0:
            sg.popup('[ERRO] Number less than 0')
        
        # Number between 0 and 10 but not is a drawn number
        elif int(values['num']) != drawn:
            tip = ''
            
            # Number greater than drawn 
            if int(values['num']) > drawn:
                tip = 'less'
            # Number less than drawn
            else:
                tip = 'bigger'
            
            lives -= 1
            window['lives'].update(f'Lives: {lives}')
            Historic(historic)

        # Number between 0 and 10 but is a drawn number
        elif int(values['num']) == drawn:
            sg.popup(f"Congratulations {values['num']} is the correct number!!\nYour game will be reset")
            drawn, historic, lives = Reset()
    
    # Reset button
    elif event == 'Reset':
        drawn, historic, lives = Reset()
    
    # Lose Game
    if lives < 1:
        drawn, historic, lives = Reset()
        sg.popup("You lose\nYour game will be reset")    

window.close()