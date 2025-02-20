import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMessageBox

def get_script_path(filename):
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.path.abspath(os.path.dirname(__file__))

    return os.path.join(bundle_dir, filename)

def run_python_script(script_path):
    if os.path.exists(script_path):
        try:
            subprocess.run([sys.executable, script_path])
        except Exception as e:
            show_message(f"An error occurred while trying to run the script: {e}")
    else:
        show_message("The specified script was not found.")

def show_message(message):
    app = QApplication([])
    QMessageBox.critical(None, "Error", message)
    app.exec_()

if __name__ == "__main__":
    script_name = "main.py" 
    script_path = get_script_path(script_name)
    
    run_python_script(script_path)
