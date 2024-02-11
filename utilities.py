import turtle
import pygame

from datetime import datetime, timedelta
from time import sleep

from datas import update_and_show_high_score, save_theme_settings, load_theme_setting, update_record
from settings import settings, user_settings


def change_user_theme(theme_num):
    user_settings['theme'] = settings['themes'].get(theme_num)
    save_theme_settings(user_settings['theme'])

def change_background(win):
    win.bgpic(settings['backgrounds'][f'{load_theme_setting()["bg"]}PATH'])

def change_direction(head, direction):
    if user_settings['mode'] != 'comfortable':
        if head.direction == 'up' and direction != 'down':
            head.direction = direction

        elif head.direction == 'down' and direction != 'up':
            head.direction = direction
        
        elif head.direction == 'right' and direction != 'left':
            head.direction = direction

        elif head.direction == 'left' and direction != 'right':
            head.direction = direction
        
        elif head.direction == 'stop':
            head.direction = direction
    else:
        head.direction = direction

def move(head):
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

def translate_numbers(number):
    text = str(number).maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return str(number).translate(text)

def write_up_page(win, writer, score=None, custom_text=None, seconds=None):
    writer.clear()
    writer.up()
    writer.goto(0, win.window_height() // 2 - 50)
    writer.down()
    writer.color(load_theme_setting()['text'])
    if custom_text is not None:
        writer.write(custom_text, align="center",font=("Vazir Bold", 20)) 
    
    else:
        match user_settings['mode']:
            case 'comfortable' | 'normal':
                message = f"امتیاز: {translate_numbers(score)} - بالا‌ترین امتیاز: {translate_numbers(update_and_show_high_score(score))}"
            
            case 'timed':
                message = "امتیاز: {} رکورد: {} - {} ثانیه تا پایان".format(translate_numbers(score), translate_numbers(update_record(score)), translate_numbers(int((end_time() - datetime.now()).total_seconds())))

        writer.write(message, align="center",font=("Vazir Bold", 20)) 
    
    writer.color('black')
    win.update()

# speed
def increase_delay(win, status_writer):
    if settings['general']['delay'] - 0.05 >= 0:
        if not  settings['general']['is_shift_pressed']: #poshte ham  naghire ke delay sefr beshe
            settings['general']['delay'] -= 0.05
            settings['general']['is_shift_pressed'] = True
            play_shift_sound()
            speed_status(win, status_writer)

def reset_delay(win, status_writer):
    settings['general']['delay'] =  settings['general']['initial_delay']
    settings['general']['is_shift_pressed'] = False
    speed_status(win, status_writer, True)

def speed_up(score):
    if score //  settings['general']['SUA'] and settings['general']['delay'] -  settings['general']['SDT'] >= 0:
        settings['general']['delay'] -=  settings['general']['SDT']

def speed_status(win, status_writer, reset=False):
    if reset:
        status_writer.hideturtle()

    else:
        status_writer.showturtle()
        turtle.addshape(settings['SPEED_ICON_PATH'])
        turtle.register_shape(settings['SPEED_ICON_PATH'])
        status_writer.up()
        status_writer.goto(-win.window_width() / 2 + 30, -win.window_height() / 2 + 30)
        status_writer.shape(settings['SPEED_ICON_PATH'])

# sounds effect
pygame.mixer.init()
def play_background_sound():
    sound = pygame.mixer.Sound(settings['BACKGROUND_SOUND_PATH'])
    sound.set_volume(0.4)
    sound.play()

def play_score_sound():
    pygame.mixer.Sound(settings['GET_SCORE_SOUND_PATH']).play()

def play_wall_sound():
    pygame.mixer.Sound(settings['WALL_SOUND_PATH']).play()

def play_shift_sound():
    pygame.mixer.Sound(settings['SHIFT_SOUND_PATH']).play()

# game over
def game_over_message(win, writer, message='!!خوردی به دیوار! باختی'):
    global current_time
    play_wall_sound()
    for i in range(4):
        writer.up()
        writer.goto(0, 0)
        writer.down()
        if i % 2 == 0:
            writer.color('crimson')
            writer.write(message, align="center", font=("Vazir Bold", 21))
        else:
            writer.color('darkcyan')
            writer.write(message, align="center", font=("Vazir Bold", 19))

        win.update()
        sleep(0.7)
        writer.clear()

        i += 1

# timed moode
current_time = 0
execution_time = [0]
def save_current_time(): # for one time
    global current_time, execution_time
    if execution_time[0] == 0:
        current_time = datetime.now()
        execution_time[0] += 1

def end_time():
    global current_time
    save_current_time()
    time_lose = current_time + timedelta(seconds=user_settings['timed'])
    return time_lose

def mode_status(win, status_writer):
    status_writer.showturtle()
    status_writer.up()
    status_writer.goto(win.window_width() / 2 - 90, -win.window_height() / 2 + 5)

    match user_settings['mode']:
        case 'comfortable':
            status_writer.fd(50)
            mode = 'آسان'
        case 'normal':
            status_writer.fd(50)
            mode = 'عادی'
        case 'timed':
            status_writer.backward(10)
            mode = f'زمان‌دار {translate_numbers(user_settings["timed"] // 60)} دقیقه‌ای'

    status_writer.down()
    status_writer.color(load_theme_setting()['text'])
    status_writer.write(mode, align="center",font=("Vazir Bold", 16)) 
    status_writer.hideturtle()
