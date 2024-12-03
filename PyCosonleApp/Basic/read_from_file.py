import io

with io.open("file_data", "r", encoding="utf-8") as f1:
    data = f1.read()
    f1.close()
print(data)