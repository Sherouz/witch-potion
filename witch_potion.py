# Python Script - Witch's Potion 🧪
# A short, fun Halloween game built with Python OOP + functions.
# The player must guess the witch’s secret ingredient combo before it explodes!

"""
A tiny Halloween-themed console game using basic Object-Oriented Programming.

The player (as the apprentice) selects 3 ingredients to try to match
the witch’s secret potion combination. If the combo matches, you win —
if not, the potion explodes in your face!

Includes classes for Potion, Apprentice, and Game, plus simple random logic.
"""

import random
import time


class Potion:
    """Holds the list of ingredients and the witch's secret 3-item combo."""
    def __init__(self, ingredients):
        # store available ingredients
        self.ingredients = ingredients
        # pick a random secret combination (3 unique items)
        self.secret_combo = random.sample(ingredients, 3)


class Apprentice:
    """Represents the player (the apprentice). Handles input and choice logic."""
    def __init__(self, name="You"):
        self.name = name

    def choose_ingredients(self, ingredients):
        # display ingredient list and ask player to pick 3
        print("\n🧪 Choose wisely, apprentice...")
        print("Pick 3 ingredients (comma separated, e.g., 1,3,5):\n")

        for i, item in enumerate(ingredients, 1):
            print(f"  {i}. {item}")

        choice = input("\n👉 Your choice: ").split(",")

        try:
            # convert input numbers to actual ingredient names
            return [ingredients[int(i.strip()) - 1] for i in choice]
        except (ValueError, IndexError):
            # fallback in case of invalid input
            print("\n😅 Invalid input! The spirits choose for you...")
            return random.sample(ingredients, 3)


class Game:
    """Main controller — manages display, timing, and results."""
    def __init__(self):
        # all possible ingredients in the game
        self.ingredients = [
            "Eye of Newt",
            "Frog Leg",
            "Pumpkin Seed",
            "Bat Wing",
            "Ghost Dust"
        ]
        # initialize potion and player
        self.potion = Potion(self.ingredients)
        self.player = Apprentice()

    def slow_print(self, text, delay=0.05):
        """Print text slowly for a dramatic effect (Halloween vibe 😈)."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  # newline after the text

    def play(self):
        # intro screen
        print("\n" + "═" * 50)
        print("🧙‍♀️  WITCH’S POTION  🧪".center(50))
        print("═" * 50)
        self.slow_print("\nThe witch is away... Can you brew her secret potion?\n", 0.03)
        time.sleep(1)

        # player selects 3 ingredients
        player_choice = self.player.choose_ingredients(self.ingredients)

        # mix process
        print("\n✨ Mixing your ingredients...")
        time.sleep(1.2)
        print("💨 The cauldron bubbles and hisses ominously...\n")
        time.sleep(1.4)

        # compare player combo with secret combo
        if set(player_choice) == set(self.potion.secret_combo):
            self.slow_print("🎉 You made the PERFECT potion! The witch is impressed! 🎃", 0.03)
        else:
            self.slow_print("💥 The potion EXPLODES! Wrong mix!", 0.04)
            time.sleep(1)
            print(f"\n🧪 The secret combo was: {', '.join(self.potion.secret_combo)}")
            self.slow_print("🐸 The witch returns and turns you into a frog!", 0.04)

        # outro
        print("\n" + "═" * 50)
        print("⚰️  END OF THE GAME  ⚰️".center(50))
        print("═" * 50 + "\n")


if __name__ == "__main__":
    # run the game if file executed directly
    Game().play()
