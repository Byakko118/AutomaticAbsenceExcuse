import configparser
import json
import random
import re

def replace_tags(message, u_gender, t_gender):
    """Replace tags in the message based on user and teacher gender."""
    replacements = {
        '<u-a>': 'a' if u_gender == 'female' else '',
        '<u-a/y>': 'a' if u_gender == 'female' else 'y',
        '<t-a>': 'a' if t_gender == 'female' else '',
        '<pan/pani>': 'pani' if t_gender == 'female' else 'pan',
        '<u-a/e>': 'a' if u_gender == 'female' else 'e',
        '<u-e/ą>': 'e' if u_gender == 'female' else 'ą'
    }

    for tag, replacement in replacements.items():
        message = message.replace(tag, replacement)

    return message

def generate_message():
    config = configparser.ConfigParser()
    config.read('config.ini', 'utf-8')

    details_config = config['Details']

    t_gender = details_config.get("teacher_gender")
    u_gender = details_config.get("user_gender")

    with open('message_db.json', 'r', encoding='utf-8') as file:
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

    print("Przywitanie:", przywitanie)
    print("Prośba:", prosba)
    print("Powód wstęp:", powod_wstep)
    print("Powód:", powod)
    print("Pożegnanie:", pozegnanie)

generate_message()
