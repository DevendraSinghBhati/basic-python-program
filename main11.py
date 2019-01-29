#file io - reading the content of a file

file1=open('dev.text','r+')
text_to_read=file1.read()
print(text_to_read)