#CREATE TO DO LIST
my_to_do = ["Go grocery shopping", "buy clothes", "wash shirts"]

print("My To Do List")
for task in my_to_do:
  print(task)

print("What would you like to do?")
add = input()
my_to_do.append(add)

for task in my_to_do:
  print(task)

print("What would you like to remove?")
remove = input()
my_to_do.remove(remove)

for task in my_to_do:
  print(task)

# print("My TO DO List")
# #PRINT OUT HOW MANY ITEMS I HAVE LEFT ON MY TODO LIST
# print(f'{len(my_to_do)} things(s) left to do')
# #FOR LOOP THAT PRINTS OUT EACH ITEM IN MY TODO LIST
# for task in my_to_do:
#   print(task)


# #ADD TO LIST
# print("What task would you like to add?")
# add = input()
# my_to_do.append(add)

# #CODE EXECUTES FROM TOP TO BOTTOM
# #WE NEED TO DUPLICATE THIS PIECE OF CODE TO PRINT OUT OUR LIST AGAIN
# print("My TO DO List")
# print(f'{len(my_to_do)} thing(s) left to do')
# for task in my_to_do:
#   print(task)

# #REMOVE FROM LIST
# print("What task did you complete?")
# complete = input()
# my_to_do.remove(complete)

# #DUPLICATE THIS PIECE OF CODE AGAIN
# print("My TO DO List")
# print(f'{len(my_to_do)} thing(s) left to do')
# for task in my_to_do:
#   print(task)






#################################
#WRITING OUR TO DO AS A FUNCTION
#################################
# #CREATE MY TO DO LIST
# my_to_do = []

# #FUNCTION (BLOCK OF CODE THAT ONLY RUNS WHEN ITS CALLED)
# def toDoList():
#   #defining variable 'action' to accept input from user
#   action = input("What would you like to do?")
#   #if 'action' equals view then...
#   if action == "view":
#     #check if the length of my to do is greater than zero
#     if len(my_to_do) > 0:
#     #if greater than 0, do the following:  
#       print("TO DO")
#       #for each item in my to do list, print
#       for item in my_to_do:
#         print(item)
#       #and call my toDoList() function to repeat from the beginning. 
#       #recursive - function is calling itself
#       toDoList()
#     ##if list is NOT greater than 0
#     else:
#       #print "You are done..."
#       print("You are done with your list!")
#     toDoList()
#   #else, if action is "add"  
#   elif action == "add":
#     newItem = input("What would you like to add to your to do list?")
#     my_to_do.append(newItem)
#     toDoList()
#   #else, if action is "remove"  
#   elif action == "remove":
#     doneItem = input("What have you completed from your to do list?")
#     my_to_do.remove(doneItem)
#     toDoList()
#   else:
#     print("Sorry, that's not an option")
#     toDoList()

# print ("Your To Do List")
# print ("You can 'view', 'add' to, or 'remove' from your to do list.")
# #CALL YOUR TO DO LIST!
# toDoList()