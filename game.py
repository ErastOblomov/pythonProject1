import pygame, sys, time, random

difficulty = 10

frame_size_x = 720
frame_size_y = 480

pygame.init()

pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 255, 255)

fps_controller = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

food_pos = [random.randrange(1, (frame_size_x//10))*10,
            random.randrange(1, (frame_size_y//10))*10]

food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x//2, frame_size_y//4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def show_score():
    my_font = pygame.font.SysFont('times new roman', 20)
    game_over_surface = my_font.render(f'Score: {score}', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x//10, 15)
    game_window.blit(game_over_surface, game_over_rect)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))

    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x // 10)) * 10,
                    random.randrange(1, (frame_size_y // 10)) * 10]
    food_spawn = True

    game_window.fill(black)
    counter = 0
    for pos in snake_body:
        if counter == 0:
            pygame.draw.rect(game_window, red,
                             pygame.Rect(pos[0], pos[1], 10, 10))
            counter += 1
        else:
            pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white,
                     pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x - 10:
        game_over()

    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - 10:
        game_over()

    if score >= 2:
        for block in snake_body[4::]:
            if block[0] == snake_pos[0] and block[1] == snake_pos[1]:
                game_over()

    show_score()
    pygame.display.update()
    fps_controller.tick(difficulty)

