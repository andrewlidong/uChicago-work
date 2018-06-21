import random #in this program to randomly select a position in 4*4 list
khopi_attempt = 0
points = 0
print "----------Game Rules----------\n"
print "the points will be rewarded in a format 'tile number after joining ^ 2' eg>>>> 2 2 8 16 >>>>left movement>>>4 8 16 0 >>>>>points = 4^2"
print "joining two '2' tiles will give 4 points\n"
print "joining two '4' tiles will give 16 points\n"
print "joining two '8' tiles will give 64 points and so on\n"
#----------Game Initialization section begins----------
game_box = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #initially making the 4*4 array's value 0 or "nothing" for all positions
first_position_list = [0,1,2,3] 
first_row_to_begin = random.choice(first_position_list)
first_column_to_begin = random.choice(first_position_list)
game_box[first_row_to_begin][first_column_to_begin] = 2 #placing the first 2 to begin the game in position selected randomly
 
#----------Game Initialization Completes----------
 
#----------Upward movement function begins----------
def up_movement(game_box): #function for up movement 
    i =0
    for j in range(0,4): #looping through all four 4 columns 
        if game_box[i][j]!=0 or game_box[i+1][j]!=0 or game_box[i+2][j]!=0 or game_box[i+3][j]!=0: #condition to check whether any members of a column is non-zero to proceed
            if game_box[i][j]==0: #condition to check if first member of a column is zero
                while game_box[i][j] == 0: #looping until the first member of a column becomes non zero i.e moving lower members to top 
                    game_box[i][j] = game_box[i+1][j]
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0
                     
            if game_box[i+1][j]==0 and (game_box[i+2][j]!=0 or game_box[i+3][j]!=0): #condition to check if the second member of a column is zero and members below it are non-zero
                while game_box[i+1][j]==0: #looping until second member of a column becomes non-zero i.e moving lower member upwards
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0
            if game_box[i+2][j] == 0 and game_box[i+3][j]!=0: #condition to check if the third member of a column is zero and member below it or the last member is non-zero          
                while game_box[i+2]==0: #looping until the third member of a column becomes non-zero
                    game_box[i+2] = game_box[i+3]
                    game_box[i+3][j] = 0
 
#----------Upward movement function ends----------
 
#----------Addition function after upward movement begins----------
def up_addition(game_box): #function for upward addition after upward movement 
    i=0
    global points
    for j in range(0,4): #looping through all the columns 
        if game_box[i][j]==game_box[i+1][j]: #condition to check if the first and second member of a column are equal or same
            game_box[i][j]=game_box[i][j]+game_box[i+1][j] #adding first and second member of a column and storing it as the first member
            points += game_box[i][j] ** 2 #adding point for joining simillar tiles
            game_box[i+1][j]=game_box[i+2][j] #moving third member of a column to second position 
            game_box[i+2][j]=game_box[i+3][j] #moving fourth member of a column to third position 
            game_box[i+3][j]=0 #assigning fourth member of a column as 0 i.e nothing
 
        if game_box[i+1][j]==game_box[i+2][j]: #condition to check if the second and third member of a column are equal or same
            game_box[i+1][j]=game_box[i+1][j]+game_box[i+2][j] #adding second and third member of a column and storing it as second member
            points += game_box[i+1][j] ** 2 #adding points for joining simillar tiles
            game_box[i+2][j]=game_box[i+3][j] #moving fourth member to third position
            game_box[i+3][j]=0 #assigning the fourth member to 0 or nothing
 
        if game_box[i+2][j]==game_box[i+3][j]: #condition to check if the third and fourth member of a column are equal or same
            game_box[i+2][j]=game_box[i+2][j]+game_box[i+3][j] #adding third and fourth member of a column and storing it a third member
            points += game_box[i+2][j] ** 2 #adding points for joining simillar tiles
            game_box[i+3][j]=0 #assigning fourth member to 0 or nothing
     
 
#----------Addition function after upward movement ends----------
                                         
#----------Downward movement function begins----------
 
def down_movement(game_box): #function for down movement
    i=0
    for j in range(0,4): #looping through all the columns
        if game_box[i][j]!=0 or game_box[i+1][j]!=0 or game_box[i+2][j]!=0 or game_box[i+3][j]!=0: #condition to check if any members of a column is non-zero in order to begin
            if game_box[i+3][j]==0: #condition to check if the last member(fourth member) of a column is zero
                while game_box[i+3][j]==0: #looping until the fourth member of a column becomes non-zero i.e moving the upper members to the bottom
                    game_box[i+3][j]=game_box[i+2][j]
                    game_box[i+2][j]=game_box[i+1][j]
                    game_box[i+1][j]=game_box[i][j]
                    game_box[i][j]=0
 
            if game_box[i+2][j]==0 and (game_box[i+1][j]!=0 or game_box[i][j]!=0): #condition to check if the third member of a column is zero and any members above it is non-zero
                while game_box[i+2][j]==0: #looping until the third member of a column becomes non-zero
                    game_box[i+2][j]=game_box[i+1][j]
                    game_box[i+1][j]=game_box[i][j]
                    game_box[i][j]=0
 
            if game_box[i+1][j]==0 and game_box[i][j]!=0: #condition to check if the second member of a column is zero and member above it(first member is non-zero)
                while game_box[i+1][j]==0: #looping until the second member becomes non-zero
                    game_box[i+1][j]=game_box[i][j]
                    game_box[i][j]=0
 
#----------Downward movement function ends----------
                                         
#----------Addition function after downward movement begins----------
 
def down_addition(game_box): #function for downward addition after downward movement
    i=0
    global points
    for j in range(0,4): #looping through all the columns
        if game_box[i+3][j]==game_box[i+2][j]: #condition to check if the fourth member and third member of a column are equal or same
            game_box[i+3][j]=game_box[i+3][j] + game_box[i+2][j] #Adding fourth and third member of a column and storing as the fourth member
            points += game_box[i+3][j] ** 2 #adding points for joining simillar tiles
            game_box[i+2][j]=game_box[i+1][j] #Moving the second member to third position in a column 
            game_box[i+1][j]=game_box[i][j] #Moving the first member to second position in a column
            game_box[i][j]=0 #Assigning the first member of a column to zero
 
        if game_box[i+2][j]==game_box[i+1][j]: #condition to check if the third member and second member of a column are equal or same
            game_box[i+2][j]=game_box[i+2][j]+game_box[i+1][j] #Adding third and second member of a column and storing as the third member
            points += game_box[i+2][j] ** 2 #adding points for joining simillar tiles
            game_box[i+1][j]=game_box[i][j] #Moving the first member to second position in a column
            game_box[i][j]=0 #Assigning zero to the first member of a column 
 
        if game_box[i+1][j]==game_box[i][j]: #condition to check if the seconf and first member of a column are equal or same
            game_box[i+1][j]=game_box[i+1][j]+game_box[i][j] #Adding the second and first member of a column and storing as the second member
            points += game_box[i+1][j] ** 2 #adding points for joining simillar tiles
            game_box[i][j]=0 #Assigning zero to the first member of a column
     
 
#----------Addition function after downward movement ends----------
 
#----------Left movement function begins----------
 
def left_movement(game_box): #function for left movement
    j=0
    for i in range(0,4): #looping through all the rows
 
        if game_box[i][j]!=0 or game_box[i][j+1]!=0 or game_box[i][j+2]!=0 or game_box[i][j+3]!=0: #condition to check if members of a row is non-zero to proceed
            if game_box[i][j]==0: #Condition to check if the first member of a row is zero
                while game_box[i][j]==0: #looping until the first member of a row becomes non-zero
                    game_box[i][j]=game_box[i][j+1]
                    game_box[i][j+1]=game_box[i][j+2]
                    game_box[i][j+2] = game_box[i][j+3]
                    game_box[i][j+3]=0
 
            if game_box[i][j+1]==0 and (game_box[i][j+2]!=0 or game_box[i][j+3]!=0): #condition to check if second member of a row is zero and any members right to it is non-zero
                while game_box[i][j+1]==0: #looping until the second member of a row becomes non-zero
                    game_box[i][j+1]=game_box[i][j+2]
                    game_box[i][j+2]=game_box[i][j+3]
                    game_box[i][j+3]=0
 
            if game_box[i][j+2]==0 and (game_box[i][j+3]!=0): #condition to check if third member of a row is zero and the member right to it(fourth member is non-zero
                while game_box[i][j+2]==0: #looping until the third member of a row becomes non-zero
                    game_box[i][j+2]=game_box[i][j+3]
                    game_box[i][j+3]=0
 
#----------Left movement function ends----------
                                         
#----------Addition function after left movement begins----------
                                         
def left_addition(game_box): #function for left addition after left movement
    j=0
    global points
    for i in range(0,4): #looping through all the rows
        if game_box[i][j]==game_box[i][j+1]: #condition to check if the first member of a row is equal to the second member of a row
            game_box[i][j]=game_box[i][j]+game_box[i][j+1] #Adding the first and second member and storing result as first member of a row
            points += game_box[i][j] ** 2 #adding points for joining simillar tiles
            game_box[i][j+1]=game_box[i][j+2] #Moving the third member of a row to second position 
            game_box[i][j+2]=game_box[i][j+3] #Moving the fourth member of a row to third position 
            game_box[i][j+3]=0 #Assigning 0 to the fourth member of a row
 
        if game_box[i][j+1]==game_box[i][j+2]: #Condition to check if the second member of a row is equal to the third member of that row
            game_box[i][j+1]=game_box[i][j+1]+game_box[i][j+2] #Adding second and third member of a row and storing as second member
            points += game_box[i][j+1] ** 2 #adding points for joining simillar tiles
            game_box[i][j+2]=game_box[i][j+3] #Moving the fourth member of a row to third position 
            game_box[i][j+3]=0 #Assigning zero to the fourth member of a row
 
        if game_box[i][j+2]==game_box[i][j+3]: #Condition to check if the third and fourth member of a row are equal or same
            game_box[i][j+2]=game_box[i][j+2]+game_box[i][j+3] #Adding the third and the fourth member of a row
            points += game_box[i][j+2] ** 2 #adding points for joining simillar tiles
            game_box[i][j+3]=0 #Assigning zero to the fourth member of a row
     
                                         
#----------Addition function after left movement ends----------
                                         
#----------Right movement function begins----------
 
def right_movement(game_box): #function for right movement
    j=0
    for i in range(0,4): #looping through all the rows
        if game_box[i][j]!=0 or game_box[i][j+1]!=0 or game_box[i][j+2]!=0 or game_box[i][j+3]!=0: #condition to check if any members of a row is non zero in order to proceed
            if game_box[i][j+3]==0: #Condition to check if the last(fourth) member of a row is zero
                while game_box[i][j+3]==0: #looping until the last member of a row becomes non-zero
                    game_box[i][j+3]=game_box[i][j+2]
                    game_box[i][j+2]=game_box[i][j+1]
                    game_box[i][j+1]=game_box[i][j]
                    game_box[i][j]=0
 
            if game_box[i][j+2]==0 and (game_box[i][j+1]!=0 or game_box[i][j]!=0): #Condition to check if the third member of a row is zero and any member before it(first and second) is non-zero 
                while game_box[i][j+2]==0: #looping until the third member of a row becomes non-zero
                    game_box[i][j+2]=game_box[i][j+1]
                    game_box[i][j+1]=game_box[i][j]
                    game_box[i][j]=0
 
            if game_box[i][j+1]==0 and game_box[i][j]!=0: #Condition to check if the second member of a row is zero and member before it(first member) is non-zero
                while game_box[i][j+1]==0: #looping until the second member becomes non-zero
                    game_box[i][j+1]=game_box[i][j]
                    game_box[i][j]=0
 
#----------Right movement function ends----------
                                 
#----------Addition function after right movement begins----------
 
def right_addition(game_box): #function for right addition after right movement
    j=0
    global points
    for i in range(0,4): #looping through all the rows
        if game_box[i][j+3]==game_box[i][j+2]: #Condition to check if the fourth and third member of a row are equal
            game_box[i][j+3]=game_box[i][j+3] + game_box[i][j+2] #Adding the fourth and third member of a row and storing it as the fourth member
            points += game_box[i][j+3] ** 2 #adding points for joining simillar tiles
            game_box[i][j+2]=game_box[i][j+1] #Moving the second member of a row to third position
            game_box[i][j+1]=game_box[i][j] #Moving the first member of a row to second position 
            game_box[i][j]=0 #Assigning zero to the first member of a row
 
        if game_box[i][j+2]==game_box[i][j+1]: #Condition to check if the third and second member of a row are equal or same
            game_box[i][j+2]=game_box[i][j+2]+game_box[i][j+1] #Adding the third and second member and storing it as the third member
            points += game_box[i][j+2] ** 2 #adding points for joining simillar tiles
            game_box[i][j+1]=game_box[i][j] #Moving first member of a row to second position
            game_box[i][j]=0 #Assigning zero to the first member of a row
 
        if game_box[i][j+1]==game_box[i][j]: #Condition to check if the second and first member of a row are equal or same
            game_box[i][j+1]=game_box[i][j+1]+game_box[i][j] #Adding second and first member of a row and storing it as second member of that row
            points += game_box[i][j+1] ** 2 #adding points for joining simillar tiles
            game_box[i][j]=0 #Assigning zero to the first member of a row
                                         
#----------Addition function after right movement ends----------
 
while True:
    print "Points>>>>>>"
    print str(points)
    print "\n\n"
    print game_box[0][0],"\t",game_box[0][1],"\t",game_box[0][2],"\t",game_box[0][3],"\n"
    print game_box[1][0],"\t",game_box[1][1],"\t",game_box[1][2],"\t",game_box[1][3],"\n"
    print game_box[2][0],"\t",game_box[2][1],"\t",game_box[2][2],"\t",game_box[2][3],"\n"
    print game_box[3][0],"\t",game_box[3][1],"\t",game_box[3][2],"\t",game_box[3][3],"\n"
    movement_choice = raw_input("Make your move::::>>>>    ") #Taking user input for the movement choice
    if movement_choice == "w":
        up_movement(game_box)
        up_addition(game_box)
    elif movement_choice == "s":
        down_movement(game_box)
        down_addition(game_box)
    elif movement_choice == "a":
        left_movement(game_box)
        left_addition(game_box)
    elif movement_choice == "d":
        right_movement(game_box)
        right_addition(game_box)
    else:
        khopi_attempt += 1
        continue
    row_indexes_with_zero = []
    column_indexes_with_zero = []
    for i in range(0,4):
        for j in range(0,4):
            if game_box[i][j] == 0:
                row_indexes_with_zero.append(i)
                column_indexes_with_zero.append(j)
            if game_box[i][j] == 2048:
                print "Congratulations!! You've successfully sumed up a 2048 tile"
                break
    if len(row_indexes_with_zero) > 1:
        random_index = row_indexes_with_zero.index(random.choice(row_indexes_with_zero))
        row_to_place_entry = row_indexes_with_zero[random_index]
        column_to_place_entry = column_indexes_with_zero[random_index]
        game_box[row_to_place_entry][column_to_place_entry] = 2
    elif len(row_indexes_with_zero) == 1:
        row_to_place_entry = row_indexes_with_zero[0]
        column_to_place_entry = column_indexes_with_zero[0]
        game_box[row_to_place_entry][column_to_place_entry] = 2
    else:
        break
 
print "Congratulations!! You scored ", str(points), "points"
print "\n\n"
print "Total Khopi Attempt >>>>>", str(khopi_attempt)
