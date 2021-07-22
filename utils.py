# coding=UTF-8
import json


def load_json(path):
    with open(path, 'r', encoding='UTF-8') as f:
        content = json.load(f)

    return content