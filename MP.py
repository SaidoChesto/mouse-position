import pyautogui as pag
import time

# Enquanto o programa rodar, a cada 0.3 segundos ele vai dar a posição do mouse
while True:
    x , y = pag.position()
    print(x, y)
    time.sleep(0.5)