import turtle
import random



#Initialize lists
pos_list = []
stamp_list = []
food_stamps = []
food_pos = []

turtle.bgpic('rocki.gif')
SIZE_X=1100
SIZE_Y=1100
turtle.setup(SIZE_X, SIZE_Y)
maze = turtle.clone()


turtle.hideturtle()
maze.pensize(25)
maze.speed(300)


def new_stamp():
    maze_pos = maze.pos()
    pos_list.append(maze_pos)
    maze_stamp = maze.stamp()
    stamp_list.append(maze_stamp)
   
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

drawmaze()
turtle.showturtle()
food = turtle.clone()
turtle.register_shape('chicken.gif')
food.shape('chicken.gif')

turtle.hideturtle()
food.penup()

turtle.showturtle()


food_stamps=[]
food_pos=[]



for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)

food.hideturtle()

#this one
def make_food():
    min_x=-int(1000/2/50)+1
    max_x=int(1000/2/50)-1
    min_y=-int(1000/2/50)+1
    max_y=int(1000/2/50)-1

    food_x = random.randint(min_x,max_x)*50
    food_y = random.randint(min_y,max_y)*50
    food_xy=(food_x,food_y)
    if food_xy not in pos_list:           
        food.goto(food_x,food_y)
        food_pos.append(food.pos())
        food_stamps.append(food.stamp())
    print('i added one food')




scar = turtle.clone()
turtle.register_shape("hunter.gif")
scar.shape("hunter.gif")





turtle.tracer()

turtle.penup()
#makes the turtle move more smoothly.
simba = turtle.clone()


turtle.register_shape("simba2.gif")
simba.shape("simba2.gif")
turtle.hideturtle()
simba.goto(400,-350)
simba.direction = 'Up'


score=0

#that will make simba move using the arrows:
def move_simba():
    #global food_stamps
    my_pos = simba.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if simba.pos() in pos_list:
        print("you touched the wall")
        simba.goto(450,-450)
#if you press the up arrow simba will move forward
    elif simba.direction == 'Up' :   
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


    global score

       
    if simba.pos() in food_pos:
        food_index=food_pos.index(simba.pos())
        food.clearstamp(food_stamps[food_index])
        food_pos.pop(food_index)
        food_stamps.pop(food_index)
        print("You have eaten the food!")
        score=score+1
        turtle.undo()
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(-398,200)
        turtle.pendown()
        turtle.write(score, False,align="left", font=("arial",20,"normal"))


        
#this one
    if len(food_stamps) <= 1:
        make_food()
    
    
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


simba.speed(-2)
        

        

my_pos=simba.pos()
scar_pos=scar.pos()

x_pos1=scar.pos()[0]
y_Pos1=scar.pos()[1]

while 1==1:
    scar.penup()
    scar.speed(5)
    scar.goto((random.randint(-500,500)),(random.randint(-500,500)))















print(pos_List)
move_simba()

turtle.mainloop()

