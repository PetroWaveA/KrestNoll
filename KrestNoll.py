field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
def show_field(a):
    print("  0 1 2")
    for i in range(len(field)):
        print(str(i), *field[i])
def player_input(a):
    while True:
        coordinates = input("Введите координаты : ").split()
        if len(coordinates) != 2:
            print("Введите две координаты!")
            continue
        if not (coordinates[0].isdigit() and coordinates[1].isdigit()):
            print("Нужно ввести числа!")
            continue
        x, y = map(int, coordinates)
        if not (0 <= x <= 2 and 0 <= y <= 2):
            print("Введите числа от 0 до 2!")
            continue
        if a[x][y] != '-':
            print("Клетка занята!")
            continue
        break
    return x, y
def win_game(a, player):
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for coord in win_coord:
        symbols = []
        for c in coord:
            symbols.append(a[c[0]][c[1]])
        if symbols == [player, player, player]:
            return True
    return False
count = 0
print('Добро пожаловать в игру "крестики-нолики"')
while True:
    if count == 9:
        print("Ничья!")
        break
    if count % 2 == 0:
        player = 'x'
    else:
        player = 'o'
    show_field(field)
    x, y = player_input(field)
    field[x][y] = player
    if win_game(field, player):
        print(f'Выиграл {player}, Поздравляю!!!')
        show_field(field)
        break
    count += 1