import threading

from app import app
from model import model

if __name__ == "__main__":
    t1 = threading.Thread(target=model)
    t2 = threading.Thread(target=app)
    t1.start()
    t2.start()
    t1.join()
    t2.join()