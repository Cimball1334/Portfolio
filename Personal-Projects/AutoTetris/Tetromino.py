import pygame 
import random
'''
Tetris Piece class
handles the peice implementation and rotation backend
'''

peice_colors = [
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

class Tetromino:

    def __init__(self,shape) -> None:
        if shape == 'I':
            self.shape = [
                [1,1,1,1]
                ]
        elif shape == 'O':
            self.shape = [
                [1,1],
                [1,1]
            ]
        elif shape == 'L':
            self.shape = [
                [1,1,1],
                [1,0,0]
            ]
        elif shape == 'J':
            self.shape = [
                [1,0,0],
                [1,1,1]
            ]
        elif shape == 'T':
            self.shape = [
                [1,1,1],
                [0,1,0]
            ]
        elif shape == 'S':
            self.shape = [
                [0,1,1],
                [1,1,0]
            ]
        elif shape == 'Z':
            self.shape = [
                [1,1,0],
                [0,1,1]
            ]

        self.color = peice_colors[random.randint(0,5)]

    def width(self) -> int:
        return len(self.shape[0])
    
    def height(self) -> int:
        return len(self.shape)
    
    def rotate(self) -> None:
        #CCW Rotation - I Think this is normal rotation for tetris classic
        self.shape = [[self.shape[j][i] for j in range(len(self.shape))] for i in range(len(self.shape[0])-1,-1,-1)]
        


'''
Game manager class
'''
class Game:

    def __init__(self,width,height) -> None:
        self.height = height
        self.width = width
        self.active_peice = None
        self.x , self.y = 10 , 10

        self.next_x , self.next_y = 300,100
        self.feild = [[0 for x in range(height)] for x in range(width)]
        pass

    def new_peice(self) -> None:
        possible = ['I','O','L','S','Z','J','T']
        self.active_peice = Tetromino(possible[random.randint(0,6)])
        self.active_x , self.active_y = 90 , 10

        self.next_peice = Tetromino(possible[random.randint(0,6)])

    def intersect(self) -> bool:
        location = self.feild
        

        return False

    def move_left(self) -> None:
        self.active_x -= 20

    def move_right(self) -> None:
        self.active_x += 20

    def freeze():
        #add active to field
        #save next piece and generate new
        pass

    def tick(self) -> None:
        self.active_y += 20
        if self.intersect():
            self.active_y -= 20
            self.freeze()
    

    

        




pygame.init()

screen_size = (450,500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tetris")

game = Game(20,10)
game.new_peice()

# print(game.feild)

game_run = True
clock = pygame.time.Clock()
count = 0
fps = 24
while game_run:

    if count % (fps//2) == 0:
        game.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
                
            if event.key == pygame.K_RIGHT:
                game.move_right()
                
            if event.key == pygame.K_UP:
                game.active_peice.rotate()
                
            if event.key == pygame.K_DOWN:
                #drop
                pass


    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    screen.fill(WHITE)
    
    

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY,[i*20+game.x,j*20+game.y,20,20],1)

    
    # pygame.draw.rect(screen,game.active_peice.color,[game.active_x,game.active_y,20,20])

    for s in range(0,len(game.next_peice.shape[0])):
        for h in range(0,len(game.next_peice.shape)):
            if game.next_peice.shape[h][s] == 1:
                pygame.draw.rect(screen,game.next_peice.color,[game.next_x+s*20,game.next_y+h*20,20,20])

    for s in range(0,len(game.active_peice.shape[0])):
        for h in range(0,len(game.active_peice.shape)):
            if game.active_peice.shape[h][s] == 1:
                pygame.draw.rect(screen,game.active_peice.color,[game.active_x+s*20,game.active_y+h*20,20,20])


    pygame.display.update()
    clock.tick(fps)
    count+=1