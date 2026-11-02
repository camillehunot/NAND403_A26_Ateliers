import os #permet d'inclure les paths
import ui

print(os.path.curdir) #curdir = current directory
print("^ ^ ^ you are here ^ ^ ^")

print(os.path.realpath(os.path.curdir)) 

absolute_path = os.path.realpath(os.path.curdir)
print(absolute_path)