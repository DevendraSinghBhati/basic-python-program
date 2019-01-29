#file io
file1 = open("dev.text","wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("Write this to my file","UTF-8"))
file1.close()