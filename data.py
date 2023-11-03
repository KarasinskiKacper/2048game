# from pickle import dump, load
# from os.path import isfile

data = {
    'map': [[None for _ in range(4)] for _ in range(4)],
    'score': 0,
    'highscore': 0,
}

# def force_save_data():
#     with open('./.save', 'wb') as file:
#         dump(data, file)
        
# def save_highscore(new_highscore: int):
#     if isfile('./.save'):
#         saved_data = {}
#         with open('./.save', 'rb') as file:
#             saved_data = load(file)
            
#         saved_data['highscore'] = new_highscore
#         with open('./.save', 'wb') as file:
#             dump(saved_data, file)
            
#     else:
#         with open('./.save', 'wb') as file:
#             dump({'highscore': data['highscore']}, file)
        
# def load_data():
#     if isfile('./.save'):
#         with open('./.save','rb') as file:
#             loaded_data = load(file)
#             for k, v in loaded_data.items():
#                 data[k] = v
    