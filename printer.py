import win32print
import win32api
def print_text(text):
    # Save the text to a temporary file for printing
    temp_file = "temp_print.txt"
    with open(temp_file, "w") as file:
        file.write(text)

    printer_name = win32print.GetDefaultPrinter()
    win32api.ShellExecute(
        0,
        "print",
        temp_file,
        '/d:"%s"' % printer_name,
        ".",
        0
    )
