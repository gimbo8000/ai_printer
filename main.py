from http.client import responses

from listen import *
from AI import *
text = listen()
if text:  # Check if text is not None
            print(f"Received text to print: {text}")
            awnser = AI(text)
            print_text(awnser)
            print("printed")
