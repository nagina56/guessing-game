import random

# Get attempts based on level
def get_attempts(level):
    levels = {
        "easy": 10,
        "medium": 7,
        "hard": 5
    }
    return levels[level]


# Choose difficulty level
def choose_level():
    print("\nSelect Difficulty Level:")
    print("easy / medium / hard")

    while True:
        level = input("Enter level: ").lower()
        if level in ["easy", "medium", "hard"]:
            return level
        else:
            print("Invalid choice! Try again.")


# Choose number range
def choose_range():
    try:
        low = int(input("Enter minimum number: "))
        high = int(input("Enter maximum number: "))
        return low, high
    except ValueError:
        print("Invalid input! Using default range 1-100.")
        return 1, 100


# Load high score
def load_highscore():
    try:
        with open("highscore.txt", "r") as f:
            score = f.read()
            return int(score) if score else None
    except:
        return None


# Save high score
def save_highscore(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))


# Main game logic
def play_game():
    low, high = choose_range()
    number = random.randint(low, high)

    level = choose_level()
    attempts_left = get_attempts(level)
    attempts_used = 0

    print(f"\n🎯 Guess the number between {low} and {high}")

    while attempts_left > 0:
        try:
            guess = int(input(f"\nEnter your guess ({attempts_left} attempts left): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts_used += 1
        attempts_left -= 1

        # Smart hint system
        if abs(guess - number) <= 5:
            print("Very close!")

        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            print(f"\n Correct! You guessed it in {attempts_used} attempts.")
            return attempts_used

    print(f"\n You lost! The number was {number}")
    return None


# Main function
def main():
    print("Nageen's Smart Guessing Game")

    highscore = load_highscore()
    if highscore:
        print(f"Current High Score: {highscore} attempts")

    while True:
        result = play_game()

        if result:
            if not highscore or result < highscore:
                print("New High Score!")
                save_highscore(result)
                highscore = result

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()