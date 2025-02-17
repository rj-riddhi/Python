# 1.) print the Twinkle Twinkle little star poem
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Twinkle, twinkle, little star,
How I wonder what you are!

Then the traveller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.
Twinkle, twinkle, little star,
How I wonder what you are!

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
Till the sun is in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!

As your bright and tiny spark,
Lights the traveller in the dark,—
Though I know not what you are,
Twinkle, twinkle, little star.
Twinkle, twinkle, little star,
How I wonder what you are!
''')


# 2) Use REPL and print the table of 5 
# to open the REPL write python in terminal and hit the enter


# 3) Install an external module and use it to perform your interest 
#  i have used pyttsx3 this package will speal what you have written.
import pyttsx3
engin = pyttsx3.init()
engin.say("Hey there!!! How are you? I am fine. Have a nice day. Thank you")
engin.runAndWait()


# 4) Write a python program to print the content of a directory using  os module. 
import os
# Select the dirctory path
path = '/Applications'
# Use the os  module to list the directory
content = os.listdir(path)
print(content)