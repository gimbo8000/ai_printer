from listen import *
from AI import *
from printer import *
text = listen()
#todo make a local web app mabie
while True:
    if text != False:  # Check if text is not None
                print(f"Received text to print: {text}")
                awnser = AI(text)
                print_text(awnser)
                print("printed")
                text = listen()