# Module 7 Lab-7
# Gabe Oldham
# 10/29/2024
# This code 


# Define position in section arrays
SECTION_NAME = 0
PRICE = 1
NUMBER_OF_SEATS = 2

# Main code function
def main():

    A = [
        "A", # Section name
        20,  # Price
        300  # Number of seats
    ]
    
    B = [
        "B", # Section name   
        15,  # Price  
        500  # Number of seats 
    ]
    
    C = [
        "C", # Section name
        10,  # Price 
        200  # Number of seats 
    ]
    
    # Declare the local arrays
    sections = [A, B, C]


    # Print welcome message
    printWelcome(sections)
    print("")

    tickets = []
    income = []
    totalIncome = 0
    for section in sections:
        tickets.append(getTickets(section))
        income.append(getIncome(section[PRICE], tickets[-1]))
        totalIncome = totalIncome + income[-1]
        print(f"Subtotal: ${totalIncome:,}\n")
    
    
    printTotals(totalIncome, sections, income, tickets)

# Print welcome message and state prices
def printWelcome(sections):
    print("\nWelcome to the Dramatic Theater")
    print("\nSeat prices are as follows:")
    for section in sections:
        print(f"Section {section[SECTION_NAME]}: {section[NUMBER_OF_SEATS]} seats @ ${section[PRICE]}")


# Obtain number of tickets in a, b, and c then vaildate the number   
def getTickets(section):

    tickets = section[NUMBER_OF_SEATS] + 1
    while tickets > section[NUMBER_OF_SEATS]:
        prompt = f"How many tickets were sold in section {section[SECTION_NAME]}?: "
        userInput = input(prompt)

        if userInput.isdigit():
            tickets = int(userInput)
            if tickets > section[NUMBER_OF_SEATS]:
                print(f"Number of seats cannot exceed {section[NUMBER_OF_SEATS]}")
        else:
            print("Invalid input. Please enter a number:")
    return tickets


# Calculate the total income
def getIncome(price, tickets):
    return price * tickets


# Print the amount of total income as well as income per seat location
def printTotals(totalIncome, sections, income, tickets):
    print("\nSections:")
    print("--------------------------------------------")
    i = 0
    numSections = len(sections)
    while (i < numSections): 
        section = sections[i]
        name = section[SECTION_NAME]
        price = section[PRICE]
        subtotal = income[i]
        seats = tickets[i]
        print(f"[{name}] Seats: {seats} @ ${price:,} = ${subtotal:,}")
        i = i + 1
    
    print("-------------------------------------------- ")
    print(f"Total: ${totalIncome:,}\n")

main()
