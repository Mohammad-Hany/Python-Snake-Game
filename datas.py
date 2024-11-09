import json
import os
from settings import user_settings

#Normal mode
def load_high_score():
    try:
        with open("data/high_score.txt", 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def save_high_score(high_score):
    with open("data/high_score.txt", 'w') as file:
        file.write(str(high_score))

def update_and_show_high_score(new_score):
    current_high_score = load_high_score()
    
    if new_score > current_high_score:
        save_high_score(new_score)
        return new_score
    else:
        return current_high_score
    
# Timed mode
def save_record(data):
    with open("data/record.txt", 'w') as file:
        json.dump(data, file)

def load_record():
    try:
        with open("data/record.txt", 'r') as file:
            record_dic = json.load(file)
        return record_dic
    
    except FileNotFoundError:
        n = {'60': 0, '120': 0, '180': 0}
        save_record(n)
        return load_record()
    
    except json.JSONDecodeError: #format error
        print(f"محتوای فایل data/record.txt به فرمت JSON نامعتبر است.")
        n = {'60': 0, '120': 0, '180': 0}
        save_record(n)
        return load_record()

def update_record(score):
    current_record = load_record()
    time = user_settings['timed']
    if score > current_record.get(str(time)):
        record = load_record()
        record[str(time)] = score
        save_record(record)
        return score
    else:
        return current_record[str(time)]
    
# theme settings
file_name = "data/theme.txt"
def save_theme_settings(theme_dict):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'w') as file:
        json.dump(theme_dict, file)

def load_theme_setting():
    try:
        with open(file_name, 'r') as file:
            theme_dict = json.load(file)
        return theme_dict
    
    except FileNotFoundError:
        print(f"فایل {file_name} یافت نشد.")
        save_theme_settings(user_settings['theme'])
        return user_settings['theme']
    
    except json.JSONDecodeError: #format error
        print(f"محتوای فایل {file_name} به فرمت JSON نامعتبر است.")
        save_theme_settings(user_settings['theme'])
        return user_settings['theme']