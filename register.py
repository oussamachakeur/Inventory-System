
import pickle

def save_data(inventory , filename):
    with open(filename , 'wb') as file:
        pickle.dump(inventory , file)

def load_data(filename ):
    try :
        with open(filename , 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None