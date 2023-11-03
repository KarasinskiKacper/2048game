import threading

from app import app
from model import model
from data import load_data

if __name__ == "__main__":
    load_data()
    
    t1 = threading.Thread(target=model)
    t2 = threading.Thread(target=app)
    t1.start()
    t2.start()
    t1.join()
    t2.join()