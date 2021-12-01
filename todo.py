#CREATE TO DO LIST
my_to_do = ["Go grocery shopping","Make dinner","Do the dishes"]

#PRINT OUT STRING 'MY TODO LIST'
print('My TODO List')
#PRINT OUT HOW MANY ITEMS I HAVE LEFT ON MY TODO LIST
print(f'{len(my_to_do)} thing(s) left to do')
#FOR LOOP THAT PRINTS OUT EACH ITEM IN MY TODO LIST
for task in my_to_do:
  print(task)

# #ADD TO LIST
# print('What task would you like to add?')
# add = input()
# my_to_do.append(add)

# #CODE EXECUTES FROM TOP TO BOTTOM
# #WE NEED TO DUPLICATE THIS PIECE OF CODE TO PRINT OUT OUR LIST AGAIN
# print('My TODO List')
# print(f'{len(my_to_do)} thing(s) left to do')
# for task in my_to_do:
#   print(task)

# #REMOVE FROM LIST
# print('What task did you complete?')
# complete = input()
# my_to_do.remove(complete)

# #DUPLICATE THIS PIECE OF CODE AGAIN
# print('My TODO List')
# print(f'{len(my_to_do)} thing(s) left to do')
# for task in my_to_do:
#   print(task)