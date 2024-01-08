import random
import pygame

pygame.init()
pygame.font.init()

field_size = (300, 400)
win = pygame.display.set_mode(field_size)
screen = pygame.Surface(field_size)
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill((0, 0, 0))

win_player = 0
win_bot = 0
menu = True

end = False
data = [['', '', ''],
        ['', '', ''],
        ['', '', '']]
move = [[0, 0], [0, 1], [0, 2],
        [1, 0], [1, 1], [1, 2],
        [2, 0], [2, 1], [2, 2]]


def draw_menu(scr):
    font_menu = pygame.font.Font(None, 50)
    text_menu = font_menu.render('Menu', True, (100, 200, 100))
    scr.blit(text_menu, (100, 50))

    pygame.draw.rect(scr, (20, 20, 20), (105, 140, 95, 55))
    font_bot = pygame.font.Font(None, 50)
    text_bot = font_bot.render('PvE', False, (200, 100, 100))
    # 98 134
    # 197 182
    scr.blit(text_bot, (120, 150))

    pygame.draw.rect(scr, (20, 20, 20), (105, 220, 95, 55))
    font_5 = pygame.font.Font(None, 50)
    text_5 = font_5.render('PvP', False, (100, 100, 200))
    # 104 218
    # 194 262
    scr.blit(text_5, (120, 230))


def draw_grid(scr):
    pygame.draw.line(scr, (255, 255, 255), (100, 0), (100, 300), 2)
    pygame.draw.line(scr, (255, 255, 255), (200, 0), (200, 300), 2)
    pygame.draw.line(scr, (255, 255, 255), (0, 100), (300, 100), 2)
    pygame.draw.line(scr, (255, 255, 255), (0, 200), (300, 200), 2)
    pygame.draw.line(scr, (255, 255, 255), (0, 300), (300, 300), 2)

    pygame.draw.rect(scr, (80, 80, 80), (20, 315, 110, 70))  # (125, 385)

    font = pygame.font.Font(None, 50)
    text = font.render('Clear', True, (180, 180, 180))
    scr.blit(text, (30, 335))

    pygame.draw.rect(scr, (80, 80, 80), (170, 315, 110, 70))

    font = pygame.font.Font(None, 50)
    text = font.render('Menu', True, (180, 180, 180))
    scr.blit(text, (180, 335))


def draw_play(scr, value):
    for i in range(3):
        for j in range(3):
            if value[i][j] == 'O':
                pygame.draw.circle(scr, (255, 175, 175), (j * 100 + 50, i * 100 + 50), 45)
                pygame.draw.circle(scr, (0, 0, 0), (j * 100 + 50, i * 100 + 50), 40)
            elif value[i][j] == 'X':
                pygame.draw.line(scr, (175, 175, 255), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 5)
                pygame.draw.line(scr, (175, 175, 255), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 5)


def raise_the_flag(data, player):
    flag = False
    # for line in data:
    #     if line.count(player) == 3:
    #         flag = True
    for i in range(3):
        if data[i][0] == data[i][1] == data[i][2] == player:
            flag = True
    for i in range(3):
        if data[0][i] == data[1][i] == data[2][i] == player:
            flag = True
    if data[0][0] == data[1][1] == data[2][2] == player:
        flag = True
    if data[0][2] == data[1][1] == data[2][0] == player:
        flag = True
    return flag


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            print(pos[0], pos[1])
            print(move)
            if menu:
                if 105 <= pos[0] <= 200 and 140 <= pos[1] <= 195:
                    screen.fill((0, 0, 0))
                    menu = False

            elif pos[0] <= 150 and pos[1] >= 300 and not menu:
                pygame.display.set_caption(' : '.join([str(win_player), str(win_bot)]))
                screen.fill((0, 0, 0))
                end = False
                data = [['', '', ''],
                        ['', '', ''],
                        ['', '', '']]
                move = [[0, 0], [0, 1], [0, 2],
                        [1, 0], [1, 1], [1, 2],
                        [2, 0], [2, 1], [2, 2]]
                draw_grid(screen)

            elif pos[0] > 150 and pos[1] >= 300 and not menu:
                screen.fill((0, 0, 0))
                draw_menu(screen)
                menu = True

            elif not end and not menu:
                if data[pos[1] // 100][pos[0] // 100] == '':
                    data[pos[1] // 100][pos[0] // 100] = 'X'
                draw_play(screen, data)
                # проверка на значение
                for elem in move:
                    # print(elem)
                    if data[elem[0]][elem[1]] == 'X':
                        # print('падение')
                        move.remove(elem)

                cross_win = raise_the_flag(data, 'X')
                if cross_win:
                    pygame.display.set_caption('Вы победили')
                    end = True
                    win_player += 1
                    print('победа человека')

                # ход бота
                if not end and len(move) != 0:
                    if (data[1][1] == data[2][2] != '' or data[0][1] == data[0][2] != '' or data[1][0] == data[2][0]
                        != '') and data[0][0] == '':
                        data[0][0] = 'O'
                        move.remove([0, 0])
                    elif (data[0][0] == data[1][1] != '' or data[2][0] == data[2][1] != '' or data[0][2] == data[1][2]
                          != '') and data[2][2] == '':
                        data[2][2] = 'O'
                        move.remove([2, 2])
                    elif (data[0][0] == data[1][0] != '' or data[2][1] == data[2][2] != '' or data[1][1] == data[0][2]
                          != '') and data[2][0] == '':
                        data[2][0] = 'O'
                        move.remove([2, 0])
                    elif (data[0][0] == data[0][1] != '' or data[1][2] == data[2][2] != '' or data[2][0] == data[1][1]
                          != '') and data[0][2] == '':
                        data[0][2] = 'O'
                        move.remove([0, 2])
                    elif (data[0][0] == data[2][2] != '' or data[0][1] == data[2][1] != '' or data[0][2] == data[2][0]
                          != '' or data[1][0] == data[1][2] != '') and data[1][1] == '':
                        data[1][1] = 'O'
                        move.remove([1, 1])
                    elif (data[0][0] == data[0][2] != '' or data[1][1] == data[2][1] != '') and data[0][1] == '':
                        data[0][1] = 'O'
                        move.remove([0, 1])
                    elif (data[0][1] == data[1][1] != '' or data[2][0] == data[2][2] != '') and data [2][1] == '':
                        data[2][1] = 'O'
                        move.remove([2, 1])
                    else:
                        tim = random.choice(move)
                        data[tim[0]][tim[1]] = 'O'
                        move.remove(tim)
                ###
                zero_win = raise_the_flag(data, 'O')
                if zero_win:
                    pygame.display.set_caption('Компьютер победил')  # С запазданием на ход пишет победу
                    end = True
                    win_bot += 1
                    print('победа бота')

                ###
                if len(move) == 0 and not (cross_win or zero_win):  # Так и не достиг....
                    pygame.display.set_caption('Ничья')
                    end = True
                print(move)
        if menu:
            draw_menu(screen)
        else:
            draw_play(screen, data)
            draw_grid(screen)

    # win.blit(text, (100, 150))

    # draw_grid(screen)
    win.blit(screen, (0, 0))
    pygame.display.update()
