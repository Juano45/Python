print('''
                      {}
                     oIIo
                     oIIo
                      ||
                      ||       I.
                      ||       |:
                     _||_      |:
                   .' || `.    |:
                  /   ||   \   |:
                 |    ::    |  |:
                 )_   ::   _(  |:
                  _)( :: )(_   |:
                 ) ._)::(_. (  |:
                /     II     \ |:
                |  .-.||     | |:
                 \(___)(    /  |:
                  `.__\/__.'   I'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
oneStep = str(input("Left or Right? \n"))
oneStep1 = oneStep.upper()
if oneStep1 == 'LEFT':
  twoStep= input("swim or wait? \n")
  LtwoStep = twoStep.lower()
  print(LtwoStep)
  if LtwoStep == 'wait':
    threeStep = input("Which door? Red, Yellow, Blue \n")
    Color = threeStep.upper()
    if Color == 'RED':
      print("Burned by fire.\n Game Over.")
    elif Color == 'YELLOW':
      print("You Win!")
    elif Color == 'BLUE':
      print("Eaten by beasts. \n Game Over")
    else:
      print("Game Over")
  else:
    print("Attacked by trout\n Game Over.")  
else:
  print("Fall into a hole.\n Game Over.")