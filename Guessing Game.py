import random
def play_game():
    lucky_number = random.randint(1, 50)

    while True:
        user_number = int(input("Guess the lucky number: "))

        if user_number == lucky_number:
            print("You Won. Game Over!")
            break
        elif user_number > lucky_number:
            print("Too high")
        else:
            print("Too low")

    print("Thank you for playing.")

play_game()
