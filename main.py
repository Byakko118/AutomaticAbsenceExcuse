import pywinauto
from pywinauto import Application
from pywinauto import Desktop

USERNAME = "Alan Goźliński"

def main():
    try:
        app = Application(backend="uia").connect(title_re=r".*Microsoft Teams.*")
        
    except:
        Application(backend="uia").start(r"ms-teams.exe")
        while(True):
            try:
                app = Application(backend="uia").connect(title_re=r".*Microsoft Teams.*")
                break
            except:
                print("no")

    main_window = app.window(title_re=r".*Microsoft Teams.*")
    main_window.set_focus()
    
    a = Desktop.windows()
    for window in a:
        print(window.window_text())
    
    if main_window.child_window(title_re=rf".*{USERNAME}.*", control_type="MenuItem").exists(timeout=7):
        main_window.child_window(title_re=rf".*{USERNAME}.*", control_type="MenuItem").invoke()
        

if __name__ == "__main__":
    main()