source = input("enter source file name :")
destination = input("enter destination file name :")
with open(source, "r") as f1:
    data = f1.read()
with open(destination, "w") as f2:
    f2.write(data)
print("contents copied from", source, "to", destination)