# Two types of loops
# 1) for loop
# 2) while loop

# for loop
print("For loop")
for i in range(1, 6):
    print(i)

# while loop
print("while loop")
i = 1
while (i < 6):
    print(i)
    i += 1

# for loop with else
print("for with else")
l = [1,7,8]
for item in l:
    print(item)
else:
    print("done!")  #this is printed when for loop exhusted.

# break
# 'break' used to come out the loop it exists the loop right now
print("break keyword")
for i in range(100):
    if i == 35:
        break  # exit the loop right now
    print(i)


# continue
# 'continue' used to skip that iteration and start with next iteration
print("continue keyword")
for i in range(6):
    if i == 2:
        continue  # skip this iteration
    print(i)

# pass
# it is null statement in python
# instructs to "do nothing"
print("pass keyword")
for i in range(10):
    pass
i = 0
while(i < 2):
    print(i)
    i += 1