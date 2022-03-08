import pygame, sys
from pygame.locals import *
import time
import random
import copy
 
# game parameters
pygame.init()
win_width, win_height = 930, 700
displaysurf = pygame.display.set_mode((win_width, win_height), 0, 32)
pygame.display.set_caption('game1')
 


color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_tip_white = (225, 225, 225)
color_tip_black = (25, 25, 25)

 
# chess parameters
chess_grid_row, chess_grid_col = 6, 7
chess_list = []
for i in range(chess_grid_row):
    new_line = [0 for j in range(chess_grid_col)]
    chess_list.append(new_line)
player = True
play_flag = False
 
# draw chessboard
def draw_chessboard():
    displaysurf.fill(color_white)
    fontobj = pygame.font.SysFont('Robot',50)
    text = fontobj.render("Game1", True, color_black, color_white)
    textrect = text.get_rect()
    textrect.center = (430, 70)
    displaysurf.blit(text, textrect)
    pygame.draw.rect(displaysurf, (0,0,255), (50, 170, 560, 480))
    for pix_row in range(7):
        pygame.draw.line(displaysurf, color_black, (50, 170 + pix_row * 80), (610, 170 + pix_row * 80))
    for pix_col in range(9):
        pygame.draw.line(displaysurf, color_black, (50 + pix_col * 80, 170), (50 + pix_col * 80, 650))
def draw_tip_chess(mousex, mousey, type):
    for row in range(chess_grid_row):
        for col in range(chess_grid_col):
            if chess_list[row][col] in [3,4]:
                chess_list[row][col] = 0
    col = int((mousex - 50) / 80)
    row = int((mousey - 170) / 80)
    if row == chess_grid_row:
        row -= 1
    if col == chess_grid_col:
        col -= 1
    if row < chess_grid_row - 1:
        if chess_list[row + 1][col] == 0:
            return
    if chess_list[row][col] == 0:
        chess_list[row][col] = type 

 
def clear_tip_chess():
    for row in range(chess_grid_row):
        for col in range(chess_grid_col):
            if chess_list[row][col] in [3,4]:
                chess_list[row][col] = 0
 
def draw_check_chess(mousex, mousey, type):
    for row in range(chess_grid_row):
        for col in range(chess_grid_col):
            if chess_list[row][col] in [3,4]:
                chess_list[row][col] = 0
    col = int((mousex - 50) / 80)
    row = int((mousey - 170) / 80)
    if row == chess_grid_row:
        row -= 1
    if col == chess_grid_col:
        col -= 1
    if row < chess_grid_row - 1:
        if chess_list[row + 1][col] == 0:
            return
    if chess_list[row][col] in [1, 2]:
        return False
    else:
        chess_list[row][col] = type
        return True
 
def draw_chess():
    for row in range(chess_grid_row):
        for col in range(chess_grid_col):
            if chess_list[row][col] == 0:
                pygame.draw.circle(displaysurf, (0,0,255), (90 + col * 80, 210 + row * 80), 38)
            elif chess_list[row][col] ==1 :
                pygame.draw.circle(displaysurf, color_black, (90 + col * 80, 210 + row * 80), 38)
            elif chess_list[row][col] == 2:
                pygame.draw.circle(displaysurf, color_white, (90 + col * 80, 210 + row * 80), 38)
            elif chess_list[row][col] == 3:
                pygame.draw.circle(displaysurf, color_tip_black, (90 + col * 80, 210 + row * 80), 38)
            elif chess_list[row][col] == 4:
                pygame.draw.circle(displaysurf, color_tip_white, (90 + col * 80, 210 + row * 80), 38)
 
def is_win(temp_chess_list):
    not_null_sum = 0
    for row in range(chess_grid_row):
        for col in range(chess_grid_col):
            if temp_chess_list[row][col] in [3,4]:
                temp_chess_list[row][col] = 0
            if temp_chess_list[row][col] != 0:
                not_null_sum += 1
 
            # horizontal
            if col < chess_grid_col - 3:
                if temp_chess_list[row][col] == temp_chess_list[row][col + 1] == temp_chess_list[row][col + 2] == \
                        temp_chess_list[row][col + 3] and temp_chess_list[row][col] != 0:
                    return temp_chess_list[row][col]
            # vertical
            if row < chess_grid_row - 3:
                if temp_chess_list[row][col] == temp_chess_list[row + 1][col] == temp_chess_list[row + 2][col] == \
                        temp_chess_list[row + 3][col] and temp_chess_list[row][col] != 0:
                    return temp_chess_list[row][col]
            # right slant
            if col < chess_grid_col - 3 and row < chess_grid_row - 3:
                if temp_chess_list[row][col] == temp_chess_list[row + 1][col + 1] == temp_chess_list[row + 2][
                    col + 2] == \
                        temp_chess_list[row + 3][col + 3] and temp_chess_list[row][col] != 0:
                    return temp_chess_list[row][col]
            # left slant
            if col >= 3 and row < chess_grid_row - 3:
                if temp_chess_list[row][col] == temp_chess_list[row + 1][col - 1] == temp_chess_list[row + 2][
                    col - 2] == \
                        temp_chess_list[row + 3][col - 3] and temp_chess_list[row][col] != 0:
                    return temp_chess_list[row][col]
    if not_null_sum==chess_grid_col*chess_grid_row:
        return 3
    return 0
    
 
 
def AI(chess_list,type):
    selectcol=random.randint(0,6)
    if selectcol<0 or selectcol>6:
        return 1
    if not type==1 or type==2:
        return 1
    for each in range(5,-1,-1):
        if chess_list[each][selectcol]==0:
            chess_list[each][selectcol]=type
            return 0
        
            
    
 
def draw_player(player):
    fontobj = pygame.font.SysFont('Robot', 25)
    if player:
        text = fontobj.render("First: Computer    Color: Black", True, color_black, color_white)
    else:
        text = fontobj.render("First: Player    Color: Blacl", True, color_black, color_white)
    textrect = text.get_rect()
    textrect.center = (260, 140)
    displaysurf.blit(text, textrect)
 
def button():
    pygame.draw.rect(displaysurf, color_black, (730, 200, 160, 80))
    fontobj1 = pygame.font.SysFont('Robot', 30)
    text1 = fontobj1.render("Change", True, color_white, color_black)
    textrect1 = text1.get_rect()
    textrect1.center = (810, 240)
    displaysurf.blit(text1, textrect1)
 
    pygame.draw.rect(displaysurf, color_black, (730, 360, 160, 80))
    fontobj2 = pygame.font.SysFont('Robot', 30)
    if play_flag == False:
        text2 = fontobj2.render("Start Game", True, color_white, color_black)
    else:
        text2 = fontobj2.render("Stop Game", True, color_white, color_black)
    textrect2 = text2.get_rect()
    textrect2.center = (810, 400)
    displaysurf.blit(text2, textrect2)
 
    pygame.draw.rect(displaysurf, color_black, (730, 520, 160, 80))
    fontobj3 = pygame.font.SysFont('Robot', 30)
    text3 = fontobj3.render("Reverse Game", True, color_white, color_black)
    textrect3 = text3.get_rect()
    textrect3.center = (810, 560)
    displaysurf.blit(text3, textrect3)
 
def play_type():
    fontobj = pygame.font.SysFont('Robot', 25)
    if play_flag == False:
        win_flag = is_win(chess_list)
        pygame.draw.rect(displaysurf, color_white, (400, 120, 300, 45))
        if win_flag == 0:
            text = fontobj.render("Station: Unstart", True, color_black, color_white)
        elif win_flag == 1:
            if player:
                text = fontobj.render("Station: Computer Victory", True, color_black, color_white)
            else:
                text = fontobj.render("Station: Player Victory", True, color_black, color_white)
        elif win_flag == 2:
            if player:
                text = fontobj.render("Station: Player Victory", True, color_black, color_white)
            else:
                text = fontobj.render("Station: Computer Victory", True, color_black, color_white)
        elif win_flag == 3:
            text = fontobj.render("Station: Tie", True, color_black, color_white)
    else:
        null_sum = 0
        for row in range(chess_grid_row):
            for col in range(chess_grid_col):
                if chess_list[row][col] in [0, 3, 4]:
                    null_sum += 1
        if player:
            if (chess_grid_row*chess_grid_col-null_sum) % 2 == 0:
                text = fontobj.render("Station: Computer Frist Move", True, color_black, color_white)
            else:
                text = fontobj.render("Station: Player First Move", True, color_black, color_white)
        else:
            if (chess_grid_row*chess_grid_col-null_sum) % 2 == 1:
                text = fontobj.render("Station: Computer First Move", True, color_black, color_white)
            else:
                text = fontobj.render("Station: Player First Move", True, color_black, color_white)
    textrect = text.get_rect()
    textrect.center = (570, 140)
    displaysurf.blit(text, textrect)
 
def new_play():
    global player, play_flag
    draw_chessboard()
    # AI(chess_list, 1)
    # main game loop
    while True:
        for event in pygame.event.get():
            # close game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                if play_flag:
                    if mousex > 50 and mousex < 690 and mousey > 170 and mousey < 730:
                        if player:
                            draw_tip_chess(mousex, mousey, 4)
                        else:
                            draw_tip_chess(mousex, mousey, 3)
                    else:
                        clear_tip_chess()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if play_flag:
                    if mousex > 50 and mousex < 690 and mousey > 170 and mousey < 730:
                        if player:
                            flag = draw_check_chess(mousex, mousey, 2)
                            draw_chess()
                            pygame.display.update()
                            if flag:
                                if is_win(chess_list) != 0:
                                    play_flag = False
                                play_type()
                                pygame.display.update()
                                if play_flag:
                                    AI(chess_list, 1)
                            if is_win(chess_list) != 0:
                                play_flag = False
                        else:
                            flag = draw_check_chess(mousex, mousey, 1)
                            draw_chess()
                            pygame.display.update()
                            if flag:
                                if is_win(chess_list) != 0:
                                    play_flag = False
                                play_type()
                                pygame.display.update()
                                if play_flag:
                                    AI(chess_list, 2)
                            if is_win(chess_list) != 0:
                                play_flag = False
                else:
                    if mousex > 730 and mousex < 890 and mousey > 200 and mousey < 280:
                        if is_win(chess_list) == 0:
                            if player:
                                player = False
                            else:
                                player = True
                            draw_player(player)
                if mousex > 730 and mousex < 890 and mousey > 360 and mousey < 440:
                    if play_flag:
                        play_flag = False
                    else:
                        if is_win(chess_list) == 0:
                            play_flag = True
                            play_type()
                            button()
                            pygame.display.update()
                            if player and sum(chess_list[-1]) == 0:
                                AI(chess_list,1)
                elif mousex > 730 and mousex < 890 and mousey > 520 and mousey < 600:
                    play_flag = False
                    for row in range(chess_grid_row):
                        for col in range(chess_grid_col):
                                chess_list[row][col] = 0
 
        draw_player(player)
        button()
        draw_chess()
        play_type()
        pygame.display.update()
 
def main():
    new_play()
 
 
main()

    