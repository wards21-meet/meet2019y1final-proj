
	

import turtle
import random
from pygame import mixer

turtle.bgpic('rocki.gif')

#Initialize lists
pos_list = []
stamp_list = []

#music
mixer.init()
mixer.music.load('hakouna')
mixer.music.play()

#setup
SIZE_X=1100
SIZE_Y=1100
turtle.setup(SIZE_X, SIZE_Y)
maze = turtle.clone()
turtle.hideturtle()
maze.pensize(25)
maze.speed(300)
turtle.register_shape("bush1.gif")
maze.shape("bush1.gif")


#function that creates stamps
def new_stamp():
    maze_pos = maze.pos()
    pos_list.append(maze_pos) 
    maze_stamp = maze.stamp()
    stamp_list.append(maze_stamp)

#function that moves the maze to a certain point while creating a stamps on the way  
def move(x,y):
    while maze.xcor() != x:
        if maze.xcor()<x:
            maze.goto((maze.xcor())+50,maze.ycor())
            new_stamp()
        elif maze.xcor()>x:
            maze.goto((maze.xcor())-50,maze.ycor())
            new_stamp()
    while maze.ycor() != y:
        if maze.ycor()<y:
            maze.goto((maze.xcor()),maze.ycor()+50)
            new_stamp()
        elif maze.ycor()>y:
            maze.goto((maze.xcor()),maze.ycor()-50)
            new_stamp()

#function that draws the maze using the 'move' function
def drawmaze():
    maze.penup()
    maze.goto(-500,100)
    maze.pendown()
    move(-500,500)
    move(100,500)
    move(100,300)
    maze.penup()
    maze.goto(100,150)
    maze.pendown()
    move(100,150)
    move(-100,150)
    move(-100,300)
    maze.penup()
    maze.goto(100,500)
    maze.pendown()
    move(500,500)
    move(500,300)
    move(300,300)
    move(500,300)
    move(500,0)
    move(300,0)
    move(500,0)
    move(500,-500)
    move(300,-500)
    move(300,-250)
    move(200,-250)
    move(200,-300)
    move(200,300)
    maze.penup()
    maze.goto(300,-500)
    maze.pendown()
    move(100,-500)
    maze.penup()
    maze.goto(100,-400)
    maze.pendown()
    move(100,0)
    move(-50,0)
    maze.penup()
    maze.goto(-200,0)
    maze.pendown()
    move(-200,-200)
    move(-100,-200)
    move(-100,-300)
    move(100,-300)
    move(100,-400)
    maze.penup()
    maze.goto(100,-500)
    maze.pendown()
    move(-200,-500)
    move(-200,-300)
    move(-300,-300)
    move(-300,-100)
    maze.penup()
    maze.goto(200,-500)
    maze.pendown()
    move(-500,-500)
    move(-500,100)
    move(-300,100)
    move(-300,300)
    move(-400,300)

drawmaze() #calling the function

turtle.tracer(1,0) #makes the turtle move more smoothly.

#creating simba
simba = turtle.Turtle()
turtle.hideturtle()
simba.penup()
simba.goto(450,-450)
turtle.register_shape("simba2.gif")
simba.shape("simba2.gif")
simba.direction = 'Up'
score=0

#creating scar
scar = turtle.Turtle()
turtle.hideturtle()
scar.penup()
turtle.register_shape("hunter1.gif")
scar.shape("hunter1.gif")


#function that moves simba with the arrows while checking if touching the walls or scar
def move_simba():
    my_pos = simba.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    #touching walls?
    if simba.pos() in pos_list:
        global score
        score=score-1
        turtle.undo()
        turtle.penup()
        turtle.color('red')
        turtle.hideturtle()
        turtle.goto(-470,450)
        turtle.write('score : ' + (str(score)),False, align = "left", font = ("ariel",20,'normal'))
        simba.goto(450,-450)
    
    #moving up
    elif simba.direction == 'Up' :
        simba.goto(x_pos , y_pos +50)

    #moving down
    elif simba.direction == 'Down':
    	simba.goto(x_pos, y_pos - 50)

    #moving right
    elif simba.direction == 'Right':
    	simba.goto(x_pos + 50, y_pos)

    #moving left
    elif simba.direction == 'Left' :
    	simba.goto(x_pos - 50,y_pos)

    #touching food?
    if simba.pos() in food_pos:
        food_index=food_pos.index(simba.pos())
        food.clearstamp(food_stamps[food_index])
        food_pos.pop(food_index)
        food_stamps.pop(food_index)
        turtle.undo()
        score+=1
        turtle.penup()
        turtle.color('lime')
        turtle.hideturtle()
        turtle.goto(-470,450)
        turtle.write('score : ' + (str(score)),False, align = "left", font = ("ariel",20,'normal'))

    #making food        
    if len(food_stamps) <= 1:
    	make_food()

    #touching scar?
    if simba.xcor() > scar.xcor()-100 and simba.xcor() < scar.xcor()+100 and simba.ycor() > scar.ycor()-100 and simba.ycor() < scar.ycor()+100 :
        turtle.penup()
        turtle.goto(0,0)
        turtle.write('game over. your score is: ' + (str(score)),False, align = "center", font = ("ariel",50,'bold'))
        quit()
        

#functions to move simba
def up():
	simba.direction = 'Up'
	move_simba()
turtle.onkeypress(up, 'Up')

def down():
	simba.direction = 'Down'
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

#creating food
food = turtle.Turtle()
turtle.hideturtle()
food.penup()
turtle.register_shape('chicken1.gif')
food.shape('chicken1.gif')

#food lists
food_stamps = []
food_pos = []

#creating food stamps
for this_food_pos in food_pos :
	food.goto(this_food_pos)
	food_stamp = food.stamp()
	food_stamps.append(food_stamp)

#function that is making the food
def make_food():
    min_x=-int(1000/2/50)+1
    max_x=int(1000/2/50)-1
    min_y=-int(1000/2/50)+1
    max_y=int(1000/2/50)-1

    food_x = random.randint(min_x,max_x)*50
    food_y = random.randint(min_y,max_y)*50
    food_xy = (food_x,food_y)
    if food_xy not in pos_list:
        food.goto(food_x,food_y)
        food_pos.append(food.pos())
        food_stamps.append(food.stamp())

#function that is moving scar randomly
def move_scar():
    
    scar.penup()
    
    random_pos=((random.randint(-10,10)*50),(random.randint(-10,10)*50))
    
    if scar.xcor() != random_pos[0]:
        if scar.xcor()<random_pos[0]:
            scar.goto((scar.xcor())+50,scar.ycor())
        elif scar.xcor()>random_pos[1]:
            scar.goto((scar.xcor())-50,scar.ycor())
    if scar.ycor() != random_pos[1]:
        if scar.ycor()<random_pos[1]:
            scar.goto((scar.xcor()),scar.ycor()+50)
        elif scar.ycor()>random_pos[1]:
            scar.goto((scar.xcor()),scar.ycor()-50)
    turtle.ontimer(move_scar,100)       

simba.speed(-2)    

#calling the functions and starting the game
move_scar()
move_simba()

turtle.mainloop()
