import turtle

from settings import user_settings
from utilities import change_user_theme, play_background_sound
from snake import run


def setup():
    global win, win2, t1, t2, t3, t4, m1, m2, m3, m4, writer
    win = turtle.Screen()
    win.setup(width=600, height=600)
    win.title('Python Game')
    win.bgcolor('darkorange')
    win.tracer(0)

    win2 = turtle.Screen()
    win2.setup(width=600, height=600)
    win2.title('Python Game')
    win2.bgcolor('darkorange')
    win2.tracer(0)

    t1 = turtle.Turtle()
    m1 = turtle.Turtle()
    t2 = turtle.Turtle()
    m2 = turtle.Turtle()
    t3 = turtle.Turtle()
    m3 = turtle.Turtle()
    writer = turtle.Turtle()

def draw_text(turtle_obj, x, y, text, font_size):
        turtle_obj.penup()
        turtle_obj.goto(x, y-50)
        turtle_obj.pendown()
        turtle_obj.color("black")
        turtle_obj.write(text, font=("Vazir Bold", font_size))
        turtle_obj.hideturtle()

def success_message(theme_name, custom_message=None):
    turtle.clear()
    turtle.up()
    turtle.goto(win2.window_width() / 2 - 320, -win2.window_height() / 2 + 10)
    turtle.down()
    turtle.color('green')
    if custom_message is not None:
        turtle.write(custom_message, font=("Vazir Bold", 13))
    else:
        turtle.write(f"تم {theme_name} ‌با موفقیت برای شما ذخیره شد", font=("Vazir Bold", 13))


def draw_game_theme():
    setup()
    def on_click(x, y):
        if -230 < x < -80 and 22 < y < 173:  # ahram
            win2.clear()
            setup()
            change_user_theme(1)
            draw_game_mode("اهرام")

        elif 70 < x < 221 and 24 < y < 175:
            win2.clear()
            setup()
            change_user_theme(2)
            draw_game_mode("لبخند")

        elif -230 < x < -81 and -201 < y < -50:
            win2.clear()
            setup()
            change_user_theme(3)
            draw_game_mode('کهکشان')
    
        elif 70 < x < 221 and -200 < y < -49:
            win2.clear()
            setup()
            change_user_theme(4)
            draw_game_mode('کوروش')

        elif -290 < x < -125 and -287 < y < -257:
            win2.clear()
            setup()
            draw_game_mode()


    # title
    t1.penup()
    t1.goto(-85, 240)
    t1.pendown()
    t1.color("black")
    t1.write("انتخاب قالب", font=("Vazir Bold", 24))

    # Option 1
    t1.penup()
    t1.goto(-230, 22)
    t1.pendown()
    t1.color("black")
    t1.forward(151)
    t1.left(90)
    t1.forward(151)
    t1.left(90)
    t1.forward(151)
    t1.left(90)
    t1.forward(151)

    t1.penup()
    t1.goto(-154, 97)
    t1.pendown()
    turtle.addshape(r'images\1-ahram.gif')
    t1.shape(r'images\1-ahram.gif')

    m1.hideturtle()
    m1.penup()
    m1.goto(-205, -20)
    m1.pendown()
    m1.color("darkslategray")
    m1.write("تم اهرام", font=("Vazir Bold", 22))

    # Option 2
    t2.penup()
    t2.goto(70, 175)
    t2.pendown()

    t2.penup()
    t2.goto(146, 97)
    t2.pendown()
    turtle.addshape(r'images\2-smile.gif')
    t2.shape(r'images\2-smile.gif')

    m2.hideturtle()
    m2.penup()
    m2.goto(95, -21)
    m2.pendown()
    m2.color("darkslategray")
    m2.write("تم لبخند", font=("Vazir Bold", 22))

    # Option 3
    t3.penup()
    t3.goto(-230, -50)
    t3.pendown()

    t3.penup()
    t3.goto(-153, -120)
    t3.pendown()
    turtle.addshape(r'images\3-galaxy.gif')

    t3.shape(r'images\3-galaxy.gif')

    m3.hideturtle()
    m3.penup()
    m3.goto(-220, -245)
    m3.pendown()
    m3.color("darkslategray")
    m3.write("تم کهکشان", font=("Vazir Bold", 22))


    writer.hideturtle()
    writer.up()
    writer.color('black')
    writer.goto(-285, -290)
    writer.down()
    writer.write("بازگشت", font=("Vazir Bold", 13))
    win2.update()

    turtle.onscreenclick(on_click)
    turtle.done()

def draw_rectangle(turtle_obj, x, y, width, height, color):
    turtle_obj.penup()
    turtle_obj.goto(x, y-50)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    turtle_obj.fillcolor(color)
    turtle_obj.width(3)
    for _ in range(2):
        turtle_obj.fd(width)
        turtle_obj.lt(90)
        turtle_obj.fd(height)
        turtle_obj.lt(90)
    turtle_obj.end_fill()
    turtle_obj.hideturtle()

def draw_time_mode():
    setup()
    def on_click(x, y):
        if -200 < x < 200 and 75 < y < 160:
            user_settings['timed'] = 60
            win.clear()
            run()

        elif -200 < x < 200 and -50 < y < 25:
            user_settings['timed'] = 120
            win.clear()
            run()

        elif -200 < x < 200 and -170 < y < -100:
            user_settings['timed'] = 180
            win.clear()
            run()
    

        elif -290 < x < 290 and -287 < y < -257:
            win.clear()
            draw_game_mode()



    # 60 seconds mode
    t5 = turtle.Turtle()
    t5.hideturtle()
    t5.up()
    t5.goto(0, win.window_height() // 2 - 60)
    t5.down()
    t5.write('مدت زمان بازی', align='center', font=("Vazir Bold", 30)) 
    draw_rectangle(t5, -200, 120, 400, 70, "slateblue")
    draw_text(t5, -55, 130, "یک دقیقه‌ای", 20)

    t6 = turtle.Turtle()
    draw_rectangle(t6, -200, 0, 400, 70, "slateblue")
    draw_text(t6, -55, 15, "دو دقیقه‌ای", 20)

    t7 = turtle.Turtle()
    draw_rectangle(t7, -200, -120, 400, 70, "slateblue")
    draw_text(t7, -55, -105, "سه دقیقه‌ای", 20)

    # return
    t8 = turtle.Turtle()
    draw_text(t8, -285, -240, "بازگشت", 13)
    
    turtle.onscreenclick(on_click)
    turtle.done()

def draw_game_mode(theme_name=None):
    setup()
    if theme_name is not None:
        success_message(theme_name)

    def on_click(x, y):
        if -200 < x < 200 and 75 < y < 160:
            user_settings['mode'] = 'timed'
            win.clear()
            draw_time_mode()

        elif -200 < x < 200 and -50 < y < 25:
            user_settings['mode'] = 'normal'
            win.clear()
            run()

        elif -200 < x < 200 and -170 < y < -100:
            user_settings['mode'] = 'comfortable'
            win.clear()
            run()
    

        elif -290 < x < 290 and -287 < y < -257:
            win.clear()
            draw_game_theme()



    # نوع بازی 1
    t5 = turtle.Turtle()
    t5.hideturtle()
    t5.up()
    t5.goto(0, win.window_height() // 2 - 60)
    t5.down()
    t5.write('نوع بازی', align='center', font=("Vazir Bold", 30)) 
    draw_rectangle(t5, -200, 120, 400, 70, "slateblue")
    draw_text(t5, -35, 130, "زمان‌دار", 20)

    # نوع بازی 2
    t6 = turtle.Turtle()
    draw_rectangle(t6, -200, 0, 400, 70, "slateblue")
    draw_text(t6, -25, 15, "عادی", 20)

    # نوع بازی 3
    t7 = turtle.Turtle()
    draw_rectangle(t7, -200, -120, 400, 70, "slateblue")
    draw_text(t7, -25, -105, "آسان", 20)

    # settings
    t8 = turtle.Turtle()
    draw_text(t8, -285, -240, "تنظیمات تم", 13)
    
    # نمایش صفحه
    turtle.onscreenclick(on_click)
    turtle.done()


def page_run():
    print("فقط جهت اجرای صدا از کتابخانه pygame استفاده شده\nو تنها کتابخانه گرافیکی این پروژه turtle است.")
    play_background_sound()
    setup()
    draw_game_mode()

if __name__ == "__main__":
    page_run()