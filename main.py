import curses

# 1. login
# (2. match room)
# 3. join table
# 4. start game
#  4.1. table owner is who created the table
#  4.2. table owner control when game starting
#  4.3. everyone can choose any option of 'fold', 'call', 'raise', 'all-in', 'check'
# 5. end game
# 6. exit table
# (7. exit room)
# 8. exit client


def fetch_others_info():
    pass


def update_myself_info():
    pass


def fetch_user(): pass


def summary_info():
    pass


max_y = 0
max_x = 0

main_screen = None
game_info_window = None
user_window = None
user_control_pad = None


def init_main_window():
    global max_y, max_x, main_screen
    main_screen = curses.initscr()
    curses.start_color()  # enable color for highlighting menu options
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, -1)  # color pair 1
    max_yx = main_screen.getmaxyx()
    max_y = max_yx[0]
    max_x = max_yx[1]
    main_screen.keypad(False)
    curses.noecho()
    curses.cbreak()
    curses.start_color()


def init_game_info_window():
    global game_info_window
    game_info_window = curses.newwin(20, 96, 0, 0)
    # Clear screen
    game_info_window.clear()
    game_info_window.addstr(0, 1, 'Bet: {}/{} points\n'.format(1, 2))
    game_info_window.addstr(1, 1, 'Common cards: {}, {}, {}'.format('Diamonds-A', 'Spades-J', 'Hearts-10'))
    game_info_window.addstr(2, 1, 'Pot: {} points'.format('887'))
    game_info_window.addstr(4, 1, 'Player {}: {}'.format('Tom Dwan', 'Check'))
    game_info_window.addstr(5, 1, 'Player {}: {}'.format('Garret', 'Bet 200 points'))
    game_info_window.addstr(6, 1, 'Player {}: {}'.format('Xi jinping', 'Raise to 88888 points'))
    game_info_window.addstr(7, 1, 'Player {}: {}'.format('Li Keqiang', 'Fold'))
    game_info_window.addstr(8, 1, 'Player {}: {}'.format('Li Qiang', '<--'))
    game_info_window.border('|', '|', '-', '-', '+', '+', '+', '+')
    game_info_window.refresh()


def init_user_control_pad():
    global user_control_pad
    user_control_pad = curses.newwin(0, 144, max_y - 9, 0)
    user_control_pad.clear()
    user_control_pad.addstr(0, 0, 'Please choose:')
    options = [[1, 'Check'], [2, 'Fold'], [3, 'Call'], [4, 'Raise to']]
    for x in range(len(options)):
        user_control_pad.addstr(x + 1, 0, '{}-{}'.format(options[x][0], options[x][1]), curses.A_UNDERLINE)
    user_control_pad.refresh()


def init_user_window():
    global user_window
    user_window = curses.newwin(2, 144, max_y - 2, 0)
    user_window.clear()
    user_window.keypad(True)
    user_window.addstr(0, 0, 'Your cards: {}, {}'.format('Club-J', 'Spades-2'))
    user_window.addstr(1, 0, 'Please wait...')
    user_window.refresh()
    user_window.getkey()


if __name__ == '__main__':
    init_main_window()
    init_game_info_window()
    init_user_control_pad()
    init_user_window()
