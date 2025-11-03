import random

red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
even = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36)
odd = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35)
zero = 0

#gets the players bet
def bet_type():
    print("Thank you for choosing to play Roulette.")
    while True:
        try:
            type_of_bet = input('Enter type of bet ("color" or "number"): ')
            if type_of_bet == "color" or type_of_bet == "number":
                break
            else:
                print("Please choose on color or number.")
        except ValueError:
            print('Invalid input. Please enter "color" or "number" only')
            
    return type_of_bet

#gets the players bet amount
def bet_money(type_of_bet, balance):
    if type_of_bet == "color":
        while True:
            try:
                color_bet = input("Enter your bet (black or red): ")
                number_bet = "0"
                even_odd = "N/A"
                even_odd_bet = "N/A"
                if color_bet == "black" or color_bet == "red":
                    break
                else:
                    print("Please enter black or red")
            except ValueError:
                print("Please enter black or red.")
    elif type_of_bet == "number":
        while True:
            try: 
                even_odd = input("Are you betting on even/odd or a specific number? Type even/odd or number: ")        
                if even_odd == "even/odd":
                    even_odd_bet = input('Enter "even" or "odd": ')
                    number_bet = "0"
                    color_bet = "N/A"
                    if even_odd_bet == "even" or even_odd_bet == "odd":
                        break
                    else:
                        print("Please type even or odd: ")
                elif even_odd == "number":
                    number_bet = int(input("Enter your bet (0-36): "))
                    even_odd_bet= "N/A"
                    color_bet = "N/A"
                    if 0 <= number_bet <= 36:
                        break
                    else:
                        number_bet = int(input("Try again. Enter a number (0-36): "))
                else:
                    number_bet = int(input("Please enter even/odd or number: "))
            except ValueError:
                print('Please enter "even/odd" or "number" only')



    while True:
        try:
            bet_amount = int(input("Enter the amount you are betting: $"))
            if bet_amount <=0:
                print("Bet must be more than 0. Please enter your bet amount: ")
            if bet_amount > balance:
                print("Bet amount cannot exceed balance. Enter your bet amount again.")
            else:
                break
        except ValueError:
            print("Please enter numbers only.")
    
        
    return bet_amount, color_bet, number_bet, even_odd, even_odd_bet

#spinning the wheel to get outcome
def wheel():
    print("Wheel is now being spun.")
    winning_number = random.randint(0,36)
    print(f"The winning number is: {winning_number}")
    if winning_number in red:
        winning_color = "red"
        print("The winning color is red.")
    if winning_number in black:
        winning_color = "black"
        print("The winning color is black.")

    return winning_number, winning_color

#outcome of the game
def outcome(winning_number, winning_color, type_of_bet, bet_amount, color_bet, number_bet, even_odd_bet):
    if winning_color == color_bet:
        print("Congratulations! You won!")
    elif winning_number == number_bet:
        print("Congratulations! You won!")
    elif winning_number in even:
        if even_odd_bet == "even":
            print("Congratulations! You won!")
        else:
            print("Sorry, you have unfortunately lost.")
    elif winning_number in odd:
        if even_odd_bet == "odd":
            print("Congratulations! You won!")
        else:
            print("Sorry, you have unfortunately lost.")
    else:
        print("Sorry, you have unfortunately lost.")

#calculates the player's payout
def payouts(type_of_bet, bet_amount, color_bet, number_bet, even_odd, even_odd_bet,winning_number, winning_color, balance):
    print("\n Playor Payout")
    print("-"*40)
    print(f' Bet Amount: ${bet_amount:,.2f}')
    print(f' Type of bet: {type_of_bet}')
    if type_of_bet == "color":
        print(f' Your bet: {color_bet}')
    elif type_of_bet == "number":
        if even_odd == "Y":
            print(f' Your bet: {even_odd_bet}')
        elif even_odd == "N":
            print(f' Your bet: {number_bet}')
    else:
        print("Error. You didn't place a bet.")
        
    if winning_color == color_bet:
        payout = ((bet_amount * 2) - ((bet_amount * 2)*.02))
        print(f' Your Payout: ${payout:,.2f}')
        remaining_balance = balance + payout
        print(f' Your remaining balance: ${remaining_balance:,.2f}')
    elif winning_number == number_bet:
        payout = ((bet_amount * 35) - ((bet_amount * 35)*.02))
        print(f' Your Payout: ${payout:,.2f}')
        remaining_balance = balance + payout
        print(f' Your remaining balance: ${remaining_balance:,.2f}')
    elif winning_number in even:
        if even_odd_bet == "even":
            payout = ((bet_amount * 2) - ((bet_amount * 2)*.02))
            print(f' Your Payout: ${payout:,.2f}')
            remaining_balance = balance + payout
            print(f' Your remaining balance: ${remaining_balance:,.2f}')
        else:
            payout = 0
            print(f' Your Payout: ${payout:,.2f}')
            remaining_balance = balance - bet_amount
            print(f' Your remaining balance: ${remaining_balance:,.2f}')
    elif winning_number in odd:
        if even_odd_bet == "odd":
            payout = ((bet_amount * 2) - ((bet_amount * 2)*.02))
            print(f' Your Payout: ${payout:,.2f}')
            remaining_balance = balance + payout
            print(f' Your remaining balance: ${remaining_balance:,.2f}')
        else:
            payout = 0
            print(f' Your Payout: ${payout:,.2f}')
            remaining_balance = balance - bet_amount
            print(f' Your remaining balance: ${remaining_balance:,.2f}')

    return payout, remaining_balance

#calculates the casinos house edge
def house_edge(payout, type_of_bet, bet_amount, color_bet, number_bet, even_odd, even_odd_bet, winning_number, winning_color):
    if winning_color == color_bet:
        profit = ((bet_amount * 2)*.02)
        print(f' Casino House Edge: ${profit:,.2f}')
    elif winning_number == number_bet:
        profit = ((bet_amount * 35)*.02)
        print(f' Casino House Edge: ${profit:,.2f}')
    elif winning_number in even:
        if even_odd_bet == "even":
            profit = ((bet_amount * 2)*.02)
            print(f' Casino House Edge: ${profit:,.2f}')
        else:
            print(f' Casino House Edge: ${bet_amount:,.2f}')
            profit = (bet_amount * 1)
    elif winning_number in odd:
        if even_odd_bet == "odd":
            profit = ((bet_amount * 2)*.02)
            print(f' Casino House Edge: ${profit:,.2f}')
        else:
            print(f' Casino House Edge: ${bet_amount:,.2f}')
            profit = (bet_amount * 1)
        
    return profit

#asks the player if they want to repeat
def play_again():
    balance = 1000
    print(f'Balance: ${balance:,.2f}')
    type_of_bet = bet_type()
    bet_amount, color_bet, number_bet, even_odd, even_odd_bet = bet_money(type_of_bet,balance)
    winning_number, winning_color = wheel()
    outcome(winning_number, winning_color, type_of_bet, bet_amount, color_bet, number_bet, even_odd_bet)
    payout, remaining_balance = payouts(type_of_bet, bet_amount, color_bet, number_bet, even_odd, even_odd_bet,winning_number, winning_color, balance)
    profit = house_edge(payout, type_of_bet, bet_amount, color_bet, number_bet, even_odd, even_odd_bet,winning_number, winning_color)
    print( )
    while True:
        repeat = input("Would you like to play again? Enter Y/N: ")
        if repeat == "Y":
            balance = remaining_balance
            print(f'Balance: ${balance:,.2f}')
            type_of_bet = bet_type()
            bet_amount, color_bet, number_bet, even_odd, even_odd_bet = bet_money(type_of_bet, balance)
            winning_number, winning_color = wheel()
            outcome(winning_number, winning_color, type_of_bet, bet_amount, color_bet, number_bet, even_odd_bet)
            payout, remaining_balance = payouts(type_of_bet, bet_amount, color_bet, number_bet, even_odd, even_odd_bet,winning_number, winning_color, balance)
            profit = house_edge(payout, type_of_bet, bet_amount, color_bet, number_bet, even_odd, even_odd_bet,winning_number, winning_color)
        else:
            print("Thank you for playing!")
            break
        
    return balance

def main():
    type_of_bet = bet_type()
    bet_amount, color_bet, number_bet, even_odd, even_odd_bet = bet_money(type_of_bet)
    winning_number, winning_color = wheel()
    outcome(winning_number, winning_color, type_of_bet, bet_amount, color_bet, number_bet, even_odd_bet)
    payout, remaining_balance = payouts(type_of_bet, bet_amount, color_bet, number_bet, even_odd, even_odd_bet,winning_number, winning_color)
    profit = house_edge(payout, type_of_bet, bet_amount, color_bet, number_bet, even_odd, even_odd_bet,winning_number, winning_color)
    balance = play_again()



balance = play_again()
     
    
