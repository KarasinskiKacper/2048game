from random import randrange, choice
from pynput import keyboard

from data import *

# TODO <remove>
from icecream import ic
# TODO </remove>

        
class Game():
    def __init__(self, mapSize: int = 4) -> None:
        self.mapSize = mapSize
        self.map = [[None for _ in range(mapSize)] for _ in range(mapSize)]
        self.score = 0
        self.spawnTile()
        game_data['map'] = self.map
        game_data['score'] = self.score
    
    def spawnTile(self) -> None:
        empty_space = [(i%self.mapSize, int(i//self.mapSize)) for i in range(self.mapSize**2) if self.map[i%self.mapSize][int(i//self.mapSize)] == None]
        x, y = choice(empty_space)
        self.map[x][y] = 2 if randrange(100)<90 else 4
        
    def keyboardHandler(self, player_choise):
        key = keyboard.Key
        key_code = keyboard.KeyCode        
        is_change = False
        
        if isinstance(player_choise, key):
        # move handle
            match player_choise:
                case key.left:
                    for x in range(self.mapSize):
                        for y in range(self.mapSize):
                            tile_value = self.map[x][y]
                            if tile_value != None:
                                new_x = x 
                                while new_x > 0 and (self.map[new_x-1][y] == None or self.map[new_x-1][y] == tile_value):
                                    new_x -= 1
                                if new_x != x:
                                    is_change = True
                                    self.map[x][y] = None
                                    if self.map[new_x][y] == tile_value:
                                        self.map[new_x][y] = tile_value*2
                                        self.score += tile_value*2
                                    else:
                                        self.map[new_x][y] = tile_value
                                    
                case key.right:
                    for x in range(self.mapSize-1, -1, -1):
                        for y in range(self.mapSize-1, -1, -1):
                            tile_value = self.map[x][y]
                            if tile_value != None:
                                new_x = x 
                                while new_x < self.mapSize-1 and (self.map[new_x+1][y] == None or self.map[new_x+1][y] == tile_value):
                                    new_x += 1
                                if new_x != x:
                                    is_change = True
                                    self.map[x][y] = None
                                    if self.map[new_x][y] == tile_value:
                                        self.map[new_x][y] = tile_value*2
                                        self.score += tile_value*2
                                    else:
                                        self.map[new_x][y] = tile_value
                                        
                case key.up:
                    for x in range(self.mapSize):
                        for y in range(self.mapSize):
                            tile_value = self.map[x][y]
                            if tile_value != None:
                                new_y = y 
                                while new_y > 0 and (self.map[x][new_y-1] == None or self.map[x][new_y-1] == tile_value):
                                    new_y -= 1
                                if new_y != y:
                                    is_change = True
                                    self.map[x][y] = None
                                    if self.map[x][new_y] == tile_value:
                                        self.map[x][new_y] = tile_value*2
                                        self.score += tile_value*2
                                    else:
                                        self.map[x][new_y] = tile_value
                                        
                case key.down:
                    for x in range(self.mapSize-1, -1, -1):
                        for y in range(self.mapSize-1, -1, -1):
                            tile_value = self.map[x][y]
                            if tile_value != None:
                                new_y = y 
                                while new_y < self.mapSize-1 and (self.map[x][new_y+1] == None or self.map[x][new_y+1] == tile_value):
                                    new_y += 1
                                if new_y != y:
                                    is_change = True
                                    self.map[x][y] = None
                                    if self.map[x][new_y] == tile_value:
                                        self.map[x][new_y] = tile_value*2
                                        self.score += tile_value*2
                                    else:
                                        self.map[x][new_y] = tile_value
                                        
        else:
            # can't be match, because for some reason "keyboard.KeyCode.from_char(<char>)" cause: 
            # TypeError: called match pattern must be a type
            if player_choise == key_code.from_char('r'): 
                self.resetGame()
            elif player_choise == key_code.from_char('s'):
                save_active_game_data()
            elif player_choise == key_code.from_char('l'):
                load_data()
                self.map = game_data['map'] 
                self.score = game_data['score']
                self.displayMap()
                 
        if is_change:
            self.spawnTile()
            self.displayMap()
            self.checkGameEnd()
            
    def endGame(self) -> None:
        if game_data['score'] > game_data['highscore']:
            save_highscore(game_data['score'])
            
    def resetGame(self) -> None:
        self.endGame()
        self.map = [[None for _ in range(self.mapSize)] for _ in range(self.mapSize)]
        self.score = 0
        self.spawnTile()
        self.displayMap()
        
    def checkGameEnd(self) -> None:
        is_move_possible = False
        for x in range(self.mapSize):
            for y in range(self.mapSize):
                if self.map[x][y] == None:
                    is_move_possible = True
                    break
                else:
                    if x < self.mapSize-1 and self.map[x][y] == self.map[x+1][y]:
                        is_move_possible = True
                        break
                    elif y < self.mapSize-1 and self.map[x][y] == self.map[x][y+1]:
                        is_move_possible = True
                        break
            if is_move_possible:
                break
        if not is_move_possible:
            keyboard.Controller().tap(keyboard.Key.esc)
     
    def displayMap(self, is_console_need_refresh: bool = True) -> None:
        game_data['map'] = self.map
        if is_console_need_refresh:
            LINE_UP  = '\033[1A'
            for _ in range(self.mapSize*2-1):
                print(LINE_UP, end='')
            print('\r', end='')

        res = f"score: {game_data['score']}\n"
        for i in range(self.mapSize):
            for j in range(self.mapSize):
                if self.map[j][i] == None:
                    res += "   0 "
                else:
                    res += f"{self.map[j][i]:>4} "
            res += "\n\n"
        print(res[:-2], end='')
        
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, newValue):
        game_data['score'] = newValue
        self.__score = newValue
    

def model():
    game = Game()
    game.displayMap(False)
    with keyboard.Events() as events:
        while app_data['is_game_running']:
            event = events.get()
            if type(event) == keyboard.Events.Press:
                game.keyboardHandler(event.key)
                
            if event.key == keyboard.Key.esc:
                app_data['is_game_running'] = False
                game.endGame()