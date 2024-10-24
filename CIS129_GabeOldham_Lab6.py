# Module 6 Lab-6
# Gabe Oldham
# 10/23/2024
# This code asks the user for the total number of people
# at the cookout and then calculates the number of hotdogs
# and hot dog buns needed then prints the results

import math


def main():
    # Declare the local variables
    total = 0
    neededDogs = 0
    DOGS = 10 #Hotdogs in a package
    BUNS = 8 #Buns in a package
    dogsLeft = 0
    bunsLeft = 0
    minDogs = 0
    minBuns = 0


    total = getTotalHotDogs()

    #Calculoate the number of left over hot dogs.
    dogsLeft = (DOGS - total % DOGS) % DOGS

    #Calculate the minimum number of packages of hot dogs.
    minDogs = math.ceil(total / DOGS)

    #Calculate the number of left over hot dog buns.
    bunsLeft = (BUNS - total % BUNS) % BUNS

    #Calculate the minimum number of packages of hot dog buns.
    minBuns = math.ceil(total / BUNS)

    #Output -------------------------------------------
    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

# Get the total number of hotdogs needed
def getTotalHotDogs():
    people = 0
    hotDogs = 0

    prompt = "\nHow many people will be attending the cookout?: "
    people = int(input(prompt))

    prompt = "Enter the number of hot dogs for each person: "
    hotDogs = int(input(prompt))

    total = people * hotDogs
    return total

# Print the results
def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    print(f"\nMinimum packages of hot dogs needed: {minDogs}")
    print(f"Minimum packages of hotdog buns needed: {minBuns}")
    print(f"Hot dogs left over: {dogsLeft}")
    print(f"Hot dog buns left over: {bunsLeft}\n")


main()
