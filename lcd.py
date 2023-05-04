import time
from grove_rgb_lcd import *

setRGB(0, 255, 0)
file = open("./speech.txt", "r")
for text in file:
        time.sleep(3)
        setText(text)
        # setText_norefresh(unicdoe_text)
file.close()
