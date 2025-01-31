from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QCheckBox, QPushButton, QTextEdit, QRadioButton, QHBoxLayout, QButtonGroup
from PyQt5.QtCore import Qt
import qdarkstyle
import configparser
from PyQt5.QtWidgets import QMessageBox

def on_submit():
    email = email_input.text()
    password = password_input.text()
    teacher = teacher_input.text()
    message = message_input.toPlainText()

    teacher_gender = "Male" if male_radio.isChecked() else "Female" if female_radio.isChecked() else "Unknown"
    user_gender = "Male" if user_male_radio.isChecked() else "Female" if user_female_radio.isChecked() else "Unknown"

    if auto_generate_checkbox.isChecked() and teacher_gender == "Unknown" and user_gender == "Unknown":
        QMessageBox.warning(window, "Błąd", "Proszę wybrać płeć nauczyciela oraz swoją płeć.")
        return  
    
    if auto_generate_checkbox.isChecked() and teacher_gender == "Unknown":
        QMessageBox.warning(window, "Błąd", "Proszę wybrać płeć nauczyciela.")
        return  
    
    if auto_generate_checkbox.isChecked() and user_gender == "Unknown":
        QMessageBox.warning(window, "Błąd", "Proszę wybrać swoją płeć.")
    
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Teacher: {teacher}")
    print(f"Teacher Gender: {teacher_gender}")
    print(f"User Gender: {user_gender}")
    print(f"Message: {message}")
    
    config.set('User', 'EMAIL', email)
    config.set('User', 'PASSWORD', password)
    config.set('Details', 'TEACHER', teacher)
    config.set('Details', 'MESSAGE', message)
    config.set('Details', 'TEACHER_GENDER', teacher_gender)  
    config.set('Details', 'USER_GENDER', user_gender) 
    
    is_auto_generated = "True" if auto_generate_checkbox.isChecked() else "False"
    config.set('Details', 'IS_AUTO_GENERATED', is_auto_generated)  
    
    with open('config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

    print("Configuration updated successfully.")


def on_checkbox_state_changed():
    if auto_generate_checkbox.isChecked():
        male_radio.setVisible(True)
        female_radio.setVisible(True)
        gender_label.setVisible(True)
        user_male_radio.setVisible(True)
        user_female_radio.setVisible(True)
        user_gender_label.setVisible(True)
        message_input.setVisible(False)
        message_label.setVisible(False)
        window.adjustSize()
    else:
        male_radio.setVisible(False)
        female_radio.setVisible(False)
        gender_label.setVisible(False)
        user_male_radio.setVisible(False)
        user_female_radio.setVisible(False)
        user_gender_label.setVisible(False)
        message_input.setVisible(True)
        message_label.setVisible(True)
        window.adjustSize()

def toggle_password_visibility():
    if show_password_checkbox.isChecked():
        password_input.setEchoMode(QLineEdit.Normal)
    else:
        password_input.setEchoMode(QLineEdit.Password)

config = configparser.ConfigParser()
config.read('config.ini', 'utf-8')
user_config = config['User']
details_config = config['Details']
default_email = user_config.get('EMAIL', '')
default_password = user_config.get('PASSWORD', '')
default_teacher = details_config.get('TEACHER', '')
default_message = details_config.get('MESSAGE', '')

app = QApplication([])

window = QWidget()
window.setWindowTitle("Wysyłanie wiadomości")
window.adjustSize()

layout = QVBoxLayout()

email_label = QLabel("Adres e-mail:")
email_input = QLineEdit()
email_input.setPlaceholderText("Wprowadź swój adres e-mail")
email_input.setText(default_email)
layout.addWidget(email_label)
layout.addWidget(email_input)

password_label = QLabel("Hasło:")
password_input = QLineEdit()
password_input.setPlaceholderText("Wprowadź swoje hasło")
password_input.setEchoMode(QLineEdit.Password)
password_input.setText(default_password)
layout.addWidget(password_label)
layout.addWidget(password_input)

show_password_checkbox = QCheckBox("Pokaż hasło")
show_password_checkbox.stateChanged.connect(toggle_password_visibility)
layout.addWidget(show_password_checkbox)

teacher_label = QLabel("Nauczyciel, do którego ma zostać wysłana wiadomość:")
teacher_input = QLineEdit()
teacher_input.setPlaceholderText("Wprowadź imię/nazwisko lub pseudonim nauczyciela na Teams")
teacher_input.setText(default_teacher)
layout.addWidget(teacher_label)
layout.addWidget(teacher_input)

user_gender_label = QLabel("Wybierz swoją płeć:")
user_gender_layout = QHBoxLayout()
user_male_radio = QRadioButton("Mężczyzna")
user_female_radio = QRadioButton("Kobieta")
user_gender_label.setVisible(False)
user_male_radio.setVisible(False)
user_female_radio.setVisible(False)
user_gender_layout.addWidget(user_male_radio)
user_gender_layout.addWidget(user_female_radio)
layout.addWidget(user_gender_label)
layout.addLayout(user_gender_layout)

gender_label = QLabel("Wybierz płeć nauczyciela:")
gender_layout = QHBoxLayout()
male_radio = QRadioButton("Mężczyzna")
female_radio = QRadioButton("Kobieta")
gender_label.setVisible(False)
male_radio.setVisible(False)
female_radio.setVisible(False)
gender_layout.addWidget(male_radio)
gender_layout.addWidget(female_radio)
layout.addWidget(gender_label)
layout.addLayout(gender_layout)

# Create separate button groups to allow both genders to be selected independently
teacher_gender_group = QButtonGroup()
teacher_gender_group.addButton(male_radio)
teacher_gender_group.addButton(female_radio)

user_gender_group = QButtonGroup()
user_gender_group.addButton(user_male_radio)
user_gender_group.addButton(user_female_radio)

message_label = QLabel("Wiadomość:")
message_input = QTextEdit()
message_input.setPlaceholderText("Wprowadź wiadomość, którą chcesz wysłać")
message_input.setText(default_message)
layout.addWidget(message_label)
layout.addWidget(message_input)

auto_generate_checkbox = QCheckBox("Automatycznie generuj wiadomość")
auto_generate_checkbox.stateChanged.connect(on_checkbox_state_changed)
layout.addWidget(auto_generate_checkbox)

submit_button = QPushButton("Wyślij")
submit_button.clicked.connect(on_submit)
layout.addWidget(submit_button)

window.setLayout(layout)
window.show()

window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

app.exec_()

