from listen import *
from AI import *
device_of_choice = input("\nwright 1 down for normal printer and 2 for 3d printer. remember the 3d printer option is very experamental and willonly generate a gcode for now: ")
text = listen()
#todo make a local web app mabie
while True:
    if text != False:  # Check if text is not None
                print(f"Received text to print: {text}")
                awnser = AI(text)
                print_text(awnser)
                print("printed")
                text = listen()