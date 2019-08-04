import turtle
scar = turtle.clone()
turtle.register_shape("hunter.gif")
scar.shape("hunter.gif")
scar.penup()
scar.goto(-400,300)
scar.pendown()









turtle.tracer
turtle.penup()
#makes the turtle move more smoothly.
simba = turtle.clone()
turtle.hideturtle()

turtle.register_shape("simba.gif")
simba.shape("simba.gif")
simba.direction = 'Up'

def up():
    simba.direction = 'Up'
    print('you pressed the up key!')
    move_simba()
turtle.onkeypress(up, 'Up')

def down():
    simba.direction = 'Down'
    print('you pressed the down key!')
    move_simba()
turtle.onkeypress(down, 'Down')

def right():
    simba.direction = 'Right'
    move_simba()
turtle.onkeypress(right,'Right')

def left() :
    simba.direction = 'Left'
    move_simba()
turtle.onkeypress(left,'Left')



turtle.listen()
#that will make simba move using the arrows:
def move_simba():
    my_pos = simba.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

#if you press the up arrow simba will move forward
    if simba.direction == 'Up' :   
        simba.goto(x_pos , y_pos +50)
        print('you moved up')

#if you press the down arrow simba will move down
    elif simba.direction == 'Down':
        simba.goto(x_pos, y_pos - 50)
        print('you moved down')

    elif simba.direction == 'Right':
        simba.goto(x_pos + 50, y_pos)
        print('you moved right')

    elif simba.direction == 'Left' :
        simba.goto(x_pos - 50,y_pos)
        print('you moved left')

simba.speed(0)        
move_simba()
        
























while 1==1:
    scar.goto(my_pos)
scar_pos=scar.pos()
if scar_pos in simba_pos:
    quit()








turtle.mainloop()
