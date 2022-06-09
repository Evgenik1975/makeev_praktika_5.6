plase = list(range(1, 10))

def plase_game(plase):
    print('-' * 13)
    for i in range(3):
        print('|', plase[0 + i * 3], '|', plase[1 + i * 3], '|', plase[2 + i * 3], '|')
        print('-' * 13)
plase_game(plase)


def result(plase):
    V = ((0,1,2), (3,4,5), (6,7,8), (0,4,8), (2,4,6), (0,3,6), (1,4,7), (2,5,8))
    for p in V:
        if plase[p[0]] == plase[p[1]] == plase[p[2]]:
            return plase[p[0]]     
    return False


def answer(plase):
    n = 0
    c = False
    while not c:
        
        if n % 2 == 0:
            plase[(int(input('Введите номер клетки для 0:'))) - 1] = '0'
        else:
            plase[(int(input('Введите номер клетки для Х:'))) - 1] = 'X'
        n += 1

        plase_game(plase)

        if n > 4:
            d = result(plase)
            if d:
                print('Победил', d, '!!!')
                c = True
                break
        if n == 9:
            print('Ничья!!!')
            break

        result(plase)
        
answer(plase)

print('game over')
    