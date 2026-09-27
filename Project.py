import random
from datetime import datetime
          

# ============================================================
# ROCK PAPER SCISSORS GAME
# ============================================================


CHOICES = ["rock", "paper", "scissors"]


# ============================================================
# PLAYER CLASS
# ============================================================


class Player:

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.total_games = 0
        self.current_streak = 0
        self.best_streak = 0

    def add_win(self):
        self.wins += 1
        self.total_games += 1
        self.current_streak += 1

        if self.current_streak > self.best_streak:
            self.best_streak = self.current_streak

    def add_loss(self):
        self.losses += 1
        self.total_games += 1
        self.current_streak = 0

    def add_tie(self):
        self.ties += 1
        self.total_games += 1

    def show_statistics(self):
        print("\n========== PLAYER STATISTICS ==========")
        print(f"Player: {self.name}")
        print(f"Games Played: {self.total_games}")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Ties: {self.ties}")
        print(f"Best Winning Streak: {self.best_streak}")

        if self.total_games > 0:
            win_percentage = (self.wins / self.total_games) * 100
            print(f"Win Percentage: {win_percentage:.2f}%")

        print("=======================================\n")


# ============================================================
# DISPLAY FUNCTIONS
# ============================================================


def display_title():
    print()
    print("=" * 60)
    print("                 ROCK PAPER SCISSORS")
    print("=" * 60)
    print()


def display_rules():
    print("\n========== GAME RULES ==========")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print()
    print("Enter:")
    print("  rock")
    print("  paper")
    print("  scissors")
    print("================================\n")


def display_main_menu():
    print("\n========== MAIN MENU ==========")
    print("1. Play Game")
    print("2. View Rules")
    print("3. View Statistics")
    print("4. View Match History")
    print("5. View Achievements")
    print("6. Reset Statistics")
    print("7. Exit")
    print("===============================\n")


# ============================================================
# COMPUTER FUNCTIONS
# ============================================================


def computer_easy():
    return random.choice(CHOICES)


def computer_medium(player_history):

    if not player_history:
        return random.choice(CHOICES)

    rock_count = player_history.count("rock")
    paper_count = player_history.count("paper")
    scissors_count = player_history.count("scissors")

    most_used = max(
        ["rock", "paper", "scissors"],
        key=lambda choice: player_history.count(choice)
    )

    if most_used == "rock":
        return "paper"

    elif most_used == "paper":
        return "scissors"

    else:
        return "rock"


def computer_hard(player_history):

    # Sometimes play randomly so the computer
    # does not become completely predictable.

    if random.random() < 0.25:
        return random.choice(CHOICES)

    return computer_medium(player_history)


def get_computer_choice(difficulty, player_history):

    if difficulty == "easy":
        return computer_easy()

    elif difficulty == "medium":
        return computer_medium(player_history)

    elif difficulty == "hard":
        return computer_hard(player_history)

    return computer_easy()


# ============================================================
# GAME LOGIC
# ============================================================


def determine_winner(player_choice, computer_choice):

    if player_choice == computer_choice:
        return "tie"

    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winning_combinations[player_choice] == computer_choice:
        return "player"

    return "computer"


def get_player_choice():
    while True:
        choice = input(
            "Enter rock, paper, scissors, or quit: "
        ).lower().strip()

        if choice == "quit":
            return "quit"

        if choice in CHOICES:
            return choice

        print("Invalid choice.")
        print("Please enter rock, paper, or scissors.")


# ============================================================
# DIFFICULTY
# ============================================================


def choose_difficulty():
    while True:
        print("\nChoose Difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        option = input("Enter option: ").strip()

        if option == "1":
            return "easy"
        elif option == "2":
            return "medium"
        elif option == "3":
            return "hard"
        else:
            print("Invalid option. Try again.")


# ============================================================
# ROUND
# ============================================================


def play_round(player, difficulty, player_history, match_history):
    player_choice = get_player_choice()
    if player_choice == "quit":
        return False
    player_history.append(player_choice)

    computer_choice = get_computer_choice(
        difficulty,
        player_history[:-1]
    )

    print()
    print(f"{player.name} chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(
        player_choice,
        computer_choice
    )

    if result == "tie":
        print("It's a tie!")
        player.add_tie()

    elif result == "player":
        print(f"{player.name} wins!")
        player.add_win()

    else:
        print("Computer wins!")
        player.add_loss()

    match_history.append({
        "player": player_choice,
        "computer": computer_choice,
        "result": result,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    return True


# ============================================================
# MATCH HISTORY
# ============================================================


def show_match_history(match_history):
    print("\n========== MATCH HISTORY ==========")
    if not match_history:
        print("No games have been played yet.")
        return

    for number, match in enumerate(match_history, start=1):
        print(f"\nGame {number}")

        print(
            f"Player: {match['player']}"
        )
        print(
            f"Computer: {match['computer']}"
        )

        print(
            f"Result: {match['result']}"
        )
        print(
            f"Time: {match['time']}"
        )
    print("\n===================================")


# ============================================================
# ACHIEVEMENTS
# ============================================================


def show_achievements(player):
    print("\n========== ACHIEVEMENTS ==========")
    achievements = []
    if player.wins >= 1:
        achievements.append(
            "First Victory - Win your first game"
        )

    if player.wins >= 5:
        achievements.append(
            "Winner - Win 5 games"
        )

    if player.wins >= 10:
        achievements.append(
            "Champion - Win 10 games"
        )

    if player.best_streak >= 3:
        achievements.append(
            "On Fire - Win 3 games in a row"
        )

    if player.best_streak >= 5:
        achievements.append(
            "Unstoppable - Win 5 games in a row"
        )

    if player.total_games >= 10:
        achievements.append(
            "Regular Player - Play 10 games"
        )

    if not achievements:
        print("No achievements unlocked yet.")
    else:
        for achievement in achievements:
            print(f"* {achievement}")

    print("==================================\n")


# ============================================================
# RESET
# ============================================================


def reset_statistics(player, match_history, player_history):
    print("\nWARNING!")
    print("This will reset all game statistics.")
    answer = input(
        "Are you sure? (yes/no): "
    ).lower().strip()

    if answer == "yes":
        player.wins = 0
        player.losses = 0
        player.ties = 0
        player.total_games = 0
        player.current_streak = 0
        player.best_streak = 0

        match_history.clear()
        player_history.clear()

        print("Statistics reset successfully.")

    else:
        print("Reset cancelled.")


# ============================================================
# MAIN GAME
# ============================================================


def game():
    display_title()
    print("Welcome to Rock-Paper-Scissors!")
    name = input(
        "Enter your name: "
    ).strip()

    if not name:
        name = "Player"
    player = Player(name)
    player_history = []
    match_history = []

    difficulty = choose_difficulty()

    while True:
        display_main_menu()
        option = input(
            "Choose an option: "
        ).strip()

        if option == "1":
            print("\nStarting game...")
            print(f"Difficulty: {difficulty}")

            while True:
                continue_game = play_round(
                    player,
                    difficulty,
                    player_history,
                    match_history
                )

                if not continue_game:
                    break

                print()

                again = input(
                    "Play another round? (yes/no): "
                ).lower().strip()

                if again != "yes":
                    break

        elif option == "2":
            display_rules()

        elif option == "3":
            player.show_statistics()

        elif option == "4":
            show_match_history(
                match_history
            )

        elif option == "5":
            show_achievements(
                player
            )

        elif option == "6":
            reset_statistics(
                player,
                match_history,
                player_history
            )

        elif option == "7":
            print()
            print(
                f"Thanks for playing, {player.name}!"
            )
            print("Goodbye!")
            break

        else:
            print(
                "Invalid menu option. Please try again."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================


if __name__ == "__main__":
    game()