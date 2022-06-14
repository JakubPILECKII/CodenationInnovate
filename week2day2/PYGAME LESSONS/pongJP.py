import pygame, sys, random


#? THIS IMPORTS PYGAME AND ALOWS YOUR SYSTEM TO ACCS MORE OF FUNCTIONALITY 

pygame.init()
#? innities all pygae moodules 
#? REQUIRED IN ALL PYGAME PORJECTS

clock = pygame.time.Clock()
#? Variable clock 


######################? CREATA THE GAME WINDOW ######################
screen_width = 1280
screen_height = 960
##?##################################################################

screen = pygame.display.set_mode((screen_width, screen_height))

#?########## THIS IS IMPORTANT
#?########## RETURNS A DUSPLAY SURFACE OBJECT
#?########## STORED IN A VARIABLE CALLED SCREEN    

pygame.display.set_caption("PONG JP")


#?#################### F U N C T I O N S    

def ball_animation():
        global ball_speed_x, ball_speed_y

        ball.x += ball_speed_x
        ball.y += ball_speed_y
        if ball.top <= 0 or ball.bottom>= screen_height:
            ball_speed_y *= -1

        if ball.left <= 0 or  ball.right >= screen_width:
            ball_restart()

        if ball.colliderect (player) or ball.colliderect(opponent):
            ball_speed_x *= -1

def player_animation():
        player.y += player_speed
        if player.top <= 0:
            player.top =0
        if player.bottom >= screen_height:
            player.bottom = screen_height

def opponent_animation():
        if opponent.top < ball.y:
            opponent.top += opponent_speed
        if opponent.bottom > ball.y:
            opponent.bottom -= opponent_speed

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))




#?#########################  GAME RECTANGLES ########################
#?####################### takes X and Y position 
ball = pygame.Rect(screen_width/2 -15, screen_height/2 -15, 30, 30)

#?##################################

player= pygame.Rect(screen_width -20, screen_height/2 -70, 10,140)
#?########## defining the size of the player and its position #####
#?########## 10px wide and 140px high #######
#?########## SETING PLAYER TO THE TOP LEFT (-20) #########
#?########## screen heigh is devided by "2/" and then half player heighq(140)
#?##################################################################

opponent = pygame.Rect(10, screen_height/2 -70, 10, 140)
#?########## same heigh as the player #######
#?########## positioned left on the screen #########


#?########## COLOURS ############################
bg_colour = pygame.Color('grey12')
green = (20, 200, 10)
yellow =(255,215,0)



#?##########   ANIMATION 
ball_speed_x =7 *random.choice((1, -1))
ball_speed_y = 7 *random.choice((1, -1))
player_speed = 0 
opponent_speed = 7






###? SETING UP THE "WHILE LOOP" TO MAKE GAME PLAY
while True:
    #? HANDLING INPUT FROM USER
    for event in pygame.event.get():
        #? ALL USER INPUTS IS CLASSED AS AN EVEN IN PYGAME
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        player_speed += 7
                    if event.key == pygame.K_UP:
                        player_speed -= 7
                        
        if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        player_speed -= 7
                    if event.key == pygame.K_UP:
                        player_speed += 7

        
    
    screen.fill(bg_colour)


    
    ball_animation()
    player_animation()
    opponent_animation()






    player.y += player_speed
    ##? above we added speed to player on every frame


        #? CHECKS TO SEE IF THE USER CLOCKED X TO CLOSE SCREEN 
        ###? CODE ABOVE MEAN THAT AS LONG AS NOBY CLOCK "x" TO CLOSE THE GAME THEN THE GAME RUNS. 
    pygame.draw.rect(screen, green, player)
    pygame.draw.rect(screen, green, opponent)    
    ###?##### WEE ADD THE BALL
    pygame.draw.ellipse(screen, green, ball)


    pygame.draw.aaline(
        screen, yellow,
        (screen_width/2,0),
        (screen_width/2,
        screen_height))

##?  WHEN YOU DRWA IN PYTHON ELEMENTS ARE DRAWN ON TOP OF EACH OTHER 
##?  SO BACKGROUND WOULD HAVE TO BE FIRST IN CODE AS ITS LAST LEYER. 
##?  WE NEED TO DRAW IN ORDER 

    pygame.display.flip() 
    clock.tick(60)
    



##?####################### UPDATIND THE WINDOW ###############################






