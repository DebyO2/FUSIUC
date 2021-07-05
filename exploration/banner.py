import os
import time
  

WIDTH = 250
  
message = "FUSIUC".upper()
  
#The message will get printed here.
printedMessage = [ "","","","","","","" ]
  
characters = { " " : [ "|",
                       "|",
                       "|",
                       "|",
                       "|",
                       "|",
                       "|" ],
  
               "U" : [ "*   * ",
                       "*   * ",
                       "*   * ",
                       "*   * ",
                       "*   * ",
                       "*   * ",
                       "***** " ],
  
               "I" : [ "***** ",
                       "  *   ",
                       "  *   ",
                       "  *   ",
                       "  *   ",
                       "  *   ",
                       "***** " ],
                 
               "C" : [ "   **** ",
                       "  *    ",
                       " *   ",
                       " *   ",
                       " *   ",
                       "  *    ",
                       "   **** " ],
                 
               "S" : ["  **** ",
                       " *     ",
                       " *     ",
                       "  ***  ",
                       "     * ",
                       "     * ",
                       " ****  " ],
  
                 
  
               "F" : ["***** ",
                       "*     ",
                       "*     ",
                       "****  ",
                       "*     ",
                       "*     ",
                       "*     " ],
    
               }
  
  
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")
  
offset = WIDTH
while True:
    os.system("cls")
  
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
  
    offset -=1
  
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
  
    #Use this to change the speed of the animation that you wish to keep.
    time.sleep(0.05)