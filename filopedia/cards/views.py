from django.shortcuts import render
import json
from cards.data_reader import get_all_data
from cards.constants import DATA_PATH

def index(request):
    arquivos = get_all_data()

    cards = []

    for arquivo in arquivos:
        with open(f"{DATA_PATH}{arquivo}", "r", encoding="utf-8") as f:
           cards.append(json.load(f))

    context = {
            "cards": cards
        }

    return render(request, "index.html", context=context)