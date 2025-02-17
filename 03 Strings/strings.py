a = 'string' # defined string using single quote
b = "string" # defined string using double quote
c = '''string''' # defined string using tripple sign;e/dbl quote if the string is long
print(a)
print(b)
print(c)

# string is immutable in python - we can not change it once it is defined
name = "Radhika"
print("length of name is", len(name))
name_srt = name[0:5]   # This is string sliceing, syntax: name[index_start:index_end]  it excludes end index (starts from 0 till 4)
print("Short name is:",name_srt)
print("First character is",name[0])

# Negative sliceing 
print("Print short name from the end is",name[-4:-1])

# If start index not given
print("Print start index is not given", name[:5]) # takes 0 as first index (name[0:5])

# If end index is not given
print("Print end index is not given", name[1:]) # takes last index as end index (name[1:6])

# Slicing with skip steps
print("Outpust with skipped steps of 2 is:", name[0:5:2]) # op of [0:5] = Radhi => now skip 2 steps op of [0:5:2] = Rdi

# String functions (String functions are case sensitive)
# 1.) len => gives length of string
print("Length of name is:", len(name))

# 2.) endswith() => gives true,false if ends with given string
print("Name ends with 'ka':", name.endswith('ka'))

# 3.) startswith() => gives true,false if starts with given string
print("Name ends with 'r':", name.startswith('r')) # will give false as it is casesensitive

# 4.) count() => gives occurences of given letter
print("Give occurences of 'a':", name.count('a'))

# 5.) capitalize(), etc... many strings functions available
name = 'radhika'
print("Give capitalized name:", name.capitalize())


# use of Escape sequance characters (\n, \t, \', \")
new_name = "Radhika is a good girl \nbut not\ta bad girl \nand \"she\" is smart\tgirl"
print(new_name)

# Use of fstring => if we want to print variable inside the string
user_name = input("Enter your name ")
print(f"Good morning, {user_name}")






 
