import re
filename = input("enter filename:")
try:
    with open(filename, "r") as file:
        contents = file.read().split()
        words = re.findall(r'\b\w+\b', contents)
        unique_words = sorted(set(words))
        print("Unique words in alphabetical order:")
        for words in unique_words:
            print(words)
except FileNotFoundError:
    print("file not found")