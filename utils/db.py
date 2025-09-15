import os

def init_data_dir():
    if not os.path.exists("data"):
        os.makedirs("data")
