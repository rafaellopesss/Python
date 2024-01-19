import pyautogui #Biblioteca automatizada
from time import sleep
import webbrowser

pyautogui.alert('O código vai começar')
webbrowser.open("https://web.whatsapp.com/")
sleep(10)
pyautogui.click(816,444, duration=5)
sleep(5)
pyautogui.click(1180,645, duration=3)
sleep(2)
pyautogui.write('Bora casar logo')
sleep(2)
pyautogui.press('enter')
