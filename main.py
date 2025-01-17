import pywinauto
from pywinauto import Application
from pywinauto import Desktop

def main():
    try:
        app = Application(backend="uia").connect(title_re=r".*Google Chrome.*")
    except:
        app = Application(backend="uia").start(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    main_window = app.window(title_re=r".*Google Chrome.*")
    search_bar = main_window.child_window(title="Pasek adresu i wyszukiwania").draw_outline()

if __name__ == "__main__":
    main()