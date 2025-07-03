import random

def safe_convert(value: any, to_type: type):
    try:
        return to_type(value)
    except Exception as error:
        transactions_file.close()
        save_file.close()
        raise error

transactions_file = open('transactions.txt', 'a')
save_file = open('save.json', 'r+')
data = save_file.read()

def new_game():
    return

def main_loop():
    return

if input('Continue from last save on "ADD LAST SAVE HERE" ? (y/n)')[0].lower() == 'n':
    new_game()
else:
    main_loop()

transactions_file.close()
save_file.close()