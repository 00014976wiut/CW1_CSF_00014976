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
