fd = open("sample.txt","r")
contents = fd.read()
print(contents)
fd.close()