import time
import json

def current_time():
    return time.strftime("Date: %d/%m/%Y, Time: %H:%M", time.localtime())

transactions_file = open('transactions.txt', 'a')
save_file = open('save.json', 'r+')
data = json.load(save_file)

def update_save():
    save_file.seek(0)
    save_file.truncate()
    json.dump(data, save_file)

def main_loop():
    while True:
        print('''
Options (Enter a number):
1. Make transaction
2. View leaderboard
3. Save and exit
''')
        choice = input('Choice: ')

        if choice == '1':
            amount = int(input('Amount: '))
            print('Accounts:')
            print('0: Bank')
            for number in range(len(data["players"])):
                print(f'{number + 1}: {data["players"][number]}')
            tranfer_from = int(input('Transfer from (enter number): '))
            tranfer_to = int(input('Transfer to (enter number): '))
            if tranfer_from != 0:
                data["cash"][tranfer_from-1] -= amount
            if tranfer_to != 0:
                data["cash"][tranfer_to-1] += amount
            update_save()
            tranfer_from_str = 'Bank' if tranfer_from == 0 else data["players"][tranfer_from-1]
            tranfer_to_str = 'Bank' if tranfer_to == 0 else data["players"][tranfer_to-1]
            transactions_file.write(f'Transfered {amount} from {tranfer_from_str} to {tranfer_to_str} at {current_time()}\n')
        
        elif choice == '2':
            print('\nLeaderboard:')
            sorted_cash = sorted(data["cash"], reverse=True)
            for amount in sorted_cash:
                position = sorted_cash.index(amount)
                print(f'{data["players"][position]}: {amount}')
                data['players'].pop(position)
        elif choice == '3':
            break
        else:
            print('Invalid choice, enter 1, 2, or 3')

def new_game():

    data['players'] = []
    data['cash'] = []
    data['last_save'] = current_time()

    start_cash = int(input('Enter starting cash (int value): '))

    #collect player names
    for player in range (1, 17):
        print('Enter player names below. Max players is 16. Enter "done" when finished')
        data['players'].append(input(f'Player {player} name: '))
        if data['players'][-1].lower() == 'done':
            data['players'].pop(-1)
            break
        else:
            data['cash'].append(start_cash)
    
    transactions_file.seek(0)
    transactions_file.truncate()

    update_save()
    main_loop()

if input(f'Continue from last save on ({data["last_save"]}) with players {data["players"]}? (y/n): ')[0].lower() == 'n':
    new_game()
else:
    main_loop()

transactions_file.close()
save_file.close()