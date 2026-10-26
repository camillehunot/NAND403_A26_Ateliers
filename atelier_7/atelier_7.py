import maya.cmds as cmds 
import sys
item_selected = cmds.ls(selection=True)
horse = item_selected
def clean_key():
    cmds.cutKey(horse, clear=True) 

def add_key():
    objet = horse
    for i in range(3):
        cmds.setKeyframe(objet, attribute="translateZ", value = 10+ (10*i), time=(0 + (33*i)))
        
clean_key()
add_key()
