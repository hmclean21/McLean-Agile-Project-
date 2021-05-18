#!/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Bunker Quest
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see ' + str(rooms[currentRoom]['item']))
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

itemvales = {
"water": 3,
"screw_driver": 1,
"canned_food": 3,
"bandage": 2, 
"first_aid_kit": 6,
"kitchen_knife": 7,
"hammer": 6,
"snack" : 1,
"soda" : 1,
"gas_can": 4,
"lighter": 2,
"gas_mask": 8,
"hand_gun": 8,
"batterys": 1,
}

def bunker():
  sum=0

  for item in inventory:
    value = itemvales[item]

    print("ITEM is: ", end="")
    print(item) # print the item
    print("value is: ", end="")
    print(value) # get value of current item
    sum=sum+value 
  print(sum)


#a dictionary linking a room to other rooms
rooms = {

            'Backyard' : { 
                  'south' : 'Kitchen',
                  'north' : 'Living room'
                },

            'Kitchen' : {
                  'south' : 'Dining room',
                  'east' :'Daughters room',
                  'item' : ['canned_food',
                  'water','kitchen_knife']
                  
            
                },

            'Living room' : {
                  'north' : 'Bathroom',
                  'west' : 'Sons room',
                  'item' : ['snack','batterys']
                },

             'Bathroom' : {
                  'north' : 'Garage',
                  'item' : ['bandage','first_aid_kit']
                },  

            'Sons room' : {
                  'south' : 'Up stairs bathroom',
                  'east' : 'Master bedroom',
                  'item' : ['screw_driver','snack','water']
                },  

            'Dining room' : {
                  'east' : 'Up stairs bathroom',
                  'south' : 'Master bedroom',
                  'item' : ['canned food','soda','water']
                }, 

            'Daughters room' : {
                  'north' : 'Up stairs bathroom',
                  'west' : 'Master bedroom',
                  'item' : ['lighter','snack','bandage']
                },   

            'Up stairs bathroom' : {
                  'north' : 'Attic',
                  'item' : ['first_aid_kit','bandage','water']
                }, 

            'Attic' : {
                  'south' : 'Bunker',
                  'item' : ['gas_mask']
                }, 

            'Garage' : {
                  'south' : 'Bunker',
                  'item' : ['hammer','lighter','gas_can','screw_driver'] 
            },
            
            'Master bedroom' : {
                  'south' : 'Bunker',
                  'item' : ['hand_gun','batterys','snack']
            },
               
            'Bunker' : {
                  
            },                                                
}
#start the player in the backyard
currentRoom = 'Backyard'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go': 
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
      if currentRoom=='Bunker':
        bunker()
    #there is no door (link) to the new room
    #add if statment, is room locked?
    #check if room is valid.
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    item=move[1]
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      rooms[currentRoom]['item'].remove (item)
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

