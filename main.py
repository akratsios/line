from display import *
from draw import *

screen = new_screen()

x = 0
y = 0

while (x <= 200):
	draw_line(screen,0,y+450,x+300,0,[255,255,255])
	draw_line(screen,0,20-y,10000-x,0,[255,0,255])
	draw_line(screen,0,500-y,3000-x,0,[0,0,255])
	draw_line(screen,0,500-y,100-x,0,[255,200,0])
	x+=7
	y+=4



display(screen)
