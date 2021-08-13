## utiliza o navegador e o mouse do computador
# entrar no terminal e instalar pyautogui

import pyautogui
import pyperclip
import time

#pyautogui.hotkey('ctrl','t')
pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('google.com')
pyautogui.press('enter')

#tempo para a pagina caregar
time.sleep(3)
pyautogui.write('gmail.com')
pyautogui.press('enter')

assunto = ''' 
assunto referente ao trabalho
        porfavor escrever algo aqui
    ps bom dia '''

time.sleep(6)
#posição da opção "escrever" do gmail
pyautogui.click(x=78, y=181)

time.sleep(6)
pyautogui.write('atilalves48@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('assunto referente ao trabalho')
pyautogui.press('tab')
pyautogui.write(assunto)
pyautogui.hotkey('ctrl','enter')