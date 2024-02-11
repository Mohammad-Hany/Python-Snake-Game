settings = {
    'general': {
        'delay': 0.1,
        'initial_delay': 0.1,
        'is_shift_pressed': False,
        'SUA': 20,    # speed up after -> S.U.A
        'SDT': 0.007, # speed down to  -> S.D.T
        },
    
    'backgrounds': {
        '1PATH': r'images\bg1.gif',
        '2PATH': r'images\bg2.gif',
        '3PATH': r'images\bg3.gif',
    },
    
    'shape': {
        'snake_head': 'circle',
        'snake_body': 'circle',
        'food': 'circle'
    },

    'themes': {
        1: {'bg': '1', 'head': 'chocolate', 'body': 'firebrick', 'food': 'darkturquoise', 'text': 'orange'},
        2: {'bg': '2', 'head': 'darkblue', 'body': 'darkslateblue', 'food': 'darkred', 'text': 'black'},
        3: {'bg': '3', 'head': 'blueviolet', 'body': 'darkcyan', 'food': 'white', 'text': 'orange'},
        4: {'bg': '4', 'head': 'chocolate', 'body': 'firebrick', 'food': 'darkturquoise', 'text': 'orange'}
    },

    'BACKGROUND_SOUND_PATH': r'sounds_effect\background_sound.wav',
    'SPEED_ICON_PATH': r'images\airplane.gif',
    'GET_SCORE_SOUND_PATH': r"sounds_effect\score.wav",
    'WALL_SOUND_PATH': r"sounds_effect\wall.wav",
    'SHIFT_SOUND_PATH': r"sounds_effect\shift.mp3"
}

user_settings = {
    'theme': {
        'bg': '2',
        'head': 'darkblue',
        'body': 'darkslateblue',
        'food': 'darkred',
        'text': 'black'
    },

    'mode': 'normal', #has three modes: Normal, Comfortable, Timed
    'timed': 60, #can choice between 2m and 5m
}