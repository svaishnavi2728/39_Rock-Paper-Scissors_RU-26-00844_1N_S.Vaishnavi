import random

moves = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
draws = 0

# Fixed choices for player testing
test_choices = ["scissors", "rock", "paper"]

# False for normal random game
# True for player test cases
test_mode = True


def check_winner(me, pc):

    if me == pc:
        return "draw"

    elif me == "rock" and pc == "scissors":
        return "player"

    elif me == "paper" and pc == "rock":
        return "player"

    elif me == "scissors" and pc == "paper":
        return "player"

    else:
        return "computer"


def play_game():

    global player_score, computer_score, draws

    while True:

        player_score = 0
        computer_score = 0
        draws = 0

        for i in range(3):

            while True:

                me = input("Enter rock, paper or scissors: ").lower()

                if me in moves:
                    break

                print("Invalid choice. Enter rock, paper or scissors.")

            if test_mode:
                pc = test_choices[i]
            else:
                pc = random.choice(moves)

            print("Computer chose:", pc)

            result = check_winner(me, pc)

            if result == "player":
                print("You win!")
                player_score += 1

            elif result == "computer":
                print("Computer wins!")
                computer_score += 1

            else:
                print("Draw!")
                draws += 1

            print("--------------------")

        print("Final Score")
        print("You:", player_score)
        print("Computer:", computer_score)
        print("Draws:", draws)

        if player_score > computer_score:
            print("Result: You win the match.")

        elif computer_score > player_score:
            print("Result: Computer wins the match.")

        else:
            print("Result: Match draw.")

        again = input("Play again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break


play_game()
