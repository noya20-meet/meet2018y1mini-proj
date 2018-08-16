import turtle
import random

turtle.tracer(1,0) 

SIZE_X=900
SIZE_Y=900
turtle.setup(SIZE_X, SIZE_Y)  
border = turtle.clone()
border.hideturtle()
border.penup()
border.goto(400,400)
border.pendown()
border.goto(400,-400)
border.goto(-400,-400)
border.goto(-400,400)
border.goto(400,400)
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 1

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("circle")
snake.color("yellow")
snake.pencolor("pink")

turtle.register_shape("trash.gif") 
food = turtle.clone()
food.shape("trash.gif") 
food.ht()


#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
for number in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE 

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    IASA_FOOD = snake.stamp()
    stamp_list.append(IASA_FOOD)
    ###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
LEFT = 1
RIGHT = 2
DOWN = 3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 400
DOWN_EDGE = -400
RIGHT_EDGE = 400
LEFT_EDGE = -400



def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    
    print("You pressed the up key!")

def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    
    print("You pressed the left key!")

def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    
    print("You pressed the right key!")

def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    
    print("You pressed the down key!")



 




#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, "Up") # Create listener for up key
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()


def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(800/2/SQUARE_SIZE)+3
    max_x=int(800/2/SQUARE_SIZE)-3
    min_y=-int(800/2/SQUARE_SIZE)+3
    max_y=int(800/2/SQUARE_SIZE)-3
    print(min_x,max_x,min_y,max_y)
    
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    print(food_x,food_y)
    foodPos = (food_x, food_y)
    food.goto(foodPos)
    food_pos.append(foodPos)
    stamp_ID = food.stamp()
    food_stamps.append(stamp_ID)

make_food()

 

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==DOWN:
         snake.goto(x_pos, y_pos- SQUARE_SIZE)
         print("You moved down!")
    elif direction==UP:
        snake.goto(x_pos, y_pos+ SQUARE_SIZE)
        print("You moved up!")

    if snake.pos() in pos_list:
        quit()

    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        print(food_ind)
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        make_food()

    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    
    #HINT: This if statement may be useful for Part 8

   
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()
   


    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()

    elif new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()

    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        quit()
        



    
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()





    








    




     
