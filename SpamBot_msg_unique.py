import pyautogui
from time import sleep

sleep(5)     # après avoir lancer le programme, tu a 5 seconde pour clické dans un espace de text et le spam commence
nb = 0
for nb in range(200):     # met entre parenthèse le nombre de fois à spam le message
    pyautogui.typewrite("je suis le meilleur en spam")      # tape dans les guillemets le message à spam
    pyautogui.press("enter")
    nb = nb + 1
