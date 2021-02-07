import re

with open('agenda.txt', 'r') as file:
    agenda = file.read()

with open('todos.txt', 'r') as file:
    todos = file.read()

print(agenda)
print(todos)

agenda = re.sub(' +', ' ', agenda)
agenda = re.sub(r'\.\.+', '\n ', agenda).replace('.', '')
agenda = agenda.replace('Monday', 'Monday     ').replace('Tuesday', 'Tuesday    ').replace('Wednesday', 'Wednesday  ').replace('Thursday', 'Thursday   ').replace('Friday', 'Friday     ').replace('Saturday','Saturday   ').replace('Sunday', 'Sunday     ')
todos = re.sub(' +', ' ', todos)
todos = todos.replace('c_gtd: ', '')
agenda = agenda.replace('c_gtd: ', '')

print(agenda)
print(todos)

with open('agenda.txt', 'w') as file:
    file.write(agenda)

with open('todos.txt', 'w') as file:
    file.write(todos)
