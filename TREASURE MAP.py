
row1 = ["🅾", "🅾", "🅾"]
row2 = ["🅾", "🅾", "🅾"]
row3 = ["🅾", "🅾", "🅾"]


map = [row1, row2, row3] # this line of code is use to nest list of variable row1, row2 and row3
print (f"{row1}\n{row2}\n{row3}") #this line of code print out the variable using the F-string

#we ask for the users input
#whereby the we have two value 
position = input ("where do you want to put the tresure?\n")

# we convert it to an integer and then assigned it to a variable
#the horizontal var gets hold of the first value which starts from index 0
#the vertical var gets hold of the second value which start from index 1
horizontal = int(position[0])
vertical = int(position[1])

#this line of code assign the value of x to the bigger picture before the smaller picture
#[  [1,[small],3]   [4,[small],6]   [7,[small],9]  ]
# bigger picture means  == [1,[small], 3] overall of it
#small picture means == [small]
# Row is the Bigger Picture while Column is the Small Picture
# (n-1) is to firstly prevent an error and secondly to get the exact value of the input
# knowing that that the computer counts from zero
map [vertical - 1][horizontal-1] = "✖" #this help to assign the value of X

print (f"{row1}\n{row2}\n{row3}")

