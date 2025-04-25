#  Write a program to find the greatest number out of fout numbers enterd by user
print("Program 1 start........")
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
d = int(input("Enter number: "))

if a > b and a > c and a > d :
    print("Greatest number is: ", a)
elif b > a and b > c and b > c :
    print("Greatest number is: ", b)
elif c > a and c > b and c > d : 
    print("Greatest number is: ", c)
else : 
    print("Greatest number is: ", d)
print("Program 1 end........")

# Write a program to find student is pass or not, it requires total 40% to pass and each subsject should have at lease 33% to pass
print("Program 2 start........")
marks1 = int(input("Enter subject1 marks: "))
marks2 = int(input("Enter subject2 marks: "))
marks3 = int(input("Enter subject3 marks: "))

total_per = (100*(marks1 + marks2 + marks3)) / 300

if(total_per > 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are passed with percentage:",total_per)
else:
    print("You are failed, try next year:",total_per)
print("Program 2 end........")

# Write a program to detect spam comment if comments containing below mentioned keyword
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
print("Program 3 start........")
message = input("Enter comment: ")
if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This is spam comment")
print("Program 3 end........")

# Write a program to find given keyword is present in list or not
print("Program 4 start....")
list = ["Hello", "fruites"]
keyword = input("Enter keyword: ")
if keyword in list :
    print("List contains entered keyword")
else :
    print(f"{keyword} not in the list")
print("Program 4 end....")



