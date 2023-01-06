#-----------------------------------------------------------------------------
# Name:        New File Generator (main.py)
# Purpose:     To show understanding of python concepts that I have learned
#
# Author:      
# Created:     10-Dec-2020
# Updated:     18-Dec-2020
#-----------------------------------------------------------------------------
# function that converts military time to standard time for user
def militaryTimeToStandardTime(timeOnClock):
  if timeOnClock < 0 or timeOnClock > 24:
    return 'invalid'
  else: 
     if timeOnClock <= 12.59:
      timeOnClock = timeOnClock
      standardTime = round (timeOnClock,3)
      return standardTime
     else:
      timeOnClock = timeOnClock-12
      standardTime = round (timeOnClock,3)
      return standardTime
#function that tracks time trapped in cell 
def trackingTimeTrapped (hours, minutes):
  if hours < 0 or minutes <0:
    return ("Either the hour or the minute is negative, please re enter the time")
  #this is for when
  else:
    if hours < 8:
      hourTimeDifference = 8 - hours
      hoursSpentInCell = 24 - hourTimeDifference
      minutesSpentInCell = minutes - 25
      return hoursSpentInCell, minutesSpentInCell
  #this is for when the user has been in the cell for less than an hour
    elif minutes < 25 and hours == 9:
      minutesSpentInCell = 25 - minutes
      hoursSpentInCell = 0
      return hoursSpentInCell, minutesSpentInCell
  #this is for when the minute part of the time that the user inputs is less than 25
    elif minutes < 25:
      minuteTimeDifference = 25 - minutes
      minutesSpentInCell = 60 - minuteTimeDifference
      hoursSpentInCell = hours - 8
      return hoursSpentInCell, minutesSpentInCell
  #this is for when the the user hour and minute components are greater than 8 and 25
    else:
      hoursSpentInCell = hours - 8
      minutesSpentInCell = minutes - 25
      return hoursSpentInCell, minutesSpentInCell

#number part of code
numberCode = [1, 2, 4, 5, 8, 9, 10 ]
#letter part of code 
letterCode = ['C', 'D', 'F','G', 'J', 'K', 'L']
print("Imagine you’re walking to school on a bright sunny day.")
print( 

)
print("Nothing could go wrong right? WRONG. You start to see several black SUVs speeding on the road as if they are chasing someone. You have two choices, to either stand and watch the car chase or to continue walking to school")
print( 

)
optionChosen = input('Do you choose to "stand and watch" or "continue walking"? ')
print(

)
#situations for user inputs 
while optionChosen != "continue walking" and optionChosen != "stand and watch":
  print("Invalid option chosen, please re enter your action")
  optionChosen = input('Do you choose to "stand and watch" or "continue walking"? ')
else:
  if optionChosen == "stand and watch":
    print("You continue watching and see the cars drive off into the distance and have to hurry up and run to school")
  elif optionChosen == "continue walking":
    print("You continue to walk towards school and forget about the incident")

print("As you're a minute away from school, you notice that there is a black SUV following YOU. What could you have done? After a few minutes it catches up to you until the driver rolls down their windshield telling you they are from the FBI")
print( 

)
print("Wait what? In Canada? And that you need to be interrogated as you were a witness to the crime (and what crime?)")
print( 

)
goWithTheFBI = input("Do you choose to go with the FBI? ")
#situation for the option user chooses about FBI
while goWithTheFBI != "yes" and goWithTheFBI != "no":
  print("Invalid option chosen, please re enter your answer")
  goWithTheFBI = input("Do you choose to go with the FBI? ")
else: 
  if goWithTheFBI == "yes":
   print("You choose to go with them anyway because they’re the government")
  elif goWithTheFBI == "no":
    print("You politely decline and continue walking to school, but are then kidnapped.")
print( 

)
print ("After a few minutes, you see that you’re out of the city and you only see warehouses and lots of plain fields.")
print( 

)
print ("You ask where you’re going but only hear some talking in a foreign language and you realize you’re not with the FBI.")
print(

)
print ("You also find a small code sticking out of the drivers pocket. Before the car stops moving, you can see that the number 1 is equal to the letter C and number 2 is equal to D. ")
print("Here's what it looks like: ")

#prints the code using the two lists from before
for i in range(0, len(numberCode)):
    print(str(numberCode[i]) + " = " + letterCode[i])
print(

)
print("Soon you arrive at your destination before you can remember the entire code. You’re now stuck in some jail cell.")
print(

)
print("You also see a digital clock in the jail cell but why are the times more than 12:00? You then realize that today was the day that you had to learn about military time at school.")
print(
  
)
print("What a coincidence. But you can input the time you see on the clock and your time converter will convert it to normal time for you.")
print(

)
print("When entering the time, enter it as a decimal. (ex. if the clock shows 1632, enter it as 16.32.)")
#user inputs the time they want to convert
myTime = float(input('What is the time you see on the clock? '))
print(

)
#military time to standard time function is called
standardTime = militaryTimeToStandardTime(myTime)
if myTime <= 11.59:
  print("The time is " + str(standardTime) + " AM") 
elif 12 <= myTime <= 24:
  print("The time is " +str(standardTime) + " PM")
else: 
  print("The time is " + str(standardTime) + ". Re enter the time on the clock.")
  myTime = float(input('What is the time you see on the clock? '))
  standardTime = militaryTimeToStandardTime(myTime)
print(

)
print("You are also able to count the hours you are stuck in your jail cell since the time of your kidnapping was 8:25 AM.")

#creating variables to track the amount of hours user is kidnapped
userHours = float(input("What is the hour part of the time? (in military time) "))
userMinutes = float(input("What is the minute part of the time? (in military time) "))

hoursSpentInCell, minutesSpentInCell = trackingTimeTrapped(userHours, userMinutes)
print ("You have spent " + str(hoursSpentInCell) + " hours and " + str(minutesSpentInCell) + " minutes in the jail cell.")
print(

)
print("Someone comes into your cell to give you food but on their way out they drop the code list from before (how clumsy of them)")
print(
  
)
print("This list is incomplete but you can see that each letter is three letters after its corresponding number.")
print(
  
)
print("There are three missing numbers, so you decide to complete the list. ")

print("Here it is.")
#printing the code chart
for i in range(0, len(numberCode)):
    print(str(numberCode[i]) + " = " + letterCode[i])

print("Remember that when you are adding letters to the list, the letters should be capitalized")
#Lines 175-191 are for the user adding in the three missing values
firstNewNumber = int(input('Please input the first missing number you want to add: '))
numberCode.append(firstNewNumber)

firstNewAlpha = input('Please input the first letter that is missing: ')
letterCode.append(firstNewAlpha)

secondNewNumber = int(input('Please input the second missing number you want to add: '))
numberCode.append(secondNewNumber)

secondNewAlpha = input('Please input the second letter that is missing: ')
letterCode.append(secondNewAlpha)

thirdNewNumber = int(input('Please input the third missing number you want to add: '))
numberCode.append(thirdNewNumber)

thirdNewAlpha = input('Please input the third letter that is missing: ')
letterCode.append(thirdNewAlpha)
#the code is now sorted chronologically and alphabetically
numberCode.sort()
letterCode.sort()
#allows user to see the code with their added values
print("Here is your new list with your added values")
print(

)
#printing the code with the users added values 
for i in range(0, len(numberCode)):
    print(str(numberCode[i]) + " = " + letterCode[i])
#if the user made any mistakes, they are given chances to fix them
mistake = input("Are there any mistakes in this list? ")

while mistake ==  "yes":
  mistakeNumber = int(input("What is the number you want to delete? "))
  numberCode.remove (mistakeNumber)

  mistakeLetter = (input("What is the letter you want to delete? " ))
  letterCode.remove (mistakeLetter)

  for i in range(0, len(numberCode)):
      print(str(numberCode[i]) + " = " + letterCode[i])
  #if user deletes value from list, they must replace it as well
  newNumberAfterDeleting = int(input("What is the number you want to add to your list into the list? "))
  newLetterAfterDeleting = (input("What is the letter you want to add to your list? "))
  numberCode.append (newNumberAfterDeleting)
  letterCode.append (newLetterAfterDeleting)

  numberCode.sort()
  letterCode.sort()
  for i in range(0, len(numberCode)):
      print(str(numberCode[i]) + " = " + letterCode[i])

  mistake = input("Did you make any mistakes while adding in values to your list? ")
#these are the other situations for if the user did not make a mistake
else:
  if mistake == "no":
    print("You may continue on with your escape")
  else:
    print ("invalid answer")
    mistake = input("Did you make any mistakes while adding in values to your list? ")
print(

)
print("Now that you have completed the code list, you start looking around for clues. You see that there is a number written on the jail cell. It says '473 10 2' You also see that there is a keypad made of letters.")

print("Using your code chart, you can decode this number to come up with letters that can be entered into the keypad")
#the user now has to input the correct letters in order to escape
escapeCode = input("What are the letters to escape? (type in CAPS) ")
while escapeCode != "FIELD" and escapeCode != "field":
  print("Wrong. Those letters were incorrect and you must try again to escape")
  escapeCode = input("What are the letters to escape? ")
else:
  print("Correct! You are able to leave your jail cell!")
print(

)
print("You run towards the door but you see that this time there is riddle you have to answer and type in that answer ")
print(

)
print("The riddle is: What building has the most stories? ")
answerForRiddle = input("What is your answer to the riddle? ")
#the while loop is for when the user inputs the wrong answer
while answerForRiddle != "library" and answerForRiddle != "the library" and answerForRiddle != "a library" :
  print("Wrong answer.")
  #the user is given the chance to ask for a hint
  hintOption = input("Would you like a hint? ")
  if hintOption == "yes": 
    print("You can go here to borrow books or dvds.")
    answerForRiddle = input("What is your answer to the riddle? ")
  else: 
    answerForRiddle = input("What is your answer to the riddle? ")
#this else loop is for when the correct answer is inputted
else:
 print("Correct! You were able to open the door and can see a window that shows the outside world! You are close to escaping. ")

print(

)
print("At the next door, there’s another keypad with letters but there's no numbers around this time. But on the top of the door you do see the word 'TIME.'")
print(

)
print("Somehow you think that maybe once you convert the military time to standard time and then convert that time to letters using the code chart, you will be able to get through the door.")
print(

)
#the military time to standard time function is called
print("The time on the clock shows it to be 16:32.")
escapeTime = float(input("Enter that time into your time converter. (using a decimal in place of the colon"))

standardTime = militaryTimeToStandardTime(escapeTime)

print("This time is now " + str(standardTime) + " PM")
print("You now have to convert the time into letters")

#the user can request to see the list again
userRequestForList = input("Do you need to see the list? ")
if userRequestForList == "yes":
  for i in range(0, len(numberCode)):
      print(str(numberCode[i]) + " = " + letterCode[i])
elif userRequestForList == "no":
  answerForTimeCode = input("What are the letters to escape ")
else:
  print ("Invalid answer")
  userRequestForList = input("Do you need to see the list? ")
  
#after the users choice to see or not see the list, they have to enter the correct code in order to escape
userTimeCode = input("What is this time converted into letters? (without using decimals) ")
if userTimeCode == "FED" or userTimeCode == "fed":
  print("Correct! That was the last door to escape!")
else:
  print ("Not quite. Try again")
  userTimeCode = input("What is this time converted into letters? ")

print("You bolt outside after passing through the door somehow outrunning all the security agents in the building. You also were able to steal your phone back")
print(

)
print("Since you have your phone, you called the real cops, who came and arrested the people who kidnapped you")
print(

)
print("They were the Russian mafia, but anyways congrats on escaping and winning the game. Tune back in for the second version!")



