import curses
from ui.cards import CardMap

main_screen = None
game_info_window = None
player_info_window = None
user_window = None
user_control_pad = None
max_y = 0
max_x = 0


def __init_main_window():
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


def __init_game_info_window():
    global game_info_window
    game_info_window = curses.newwin(6, 96, 0, 0)
    # Clear screen
    game_info_window.clear()
    game_info_window.addstr(1, 1, 'Bet: ?/? points')
    game_info_window.addstr(2, 1, 'Common cards: ?')
    game_info_window.addstr(3, 1, 'Pot: 0 points')

    game_info_window.border('|', '|', '-', '-', '+', '+', '+', '+')
    game_info_window.refresh()


def __init_player_info_window():
    global player_info_window
    player_info_window = curses.newwin(14, 96, 7, 0)
    player_info_window.keypad(False)
    player_info_window.clear()
    player_info_window.addstr(1, 1, 'Wait more players to start game!')

    player_info_window.border('|', '|', '-', '-', '+', '+', '+', '+')
    player_info_window.refresh()


def __init_user_control_pad():
    global user_control_pad
    user_control_pad = curses.newwin(0, 144, max_y - 9, 0)
    user_control_pad.clear()
    user_control_pad.addstr(0, 0, 'Please choose:')
    options = [[1, 'Check'], [2, 'Fold'], [3, 'Call'], [4, 'Raise to']]
    for x in range(len(options)):
        user_control_pad.addstr(x + 1, 0, '{}-{}'.format(options[x][0], options[x][1]), curses.A_UNDERLINE)
    user_control_pad.refresh()


def __init_user_window():
    global user_window
    user_window = curses.newwin(2, 144, max_y - 2, 0)
    user_window.clear()
    user_window.keypad(True)
    user_window.addstr(0, 0, 'Your cards: {}, {}'.format('Club-J', 'Spades-2'))
    user_window.addstr(1, 0, 'Please wait...')
    user_window.refresh()
    user_window.getkey()


def init_ui():
    __init_main_window()
    __init_game_info_window()
    __init_player_info_window()
    __init_user_control_pad()
    __init_user_window()


def update_game_info(data):
    if game_info_window is None:
        return

    game_info_window.clear()
    bet_rate = data["bet_rate"]
    total_pot = data["total_pot"]
    table_id = data["table_id"]

    card_on_table = ', '.join(list(map(lambda card: CardMap[card], data["cards_on_table"])))

    game_info_window.addstr(1, 1, f'Table ID: {table_id}')
    game_info_window.addstr(2, 1, f'Bet: {bet_rate} points')
    game_info_window.addstr(3, 1, f'Common cards: {card_on_table}')
    game_info_window.addstr(4, 1, f'Pot: {total_pot} points')

    game_info_window.border('|', '|', '-', '-', '+', '+', '+', '+')
    game_info_window.refresh()


def update_player_info(data):
    if player_info_window is None:
        return

    player_info_window.clear()
    pil = data['player_list']

    for pindex in range(len(pil)):
        p = pil[pindex]
        card1 = CardMap[p['cards_in_hand'][0]]
        card2 = CardMap[p['cards_in_hand'][1]]

        player_info_window.addstr(pindex + 1, 1, '[{}] {}: {}, {}'.format(p['role'], p['name'], card1, card2))

    player_info_window.border('|', '|', '-', '-', '+', '+', '+', '+')
    player_info_window.refresh()
