import turtle
import random
import time
from time import sleep

score = [0]

from utilities import *
from settings import settings
from datas import load_theme_setting, update_record

# segments
segments = []

def setup(theme):
    global win, writer, status_writer, head, food
    win = turtle.Screen()
    win.title('SnakeWarrior')
    change_background(win)
    win.setup(width=600, height=600)
    win.tracer(0)

    # writer text
    writer = turtle.Turtle()
    writer.hideturtle()
    write_up_page(win, writer, score[0])

    status_writer = turtle.Turtle()
    status_writer.hideturtle()
    mode_status(win, status_writer)

    # snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape(settings['shape']['snake_head'])
    head.color(theme['head'])
    head.penup()
    head.goto(0,0)
    head.direction = 'stop'

    # food
    food = turtle.Turtle()
    food.speed(0)
    food.shape(settings['shape']['food'])
    food.color(theme['food'])
    food.penup()
    food.goto(0,100)

def on_click(x, y):
    from main import draw_game_mode, setup as main_setup
    if -290 < x < -230 and -290 < y < -250 and head.direction == "stop":
        win.clear()
        main_setup()
        draw_game_mode()

def game_over_body():
    win.update()
    head.goto(0,0)
    head.direction = 'stop'

    # hide segments
    for segment in segments:
        segment.goto(1000,1000)

    # clear segments and text
    writer.clear()
    segments.clear()
    score[0] = 0
    settings['general']['delay'] = settings['general']['initial_delay']
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)

def game_over():
    global score, execution_time
    mode = user_settings['mode']
    if mode != 'comfortable':
        for index in segments:
            if head.distance(index) < 10:
                difference = end_time() - datetime.now()
                seconds = user_settings['timed'] - int(difference.total_seconds())
                game_over_message(win, writer, '!باختی! خوردی به بدن خودت')
                game_over_body()
                execution_time[0] = 0


    if (mode == 'normal' or mode == 'comfortable') and (head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290):
        game_over_message(win, writer)
        game_over_body()
        
    if mode == 'timed' and datetime.now() > end_time():  
        update_record(score[0])
        game_over_message(win, writer, f"!زمانت تموم شد\nتونستی در {translate_numbers(user_settings['timed'])} ثانیه، {translate_numbers(score[0])} امتیاز بگیری!")
        game_over_body()
        execution_time[0] = 0

    if mode == 'timed' and head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        difference = end_time() - datetime.now()
        seconds = user_settings['timed'] - int(difference.total_seconds())
        game_over_message(win, writer, f"!خوردی به دیوار\nتونستی در {translate_numbers(seconds)} ثانیه، {translate_numbers(score[0])} امتیاز به دست بیاری!")
        game_over_body()
        execution_time[0] = 0

def snake_game():

    # bindings
    win.listen()
    win.onkeypress(lambda: change_direction(head, 'up'), 'w')
    win.onkeypress(lambda: change_direction(head, 'down'), 's')
    win.onkeypress(lambda: change_direction(head, 'right'), 'd')
    win.onkeypress(lambda: change_direction(head, 'left'), 'a')
    # or use of other keys
    win.onkeypress(lambda: change_direction(head, 'up'), 'Up')
    win.onkeypress(lambda: change_direction(head, 'down'), 'Down')
    win.onkeypress(lambda: change_direction(head, 'right'), 'Right')
    win.onkeypress(lambda: change_direction(head, 'left'), 'Left')
    # speed keys
    win.onkeypress(lambda: increase_delay(win, status_writer), 'Shift_L')
    win.onkeyrelease(lambda: reset_delay(win, status_writer), 'Shift_L')
    win.onkeypress(lambda: increase_delay(win, status_writer), 'Shift_R')
    win.onkeyrelease(lambda: reset_delay(win, status_writer), 'Shift_R')

    current_time = datetime.now()
    while True:
        if current_time + timedelta(minutes=8) < datetime.now():
            play_background_sound()
            current_time = datetime.now()

        difference = end_time() - datetime.now()
        seconds = user_settings['timed'] - int(difference.total_seconds())
        write_up_page(win, writer, score[0], seconds=seconds)
        win.update()

        if head.direction == "stop":
            turtle.onscreenclick(on_click)
            writer.hideturtle()
            writer.up()
            writer.color('red')
            writer.goto(-285, -290)
            writer.down()
            writer.write("بازگشت", font=("Vazir Bold", 13))
            win.update()
            
        # game over ways
        game_over()

        # eat happened
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # add segments
            newsegment = turtle.Turtle()
            newsegment.speed(0)
            newsegment.shape(settings['shape']['snake_body'])
            newsegment.color(load_theme_setting()['body'])
            newsegment.penup()
            segments.append(newsegment)
            newsegment.hideturtle()
            score[0] += 1
            play_score_sound()
            speed_up(score[0])

            write_up_page(win, writer, score[0], seconds=seconds)


        # move segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].showturtle()
            segments[index].goto(x, y)

        # move 0 segment
        # first segment after head snake
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].showturtle()
            segments[0].goto(x, y)

        move(head)

        sleep(settings['general']['delay'])

def run():
    setup(load_theme_setting())
    snake_game()

if __name__ == "__main__":
    run()