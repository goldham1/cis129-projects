# Module 7 Assignment-7
# Gabe Oldham
# 10/30/2024
# 


# Step 4: Add libraries needed
import random

# Step 3: Main function``
def main():
    print()

    # Step 5: Initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'
    player1Score = 0
    player2Score = 0

    # Step 6: Call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # Step 7: While loop to run the program again
    while endProgram.lower() == 'no':
        
        # Step 7: Initialize values for each round
        winnerName = 'NO NAME'
        p1number = 0
        p2number = 0

        # Step 8: Call to rollDice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)

        # Update the running score
        if playerOne == winnerName:
            player1Score = player1Score + 1
        elif playerTwo == winnerName:
            player2Score = player2Score + 1

        # Step 9: Call to displayInfo
        displayInfo(winnerName)

        # Print the running score
        printScore(playerOne, playerTwo, player1Score, player2Score)

        # End loop check
        endProgram = input('Do you want to end program? (yes/No): ')

        if endProgram == "":
            endProgram = "no"

        

# Step 10: This function gets the players' names
def inputNames(playerOne, playerTwo):
    playerOne = input("Enter the name of Player 1: ")
    playerTwo = input("Enter the name of Player 2: ")
    return playerOne, playerTwo

# Step 11: This function will get random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    # Display the number that was rolled for each player
    print(f"\n{playerOne} rolled: {p1number}")
    print(f"{playerTwo} rolled: {p2number}")


    # Step 12: Determine the winner
    if p1number > p2number:
        winnerName = playerOne
    elif p2number > p1number:
        winnerName = playerTwo
    else:
        winnerName = "TIE"
    
    # Step 13: Return winnerName
    return winnerName

# Step 14: This function displays the winner
def displayInfo(winnerName):
    print("The winner is:", winnerName)

# Keep running score until player hits 10 wins
def printScore(playerOne, playerTwo, player1Score, player2Score):

    
    print(f"\nThe score is:")
    print(f"{playerOne} with {player1Score} points")
    print(f"{playerTwo} with {player2Score} points")



    

# Call main to start the program
main()
