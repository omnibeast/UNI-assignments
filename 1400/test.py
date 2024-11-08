#To store the list
roster = []

#Load roster from file
try:
  #open the file
  rosterFile = open('roster.txt', 'r')

  for line in rosterFile:
    roster.append(line.strip())
except FileNotFoundError as err:
  print(err)
  print('Creating file for roster.')
  #Creates empty file
  rosterFile = open("roster.txt", "x")
  print('File created.')

rosterFile.close()

while True:
  print(roster)
  while True:
    try:
        print('1. Add Name\n2. Remove Name \n3. Quit')
        #Make sure 1, 2, or 3 is entered
        choice = int(input())
        break
    except ValueError as errCheck:
        print(errCheck)
        choice = 3

  if choice == 1:
    print('Add Name:')
    toAdd = input()
    roster.append(toAdd)
  elif choice == 2:
    while True:
        print('Remove Name:')
        toRemove = input()
        try:
            roster.remove(toRemove)
            break
        except:
            print('Error removing name')
  else:
    break

#Saves the list to the file
try:
    rosterFile = open('roster.txt', 'w')
    #write to a file
    for n in roster:
        rosterFile.write(n + '\n')
except:
    print('Error writing to file.')

rosterFile.close()