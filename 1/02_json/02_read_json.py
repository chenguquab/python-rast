import json
from pathlib import Path

data = Path("data.json").read_text()

print(type(data))
print(data)
print()
print(data[2])

movies = json.loads(data)


print(type(movies))
print(movies)
print()
print(movies[0]["year"])