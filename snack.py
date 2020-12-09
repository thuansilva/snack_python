import pygame, sys,time

posicao_x= 280
posicao_y= 280
pygame.display.set_caption('Jogo da Cobrina')
janela_jogo = pygame.display.set_mode((posicao_x,posicao_y))

fps_controller = pygame.time.Clock()


snake_pos = [100, 100]
snake_body = [[100, 100], [100-10, 100], [100-(2*10), 100]]

direction= 'RIGHT'
change_to = direction

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# logica dos comandos de direção
while True: 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        change_to = 'UP'
      if event.key == pygame.K_DOWN:
        change_to = 'DOWN'
      if event.key == pygame.K_RIGHT:
        change_to = 'RIGHT'
      if event.key == pygame.K_LEFT:
        change_to = 'LEFT'

  if change_to == 'UP' and direction != 'DOWN':
    direction ='UP'
  if change_to == 'DOWN' and direction != 'UP':
    direction = 'DOWN'
  if change_to == 'RIGHT' and direction != 'LEFT':
    direction = 'RIGHT'
  if change_to == 'LEFT' and direction != 'RIGHT':
    direction = 'LEFT'

# logica do movimentando 
  if direction == 'UP':
    snake_pos[1] -= 10
  if direction == 'DOWN':
    snake_pos[1] += 10
  if direction == 'LEFT':
    snake_pos[0] -= 10
  if direction == 'RIGHT':
    snake_pos[0] += 10

# corpo da cobrinha 
  snake_body.insert(0, list(snake_pos))
  print(snake_body.pop())

  janela_jogo.fill(black)
  for pos in snake_body:
    pygame.draw.rect(janela_jogo, green, pygame.Rect(pos[0], pos[1], 10, 10))

  # Condicao de game over
  if snake_pos[0] < 0 or posicao_x-10 < snake_pos[0] :
    print('game over')
  if snake_pos[1] < 0 or snake_pos[1] > posicao_y-10:
    print('game over')

  
  pygame.display.update()
  fps_controller.tick(10)
