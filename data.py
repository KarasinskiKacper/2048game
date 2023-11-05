from pickle import dump, load
from os.path import isfile

data = {
    'map': [[None for _ in range(4)] for _ in range(4)],
    'score': 0,
    'highscore': 0,
}

def force_save_data():
    with open('./game.save', 'wb') as file:
        dump(data, file)

def force_save_custom_data(data_to_save: dict):
    with open('./game.save', 'wb') as file:
        dump(data_to_save, file)
        
def save_highscore(new_highscore: int):
    if isfile('./game.save'):
        saved_data = {}
        with open('./game.save', 'rb') as file:
            saved_data = load(file)
            
        saved_data['highscore'] = new_highscore
        with open('./game.save', 'wb') as file:
            dump(saved_data, file)
            
    else:
        with open('./game.save', 'wb') as file:
            dump({'highscore': data['highscore']}, file)
        
def save_active_game_data():
    data_to_save = {
        'map': data['map'],
        'score': data['score']
    }
    with open('./game.save', 'wb') as file:
        dump(data_to_save, file)        
        
def load_data():
    if isfile('./game.save'):
        with open('./game.save','rb') as file:
            loaded_data = load(file)
            for k, v in loaded_data.items():
                data[k] = v

def print_saved_data():
    if isfile('./game.save'):
        with open('./game.save','rb') as file:
            loaded_data = load(file)
            print(loaded_data)
    else:
        print("File not found.")