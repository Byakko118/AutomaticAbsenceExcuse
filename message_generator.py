import configparser
import json
import random
import re
from datetime import datetime, timedelta
import os
import sys

def get_data_file_path(filename):
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS  
    else:
        bundle_dir = os.path.abspath(os.path.dirname(__file__))

    return os.path.join(bundle_dir, filename)

def replace_date(text):
    today = datetime.today()
    two_weeks_ago = today - timedelta(weeks=2)

    text = text.replace("<od>", two_weeks_ago.strftime("%d.%m"))
    text = text.replace("<do>", today.strftime("%d.%m"))

    return text

def replace_tags(message, u_gender, t_gender):
    replacements = {
        '<u-a>': 'a' if u_gender == 'Female' else '',
        '<u-a/y>': 'a' if u_gender == 'Female' else 'y',
        '<t-a>': 'a' if t_gender == 'Female' else '',
        '<pan/pani>': 'pani' if t_gender == 'Female' else 'pan',
        '<u-a/e>': 'a' if u_gender == 'Female' else 'e',
        '<u-e/ą>': 'e' if u_gender == 'Female' else 'ą'
    }

    for tag, replacement in replacements.items():
        message = message.replace(tag, replacement)

    return message

def generate_message():
    config_path = get_data_file_path('config.ini')
    json_path = get_data_file_path('message_db.json')

    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')

    details_config = config['Details']

    t_gender = details_config.get("teacher_gender")
    u_gender = details_config.get("user_gender")

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    przywitanie = random.choice(data['przywitanie'])
    prosba = random.choice(data['prosba'])
    powod_wstep = random.choice(data['powod-wstep'])
    powod = random.choice(data['powód'])
    pozegnanie = random.choice(data['pozegnanie'])

    przywitanie = replace_tags(przywitanie, u_gender, t_gender)
    prosba = replace_tags(prosba, u_gender, t_gender)
    powod_wstep = replace_tags(powod_wstep, u_gender, t_gender)
    powod = replace_tags(powod, u_gender, t_gender)
    pozegnanie = replace_tags(pozegnanie, u_gender, t_gender)

    prosba = replace_date(prosba)

    return f"{przywitanie} {prosba} {powod_wstep} {powod} {pozegnanie}"

if __name__ == "__main__":
    print(generate_message())
