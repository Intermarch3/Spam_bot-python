import pyautogui
from time import sleep

msg = input("Tape le message a spam: ")
nb = int(input("Combien de fois on le spam ?\n"))

sleep(5)     # après avoir lancer le programme, tu a 5 seconde pour clické dans un espace de text et le spam commence
for i in range(nb):     
    pyautogui.typewrite(msg)      
    pyautogui.press("enter")
