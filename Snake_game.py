import pygame
import random

#starting pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake Game")

score = 0
font = pygame.font.SysFont("Pixeltype.ttf",30)


#snake properties
snake_pos = [180,100]                           #snake head
snake_body = [[180,100],[170,100],[160,100]]    #snake body
snake_direction = "RIGHT"

def draw_snake():
    for segment in snake_body:
        pygame.draw.rect(screen,(255,0,0),(segment[0],segment[1],10,10))


#food properties
food_pos = [random.randrange(1,50)*10,random.randrange(1,50)*10]

def draw_food():
    pygame.draw.rect(screen,(150,50,250),(food_pos[0],food_pos[1],10,10))

running = True
while running:
    pygame.time.delay(55)
    screen.fill((0,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

    #snake restrictions    
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
        
            elif event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"

            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
        
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            
        #movement of snake

    if snake_direction == "RIGHT":
        snake_pos[0] += 10

    if snake_direction == "LEFT":
        snake_pos[0] -= 10
    
    if snake_direction == "UP":
        snake_pos[1] -= 10
    
    if snake_direction == "DOWN":
        snake_pos[1] += 10

    snake_body.insert(0,list(snake_pos))

    if snake_pos == food_pos:
        score += 1
        food_pos = [random.randrange(1,50)*10,random.randrange(1,50)*10]
    else:
        snake_body.pop()

    
   

    if snake_pos[1] >= 600 or snake_pos[1] <=0 or snake_pos[0] >= 600 or snake_pos[0] <= 0:
        running = False
        print("Game Over!")
    
    if snake_pos in snake_body[1:]:
        running = False
    
    #score UI
    score_text = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(score_text, (10, 10))

    draw_snake()
    draw_food()

    pygame.display.update()

pygame.quit()