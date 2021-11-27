import json
from pathlib import Path

movies = [
    {"id": 1, "name": "Titanic", "year": 1997},
    {"id": 2, "name": "Tenet", "year": 2020},
]

data = json.dumps(movies)
# print(type(data))
# print(data)
path = Path("data.json")
path.write_text(data)