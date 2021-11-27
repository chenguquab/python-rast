from pathlib import Path

# current_path = Path()
# #print(current_path.absolute())

# commerce_path = Path() / Path("commerce")
# print(commerce_path)

ecommerce_path = Path("ecommerce/main.py")
print(ecommerce_path.exists())
print(ecommerce_path.is_dir())
print(ecommerce_path.name)
print(ecommerce_path.stem)
print(ecommerce_path.suffix)
print(ecommerce_path.parent)