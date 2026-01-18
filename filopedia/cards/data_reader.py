from cards.constants import DATA_PATH
from pathlib import Path

def get_all_data():
    data_directory = Path(DATA_PATH)
    arquivos = [arquivo.name for arquivo in data_directory.iterdir() if "404" not in arquivo.name]

    return arquivos