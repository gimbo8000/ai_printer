# tests/test_script.py

import time
# Import the listen function from the listen.py module in the src directory
from src.listen import listen

def test_listen():
    # This function will test the listen() function
    print("Starting test...")

    # You can adjust the number of iterations for testing
    for i in range(3):
        print(f"Test {i + 1}...")
        listen()  # Call the listen function to test recording and transcription
        time.sleep(3)  # Wait for a few seconds between tests

if __name__ == "__main__":
    test_listen()

