#-----------------------------------------------------------------------------
# Name:        Python Assignment 2 (main.py)
# Purpose:     To show learning on new python topics
#
# Author:      Gaurika Mahajan
# Created:     18-Jan-2021
# Updated:     02-Feb-2021
#-----------------------------------------------------------------------------
'''
3) Loops
 
Used "for" loop as way to answer riddle, instead of using it to go through list (line 228)

6) Functions (with parameters)

Added additional calls of movingCost() function and gasMoney() function (lines 134, 145, 169, 191)

9) Assertions

Added 4 more assertions per function 119, 120, 121, 122, 128, 129, 130, 131
'''

import logging

logging.basicConfig(filename='log.txt',
                    level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

#logging.disable(logging.ERROR)
logging.info("Beginning of Program")


def movingCost(sizeOfHouse, estimateHours):
  '''
    Calculates the cost of moving house

    Calculates the cost of moving your house using Mahajan Movers based on the size of your house and the amount of hours it is estimated to empty house. Calculation is only done if the size is small, medium, or big and hours > 0.

    Parameters
    ----------
    sizeOfHouse : str
        The size of house.
    estimateHours : int
        The estimated amount of hours to empty house.


    Returns
    -------
    float
        The total cost to move house.

    Raises
    ------
    TypeError
        Raised if any of the parameters are incorrect type.
    ValueError
        Raised if hours is negative or if size is not one of the options.
    '''
  logging.info("movingCost() function begins with house size of: " +
               str(sizeOfHouse) + " and estimate of: " + str(estimateHours) +
               " to move house.")
  # Checking if parameters are the correct type
  if not isinstance(sizeOfHouse, str) and not isinstance(estimateHours, int):
    logging.error('One of the parameters is not the correct type.')
    raise TypeError("One of the parameters is not the correct type.")
  # Checking if parameters have valid values.
  if sizeOfHouse != "small" and sizeOfHouse != "medium" and sizeOfHouse != "big" or estimateHours <= 0:
    logging.error('One of the parameters is an invalid value!')
    raise ValueError('One of the parameters is an invalid value!')
  # If both pass check, the total cost is calculated and result is returned.
  else:
    logging.debug(
      'Everything has gone well, will start to calculate moving house.')
    if sizeOfHouse == "small":
      dollarsPerHour = 30.00 * estimateHours
      totalCost = round((dollarsPerHour) * 2 + 10, 3)
      logging.info('Total cost is calculated to be $: ' + str(totalCost))
      return totalCost
    elif sizeOfHouse == "medium":
      dollarsPerHour = 40.00 * estimateHours
      totalCost = round(dollarsPerHour * 3 + 20.00, 3)
      logging.info('Total cost is calculated to be $: ' + str(totalCost))
      return totalCost
    elif sizeOfHouse == "big":
      dollarsPerHour = 50.00 * estimateHours
      totalCost = round(dollarsPerHour * 4 + 30.00, 3)
      logging.info('Total cost is calculated to be $: ' + str(totalCost))
      return totalCost


def gasMoney(distance, costOfGas):
  '''
    Calculates the cost of making trips between the two houses.

    Calculates the cost of making round trips between the two houses based on the distance in kilometers, gas price in dollars per liters, and kilometers per liter for the fuel efficiency to determine the cost. Calculation is only done if both values are positive.

    Parameters
    ----------
    distance : int/float
        The distance between the two houses.
    costOfGas : float
        The current cost of gas in your area. 

    Returns
    -------
    float
        The total cost of gas to move boxes between houses.

    Raises
    ------
    TypeError
        Raised if any of the parameters are incorrect type.
    ValueError
        Raised if distance and cost of gas is negative.
  '''
  logging.info("gasMoney() function begins with distance of " + str(distance) +
               " km between the two houses and gas price of $" +
               str(costOfGas))
  # Checking if parameter (distance and costOfGas) are the correct type
  if not isinstance(distance,
                    (int, float)) or not isinstance(costOfGas, (int, float)):
    logging.error("One of the parameters is not the correct type.")
    raise TypeError("One of the parameters is not the correct type.")
  # Checking if parameter (distance and costOfGas) have a valid value
  if distance <= 0 or costOfGas <= 0:
    logging.error('One of the parameters is an invalid value.')
    raise ValueError('One of the parameters is an invalid value.')
  # If both pass check, gas cost is calculated and result is returned.
  else:
    logging.debug(
      'Everything has gone well, will start to calculate the extra cost of gas.'
    )
    gasCost = round((2 * distance / (40 / 100)) * costOfGas, 2)
    logging.info('Gas money is calculated to be: ' + str(gasCost))
    return gasCost


# Testing movingCost function
assert movingCost("small",
                  4) == 250.0, "small house with 4 hours should cost $250.0"
assert movingCost("medium",
                  6) == 740.0, "medium house with 6 hours should cost $740.0"
assert movingCost("big",
                  20) == 4030.0, "big house with 20 hours should cost $4030.0 "
assert movingCost(
  "medium",
  100) == 12020.0, "medium house with 100 hours should cost $12020.0 "
assert movingCost("small",
                  5) == 310.0, "small house with 5 hours should cost $310.0 "
assert movingCost("big",
                  7) == 1430.0, "big house with 7 hours should cost $1430.0 "
assert movingCost("small",
                  1) == 70.0, "small house with 1 hour should cost $70.0 "

#Testing simpleInterest function
assert gasMoney(
  5, 1.25
) == 31.25, "A distance of 5 kilometers with a gas price of $1.25 should cost $31.25 based on fuel efficiency."
assert gasMoney(
  3, 2
) == 30.00, "A distance of 3 kilometers with a gas price of $2.00 should cost $30.00 based on fuel efficiency."
assert gasMoney(
  7, 1.35
) == 47.25, "A distance of 7 kilometers with a gas price of $1.35 should cost $47.25 based on fuel efficiency."
assert gasMoney(
  2, 1.15
) == 11.50, "A distance of 2 kilometers with a gas price of $1.15 should cost $11.50 based on fuel efficiency."
assert gasMoney(
  4, 1.05
) == 21.00, "A distance of 4 kilometers with a gas price of $1.05 should cost $21.00 based on fuel efficiency."
assert gasMoney(
  8, 0.95
) == 38.00, "A distance of 8 kilometers with a gas price of $0.95 should cost $38.00 based on fuel efficiency."
assert gasMoney(
  3, 1.17
) == 17.55, "A distance of 3 kilometers with a gas price of $1.17 should cost $17.55 based on fuel efficiency."

#Main Code
print("You are moving out and need someone to help move your house. ")
# Trying/excepting the moving cost values.
try:
  logging.debug(
    "Trying out function movingCost() to demonstrate using try/except")
  myMovingCost = movingCost("big", 5)
except ValueError as e:
  print(str(e))
except TypeError as e:
  print(str(e))
else:
  logging.info("Try block was successful, moving cost calculated to be: " +
               str(myMovingCost))
  print("You hear that it cost me $" + str(myMovingCost) +
        " to move my big house in 5 hours.")
# Trying/excepting the gas cost values.
try:
  logging.debug(
    "Trying out function gasMoney() to demonstrate using try/except")
  myGasMoney = gasMoney(5.7, 1.22)
except ValueError as e:
  print(str(e))
except TypeError as e:
  print(str(e))
else:
  logging.info('Try block was successful, gas money calculated to be: ' +
               str(myGasMoney))
  print("It also cost me $" + str(myGasMoney) +
        " for all the trips I had to make between the two houses.")

print("You decide to contact Mahajan Movers for the job. ")
print()
print("They ask for some information before giving you the cost.")
print()
try:
  # Gathering house size and hours from user
  logging.debug('About to gather input from user')
  yourHouseSize = str(
    input(
      "Is the size of your house small medium or big? (type in lowercase) "))
  yourEstimateHours = int(
    input(
      "How long do you expect it will take to empty your house? (round to nearest hour) "
    ))
  logging.info("The user input values of: " + str(yourHouseSize) +
               " as their house size and " + str(yourEstimateHours) +
               " hours ")
  # Calling function with user values
  yourCostToMove = movingCost(yourHouseSize, yourEstimateHours)
  # If ValueError or TypeError gets raised
except ValueError:
  print("One of the inputs could not be converted.")
except TypeError as e:
  print(str(e))
# If try block is successful, print the result.
else:
  logging.info('Try block successful, result was: ' + str(yourCostToMove))
  print("The cost to move your house is $" + str(yourCostToMove) + ".")

print(
  "You also do not have a truck to move your boxes so you have to pay for the cost of gas it will take to move your items between the houses"
)
print()
try:
  # Gathering distance between two houses and cost of gas from user
  logging.debug('About to gather more input from user')
  yourDistanceBetweenHouses = float(
    input("What is the distance between the two houses (in kilometers)? "))
  yourCostOfGas = float(input("What is the cost of gas in your area ($/L)? "))
  logging.info('The user input values of: ' + str(yourDistanceBetweenHouses) +
               " and " + str(yourCostOfGas))
  # Calling function with user values
  yourGasMoney = gasMoney(yourDistanceBetweenHouses, yourCostOfGas)
  # If ValueError or TypeError gets raised
except ValueError:
  print("One of the inputs could not be converted.")
except TypeError as e:
  print(str(e))
# If try block is successful, print the result.
else:
  logging.info('Try block successful, result was: ' + str(yourGasMoney))
  print("Along with the $" + str(yourCostToMove) +
        " to move your house, you will also have to pay $" +
        str(yourGasMoney) +
        " to Mahajan Movers for every trip back and forth.")

print()
print(
  "Now that you know the total cost of moving your house, it is time to make the payment. "
)
print()
print(
  "There is a 10% discount IF you answer a riddle correctly, given two chances. Here is the riddle: "
)

print(
  "I am free, yet priceless. You can't own me, but you can use me. You can't keep me, but you can spend me. Once you have lost me, you can never retrieve me. What am I? You have 4 options: 1 time, 2 money, 3 diamonds, and 4 water"
)
print()
try:
  logging.debug("About to gather answer from user")
  answer = int(input("Enter the number of your answer "))
  logging.info("The user input option " + str(answer) +
               str(" as their answer."))
except ValueError:
  print("Your answer could not be converted. You do not get any discount.")
  # If ValueError or TypeError gets raised
except TypeError as e:
  print(str(e))
  # If try block is successful, continue to for loop.
else:
  logging.info("Try block successful, user's answer was option " +
               str(answer) + " to the riddle")
  for count in range(0, 2):
    if answer == 1:
      print()
      logging.info("For loop was successful, correct answer was option " +
                   str(answer))
      print(
        "Correct! You have earned the 10% discount. Originally you would have to pay $"
        + str(yourCostToMove + yourGasMoney) +
        ", but with the discount you only have to pay $" +
        str(0.9 * (yourCostToMove + yourGasMoney)))
      break
    # User if user enters wrong answer on first try
    else:
      print("Wrong Answer!")
      # User is given one more try
      if count < 1:
        print("Try again")
        print()
        answer = int(input("Enter the number of your answer "))
      # User enters wrong answer on both tries.
      else:
        logging.info(
          "For loop successful, but user did not input correct answer.")
        print(
          "You did not answer correctly, so you had to pay a total of" +
          str(yourCostToMove + yourGasMoney) +
          "t turns out you do not have enough funds to pay for the service and must come back another day. "
        )
