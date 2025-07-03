import random

def safe_convert(value: any, to_type: type):
    try:
        return to_type(value)
    except:
        transactions_file.close()
        save_file.close()

transactions_file = open('transactions.txt', 'a')
save_file = open('save.json', 'r+')
data = save_file.read()

def new_game():

    data = {
        'players': [],
        'cash': [],
        'last_save': False,
        #DO LAST SAVE PROGRMMING
    }

    start_cash = safe_convert(input('Enter starting cash (int value): '), int)

    #collect player names
    for player in range (1, 17):
        print('Enter player names below. Max players is 16. Enter "done" when finished')
        data['players'].append(input(f'Player {player} name: '))
        if data['players'][-1].lower() == 'done':
            data['players'].pop(-1)
            break
        else:
            data['cash'].append(start_cash)

def main_loop():
    return

if input('Continue from last save on "ADD LAST SAVE HERE" ? (y/n)')[0].lower() == 'n':
    new_game()
else:
    main_loop()

transactions_file.close()
save_file.close()