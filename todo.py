myTodo = ["Go grocery shopping","Make dinner","Do the dishes"]

print('My TODO List')

print(f'{len(myTodo)} thing(s) left to do')

for task in myTodo:
  print(task)

print('What task would you like to add?')

add = input()

myTodo.append(add)

print('My TODO List')

print(f'{len(myTodo)} thing(s) left to do')

for task in myTodo:
  print(task)

print('What task did you complete?')

complete = input()

myTodo.remove(complete)

print('My TODO List')

print(f'{len(myTodo)} thing(s) left to do')

for task in myTodo:
  print(task)