
 

# 1.2 Using ipdb (Improved pdb) 
# ipdb provides better debugging with syntax highlighting and tab completion. 
# ipdb works similarly to pdb, but with a better user experience! 

# Installation 
# pip install ipdb 


import ipdb 

def multiply(x, y): 
    ipdb.set_trace()
    result = x * y 
    return result 

print(multiply(5, 3)) 



 