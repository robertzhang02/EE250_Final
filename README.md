# EE250_Final

#Team members: Robert Zhang and Jiansong Li

#Link to our demo video: https://drive.google.com/file/d/1myDE-PqRci2Lu9yxwQPe_3Xbz_2OvKVm/view?usp=share_link
#Instruction: 

Firstly, make sure recorder.py and server.py are downloaded on labtop or VM, and lcd.py and client.py are downloaded on your RPi. 

Install Python libraries listed in the requirements.txt. Then, run the python file recorder.py to record audio input and get text file output as speech.txt. The API key and endpoint are provided in the code. Then, in order to transfering the text file from labtop to RPi, run the server.py on your labtop, PC, or VM. 

Then, before you have ssh into the RPi, please check if your RPi can work with grovepi. Basically, you have to check GrovePi's firmware and I2C on RPi. Then, make sure the lcd screen is connected correctly to the Grovepi and RPI.  After finishing with these setup work, you need to open a terminal and ssh into your RPi. On your RPi, run client.py to send a request to receieve the speech text file from server node(your PC, VM, or labtop). 

After that, use ls command in the terminal to check if there is a text file which contains the speech you have recorded. It should have the same speech.txt, which  is indentical to what your recorder.py has outputed. Then, to display the speech you have recorded, run lcd.py to display speech text on the lcd screen. Finally,      you can see what you have recorded previously on the lcd screen. Please be careful to check if the speech-to-text conversion is good or not.

#List of external libraries:
  azure-cognitiveservices-speech
  
  scipy
  
  wavio
  
  sounddevice
  
  grove_rgb_lcd
  
  time
  
  sockets
