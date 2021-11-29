from pathlib import Path
import json
from difflib import get_close_matches


data = Path("data.json").read_text()
words_list = json.loads(data)
