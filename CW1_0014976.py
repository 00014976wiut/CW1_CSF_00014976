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

#Creating Snake
def snake_paint_item(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x*snake_item,y*snake_item, x*snake_item+snake_item,y*snake_item+snake_item,fill=snake_color2)
    id2 = canvas.create_rectangle(x*snake_item+2,y*snake_item+2,x*snake_item+snake_item-2,y*snake_item+snake_item-2,fill=snake_color1)
    snake_list.append([x,y,id1,id2])
    #print(snake_list)

snake_paint_item(canvas, snake_x, snake_y)



def check_can_we_delete_snake_item():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        #print(temp_item)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])

def check_if_we_found_present():
    global snake_size
    for i in range(len(presents_list)):
        if presents_list[i][0] == snake_x and presents_list[i][1] == snake_y:
            #print("found!!!")
            snake_size = snake_size + 1
            canvas.delete(presents_list[i][2])
            canvas.delete(presents_list[i][3])
    #print(snake_x, snake_y)

    #The movement of the snake
def snake_move(event):
    global snake_x
    global snake_y
    global snake_x_nav
    global snake_y_nav


 #In this code is one of main part of app. If the snake touc hitsel or border of the screen, the app will check for it. Plus while moving the snake its tail will remove by the way fullfilling the view of movement.   
    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
        check_can_we_delete_snake_item()
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
        check_can_we_delete_snake_item()
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    check_if_we_found_present()

canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)

def game_over():
    global Game_Running
    Game_Running = False

def check_if_borders():
    if snake_x>virtual_game_x or snake_x<0 or snake_y>virtual_game_y or snake_y<0:
        game_over()

def check_we_touch_self(f_x, f_y):
    global Game_Running
    if not (snake_x_nav == 0 and snake_y_nav == 0):
        for i in range(len(snake_list)):
            if snake_list[i][0] == f_x and snake_list[i][1] == f_y:
                print("found!!!")
                Game_Running = False
