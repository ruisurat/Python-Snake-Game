import pygame
import time
import pickle
import random

pygame.init()

white=(255, 255, 255)
yellow=(255, 255, 102)
black=(0, 0, 0)
red=(213, 50, 80)
green=(0, 255, 0)
blue=(50, 153, 213)

dis_width=600
dis_height=400

savefile='save.sv'

dis=pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by ruisu')

clock=pygame.time.Clock()

snake_block=10
snake_speed=15

poisonx = []
poisony = []

font_style=pygame.font.SysFont("bahnschrift", 25)
score_font=pygame.font.SysFont("comicsansms", 25)
high_score_font=pygame.font.SysFont("comicsansms", 15)

# function to create a pixel for each x in the snake_list array
def player_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# function to display the players current score
def player_score(score):
    value = score_font.render("Score:" + str(score), True, white)
    dis.blit(value, [5, 0])

# function to display the players high score
def player_high_score(score):
    value = high_score_font.render("High Score:" + str(score), True, white)
    dis.blit(value, [5, 30])

# message function to display text with a string and color
def message(msg,color):
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg,[dis_width/6, dis_height/6])

# really basic milestone system
def milestone_x(score):
    if score == 1:
        poisonx.append(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
    if score == 5:
        poisonx.append(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
    if score == 10:
        poisonx.append(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
    if score == 15:
        poisonx.append(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
    if score == 20:
        poisonx.append(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
    if score == 25:
        poisonx.append(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
    if score == 30:
        poisonx.append(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)

def milestone_y(score):
    if score == 1:
        poisony.append(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
    if score == 5:
        poisony.append(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
    if score == 10:
        poisony.append(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
    if score == 15:
        poisony.append(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
    if score == 20:
        poisony.append(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
    if score == 25:
        poisony.append(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
    if score == 30:
        poisony.append(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)

# loop the game functions
def gameLoop():
    game_over=False
    game_close=False

    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0

    snake_list = []
    length_of_snake = 1

    current_milestone = -1
    milestone_changed = True
    
    try:
        with open('score.sv', 'rb') as file:
            high_score = pickle.load(file)
    except:
        high_score = 0

    foodx=round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody=round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    # for i in range(0, 100, 1):
    #     print(i)
    #     if length_of_snake-1==i:
    #         poisonx.append(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
    #         poisony.append(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        

    # check that game is not over
    while not game_over:
        # check that game hasn't closed
        while game_close==True:
            dis.fill(black)
            message("You lost! Q=Quit, ENTER=Try Again", red) # tell player they have lost!
            player_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_RETURN:
                        poisonx.clear()
                        poisony.clear()
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP or event.key==pygame.K_w:
                    x1_change=0
                    y1_change=-snake_block
                elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    x1_change=0
                    y1_change=snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        for i in range(0, len(poisony)):
            pygame.draw.rect(dis, red, [poisonx[i], poisony[i], snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list)> length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x==snake_head:
                game_close=True

        player_snake(snake_block, snake_list)
        player_score(length_of_snake - 1)
        player_high_score(high_score)

        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody=round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            for i in poisonx:
                a = 0
                for v in poisony:
                    b = 0
                    poisonx[a] = (round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                    poisony[b] = (round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                    a+=1
                    b+=1

            length_of_snake+=1

            milestone_x(length_of_snake-1)
            milestone_y(length_of_snake-1)
        
        for i in poisonx:
            for v in poisony:
                if x1 == i and y1 == v:
                    game_close = True

        clock.tick(snake_speed)

        if length_of_snake-1 > high_score:
            with open('score.sv', 'wb') as file:
                pickle.dump(length_of_snake-1, file)

    pygame.quit()
    quit()

gameLoop()