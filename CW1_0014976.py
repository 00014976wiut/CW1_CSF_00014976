#CW1_00014976_CSF
#Hungry Shark



#This module is for showing the game on screen
from tkinter import *#  "*"help us to return this module without writing one mmore time
import time
import random

Game_Running = True

#Game and snake apperiance
game_width = 700
game_height = 700
snake_item = 10
snake_color1 = "black"
snake_color2 = "green"

virtual_game_x = game_width//snake_item
virtual_game_y = game_height//snake_item

snake_x=virtual_game_x//2
snake_y=virtual_game_y//2
snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 5

tk = Tk()
tk.title("Hungry Snake")
tk.resizable(0,0)

#This one will help to app be on top of all other screns
tk.wm_attributes("-topmost",1)

#This is the interface of the game
canvas = Canvas(tk, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

present_color1 = "white"
present_color2 = "black"
presents_list = []
presents_size = 55
for i in range(presents_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x*snake_item,y*snake_item, x*snake_item+snake_item,y*snake_item+snake_item,fill=present_color2)
    id2 = canvas.create_oval(x*snake_item+2,y*snake_item+2,x*snake_item+snake_item-2,y*snake_item+snake_item-2,fill=present_color1)    
    presents_list.append([x, y, id1, id2])
print(presents_list)
