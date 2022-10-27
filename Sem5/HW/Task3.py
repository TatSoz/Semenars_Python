# Создайте программу для игры в "Крестики-нолики".

board = list(range(1,10))

# вывод поля
def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

# Игроки вводят крестики или нолики (происходит замена имеющегося списка)
def choice(pl_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + pl_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Введите, пожалуйста, число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = pl_token
                valid = True
            else:
                print ("Эта клетка занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9.")

# Проверка игрового поля (создаем кортеж с выигрышными координатами и проверяем с помощью цикла)
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            choice("X")
        else:
            choice("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья, победила ДРУЖБА!")
            break
    draw_board(board)

main(board)


