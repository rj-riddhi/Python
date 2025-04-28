f = open('file.txt')
data = f.read()
print(data)
f.close()

f = open('myfile.txt','w')
f.write("This is another sample file.")
f.close()