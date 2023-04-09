#this allows so that a random number is used in the program
import random
def main():
    money = getInput()
    money = Game(money)
    money = Output(money)
def getInput():
    #this is the amount of money that someone starts out with
    money = 20
    return money
def Game(money):
    answer = 'y'
    print("Welcome to this ridiculous betting game. You have $20. Choose a number between 0-50")
    while answer == 'y' and money > 0:
        money -= 1
        #generates random number for guessing game
        guess = random.randint(1,50)
        #loops five times for guess
        for i in range(5):
            choice = int(input("Make your choice: "))
            while choice < 0 or choice > 50:
                choice = eval(input("Incorrect input. Make your choice: "))
            #if-statements for win condition or displays whether too high or too low
            if choice == guess:
                print("You win!")
                money += 3
                break
            elif choice > guess:
                print("Too high")
            else:
                print("Too low")
        print("Your money = $", money)
        #this inside def Game(money) allows this to work and ask if they want to play again
        def playerChoice():
            #this allows that you can play again 
            answer = input("Would you like to play again? ").lower()

        #this allows that the user is able to choose to play again or not
        playerChoice()
#I was not able to make this part of the program work
#whenever someone does not want to play anymore, it still makes them
def Output(money):
    if money >= 20:
        print("You have won $", money - 20)
    elif money == 20:
        print("You broke even.")
    elif money == 0:
        print("Not enough money.")
    else:
        print("You lost $", 20 - money)
    print("Game is over")
main()