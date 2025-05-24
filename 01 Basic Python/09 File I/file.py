f = open('file.txt')
data = f.read()
print(data)
f.close()

f = open('myfile.txt','w')
f.write("This is another sample file.")
f.close()

f = open("myfile.txt")
print(f.readline())
f.close()

f = open("file.txt", 'rt')
print(f.readline(2))
f.close()

f = open("myfile.txt")
print(f.readlines())
f.close()